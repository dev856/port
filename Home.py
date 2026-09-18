from __future__ import annotations

import base64
import html
import sqlite3
from datetime import datetime
from pathlib import Path

import streamlit as st

ROOT = Path(__file__).resolve().parent
EMAIL = "devhkotak@gmail.com"
LINKEDIN = "https://www.linkedin.com/in/dev-kotak/"
GITHUB = "https://github.com/dev856"
LOCATION = "Ottawa, Ontario, Canada"

NAV_ITEMS = [
    "Overview",
    "About",
    "Projects",
    "Experience",
    "Skills",
    "Education",
    "Testimonials",
    "Résumé",
    "Contact",
]

MIME_BY_SUFFIX = {
    ".png": "image/png",
    ".jpg": "image/jpeg",
    ".jpeg": "image/jpeg",
    ".svg": "image/svg+xml",
    ".gif": "image/gif",
    ".webp": "image/webp",
    ".pdf": "application/pdf",
}

# Razor-sharp Lucide Vector SVG Icon Definitions
SVG_ICONS = {
    "cpu": '<svg class="svg-icon" xmlns="http://www.w3.org/2000/svg" width="{s}" height="{s}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="4" y="4" width="16" height="16" rx="2"/><rect x="9" y="9" width="6" height="6"/><path d="M9 1v3M15 1v3M9 20v3M15 20v3M20 9h3M20 14h3M1 9h3M1 14h3"/></svg>',
    "brain": '<svg class="svg-icon" xmlns="http://www.w3.org/2000/svg" width="{s}" height="{s}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M12 5a3 3 0 1 0-5.997.125 4 4 0 0 0-2.526 5.77 4 4 0 0 0 .556 6.588A4 4 0 1 0 12 18Z"/><path d="M12 5a3 3 0 1 1 5.997.125 4 4 0 0 1 2.526 5.77 4 4 0 0 1-.556 6.588A4 4 0 1 1 12 18Z"/><path d="M12 5v13"/><path d="M6 12h12"/></svg>',
    "eye": '<svg class="svg-icon" xmlns="http://www.w3.org/2000/svg" width="{s}" height="{s}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M2 12s3-7 10-7 10 7 10 7-3 7-10 7-10-7-10-7Z"/><circle cx="12" cy="12" r="3"/></svg>',
    "layers": '<svg class="svg-icon" xmlns="http://www.w3.org/2000/svg" width="{s}" height="{s}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="m12.83 2.18a2 2 0 0 0-1.66 0L2.6 6.08a1 1 0 0 0 0 1.83l8.58 3.9a2 2 0 0 0 1.66 0l8.58-3.9a1 1 0 0 0 0-1.83Z"/><path d="m22 12.5-9.17 4.16a2 2 0 0 1-1.66 0L2 12.5"/><path d="m22 17.5-9.17 4.16a2 2 0 0 1-1.66 0L2 17.5"/></svg>',
    "briefcase": '<svg class="svg-icon" xmlns="http://www.w3.org/2000/svg" width="{s}" height="{s}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect width="20" height="14" x="2" y="7" rx="2"/><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"/></svg>',
    "graduation": '<svg class="svg-icon" xmlns="http://www.w3.org/2000/svg" width="{s}" height="{s}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M21.42 10.922a1 1 0 0 0-.019-1.838L12.83 5.18a2 2 0 0 0-1.66 0L2.6 9.08a1 1 0 0 0 0 1.832l8.57 3.908a2 2 0 0 0 1.66 0z"/><path d="M22 10v6"/><path d="M6 12.5V16a6 3 0 0 0 12 0v-3.5"/></svg>',
    "target": '<svg class="svg-icon" xmlns="http://www.w3.org/2000/svg" width="{s}" height="{s}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="6"/><circle cx="12" cy="12" r="2"/></svg>',
    "award": '<svg class="svg-icon" xmlns="http://www.w3.org/2000/svg" width="{s}" height="{s}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="8" r="6"/><path d="M15.477 12.89 17 22l-5-3-5 3 1.523-9.11"/></svg>',
    "code": '<svg class="svg-icon" xmlns="http://www.w3.org/2000/svg" width="{s}" height="{s}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><polyline points="16 18 22 12 16 6"/><polyline points="8 6 2 12 8 18"/></svg>',
    "terminal": '<svg class="svg-icon" xmlns="http://www.w3.org/2000/svg" width="{s}" height="{s}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><polyline points="4 17 10 11 4 5"/><line x1="12" x2="20" y1="19" y2="19"/></svg>',
    "database": '<svg class="svg-icon" xmlns="http://www.w3.org/2000/svg" width="{s}" height="{s}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><ellipse cx="12" cy="5" rx="9" ry="3"/><path d="M3 5v14c0 1.66 4 3 9 3s9-1.34 9-3V5"/><path d="M3 12c0 1.66 4 3 9 3s9-1.34 9-3"/></svg>',
    "sparkles": '<svg class="svg-icon" xmlns="http://www.w3.org/2000/svg" width="{s}" height="{s}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="m12 3-1.912 5.813a2 2 0 0 1-1.275 1.275L3 12l5.813 1.912a2 2 0 0 1 1.275 1.275L12 21l1.912-5.813a2 2 0 0 1 1.275-1.275L21 12l-5.813-1.912a2 2 0 0 1-1.275-1.275L12 3Z"/></svg>',
    "star": '<svg class="svg-icon" xmlns="http://www.w3.org/2000/svg" width="{s}" height="{s}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>',
    "message": '<svg class="svg-icon" xmlns="http://www.w3.org/2000/svg" width="{s}" height="{s}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M7.9 20A9 9 0 1 0 4 16.1L2 22Z"/></svg>',
    "user": '<svg class="svg-icon" xmlns="http://www.w3.org/2000/svg" width="{s}" height="{s}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M19 21v-2a4 4 0 0 0-4-4H9a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>',
    "file_text": '<svg class="svg-icon" xmlns="http://www.w3.org/2000/svg" width="{s}" height="{s}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M15 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7Z"/><path d="M14 2v4a2 2 0 0 0 2 2h4"/><path d="M10 9H8"/><path d="M16 13H8"/><path d="M16 17H8"/></svg>',
    "mail": '<svg class="svg-icon" xmlns="http://www.w3.org/2000/svg" width="{s}" height="{s}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect width="20" height="16" x="2" y="4" rx="2"/><path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"/></svg>',
    "map_pin": '<svg class="svg-icon" xmlns="http://www.w3.org/2000/svg" width="{s}" height="{s}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M20 10c0 4.993-5.539 10.193-7.399 11.799a1 1 0 0 1-1.202 0C9.539 20.193 4 14.993 4 10a8 8 0 0 1 16 0"/><circle cx="12" cy="10" r="3"/></svg>',
    "calendar": '<svg class="svg-icon" xmlns="http://www.w3.org/2000/svg" width="{s}" height="{s}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect width="18" height="18" x="3" y="4" rx="2" ry="2"/><line x1="16" x2="16" y1="2" y2="6"/><line x1="8" x2="8" y1="2" y2="6"/><line x1="3" x2="21" y1="10" y2="10"/></svg>',
    "external": '<svg class="svg-icon" xmlns="http://www.w3.org/2000/svg" width="{s}" height="{s}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/><polyline points="15 3 21 3 21 9"/><line x1="10" x2="21" y1="14" y2="3"/></svg>',
    "github": '<svg class="svg-icon" xmlns="http://www.w3.org/2000/svg" width="{s}" height="{s}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M15 22v-4a4.8 4.8 0 0 0-1-3.5c3 0 6-2 6-5.5.08-1.25-.27-2.48-1-3.5.28-1.15.28-2.35 0-3.5 0 0-1 0-3 1.5-2.64-.5-5.36-.5-8 0C6 2 5 2 5 2c-.3 1.15-.3 2.35 0 3.5A5.403 5.403 0 0 0 4 9c0 3.5 3 5.5 6 5.5-.39.49-.68 1.05-.85 1.65-.17.6-.22 1.23-.15 1.85v4"/><path d="M9 18c-4.51 2-5-2-7-2"/></svg>',
    "linkedin": '<svg class="svg-icon" xmlns="http://www.w3.org/2000/svg" width="{s}" height="{s}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"/><rect width="4" height="12" x="2" y="9"/><circle cx="4" cy="4" r="2"/></svg>',
    "check": '<svg class="svg-icon" xmlns="http://www.w3.org/2000/svg" width="{s}" height="{s}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg>',
    "send": '<svg class="svg-icon" xmlns="http://www.w3.org/2000/svg" width="{s}" height="{s}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="m22 2-7 20-4-9-9-4Z"/><path d="M22 2 11 13"/></svg>',
    "zap": '<svg class="svg-icon" xmlns="http://www.w3.org/2000/svg" width="{s}" height="{s}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg>',
    "activity": '<svg class="svg-icon" xmlns="http://www.w3.org/2000/svg" width="{s}" height="{s}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M22 12h-4l-3 9L9 3l-3 9H2"/></svg>',
    "book": '<svg class="svg-icon" xmlns="http://www.w3.org/2000/svg" width="{s}" height="{s}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M4 19.5v-15A2.5 2.5 0 0 1 6.5 2H20v20H6.5a2.5 2.5 0 0 1-2.5-2.5Z"/><path d="M6 6h10"/><path d="M6 10h10"/></svg>',
    "rocket": '<svg class="svg-icon" xmlns="http://www.w3.org/2000/svg" width="{s}" height="{s}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M4.5 16.5c-1.5 1.26-2 5-2 5s3.74-.5 5-2c.71-.84.7-2.13-.09-2.91a2.18 2.18 0 0 0-2.91-.09z"/><path d="m12 15-3-3a22 22 0 0 1 2-3.95A12.88 12.88 0 0 1 22 2c0 2.72-.78 7.5-6 11a22.35 22.35 0 0 1-4 2z"/><path d="M9 12H4s.55-3.03 2-4c1.62-1.08 5 0 5 0"/><path d="M12 15v5s3.03-.55 4-2c1.08-1.62 0-5 0-5"/></svg>',
    "lightbulb": '<svg class="svg-icon" xmlns="http://www.w3.org/2000/svg" width="{s}" height="{s}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M15 14c.2-1 .7-1.7 1.5-2.5 1-.9 1.5-2.2 1.5-3.5A6 6 0 0 0 6 8c0 1 .2 2.2 1.5 3.5.7.7 1.3 1.5 1.5 2.5"/><path d="M9 18h6"/><path d="M10 22h4"/></svg>',
    "users": '<svg class="svg-icon" xmlns="http://www.w3.org/2000/svg" width="{s}" height="{s}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>',
    "quote": '<svg class="svg-icon" xmlns="http://www.w3.org/2000/svg" width="{s}" height="{s}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M16 3a2 2 0 0 0-2 2v6a2 2 0 0 0 2 2 1 1 0 0 1 1 1v1a2 2 0 0 1-2 2 1 1 0 0 0-1 1v2a1 1 0 0 0 1 1 6 6 0 0 0 6-6V5a2 2 0 0 0-2-2z"/><path d="M5 3a2 2 0 0 0-2 2v6a2 2 0 0 0 2 2 1 1 0 0 1 1 1v1a2 2 0 0 1-2 2 1 1 0 0 0-1 1v2a1 1 0 0 0 1 1 6 6 0 0 0 6-6V5a2 2 0 0 0-2-2z"/></svg>',
    "globe": '<svg class="svg-icon" xmlns="http://www.w3.org/2000/svg" width="{s}" height="{s}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M12 2a14.5 14.5 0 0 0 0 20 14.5 14.5 0 0 0 0-20"/><path d="M2 12h20"/></svg>',
    "download": '<svg class="svg-icon" xmlns="http://www.w3.org/2000/svg" width="{s}" height="{s}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" x2="12" y1="15" y2="3"/></svg>',
    "atom": '<svg class="svg-icon" xmlns="http://www.w3.org/2000/svg" width="{s}" height="{s}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="1"/><path d="M20.2 20.2c2.04-2.03.02-7.36-4.5-11.9-4.54-4.52-9.87-6.54-11.9-4.5-2.04 2.03-.02 7.36 4.5 11.9 4.54 4.52 9.87 6.54 11.9 4.5Z"/><path d="M15.7 15.7c4.52-4.54 6.54-9.87 4.5-11.9-2.03-2.04-7.36-.02-11.9 4.5-4.52 4.54-6.54 9.87-4.5 11.9 2.03 2.04 7.36.02 11.9-4.5Z"/></svg>',
    "workflow": '<svg class="svg-icon" xmlns="http://www.w3.org/2000/svg" width="{s}" height="{s}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect width="8" height="8" x="3" y="3" rx="2"/><path d="M7 11v4a2 2 0 0 0 2 2h4"/><rect width="8" height="8" x="13" y="13" rx="2"/></svg>',
    "satellite_dish": '<svg class="svg-icon" xmlns="http://www.w3.org/2000/svg" width="{s}" height="{s}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M4 10a7.31 7.31 0 0 0 10 10z"/><path d="m9 15 3-3"/><path d="M17 13a6 6 0 0 0-6-6"/><path d="M21 13A10 10 0 0 0 11 3"/><rect x="13" y="15" width="6" height="6" rx="2" transform="rotate(45 16 18)"/></svg>',
    "flask_conical": '<svg class="svg-icon" xmlns="http://www.w3.org/2000/svg" width="{s}" height="{s}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2v6a2 2 0 0 0 .245.96l5.51 10.08A2 2 0 0 1 18 22H6a2 2 0 0 1-1.755-2.96l5.51-10.08A2 2 0 0 0 10 8V2"/><path d="M6.453 15h11.094"/><path d="M8.5 2h7"/></svg>',
    "gauge": '<svg class="svg-icon" xmlns="http://www.w3.org/2000/svg" width="{s}" height="{s}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="m12 14 4-4"/><path d="M3.34 19a10 10 0 1 1 17.32 0"/></svg>',
    "shield_check": '<svg class="svg-icon" xmlns="http://www.w3.org/2000/svg" width="{s}" height="{s}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M20 13c0 5-3.5 7.5-7.66 8.95a1 1 0 0 1-.67-.01C7.5 20.5 4 18 4 13V6a1 1 0 0 1 1-1c2 0 4.5-1.2 6.24-2.72a1.17 1.17 0 0 1 1.52 0C14.51 3.81 17 5 19 5a1 1 0 0 1 1 1z"/><path d="m9 12 2 2 4-4"/></svg>',
    "trending_up": '<svg class="svg-icon" xmlns="http://www.w3.org/2000/svg" width="{s}" height="{s}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><polyline points="22 7 13.5 15.5 8.5 10.5 2 17"/><polyline points="16 7 22 7 22 13"/></svg>',
    "git_branch": '<svg class="svg-icon" xmlns="http://www.w3.org/2000/svg" width="{s}" height="{s}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><line x1="6" x2="6" y1="3" y2="15"/><circle cx="18" cy="6" r="3"/><circle cx="6" cy="18" r="3"/><path d="M18 9a9 9 0 0 1-9 9"/></svg>',
    "cloud": '<svg class="svg-icon" xmlns="http://www.w3.org/2000/svg" width="{s}" height="{s}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M17.5 19H9a7 7 0 1 1 6.71-9h1.79a4.5 4.5 0 1 1 0 9Z"/></svg>',
    "medal": '<svg class="svg-icon" xmlns="http://www.w3.org/2000/svg" width="{s}" height="{s}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M7.21 15 2.66 7.14a2 2 0 0 1 .13-2.2L4.4 2.8A2 2 0 0 1 6 2h12a2 2 0 0 1 1.6.8l1.6 2.14a2 2 0 0 1 .14 2.2L16.79 15"/><path d="M11 12 5.12 2.2"/><path d="m13 12 5.88-9.8"/><path d="M8 7h8"/><circle cx="12" cy="17" r="5"/><path d="M12 18v-2h-.5"/></svg>',
}


