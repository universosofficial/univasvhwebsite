# -*- coding: utf-8 -*-
"""
Inline 3D Gallery Hero CSS directly into <style> block of index.html
and bump stylesheet version to ?v=20261124_anam to eliminate all caching issues.
"""

path = r"C:\Users\user\Downloads\websites\templatemo_633_celadon\index.html"

with open(path, "r", encoding="utf-8") as f:
    html = f.read()

# 1. Bump cache buster
html = html.replace('href="templatemo-633-celadon-style.css?v=20261123c"', 'href="templatemo-633-celadon-style.css?v=20261124_anam"')

# 2. Read the gallery hero CSS
css_path = r"C:\Users\user\Downloads\websites\templatemo_633_celadon\templatemo-633-celadon-style.css"
with open(css_path, "r", encoding="utf-8") as f:
    css_all = f.read()

gallery_marker = "/* ==========================================================================\n   ANAM / HALO-LAB 3D GALLERY HERO"
if gallery_marker in css_all:
    gallery_css = css_all[css_all.find(gallery_marker):]
else:
    print("Warning: gallery_marker not found exactly, using fallback slice")
    gallery_css = ""

# Insert gallery_css right before </style> in index.html
if "</style>" in html and "gallery-hero-wrap" not in html[:html.find("</style>")]:
    idx = html.find("</style>")
    html = html[:idx] + "\n\n" + gallery_css + "\n" + html[idx:]
    print("Inlined gallery CSS into <head><style> block in index.html!")

with open(path, "w", encoding="utf-8") as f:
    f.write(html)

print("Updated index.html with inlined gallery CSS successfully!")
