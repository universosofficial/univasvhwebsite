import os
import re

BASE_DIR = r"C:\Users\user\Downloads\websites\templatemo_633_celadon"

def fix_index():
    path = os.path.join(BASE_DIR, "index.html")
    with open(path, "r", encoding="utf-8") as f:
        html = f.read()

    # 1. Fix #expert-opportunity buttons to use class="acts rv d2"
    old_opp = re.search(r'<div style="margin-top:24px;" class="rv d2">\s*<a class="btn solid" href="companion\.html">Create Your Companion</a>\s*<a class="btn" href="experts\.html"[^>]*>Become an Expert Creator</a>\s*</div>', html)
    if old_opp:
        new_opp = '''<div class="acts rv d2" style="margin-top:24px;">
                          <a class="btn solid" href="companion.html">Create Your Companion</a>
                          <a class="btn" href="experts.html">Become an Expert Creator</a>
                      </div>'''
        html = html[:old_opp.start()] + new_opp + html[old_opp.end():]
        print("Updated #expert-opportunity to use class='acts'")

    # 2. Fix room-backplate top offset on mobile so it doesn't touch the tagline
    html = re.sub(
        r'\.room-backplate\s*\{\s*width:\s*90%\s*!important;\s*height:\s*58%\s*!important;\s*top:\s*6%\s*!important;',
        '.room-backplate { width: 90% !important; height: 50% !important; top: 125px !important;',
        html
    )

    # 3. Prevent any horizontal expansion on index.html
    html = re.sub(
        r'body\s*\{\s*background:\s*#F5F2EA\s*!important;\s*color:\s*#303631\s*!important;\s*\}',
        'html, body { overflow-x: hidden !important; max-width: 100vw !important; width: 100% !important; margin: 0; padding: 0; }\nbody { background: #F5F2EA !important; color: #303631 !important; }',
        html
    )

    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print("Fixed index.html")

def fix_css():
    css_path = os.path.join(BASE_DIR, "templatemo-633-celadon-style.css")
    with open(css_path, "r", encoding="utf-8") as f:
        css = f.read()

    # Ensure overflow-x: hidden on html, body
    if "html, body { overflow-x: hidden" not in css:
        css = "html, body { overflow-x: hidden !important; max-width: 100vw !important; width: 100% !important; }\n" + css

    # Update backplate top offset in master mobile css
    css = re.sub(
        r'\.room-backplate\s*\{\s*width:\s*90%\s*!important;\s*height:\s*58%\s*!important;\s*top:\s*6%\s*!important;',
        '.room-backplate { width: 90% !important; height: 50% !important; top: 125px !important;',
        css
    )

    with open(css_path, "w", encoding="utf-8") as f:
        f.write(css)
    print("Fixed templatemo-633-celadon-style.css")

if __name__ == "__main__":
    fix_index()
    fix_css()