def svg_icon(name: str, size: int = 18) -> str:
    """Return pure inline vector SVG markup."""
    template = SVG_ICONS.get(name, SVG_ICONS["zap"])
    return template.format(s=size)


def icon_box(name: str, size: int = 20, sm: bool = False) -> str:
    """Return a styled glowing frosted glass vector icon badge."""
    cls = "icon-box sm" if sm else "icon-box"
    return f'<span class="{cls}">{svg_icon(name, size)}</span>'


st.set_page_config(
    page_title="Dev Kotak · Software & Machine Learning Engineer",
    page_icon=str(ROOT / "assets" / "phot.jpeg") if (ROOT / "assets" / "phot.jpeg").exists() else "⚡",
    layout="wide",
    initial_sidebar_state="expanded",
)


def init_db() -> None:
    """Initialize SQLite database to safely preserve contact form inquiries."""
    try:
        db_path = ROOT / "portfolio_contacts.db"
        conn = sqlite3.connect(db_path)
        cur = conn.cursor()
        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS inquiries (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                subject TEXT,
                message TEXT NOT NULL,
                submitted_at TEXT NOT NULL
            )
            """
        )
        conn.commit()
        conn.close()
    except Exception:
        pass


def save_inquiry(name: str, email_address: str, subject: str, message: str) -> bool:
    """Save an incoming contact inquiry to the database."""
    try:
        db_path = ROOT / "portfolio_contacts.db"
        conn = sqlite3.connect(db_path)
        cur = conn.cursor()
        cur.execute(
            """
            INSERT INTO inquiries (name, email, subject, message, submitted_at)
            VALUES (?, ?, ?, ?, ?)
            """,
            (name, email_address, subject, message, datetime.utcnow().isoformat()),
        )
        conn.commit()
        conn.close()
        return True
    except Exception:
        return False


def safe(value: object) -> str:
    """Escape HTML content safely."""
    return html.escape(str(value), quote=True)


def as_data_uri(path: Path) -> str | None:
    """Convert a file into an inline base64 Data URI for fast, zero-flicker loading."""
    if not path.exists():
        return None
    mime = MIME_BY_SUFFIX.get(path.suffix.lower(), "application/octet-stream")
    return f"data:{mime};base64,{base64.b64encode(path.read_bytes()).decode()}"


def initials(name: str) -> str:
    words = [w for w in name.split() if w]
    return "".join(w[0].upper() for w in words[:2]) or "?"


def tag_row(items: list[str]) -> None:
    markup = " ".join(f'<span class="tag">{safe(item)}</span>' for item in items)
    st.markdown(f'<div class="tag-row">{markup}</div>', unsafe_allow_html=True)


def tag_html(items: list[str]) -> str:
    return " ".join(f'<span class="tag">{safe(item)}</span>' for item in items)


# Safe navigation state handler to avoid widget modification exception
if "target_nav" in st.session_state and st.session_state.target_nav:
    st.session_state.nav = st.session_state.target_nav
    st.session_state.target_nav = None

if "nav" not in st.session_state or st.session_state.nav not in NAV_ITEMS:
    st.session_state.nav = "Overview"


def set_page(name: str) -> None:
    """Helper to trigger navigation safely without widget instantiation conflict."""
    for item in NAV_ITEMS:
        if name.lower() in item.lower():
            st.session_state.target_nav = item
            st.rerun()
            return
    st.session_state.target_nav = name
    st.rerun()


def section_header(kicker: str, title: str, description: str | None = None, icon_name: str = "zap") -> None:
    st.markdown(f'<p class="section-kicker">{svg_icon(icon_name, 14)} {safe(kicker)}</p>', unsafe_allow_html=True)
    st.title(title)
    if description:
        st.markdown(f'<p class="section-description">{safe(description)}</p>', unsafe_allow_html=True)


def site_footer() -> None:
    st.markdown(
        f"""
        <footer class="site-footer">
          <div>
            <span>{svg_icon("zap", 14)} <strong>Dev Kotak</strong></span> · <span>Software &amp; Machine Learning Engineer</span> · <span>{svg_icon("map_pin", 13)} {LOCATION}</span>
          </div>
          <div class="footer-social">
            <a href="{LINKEDIN}" target="_blank" rel="noreferrer" title="LinkedIn">{svg_icon("linkedin", 17)}</a>
            <a href="{GITHUB}" target="_blank" rel="noreferrer" title="GitHub">{svg_icon("github", 17)}</a>
            <a href="mailto:{EMAIL}" title="Email">{svg_icon("mail", 17)}</a>
          </div>
        </footer>
        """,
        unsafe_allow_html=True,
    )


def timeline_item(role: dict[str, object]) -> None:
    company = str(role["company"])
    logo = role.get("logo")
    if logo and (ROOT / str(logo)).exists():
        uri = as_data_uri(ROOT / str(logo))
        logo_html = f'<div class="timeline-logo-box"><img class="timeline-logo" src="{uri}" alt="{safe(company)}" /></div>' if uri else ""
    else:
        logo_html = f'<div class="timeline-logo-box"><span class="timeline-logo timeline-logo-fallback">{initials(company)}</span></div>'
    bullets = "".join(f"<li><span class=\"bullet-icon\">{svg_icon('check', 10)}</span> <span>{safe(b)}</span></li>" for b in role["bullets"])
    st.markdown(
        f"""
        <div class="timeline-item">
          <span class="timeline-marker"></span>
          <div class="timeline-card">
            <div class="timeline-head">
              {logo_html}
              <div class="timeline-title">
                <h3>{safe(role['role'])}</h3>
                <p class="company">{safe(company)}</p>
              </div>
              <span class="date-pill">{svg_icon('calendar', 12)} {safe(role['date'])}</span>
            </div>
            <p class="summary">{safe(role['summary'])}</p>
            <ul class="timeline-bullets">{bullets}</ul>
            <div class="tag-row">{tag_html(role["tags"])}</div>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


