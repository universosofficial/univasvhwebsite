import os

css_path = r"C:\Users\user\Downloads\websites\templatemo_633_celadon\templatemo-633-celadon-style.css"
with open(css_path, "r", encoding="utf-8") as f:
    css = f.read()

fix_css = """
/* Explicit white contrast for dock and drawer play buttons */
.dock-play-btn,
.dock-play-btn span,
.dock-play-btn b,
.drawer .dock-play-btn,
.drawer .dock-play-btn span,
.dock-widget-right .dock-play-btn span {
    color: #FFFFFF !important;
}

.dock-web-btn,
.dock-web-btn span,
.dock-web-btn b,
.dock-widget-right .dock-web-btn span {
    color: var(--forest, #263B35) !important;
}
"""

with open(css_path, "a", encoding="utf-8") as f:
    f.write(fix_css)

print("Applied contrast fix to CSS.")
