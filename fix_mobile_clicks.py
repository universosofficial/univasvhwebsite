"""
Fix mobile click blocking bug across all HTML files and CSS.
The bug was:
    .top {
        bottom: 16px !important;
        right: 14px !important;
        z-index: 99 !important;
    }
Which stretched <header class="top"> over the ENTIRE mobile screen, blocking all clicks.
This was intended for .up (the back-to-top floating button).
"""

import os
import glob

BASE_DIR = r"C:\Users\user\Downloads\websites\univasvhwebsite"
files = glob.glob(f"{BASE_DIR}/*.html") + [os.path.join(BASE_DIR, "templatemo-633-celadon-style.css")]

BUG_TARGET = """    .top {
        bottom: 16px !important;
        right: 14px !important;
        z-index: 99 !important;
    }"""

FIX_REPLACEMENT = """    .up {
        bottom: 16px !important;
        right: 14px !important;
        z-index: 99 !important;
    }
    .top {
        bottom: auto !important;
        pointer-events: none !important;
    }
    .top .bar {
        pointer-events: auto !important;
    }"""

for fpath in files:
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    modified = False
    if BUG_TARGET in content:
        content = content.replace(BUG_TARGET, FIX_REPLACEMENT)
        modified = True
        print(f"Fixed bug in {os.path.basename(fpath)}")

    if modified:
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(content)

# Also ensure .scrim and .drawer have defensive pointer-events in CSS
css_file = os.path.join(BASE_DIR, "templatemo-633-celadon-style.css")
with open(css_file, "r", encoding="utf-8") as f:
    css = f.read()

defensive_css = """
/* Defensive pointer-events guards for mobile drawer & scrim */
.scrim {
    pointer-events: none !important;
}
.scrim.on {
    pointer-events: auto !important;
}
.drawer {
    pointer-events: none;
}
.drawer.on {
    pointer-events: auto;
}
.top {
    pointer-events: none;
}
.top .bar {
    pointer-events: auto;
}
"""

if "Defensive pointer-events guards for mobile drawer & scrim" not in css:
    with open(css_file, "a", encoding="utf-8") as f:
        f.write(defensive_css)
    print("Added defensive pointer-events guards to CSS.")