POSTER_BY_PROJECT = {
    "Tone Topic": "graphic-topics.png",
    "Digital Yoga Trainer": "graphic-pose.png",
    "InsightSync": "graphic-data.png",
    "Multi-label Dataset Prediction": "graphic-ensemble.png",
    "FabriSense": "graphic-fabric.png",
    "Hydrological Basin Flux Estimator": "graphic-basin.png",
}


def project_media_html(title: str) -> str:
    """Share project illustrations and reduced-motion posters across both pages."""
    poster_name = POSTER_BY_PROJECT.get(title)
    if not poster_name:
        return ""
    path = ROOT / "images" / "gifs" / poster_name
    poster_uri = as_data_uri(path)
    if not poster_uri:
        return ""
    image_uri = poster_uri
    if st.session_state.get("animate_previews", True):
        image_uri = as_data_uri(path.with_suffix(".gif")) or poster_uri
    return (
        '<picture class="project-media">'
        f'<source media="(prefers-reduced-motion: reduce)" srcset="{poster_uri}" />'
        f'<img src="{image_uri}" alt="{safe(title)} — conceptual illustration, not a live demo" '
        'width="640" height="360" loading="lazy" />'
        '</picture>'
    )


def project_card(project: dict[str, object], image_path: str | None = None) -> None:
    with st.container(border=True, key=f"project_card_{initials(str(project['title']))}"):
        preview, content = st.columns([1, 2], gap="medium")
        with preview:
            media_html = project_media_html(str(project["title"]))
            if media_html:
                st.markdown(f'<div class="card-gif">{media_html}</div>', unsafe_allow_html=True)
            elif image_path and (ROOT / image_path).exists():
                img_uri = as_data_uri(ROOT / image_path)
                if img_uri:
                    st.markdown(
                        f'<div class="card-gif"><img src="{img_uri}" alt="{safe(project["title"])}" loading="lazy" /></div>',
                        unsafe_allow_html=True,
                    )
            tag_row(project["tags"])
        with content:
            st.markdown(f'<p class="project-type">{svg_icon("sparkles", 12)} {safe(project["type"])}</p>', unsafe_allow_html=True)
            st.subheader(str(project["title"]))
            st.write(str(project["description"]))
            st.markdown(
                f'<div class="project-outcome-box"><span class="outcome-icon">{svg_icon("target", 14)}</span> <span><strong>{safe(project["outcome_label"])}:</strong> {safe(project["outcome"])}</span></div>',
                unsafe_allow_html=True,
            )
            btn_cols = st.columns(2)
            if project.get("demo"):
                with btn_cols[0]:
                    st.link_button("Open Live App ↗", str(project["demo"]), width="stretch")
            if project.get("repo") and project.get("repo") != project.get("demo"):
                col_target = btn_cols[1] if project.get("demo") else btn_cols[0]
                with col_target:
                    st.link_button(str(project.get("repo_label", "View GitHub ↗")), str(project["repo"]), width="stretch")
            deep_dive = project.get("deep_dive")
            if deep_dive:
                with st.expander("Technical Architecture & System Details"):
                    st.write(deep_dive)


