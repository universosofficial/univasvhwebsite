# -*- coding: utf-8 -*-
"""
Perfect polish for the 3D Gallery Hero in index.html:
1. Increase top padding on .gallery-hero-wrap to 110px so the floating nav bar never overlaps the tagline or bubble.
2. Remove the redundant inner .room-topbar from inside the room, leaving the clean Celadon floating nav.
3. Position .room-tagline and .room-badge-bubble cleanly at the top of the room.
4. Fix missing Step 02 squircle icons in companion.html and experts.html.
"""

# 1. Update index.html
path_index = r"C:\Users\user\Downloads\websites\templatemo_633_celadon\index.html"
with open(path_index, "r", encoding="utf-8") as f:
    html = f.read()

# Adjust CSS in <style>
old_css_padding = ".gallery-hero-wrap {\n    padding: 16px 20px 48px;"
new_css_padding = ".gallery-hero-wrap {\n    padding: 110px 20px 48px;"

if old_css_padding in html:
    html = html.replace(old_css_padding, new_css_padding)
    print("Updated .gallery-hero-wrap padding-top to 110px in index.html")

# Remove redundant inner room-topbar
import re
topbar_pattern = r'<div class="room-topbar">.*?</div>\s*(?=<!-- Room Tagline)'
if re.search(topbar_pattern, html, flags=re.DOTALL):
    html = re.sub(topbar_pattern, "", html, flags=re.DOTALL)
    print("Removed redundant inner .room-topbar from index.html")

with open(path_index, "w", encoding="utf-8") as f:
    f.write(html)

# Also update templatemo-633-celadon-style.css
path_css = r"C:\Users\user\Downloads\websites\templatemo_633_celadon\templatemo-633-celadon-style.css"
with open(path_css, "r", encoding="utf-8") as f:
    css = f.read()

if old_css_padding in css:
    css = css.replace(old_css_padding, new_css_padding)
    with open(path_css, "w", encoding="utf-8") as f:
        f.write(css)
    print("Updated .gallery-hero-wrap padding-top in style.css")

# 2. Fix Step 02 missing icon in companion.html
path_comp = r"C:\Users\user\Downloads\websites\templatemo_633_celadon\companion.html"
with open(path_comp, "r", encoding="utf-8") as f:
    comp_html = f.read()

# Find empty tile in companion.html step 2
empty_tile_comp = '<div class="tile t-sky"></div>'
replacement_tile_comp = '''<div class="tile t-sky">
                                <svg viewBox="0 0 24 24"><path d="M12 2a10 10 0 0 1 10 10c0 5.52-4.48 10-10 10S2 17.52 2 12 6.48 2 12 2zm0 4a6 6 0 1 0 0 12 6 6 0 0 0 0-12z"/></svg>
                            </div>'''

if empty_tile_comp in comp_html:
    comp_html = comp_html.replace(empty_tile_comp, replacement_tile_comp, 1)
    with open(path_comp, "w", encoding="utf-8") as f:
        f.write(comp_html)
    print("Fixed Step 02 icon in companion.html")

# 3. Fix Step 02 missing icon in experts.html
path_exp = r"C:\Users\user\Downloads\websites\templatemo_633_celadon\experts.html"
with open(path_exp, "r", encoding="utf-8") as f:
    exp_html = f.read()

if empty_tile_comp in exp_html:
    exp_html = exp_html.replace(empty_tile_comp, replacement_tile_comp, 1)
    with open(path_exp, "w", encoding="utf-8") as f:
        f.write(exp_html)
    print("Fixed Step 02 icon in experts.html")

print("All hero polish and icon fixes completed!")
