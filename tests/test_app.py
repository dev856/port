"""Streamlit smoke tests. Run with: python -m unittest discover -s tests -v"""

import base64
from html.parser import HTMLParser
import sqlite3
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from PIL import Image
from streamlit.testing.v1 import AppTest


ROOT = Path(__file__).resolve().parents[1]


class MediaParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.images = []
        self.sources = []

    def handle_starttag(self, tag, attrs):
        if tag == "img":
            self.images.append(dict(attrs))
        elif tag == "source":
            self.sources.append(dict(attrs))


class PortfolioTests(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        connect = sqlite3.connect
        # Exercise database initialization without touching real inquiries.
        db_patch = patch(
            "sqlite3.connect",
            side_effect=lambda *args, **kwargs: connect(Path(temp.name) / "contacts.db"),
        )
        db_patch.start()
        self.addCleanup(db_patch.stop)
        self.app = AppTest.from_file(str(ROOT / "Home.py"), default_timeout=30).run()
        self.assert_no_errors()

    def assert_no_errors(self):
        self.assertEqual([error.message for error in self.app.exception], [])

    def test_theme_styles_are_injected_without_bom(self):
        styles = [item.value for item in self.app.markdown if item.value.startswith("<style>")]
        self.assertEqual(len(styles), 1)
        self.assertTrue(any("--accent:" in style for style in styles))
        for style in styles:
            self.assertNotIn("﻿", style)

    def test_all_pages_render(self):
        for dark in (True, False):
            self.app.toggle(key="dark_mode").set_value(dark).run()
            for page in self.app.radio(key="nav").options:
                with self.subTest(page=page, dark=dark):
                    self.app.radio(key="nav").set_value(page).run()
                    self.assert_no_errors()
                    self.assertEqual(self.app.toggle(key="dark_mode").value, dark)
                    styles = next(item.value for item in self.app.markdown if item.value.startswith("<style>"))
                    self.assertEqual("color-scheme: dark;" in styles, dark)

    def test_search_and_category_filter(self):
        self.app.radio(key="nav").set_value("Projects").run()
        self.app.text_input(key="proj_search_input").set_value("MediaPipe").run()
        self.assert_no_errors()
        self.assertEqual([heading.value for heading in self.app.subheader], ["Digital Yoga Trainer"])
        self.app.button(key="cat_btn_NLP").click().run()
        self.assert_no_errors()
        self.assertEqual(len(self.app.warning), 1)

    def test_both_reset_buttons_clear_search_and_category(self):
        self.app.radio(key="nav").set_value("Projects").run()
        for button_key in ("clear_search_btn", "reset_empty_search"):
            with self.subTest(button=button_key):
                self.app.button(key="cat_btn_NLP").click().run()
                self.app.text_input(key="proj_search_input").set_value("no-match-xyz").run()
                self.assertEqual(len(self.app.warning), 1)
                self.app.button(key=button_key).click().run()
                self.assert_no_errors()
                self.assertEqual(self.app.text_input(key="proj_search_input").value, "")
                self.assertEqual(self.app.session_state.project_filter, "All")
                self.assertEqual(len(self.app.warning), 0)
                self.assertEqual(len(self.app.subheader), 6)  # One card per project.

    def test_project_media_and_animation_preference(self):
        overview_sources = None
        for animate in (True, False):
            self.app.toggle(key="animate_previews").set_value(animate).run()
            for page, count in (("Overview", 3), ("Projects", 6)):
                self.app.radio(key="nav").set_value(page).run()
                self.assert_no_errors()
                self.assertEqual(self.app.toggle(key="animate_previews").value, animate)
                parser = MediaParser()
                for item in self.app.markdown:
                    if '<picture class="project-media">' in item.value:
                        parser.feed(item.value)
                self.assertEqual(len(parser.images), count)
                self.assertEqual(len(parser.sources), count)
                sources = {source["srcset"] for source in parser.sources}
                self.assertEqual(len(sources), count)
                if page == "Overview":
                    overview_sources = sources
                else:
                    self.assertTrue(overview_sources.issubset(sources))
                for image, source in zip(parser.images, parser.sources):
                    self.assertIn("conceptual illustration", image["alt"])
                    self.assertEqual(source["media"], "(prefers-reduced-motion: reduce)")
                    self.assertTrue(source["srcset"].startswith("data:image/png;base64,"))
                    expected = "gif" if animate else "png"
                    self.assertTrue(image["src"].startswith(f"data:image/{expected};base64,"))
                    payload = base64.b64decode(image["src"].split(",", 1)[1])
                    self.assertGreater(len(payload), 1000)
            self.app.radio(key="nav").set_value("About").run()
            self.assertEqual(self.app.toggle(key="animate_previews").value, animate)

    def test_generated_assets_have_distinct_frames_and_posters(self):
        names = ("topics", "pose", "data", "ensemble", "fabric", "basin")
        posters = set()
        for name in names:
            path = ROOT / "images" / "gifs" / f"graphic-{name}"
            with self.subTest(asset=name), Image.open(path.with_suffix(".gif")) as gif:
                self.assertEqual(gif.size, (640, 360))
                self.assertGreater(gif.n_frames, 1)
                self.assertEqual(gif.info["loop"], 0)
                first = gif.convert("RGB").tobytes()
                gif.seek(gif.n_frames // 4)
                self.assertTrue(first != gif.convert("RGB").tobytes(), "Animation must change between frames")
                self.assertLess(path.with_suffix(".gif").stat().st_size, 150_000)
            with Image.open(path.with_suffix(".png")) as poster:
                self.assertEqual(poster.size, (640, 360))
                posters.add(poster.tobytes())
        self.assertEqual(len(posters), 6)

    def test_skills_page_groups_and_tools(self):
        self.app.radio(key="nav").set_value("Skills").run()
        self.assert_no_errors()
        grid = next(item.value for item in self.app.markdown if 'class="skill-grid"' in item.value)
        for title in ("Software &amp; Systems", "Data Science &amp; ML", "Product &amp; Delivery"):
            self.assertIn(title, grid)
        for tool in ("Docker Basics", "MediaPipe", "Agile / Scrum"):
            self.assertIn(tool, grid)
        self.assertEqual(grid.count("<li>"), 27)  # 10 + 10 + 7 tools across the three groups.

    def test_project_expander_still_opens(self):
        self.app.radio(key="nav").set_value("Projects").run()
        self.assert_no_errors()
        # Every project exposes its deep-dive expander inside the content column.
        self.assertEqual(len(self.app.expander), 6)
        expander = self.app.expander[0]
        self.assertIn("Technical Architecture", str(expander.label))
        # Its deep-dive content is present and renderable beneath the summary.
        self.assertIn("Text Preprocessing", str(expander.markdown[0].value))
        expander.run()
        self.assert_no_errors()

    def test_hero_navigation(self):
        self.app.button(key="hero_explore_btn").click().run()
        self.assert_no_errors()
        self.assertEqual(self.app.radio(key="nav").value, "Projects")
        self.app.radio(key="nav").set_value("Overview").run()
        self.app.button(key="overview_experience_btn").click().run()
        self.assert_no_errors()
        self.assertEqual(self.app.radio(key="nav").value, "Experience")


if __name__ == "__main__":
    unittest.main()