# Initialize Database
init_db()

# Keep the theme switch mounted on every page so the choice survives navigation.
dark_mode = st.sidebar.toggle("Dark mode", value=True, key="dark_mode")
st.sidebar.toggle(
    "Animate previews", value=True, key="animate_previews",
    help="Turn off for static illustrations. Your system's reduced-motion preference always takes priority.",
)
stylesheets = ["graphic.css"]
if dark_mode:
    stylesheets.append("graphic-dark.css")
style_text = "\n".join(
    (ROOT / "styles" / stylesheet).read_text(encoding="utf-8-sig")
    for stylesheet in stylesheets
)
st.markdown(f"<style>{style_text}</style>", unsafe_allow_html=True)

# Prepare Assets
profile_path = ROOT / "assets" / "phot.jpeg"
resume_path = ROOT / "Resume-Dev.pdf"
if not resume_path.exists():
    resume_path = ROOT / "assets" / "Profile.pdf"

profile_uri = as_data_uri(profile_path)
resume_uri = as_data_uri(resume_path)

# Sidebar Branded Navigation with Vector Icons
with st.sidebar:
    st.markdown(
        '<p class="wordmark">Dev Kotak<b>.</b></p>'
        '<p class="sidebar-role">Software &amp; Machine Learning Engineer</p>',
        unsafe_allow_html=True,
    )
    st.divider()
    page = st.radio("Navigation", NAV_ITEMS, label_visibility="collapsed", key="nav")
    st.divider()
    if resume_path.exists():
        st.download_button(
            "Download Résumé PDF ⤓",
            resume_path.read_bytes(),
            "Dev-Kotak-Resume.pdf",
            "application/pdf",
            width="stretch",
            key="sidebar_resume_download",
        )
    st.markdown('<p class="sidebar-note">BASED IN OTTAWA, CANADA</p>', unsafe_allow_html=True)


# =========================================================================
# 1. OVERVIEW / HERO
# =========================================================================
if page == "Overview":
    portrait_html = (
        f'<img src="{profile_uri}" alt="Portrait of Dev Kotak" />'
        if profile_uri
        else '<div class="portrait-placeholder">DK</div>'
    )
    st.markdown(
        f"""
        <div class="graphic-masthead"><span>Independent thinking. Applied engineering.</span><span>Portfolio / 2026</span></div>
        <section class="graphic-hero">
          <div>
            <p class="section-kicker">Dev Kotak / Software &amp; ML</p>
            <h1>Complex data.<br><span>Useful software.</span></h1>
            <p class="hero-intro">I turn data and machine learning models into applications people can actually use. M.Eng graduate from Carleton University, working across software systems, computer vision, and natural language processing.</p>
          </div>
          <figure class="hero-art">{portrait_html}<figcaption><span>Dev Kotak</span><span>Ottawa, Canada</span></figcaption></figure>
        </section>
        """,
        unsafe_allow_html=True,
    )
    if st.button("Explore projects ↗", key="hero_explore_btn", type="primary"):
        set_page("Projects")

    st.markdown('<div class="graphic-section-head"><h2>Selected work</h2><span>01 — 03 / Software in practice</span></div>', unsafe_allow_html=True)
    selected_work = [
        ("01", "NLP · Web application", "Tone Topic",
         "Making unstructured text easier to explore through topic modeling and document categorization.",
         "https://tonetopic.streamlit.app/", "Open application"),
        ("02", "Computer vision", "Digital Yoga Trainer",
         "Turning pose landmarks into real-time posture feedback with MediaPipe and OpenCV.",
         "https://github.com/dev856/Yoga-Pose-Estimation", "Explore repository"),
        ("03", "Machine learning", "Multi-label Dataset Prediction",
         "Combining Random Forest estimators and a logistic meta-learner for multi-label classification.",
         None, None),
    ]
    for index, category, title, description, url, link_label in selected_work:
        image_html = project_media_html(title)
        link_html = f'<a class="text-link" href="{safe(url)}" target="_blank" rel="noreferrer">{safe(link_label)} ↗</a>' if url else ""
        row_class = "work-row reverse" if index == "02" else "work-row"
        st.markdown(
            f'<article class="{row_class}"><figure class="work-image">{image_html}</figure>'
            f'<div class="work-copy"><span class="work-number">{index} / {safe(category)}</span>'
            f'<h3>{safe(title)}</h3><p>{safe(description)}</p>{link_html}</div></article>',
            unsafe_allow_html=True,
        )

    st.markdown(
        '<div class="graphic-section-head"><h2>Research meets delivery.</h2><span>The short version</span></div>'
        '<section class="career-strip"><div><p>From satellite hydrology to backend integrations, my work pairs analytical modeling with dependable software delivery.</p></div>'
        '<div>'
        '<div class="career-entry"><strong>Ottawa Centre for Cognitive Therapy</strong><span>Software integration &amp; automated data workflows</span></div>'
        '<div class="career-entry"><strong>Space Applications Centre, ISRO</strong><span>Geospatial machine learning research</span></div>'
        '<div class="career-entry"><strong>Carleton University</strong><span>M.Eng · Electrical &amp; Computer Engineering · Data Science</span></div>'
        '</div></section>',
        unsafe_allow_html=True,
    )
    if st.button("Full experience →", key="overview_experience_btn"):
        set_page("Experience")
    st.markdown(
        f"""
        <section class="contact-banner">
          <p class="section-kicker">Have something in mind?</p>
          <h2>Let's build something useful.</h2>
          <p>Open to software engineering and applied machine learning opportunities.</p>
          <a href="mailto:{EMAIL}">Start a conversation ↗</a>
        </section>
        """,
        unsafe_allow_html=True,
    )


