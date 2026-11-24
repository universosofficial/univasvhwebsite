import os
import re

DIR = r"C:\Users\user\Downloads\websites\templatemo_633_celadon"

# 1. Update CSS
css_path = os.path.join(DIR, "templatemo-633-celadon-style.css")
with open(css_path, "r", encoding="utf-8") as f:
    css = f.read()

# Replace the responsive rules for plans
old_media = """@media (max-width: 900px) {
    .plans.grid-2, .plans.grid-3, .plans.grid-4 {
        grid-template-columns: 1fr !important;
    }
}"""

new_media = """@media (min-width: 720px) and (max-width: 1040px) {
    .plans.grid-2 {
        grid-template-columns: repeat(2, 1fr) !important;
    }
    .plans.grid-3 {
        grid-template-columns: repeat(2, 1fr) !important;
    }
    .plans.grid-4 {
        grid-template-columns: repeat(2, 1fr) !important;
    }
}
@media (max-width: 719px) {
    .plans.grid-2, .plans.grid-3, .plans.grid-4 {
        grid-template-columns: 1fr !important;
    }
}

/* Ensure trait chips align with identical height and baseline */
.chips .chip {
    display: inline-flex !important;
    align-items: center !important;
    justify-content: center !important;
    vertical-align: middle !important;
    height: 32px !important;
    box-sizing: border-box !important;
    line-height: 1 !important;
}"""

if old_media in css:
    css = css.replace(old_media, new_media)
    with open(css_path, "w", encoding="utf-8") as f:
        f.write(css)
    print("Updated CSS media queries and chip alignment")

# 2. Update companion.html icons and chips
comp_path = os.path.join(DIR, "companion.html")
with open(comp_path, "r", encoding="utf-8") as f:
    c_html = f.read()

# Replace pillar 01 SVG with brain / cognitive node icon
pillar1_old = """<div class="tile t-jade" style="width:52px; height:52px; border-radius:18px; margin-bottom:16px;">
                                <svg viewBox="0 0 24 24" style="width:24px; height:24px; stroke:var(--jade-ink); fill:none; stroke-width:2;"><path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg>
                            </div>"""

pillar1_new = """<div class="tile t-jade" style="width:52px; height:52px; border-radius:18px; margin-bottom:16px;">
                                <svg viewBox="0 0 24 24" style="width:24px; height:24px; stroke:var(--jade-ink, #1B5E4A); fill:none; stroke-width:2; stroke-linecap:round; stroke-linejoin:round;">
                                    <path d="M9.5 2A4.5 4.5 0 0 0 5 6.5c0 1.4.6 2.6 1.6 3.4-.6.6-1.1 1.4-1.4 2.3A4.5 4.5 0 0 0 9.5 17H10v3a2 2 0 0 0 2 2h0a2 2 0 0 0 2-2v-3h.5a4.5 4.5 0 0 0 4.3-4.8c-.3-.9-.8-1.7-1.4-2.3 1-.8 1.6-2 1.6-3.4A4.5 4.5 0 0 0 14.5 2c-1.3 0-2.4.5-3.2 1.4A4.5 4.5 0 0 0 9.5 2z"/>
                                    <line x1="12" y1="6" x2="12" y2="12"/>
                                    <circle cx="12" cy="14" r="1" fill="var(--jade-ink, #1B5E4A)"/>
                                </svg>
                            </div>"""

if pillar1_old in c_html:
    c_html = c_html.replace(pillar1_old, pillar1_new)
    print("Replaced pillar 1 icon")

# Replace pillar 02 SVG with robust envelope icon
pillar2_old = """<div class="tile t-sky" style="width:52px; height:52px; border-radius:18px; margin-bottom:16px;">
                                <svg viewBox="0 0 24 24" style="width:24px; height:24px; stroke:var(--sky-ink); fill:none; stroke-width:2;"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg>
                            </div>"""

pillar2_new = """<div class="tile t-sky" style="width:52px; height:52px; border-radius:18px; margin-bottom:16px;">
                                <svg viewBox="0 0 24 24" style="width:24px; height:24px; stroke:var(--sky-ink, #2B5C9C); fill:none; stroke-width:2; stroke-linecap:round; stroke-linejoin:round;">
                                    <rect x="2" y="4" width="20" height="16" rx="3"/>
                                    <path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"/>
                                </svg>
                            </div>"""

if pillar2_old in c_html:
    c_html = c_html.replace(pillar2_old, pillar2_new)
    print("Replaced pillar 2 icon")

# Also update the style block inside HTML
c_html = c_html.replace(old_media, new_media)

with open(comp_path, "w", encoding="utf-8") as f:
    f.write(c_html)

# Update style block across other pages
for fname in ["discover.html", "pricing.html", "how-it-works.html", "experts.html", "index.html", "faq.html"]:
    fpath = os.path.join(DIR, fname)
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
    if old_media in content:
        content = content.replace(old_media, new_media)
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated style in {fname}")

print("All refinements completed!")
