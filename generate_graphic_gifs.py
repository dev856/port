"""Build conceptual portfolio animations and reduced-motion posters with Pillow.

Run: python generate_graphic_gifs.py
No external media or runtime dependencies beyond the existing Pillow package.
"""
from pathlib import Path
import math

from PIL import Image, ImageDraw, ImageFont

OUT = Path(__file__).resolve().parent / "images" / "gifs"
SIZE = (640, 360)
INK = "#172033"
PAPER = "#f3f0e7"
BLUE = "#3558cf"
ORANGE = "#d76635"
TEAL = "#147e78"
FONT = ImageFont.load_default(size=17)
SMALL = ImageFont.load_default(size=13)
TITLE = ImageFont.load_default(size=23)


def base(title, number):
    image = Image.new("RGB", SIZE, PAPER)
    d = ImageDraw.Draw(image)
    d.text((24, 18), title, font=TITLE, fill=INK)
    d.text((574, 22), number, font=FONT, fill=BLUE)
    d.line((24, 57, 616, 57), fill=INK, width=2)
    d.text((24, 333), "CONCEPT ILLUSTRATION / NOT A LIVE DEMO", font=SMALL, fill=INK)
    return image, d


def topic(t):
    image, d = base("DOCUMENTS -> TOPICS", "01")
    labels = [("VISION", BLUE), ("SYSTEMS", TEAL), ("RESEARCH", ORANGE)]
    for j, (label, color) in enumerate(labels):
        y = 98 + j * 73
        d.rounded_rectangle((433, y, 608, y + 53), radius=6, fill=color)
        d.text((448, y + 16), label, font=FONT, fill="white")
        d.line((210, 189, 417, y + 26), fill="#b8bcc4", width=2)
        progress = (t + j / 3) % 1
        x = 225 + 185 * progress
        cy = 189 + (y + 26 - 189) * progress
        d.rectangle((x-10, cy-7, x+10, cy+7), fill=color)
    d.rectangle((34, 103, 192, 278), fill="white", outline=INK, width=2)
    for j in range(6):
        d.line((52, 131 + j*21, 167 - (j%2)*20, 131+j*21), fill=BLUE if j%3==0 else "#b8bcc4", width=5)
    return image


def pose(t):
    image, d = base("MOVEMENT / LANDMARKS", "02")
    d.rectangle((24, 75, 400, 315), fill="#dcebe5")
    bend = math.sin(t*2*math.pi) * 32
    points = [(211,105),(211,148),(150,166),(112,142+bend),(273,164),(315,142-bend),(211,219),(165,263),(142,301),(258,265),(300,301)]
    d.line((70,303,357,303), fill=TEAL, width=2)
    for a,b in [(0,1),(1,2),(2,3),(1,4),(4,5),(1,6),(6,7),(7,8),(6,9),(9,10)]:
        d.line((*points[a],*points[b]), fill=INK, width=7)
    for x,y in points:
        d.ellipse((x-6,y-6,x+6,y+6),fill=ORANGE,outline=PAPER,width=2)
    for j,text in enumerate(["01  Locate joints", "02  Measure angles", "03  Compare posture"]):
        d.text((423,128+j*56),text,font=SMALL,fill=INK)
    return image


def data(t):
    image,d=base("DATA / FILTER / EXPLORE", "03")
    headers=["ID", "TYPE", "REGION"]
    for j,text in enumerate(headers): d.text((43+j*100,83),text,font=FONT,fill=BLUE)
    active=int(t*6)%6
    for row in range(6):
        y=115+row*31
        fill="#d4e5df" if row==active else "white"
        d.rectangle((30,y,352,y+27),fill=fill)
        for j,text in enumerate([f"0{row+1}", ["A","B"][row%2], ["NORTH","SOUTH","WEST"][row%3]]):
            d.text((43+j*100,y+5),text,font=SMALL,fill=INK)
    d.rounded_rectangle((404,94,605,299),radius=10,fill=INK)
    d.text((424,113),"FILTER: REGION",font=SMALL,fill="white")
    d.text((424,150),["NORTH","SOUTH","WEST"][active%3],font=TITLE,fill="#b3c3ff")
    for row in range(2):
        d.rectangle((424,200+row*36,584,227+row*36),fill=TEAL)
        d.text((433,206+row*36),f"RECORD 0{active%3+1+row*3}",font=SMALL,fill="white")
    return image