# =========================================================================
# 2. ABOUT SECTION
# =========================================================================
elif page == "About":
    section_header(
        "About Dev Kotak",
        "Driven by engineering rigor, analytical depth, and clear communication.",
        "A background spanning software engineering, machine learning research, and interactive data products.",
        icon_name="user",
    )

    about_col1, about_col2 = st.columns([1.1, 0.9], vertical_alignment="top")

    with about_col1:
        with st.container(border=True):
            st.markdown(f'<h3 class="h3-icon">{svg_icon("users", 19)} Professional Narrative</h3>', unsafe_allow_html=True)
            st.write(
                "I am a **Software & Machine Learning Engineer** holding a **Master of Engineering (M.Eng) in Electrical & Computer Engineering with a Collaborative Specialization in Data Science** from **Carleton University** in Ottawa, Canada."
            )
            st.write(
                "My experience combines academic rigor with hands-on industry application. Having completed **7 appointments across research institutes, dynamic AI startups, and healthcare platforms**, I have built software ranging from satellite hydrological forecasting at the **Space Applications Centre (ISRO)** to automated client workflows at the **Ottawa Centre for Cognitive Therapy**."
            )
            st.write(
                "I specialize in bridging the gap between theoretical machine learning models and usable, dependable software applications. I prioritize code maintainability, clean API design, and intuitive user experiences."
            )

    with about_col2:
        with st.container(border=True):
            st.markdown(f'<h3 class="h3-icon">{svg_icon("lightbulb", 19)} Engineering Philosophy</h3>', unsafe_allow_html=True)
            st.markdown(
                """
                - **Data-Driven Precision:** Every architectural and modeling decision is validated through empirical metrics, baseline comparisons, and rigorous cross-validation.
                - **Production-First Mindset:** Models are only as valuable as their ability to reliably serve users via clean APIs, low latency, and robust error handling.
                - **Simplicity & Usability:** Complex data workflows should be encapsulated into frictionless interfaces that empower domain experts and stakeholders.
                """
            )
            tag_row(["Deterministic APIs", "Empirical Evaluation", "Clean Architecture", "Continuous Learning"])

    st.write("")
    st.markdown("### Focus Areas & Capabilities")
    focus_c1, focus_c2, focus_c3 = st.columns(3)
    with focus_c1:
        with st.container(border=True):
            st.markdown(f"{icon_box('brain', 20, sm=True)} &nbsp; **01. Machine Learning Systems**", unsafe_allow_html=True)
            st.write(
                "Supervised & unsupervised learning, ensemble stacking, feature extraction, NLP topic modeling, model interpretability, and hyperparameter optimization."
            )
    with focus_c2:
        with st.container(border=True):
            st.markdown(f"{icon_box('eye', 20, sm=True)} &nbsp; **02. Computer Vision & Signals**", unsafe_allow_html=True)
            st.write(
                "Real-time pose estimation, geometric joint angle calculations, anomaly defect detection, OpenCV spatial filtering, and convolutional neural nets."
            )
    with focus_c3:
        with st.container(border=True):
            st.markdown(f"{icon_box('layers', 20, sm=True)} &nbsp; **03. Backend & Full-Stack**", unsafe_allow_html=True)
            st.write(
                "RESTful API design, JSON workflow automation, schema modeling in PostgreSQL & MongoDB, Streamlit interactive applications, and Plotly visual dashboards."
            )

# =========================================================================
# 3. PROJECTS SECTION
# =========================================================================
elif page == "Projects":
    st.markdown('<span id="projects"></span>', unsafe_allow_html=True)
    section_header(
        "Selected Projects",
        "Work I can explain end to end.",
        "Each project highlights the real-world problem, architectural implementation details, and measurable technical outcomes.",
        icon_name="code",
    )

    # Project Definitions (Unified Matrix)
    all_projects = [
        {
            "category": "NLP",
            "type": "Featured Flagship Project · Natural Language Processing",
            "title": "Tone Topic",
            "description": "An interactive NLP application that transforms raw unstructured text or uploaded CSV documents into explorable semantic topic models using Latent Dirichlet Allocation (LDA) and NLTK tokenization.",
            "outcome_label": "Key Outcome",
            "outcome": "Real-time semantic topic distribution & token extraction",
            "tags": ["Python", "Streamlit", "NLTK", "Gensim", "Pandas", "Topic Modeling", "LDA"],
            "demo": "https://tonetopic.streamlit.app/",
            "repo": "https://tonetopic.streamlit.app/",
            "repo_label": "Open Live Application ↗",
            "image": "images/screen06.jpg",
            "deep_dive": "1. Text Preprocessing: Tokenization, stop-word removal, lemmatization, and n-gram phrase detection using NLTK and Gensim.\n2. Vector Space Modeling: Bag-of-Words (BoW) corpus mapping with TF-IDF filtering.\n3. Inference & Visualization: Multithreaded LDA model fitting with coherence score optimization (C_v).",
        },
        {
            "category": "Computer Vision",
            "type": "Computer Vision & Pose Estimation",
            "title": "Digital Yoga Trainer",
            "description": "Real-time pose estimation and posture correction system using MediaPipe landmark detection and OpenCV angular calculations to deliver instant bio-mechanical feedback.",
            "outcome_label": "Key Outcome",
            "outcome": "Live posture joint tracking and real-time corrective feedback",
            "tags": ["Python", "MediaPipe", "OpenCV", "NumPy", "Real-time Vision", "Biomechanics"],
            "repo": "https://github.com/dev856/Yoga-Pose-Estimation",
            "repo_label": "View GitHub Repository ↗",
            "image": "images/Tadasana.jpg",
            "deep_dive": "Calculates 3D landmark Euclidean vectors across shoulder-elbow-wrist and hip-knee-ankle joints. Measures angular deviations against canonical reference postures to deliver corrective auditory and visual overlays at 30+ FPS.",
        },
        {
            "category": "Data Analytics",
            "type": "Data Analytics & Exploration Workbench",
            "title": "InsightSync",
            "description": "Interactive data analytics platform enabling multi-variate statistical distributions, correlation matrices, dynamic filtering, and automated exploratory visual charts for complex datasets.",
            "outcome_label": "Key Outcome",
            "outcome": "Instant exploratory analysis & dynamic interactive Plotly charts",
            "tags": ["Python", "Streamlit", "Plotly", "Pandas", "Data Analytics", "EDA"],
            "demo": "https://insight-sync.streamlit.app/",
            "repo": GITHUB,
            "repo_label": "Explore GitHub Profile ↗",
            "deep_dive": "Automates exploratory data analysis (EDA) with automatic column type inference, missingness analysis, Pearson/Spearman correlation heatmaps, and customizable statistical distribution visualizations.",
        },
        {
            "category": "Machine Learning",
            "type": "Ensemble Machine Learning",
            "title": "Multi-label Dataset Prediction",
            "description": "A competition-grade modeling architecture combining Random Forest base estimators with a Logistic Regression meta-classifier for complex multi-label predictive tasks.",
            "outcome_label": "Measured Result",
            "outcome": "75% measured classification accuracy on competitive benchmark",
            "tags": ["Python", "Scikit-Learn", "Pandas", "Meta-learning", "Ensemble Stacking"],
            "repo": GITHUB,
            "repo_label": "Explore GitHub Profile ↗",
            "deep_dive": "Employs stratified k-fold out-of-fold validation to generate meta-features across diverse tree ensembles, mitigating label correlation biases and maximizing generalization accuracy.",
        },
        {
            "category": "Computer Vision",
            "type": "Computer Vision & Manufacturing",
            "title": "FabriSense",
            "description": "Automated textile inspection and defect detection solution utilizing computer vision preprocessing, spatial feature extraction, and classification algorithms.",
            "outcome_label": "Key Outcome",
            "outcome": "Automated anomaly identification & surface inspection",
            "tags": ["Python", "Streamlit", "OpenCV", "Image Processing", "Defect Detection"],
            "demo": "http://fabrisense.streamlit.app/",
            "repo": GITHUB,
            "repo_label": "Explore GitHub Profile ↗",
            "deep_dive": "Applies adaptive thresholding, morphological filtering, and spatial frequency analysis to identify weaving defects, stains, and structural anomalies in industrial fabric feeds.",
        },
        {
            "category": "Machine Learning",
            "type": "Geospatial Modeling & Remote Sensing",
            "title": "Hydrological Basin Flux Estimator",
            "description": "Geospatial machine learning models developed at ISRO benchmarked across XGBoost, LSTM neural networks, and Random Forests for discharge forecasting from MODIS and ERA5 satellite data.",
            "outcome_label": "Key Outcome",
            "outcome": "Accurate river discharge prediction across Indian river basins",
            "tags": ["Python", "Google Earth Engine", "XGBoost", "LSTM", "Geospatial Data"],
            "repo": GITHUB,
            "repo_label": "Explore GitHub Profile ↗",
            "deep_dive": "Ingests multi-spectral satellite observations, precipitation grids, and digital elevation models to model non-linear runoff dynamics using temporal recurrent networks.",
        },
    ]

    # Search & Filter Controls
    if "project_filter" not in st.session_state:
        st.session_state.project_filter = "All"

    def reset_project_filters() -> None:
        """Reset widget state before Streamlit renders the search controls."""
        st.session_state.proj_search_input = ""
        st.session_state.project_filter = "All"

    search_col, reset_col = st.columns([3.2, 0.8], vertical_alignment="bottom")
    with search_col:
        search_query = st.text_input(
            "Filter by keyword, framework, or algorithm",
            placeholder="e.g. MediaPipe, XGBoost, Streamlit, OpenCV, Topic Modeling, 31 FPS, LSTM...",
            key="proj_search_input",
        ).strip().lower()
    with reset_col:
        st.button("Clear Search", key="clear_search_btn", width="stretch", on_click=reset_project_filters)

    def matches_project(p: dict[str, object], q: str) -> bool:
        if not q:
            return True
        searchable_text = " ".join([
            str(p.get("title", "")),
            str(p.get("category", "")),
            str(p.get("type", "")),
            str(p.get("description", "")),
            str(p.get("outcome", "")),
            str(p.get("deep_dive", "")),
            " ".join(p.get("tags", [])),
        ]).lower()
        return q in searchable_text

    matching_search = [p for p in all_projects if matches_project(p, search_query)]

    cat_counts = {
        "All": len(matching_search),
        "NLP": sum(1 for p in matching_search if p["category"] == "NLP"),
        "Computer Vision": sum(1 for p in matching_search if p["category"] == "Computer Vision"),
        "Machine Learning": sum(1 for p in matching_search if p["category"] == "Machine Learning"),
        "Data Analytics": sum(1 for p in matching_search if p["category"] == "Data Analytics"),
    }

    categories = [
        ("All", f"All ({cat_counts['All']})"),
        ("NLP", f"NLP ({cat_counts['NLP']})"),
        ("Computer Vision", f"Vision ({cat_counts['Computer Vision']})"),
        ("Machine Learning", f"ML ({cat_counts['Machine Learning']})"),
        ("Data Analytics", f"Analytics ({cat_counts['Data Analytics']})"),
    ]

    f_cols = st.columns(len(categories))
    for i, (cat_val, label) in enumerate(categories):
        with f_cols[i]:
            btn_type = "primary" if st.session_state.project_filter == cat_val else "secondary"
            if st.button(label, key=f"cat_btn_{cat_val}", type=btn_type, width="stretch"):
                st.session_state.project_filter = cat_val
                st.rerun()

    current_filter = st.session_state.project_filter

    filtered_projects = [
        p for p in matching_search
        if current_filter == "All" or p["category"] == current_filter
    ]

    st.markdown(
        f"""
        <div class="filter-result-meta">
          {svg_icon('activity', 13)} Showing {len(filtered_projects)} of {len(all_projects)} production projects {f'matching "{safe(search_query)}"' if search_query else ''}
        </div>
        """,
        unsafe_allow_html=True,
    )

    if not filtered_projects:
        st.warning(f'No projects found matching query "{search_query}" in category "{current_filter}".')
        st.button("Reset Search Filters", key="reset_empty_search", type="primary", on_click=reset_project_filters)
    else:
        for proj in filtered_projects:
            project_card(proj, image_path=proj.get("image"))

# =========================================================================
# 4. EXPERIENCE SECTION
# =========================================================================
elif page == "Experience":
    section_header(
        "Experience & Appointments",
        "From research prototypes to production workflows.",
        "Current-first timeline detailing responsibilities, software architectures, and measurable technical achievements.",
        icon_name="briefcase",
    )

    roles = [
        {
            "date": "Jul 2024 — Present",
            "role": "Computer Science Student & Technical Contributor",
            "company": "Ottawa Centre for Cognitive Therapy",
            "summary": "Engineering automated data workflows, cross-platform system integrations, and administrative pipelines across EHR and client scheduling platforms.",
            "bullets": [
                "Implemented robust REST API integrations that streamlined cross-platform data synchronization and improved interaction efficiency by 50%.",
                "Designed deterministic JSON-based scheduling workflows and automation scripts that increased overall system responsiveness by 30%.",
                "Conducted data audit routines and structured schema mappings to guarantee data consistency and patient record privacy.",
            ],
            "tags": ["REST APIs", "JSON", "System Integration", "Workflow Automation", "Python", "Data Synchronization"],
        },
        {
            "date": "Dec 2022 — May 2023",
            "role": "Research Intern",
            "company": "Space Applications Centre, ISRO",
            "summary": "Applied geospatial data science and advanced machine learning to hydrological flux estimation and discharge forecasting across Indian river basins.",
            "bullets": [
                "Extracted and processed multi-spectral MODIS, CHIRPS, ERA5/CFSR, and TRMM satellite observations using Python and Google Earth Engine.",
                "Benchmarked XGBoost, LSTM neural networks, and Random Forest regressors for discharge forecasting and hydraulic parameter modeling.",
                "Optimized feature engineering pipelines across temporal and spatial dimensions to improve cross-basin generalization.",
            ],
            "tags": ["Python", "Google Earth Engine", "XGBoost", "LSTM", "Geospatial Data", "Remote Sensing"],
            "logo": "images/isro1.jpeg",
        },
        {
            "date": "Dec 2022 — Feb 2023",
            "role": "Machine Learning Intern",
            "company": "Jupiter AI Labs",
            "summary": "Engineered applied ML case studies, statistical modeling pipelines, and AI-assisted workflows for client deliveries.",
            "bullets": [
                "Executed end-to-end data pipelines covering SQL extraction, exploratory data analysis, hypothesis testing, and model evaluation.",
                "Integrated prompt-engineering patterns and LLM workflows into internal Python development and project delivery.",
                "Delivered technical presentations and visual analytics dashboards for stakeholder decision-making.",
            ],
            "tags": ["Python", "SQL", "Machine Learning", "Prompt Engineering", "Data Modeling", "LLM Workflows"],
            "logo": "images/jupiter.png",
        },
        {
            "date": "Jun 2022 — Sep 2022",
            "role": "Data Science Intern",
            "company": "Zummit Infolabs",
            "summary": "Built computer vision prototypes for facial landmark detection, emotion classification, and real-time object tracking.",
            "bullets": [
                "Trained and evaluated facial landmark detectors with Dlib and convolutional emotion classifiers with TensorFlow.",
                "Constructed modular computer vision preprocessing pipelines and integrated YOLO-based object detection models.",
                "Optimized video stream frame capture to maintain 30+ FPS during real-time inference.",
            ],
            "tags": ["TensorFlow", "YOLO", "Dlib", "OpenCV", "Computer Vision", "Real-Time Inference"],
            "logo": "images/zummit.png",
        },
        {
            "date": "Jan 2022 — Apr 2022",
            "role": "Machine Learning Intern",
            "company": "CHARUSAT",
            "summary": "Implemented statistical machine learning and predictive modeling algorithms for academic research initiatives.",
            "bullets": [
                "Conducted exploratory feature engineering and supervised model training using Scikit-Learn and Pandas.",
                "Prepared technical documentation and validation metrics comparing model performance across benchmark datasets.",
            ],
            "tags": ["Python", "Scikit-Learn", "Pandas", "Statistical Modeling", "Academic Research"],
            "logo": "images/charusat.jpg",
        },
        {
            "date": "Jun 2021 — Jul 2021",
            "role": "Node.js Intern",
            "company": "Kintu Designs",
            "summary": "Developed backend RESTful services, database schemas, and integration endpoints for dynamic web platforms.",
            "bullets": [
                "Built asynchronous API routes with Express.js and structured NoSQL schemas in MongoDB.",
                "Collaborated with frontend engineers to ensure low-latency JSON payload delivery.",
            ],
            "tags": ["Node.js", "Express", "MongoDB", "REST APIs", "Backend Engineering"],
            "logo": "images/kintu.jpeg",
        },
        {
            "date": "May 2021 — Jun 2021",
            "role": "Data Science & Business Analytics Intern",
            "company": "The Sparks Foundation",
            "summary": "Executed exploratory data analytics and predictive modeling for business intelligence case studies.",
            "bullets": [
                "Identified key business trends and performance drivers through statistical visualizations and regression modeling.",
                "Presented findings with actionable insights and interactive visual charts.",
            ],
            "tags": ["Python", "Data Science", "Exploratory Analysis", "Visualization", "Business Intelligence"],
            "logo": "images/spark.png",
        },
    ]

    st.markdown('<div class="timeline">', unsafe_allow_html=True)
    for role in roles:
        timeline_item(role)
    st.markdown("</div>", unsafe_allow_html=True)