def ensemble(t):
    image,d=base("ENSEMBLE / COMBINE DECISIONS", "04")
    d.rectangle((27,148,128,238),fill=INK)
    d.text((43,178),"INPUT",font=FONT,fill="white")
    for j,label in enumerate(["TREE A","TREE B","TREE C"]):
        y=82+j*77
        d.line((128,193,247,y+25),fill="#a3a9b7",width=2)
        d.rectangle((248,y,392,y+51),fill=[BLUE,TEAL,ORANGE][j])
        d.text((275,y+16),label,font=FONT,fill="white")
        d.line((392,y+25,493,193),fill="#a3a9b7",width=2)
        phase=(t+j/3)%1
        x=400+85*phase; cy=y+25+(193-y-25)*phase
        d.ellipse((x-5,cy-5,x+5,cy+5),fill=INK)
    d.rectangle((494,140,612,245),fill="#dbdff3",outline=BLUE,width=2)
    d.text((510,164),"COMBINE",font=FONT,fill=BLUE)
    d.text((510,202),"OUTPUT",font=SMALL,fill=INK)
    return image


def fabric(t):
    image,d=base("FABRIC / SURFACE INSPECTION", "05")
    d.rectangle((25,77,430,311),fill="#e9d7bc")
    for x in range(25,431,10): d.line((x,77,x,311),fill="#bea784",width=3)
    for y in range(77,312,10): d.line((25,y,430,y),fill="#d4be9b",width=3)
    d.polygon([(261,159),(279,176),(275,202),(257,191),(249,173)],fill=INK)
    scan=40+370*t
    d.rectangle((scan-6,78,scan+6,310),fill=TEAL)
    if t>.57:
        d.rectangle((240,148,288,210),outline=ORANGE,width=3)
        d.line((288,179,466,179),fill=ORANGE,width=2)
    d.text((465,107),"INSPECT",font=TITLE,fill=TEAL)
    d.text((465,199),"SURFACE",font=FONT,fill=INK)
    d.text((465,225),"PATTERNS",font=FONT,fill=INK)
    return image


def basin(t):
    image,d=base("SATELLITE / BASIN OBSERVATION", "06")
    d.rounded_rectangle((24,76,440,313),radius=8,fill="#d5e4de")
    for j in range(4):
        d.ellipse((50+j*28,91+j*14,411-j*26,295-j*14),outline="#8faea2",width=2)
    river=[(181,82),(223,120),(205,152),(252,184),(234,223),(300,270),(282,312)]
    d.line(river,fill=BLUE,width=9)
    d.line([(120,154),(167,170),(205,152)],fill=BLUE,width=4)
    y=85+t*218
    d.line((27,y,435,y),fill=ORANGE,width=2)
    d.rectangle((465,87,604,148),fill=INK)
    d.text((480,107),"OBSERVE",font=FONT,fill="white")
    d.line((534,150,534,196),fill=INK,width=2)
    d.rectangle((465,198,604,282),fill=BLUE)
    d.text((480,217),"MODEL",font=FONT,fill="white")
    d.text((480,249),"BASIN FLUX",font=SMALL,fill="white")
    return image


GENERATORS = {
    "graphic-topics": topic,
    "graphic-pose": pose,
    "graphic-data": data,
    "graphic-ensemble": ensemble,
    "graphic-fabric": fabric,
    "graphic-basin": basin,
}


def main():
    OUT.mkdir(parents=True,exist_ok=True)
    for name, draw in GENERATORS.items():
        frames=[draw(i/32) for i in range(32)]
        frames[20].save(OUT / f"{name}.png")
        frames[0].save(OUT / f"{name}.gif", save_all=True, append_images=frames[1:], duration=100, loop=0, optimize=True)
        print(name, (OUT / f"{name}.gif").stat().st_size, "bytes")


if __name__ == "__main__":
    main()