# =========================================================================
# 5. SKILLS SECTION
# =========================================================================
elif page == "Skills":
    section_header(
        "Capabilities & Stack",
        "Skills backed by applied engineering.",
        "Grouped by technical domain, showing how each tool is leveraged in real production and research environments.",
        icon_name="terminal",
    )

    groups = [
        (
            "01",
            "terminal",
            "Software & Systems",
            "Backend logic, API architectures, schema design, and dependable data pipelines.",
            ["Python", "SQL", "REST APIs", "JSON", "Java", "Node.js", "MongoDB", "C/C++", "Linux", "Docker Basics"],
        ),
        (
            "02",
            "brain",
            "Data Science & ML",
            "Statistical modeling, model evaluation, NLP pipelines, and computer vision algorithms.",
            ["Pandas", "NumPy", "Scikit-Learn", "TensorFlow", "PyTorch", "NLTK", "OpenCV", "MediaPipe", "Gensim", "XGBoost"],
        ),
        (
            "03",
            "layers",
            "Product & Delivery",
            "Interactive dashboards, cloud environments, version control, and stakeholder interfaces.",
            ["Streamlit", "Plotly", "Git", "GitHub", "Google Cloud", "HTML5 / CSS3", "Agile / Scrum"],
        ),
    ]

    cards = "".join(
        f'<section class="skill-card skill-domain-{index}">'
        f'<div class="skill-card-top"><span class="skill-emblem">{svg_icon(icon_n, 30)}</span><span class="skill-index">{index}</span></div>'
        f"<div>"
        f"<h3>{safe(title)}</h3>"
        f"<p>{safe(summary)}</p>"
        f"</div>"
        '<ul class="skill-tools">'
        + ''.join(f'<li>{safe(skill)}</li>' for skill in skills)
        + '</ul></section>'
        for index, icon_n, title, summary, skills in groups
    )
    st.markdown(f'<div class="skill-grid">{cards}</div>', unsafe_allow_html=True)

    st.write("")
    st.markdown("### Engineering Methodologies")
    meth_left, meth_right = st.columns(2)
    with meth_left:
        with st.container(border=False, key="skill_method_evaluation"):
            st.markdown(f'{icon_box("atom", 18, sm=True)} &nbsp; **Applied Machine Learning & Evaluation**', unsafe_allow_html=True)
            st.write(
                "Experience selecting appropriate model architectures (tree ensembles, neural networks, linear meta-models), conducting stratified cross-validation, and optimizing metrics beyond basic accuracy (precision, recall, ROC-AUC, F1-score)."
            )
            tag_row(["Cross-Validation", "Hyperparameter Tuning", "Ensemble Stacking", "Feature Importance"])

    with meth_right:
        with st.container(border=False, key="skill_method_integration"):
            st.markdown(f'{icon_box("workflow", 18, sm=True)} &nbsp; **Systems Integration & API Design**', unsafe_allow_html=True)
            st.write(
                "Experience connecting disparate software systems via structured RESTful APIs, designing deterministic JSON schema contracts, and automating repetitive data synchronization tasks with high reliability."
            )
            tag_row(["REST Architecture", "JSON Schemas", "Authentication Flows", "Asynchronous Processing"])

# =========================================================================
# 6. EDUCATION SECTION
# =========================================================================
elif page == "Education":
    section_header(
        "Academic Credentials",
        "A rigorous systems foundation with a data science focus.",
        "The academic coursework and specialized training behind the software engineering and machine learning practice.",
        icon_name="graduation",
    )

    carleton_uri = as_data_uri(ROOT / "images" / "carleton.jpg")
    charusat_uri = as_data_uri(ROOT / "images" / "charusat.jpg")

    carleton_img_html = f'<div class="edu-logo-frame"><img class="edu-logo" src="{carleton_uri}" alt="Carleton University" /></div>' if carleton_uri else ""
    charusat_img_html = f'<div class="edu-logo-frame"><img class="edu-logo" src="{charusat_uri}" alt="CHARUSAT" /></div>' if charusat_uri else ""

    st.markdown(
        f"""
        <div class="edu-grid">
          <div class="edu-card">
            {carleton_img_html}
            <div style="display: flex; gap: 0.45rem; flex-wrap: wrap; margin-bottom: 0.6rem;">
              <span class="date-pill">{svg_icon('calendar', 12)} 2023 — 2025 · Graduate</span>
              <span class="pill-chip">{svg_icon('award', 12)} Verified M.Eng</span>
            </div>
            <h3>Master of Engineering</h3>
            <p>Electrical &amp; Computer Engineering · Collaborative Specialization in Data Science</p>
            <p><strong>CGPA:</strong> 10.5 / 12.0 &nbsp;·&nbsp; <strong>Location:</strong> Ottawa, Canada</p>
            <strong class="edu-school">Carleton University</strong>
          </div>
          <div class="edu-card">
            {charusat_img_html}
            <div style="display: flex; gap: 0.45rem; flex-wrap: wrap; margin-bottom: 0.6rem;">
              <span class="date-pill">{svg_icon('calendar', 12)} 2019 — 2023 · Undergraduate</span>
              <span class="pill-chip">{svg_icon('star', 12)} Merit Scholar</span>
            </div>
            <h3>Bachelor of Technology</h3>
            <p>Computer Science &amp; Engineering</p>
            <p><strong>CGPA:</strong> 9.25 / 10.0 (WES: 3.92 / 4.0) &nbsp;·&nbsp; <strong>Merit Scholarship Awardee</strong></p>
            <strong class="edu-school">Charotar University of Science and Technology</strong>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.write("")
    st.markdown(f'<h3 class="h3-icon">{svg_icon("graduation", 19)} Academic Coursework</h3>', unsafe_allow_html=True)
    st.markdown(
        f"""
        <div class="coursework-grid">
          <div class="coursework-card">
            <h4>{svg_icon('cpu', 15)} Graduate Specialization</h4>
            <ul>
              <li>Applied Programming &amp; Algorithms</li>
              <li>Pattern Classification &amp; Machine Learning</li>
              <li>Advanced Data Visualization</li>
              <li>Data Science Seminar &amp; Research</li>
              <li>Cryptography &amp; Network Security</li>
            </ul>
          </div>
          <div class="coursework-card">
            <h4>{svg_icon('terminal', 15)} Computer Science Foundation</h4>
            <ul>
              <li>Data Structures &amp; Algorithms</li>
              <li>Database Management Systems (SQL)</li>
              <li>Operating Systems &amp; System Architecture</li>
              <li>Computer Networks &amp; Protocols</li>
              <li>Object-Oriented Programming (Java)</li>
            </ul>
          </div>
          <div class="coursework-card">
            <h4>{svg_icon('layers', 15)} Applied Engineering</h4>
            <ul>
              <li>Software Engineering Methodologies</li>
              <li>Artificial Intelligence &amp; Neural Nets</li>
              <li>Python for Scientific Computing</li>
              <li>Web Development &amp; Cloud Fundamentals</li>
              <li>Major Capstone Engineering Project</li>
            </ul>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

# =========================================================================
# 7. TESTIMONIALS SECTION
# =========================================================================
elif page == "Testimonials":
    section_header(
        "Endorsements & Feedback",
        "Collaborative feedback & peer highlights.",
        "Reflections on technical capability, collaborative problem-solving, and delivery quality.",
        icon_name="message",
    )

    st.markdown(
        f"""
        <div class="testimonial-grid">
          <div class="testimonial-card">
            <span class="quote-mark">{svg_icon('quote', 30)}</span>
            <span class="star-row">{svg_icon('star', 14)}{svg_icon('star', 14)}{svg_icon('star', 14)}{svg_icon('star', 14)}{svg_icon('star', 14)}</span>
            <p class="testimonial-quote">"Dev brings a remarkable blend of machine learning theory and practical software engineering. His ability to build robust data pipelines and translate complex models into actionable interfaces is outstanding."</p>
            <div class="testimonial-author">
              <div class="testimonial-author-avatar">RE</div>
              <div class="testimonial-author-info">
                <h4>Research &amp; Engineering Mentor</h4>
                <p>Applied AI &amp; Geospatial Science</p>
              </div>
            </div>
          </div>
          <div class="testimonial-card">
            <span class="quote-mark">{svg_icon('quote', 30)}</span>
            <span class="star-row">{svg_icon('star', 14)}{svg_icon('star', 14)}{svg_icon('star', 14)}{svg_icon('star', 14)}{svg_icon('star', 14)}</span>
            <p class="testimonial-quote">"Dev consistently delivers clean, dependable, and high-performance backend and data integration solutions. His technical curiosity and attention to detail make him an asset to any engineering team."</p>
            <div class="testimonial-author">
              <div class="testimonial-author-avatar">TL</div>
              <div class="testimonial-author-info">
                <h4>Technical Lead</h4>
                <p>Systems &amp; Product Integration</p>
              </div>
            </div>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

# =========================================================================
# 8. RÉSUMÉ SECTION
# =========================================================================
elif page == "Résumé":
    section_header(
        "Professional Résumé",
        "A concise view of credentials and experience.",
        "Download the current PDF for comprehensive appointments, technical skills, education, and projects.",
        icon_name="file_text",
    )

    st.markdown(
        f"""
        <div class="resume-panel">
          <p class="section-kicker">{svg_icon('download', 14)} Curriculum Vitae</p>
          <h3>Dev Kotak · Current Résumé</h3>
          <p>Complete record of academic credentials, software &amp; machine learning appointments, technical skills, and selected projects.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.write("")
    if resume_path.exists():
        st.download_button(
            "Download Résumé PDF ⤓",
            resume_path.read_bytes(),
            "Dev-Kotak-Resume.pdf",
            "application/pdf",
            type="primary",
        )
        st.caption("PDF document · Optimized for ATS and executive review")
    else:
        st.error("The résumé PDF is currently unavailable.")

    st.divider()
    st.markdown("### Executive Summary")
    summary_left, summary_right = st.columns(2)
    with summary_left:
        with st.container(border=True):
            st.markdown(f'{icon_box("award", 18, sm=True)} &nbsp; **Key Qualifications**', unsafe_allow_html=True)
            st.write(
                "- **Graduate Degree:** M.Eng in Electrical & Computer Engineering with Data Science Specialization from Carleton University.\n"
                "- **7 Appointments:** Experience across ISRO (Space Applications Centre), Ottawa Centre for Cognitive Therapy, Jupiter AI Labs, and Zummit Infolabs.\n"
                "- **Core Stack:** Python, SQL, REST APIs, Streamlit, Pandas, Scikit-Learn, TensorFlow, OpenCV, MediaPipe."
            )
    with summary_right:
        with st.container(border=True):
            st.markdown(f'{icon_box("target", 18, sm=True)} &nbsp; **Primary Competencies**', unsafe_allow_html=True)
            st.write(
                "- **Applied Machine Learning:** Classification, Regression, Ensemble Stacking, Evaluation Metrics.\n"
                "- **Computer Vision & NLP:** Pose estimation, Object Detection, Topic Modeling, Text Extraction.\n"
                "- **Product Delivery:** Rapid prototyping with Streamlit, Plotly visual analytics, RESTful backend APIs."
            )


# =========================================================================
# 9. CONTACT SECTION
# =========================================================================
elif page == "Contact":
    section_header(
        "Correspondence",
        "Have a problem to solve?",
        "Email and LinkedIn are the best channels for discussing roles, project collaborations, and technical opportunities.",
        icon_name="mail",
    )

    st.markdown(
        f"""
        <div class="letter-card">
          <p class="section-kicker">{svg_icon('mail', 14)} Direct Contact</p>
          <p class="letter-email"><a href="mailto:{EMAIL}">{EMAIL}</a></p>
          <p>{svg_icon('globe', 14)} Open to software engineering, data science, and applied machine learning roles in Ottawa, across Canada, and remotely.</p>
          <div class="contact-chips">
            <span class="contact-chip">{svg_icon('zap', 12)} Response &lt; 24h</span>
            <span class="contact-chip">{svg_icon('map_pin', 12)} Ottawa, ON</span>
            <span class="contact-chip">{svg_icon('globe', 12)} Remote Friendly</span>
          </div>
          <div class="contact-socials">
            <a href="{LINKEDIN}" target="_blank" rel="noreferrer">{svg_icon('linkedin', 14)} LinkedIn</a>
            <a href="{GITHUB}" target="_blank" rel="noreferrer">{svg_icon('github', 14)} GitHub</a>
            <a href="mailto:{EMAIL}">{svg_icon('mail', 14)} Email</a>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.write("")
    st.markdown(f'<h3 class="h3-icon">{svg_icon("send", 19)} Send a Direct Message</h3>', unsafe_allow_html=True)
    with st.form("contact_form", clear_on_submit=True):
        f_left, f_right = st.columns(2)
        with f_left:
            name = st.text_input("Your Name *", placeholder="e.g. Alex Morgan")
        with f_right:
            sender_email = st.text_input("Your Email *", placeholder="e.g. alex@company.com")
        subject = st.text_input("Subject", placeholder="e.g. Software Engineering Role / Project Discussion")
        message = st.text_area("Message *", placeholder="Write your message here...", height=140)
        submitted = st.form_submit_button("Send Message ↗", type="primary")

        if submitted:
            if not name.strip() or not sender_email.strip() or not message.strip():
                st.error("Please fill in all required fields (Name, Email, and Message).")
            elif "@" not in sender_email or "." not in sender_email:
                st.error("Please enter a valid email address.")
            else:
                saved = save_inquiry(name.strip(), sender_email.strip(), subject.strip(), message.strip())
                if saved:
                    st.success(f"Thank you, {safe(name)}! Your message has been safely received. I will respond to {safe(sender_email)} promptly.")
                else:
                    st.success(f"Thank you, {safe(name)}! Your message has been noted. You can also reach me directly at {EMAIL}.")


# Render Site Footer
site_footer()
