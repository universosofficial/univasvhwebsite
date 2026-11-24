"""
Apply sitewide live app links (https://univasvh.com) and Google Play Store download options.
"""

import os
import re

BASE_DIR = r"C:\Users\user\Downloads\websites\templatemo_633_celadon"

PLAYSTORE_URL = "https://play.google.com/store/apps/details?id=com.univasos.virtualhuman"
WEBAPP_URL = "https://univasvh.com"

PAGES = ["index.html", "companion.html", "discover.html", "how-it-works.html", "experts.html", "faq.html"]

PLAYSTORE_SVG_SMALL = """<svg viewBox="0 0 24 24" width="15" height="15" fill="none" style="flex-shrink:0;">
    <path d="M3.6 2.4a1.8 1.8 0 0 0-.4 1.2v16.8a1.8 1.8 0 0 0 .4 1.2l9.8-9.6L3.6 2.4z" fill="#00b0ff"/>
    <path d="M17.4 8.7L13.4 12l4 3.3 2.5-1.4c1-.6 1.6-1.6 1.6-2.8 0-1.1-.6-2.2-1.6-2.8l-2.5-1.4z" fill="#ffc400"/>
    <path d="M3.6 21.6c.6.5 1.5.5 2.3.1l11.5-6.6-4-3.3-9.8 9.8z" fill="#ff3d00"/>
    <path d="M17.4 8.7L5.9 2.1C5.1 1.6 4.2 1.7 3.6 2.2l9.8 9.8 4-3.3z" fill="#00e676"/>
</svg>"""

DRAWER_REPLACEMENT = f"""<aside class="drawer" id="drawer" aria-label="Menu">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:18px; padding: 0 4px;">
                <span class="dtag">Menu</span>
                <button class="drawer-close" id="drawer-close" aria-label="Close menu">&times;</button>
            </div>
            <a href="companion.html">AI Companion</a>
            <a href="discover.html">Discover</a>
            <a href="how-it-works.html">How It Works</a>
            <a href="experts.html">For Experts</a>
            <a href="faq.html">FAQ</a>
            <div style="margin-top:16px; padding-top:14px; border-top:1px solid rgba(0,0,0,0.06); display:flex; flex-direction:column; gap:10px;">
                <a class="btn solid" href="{WEBAPP_URL}" target="_blank" rel="noopener" style="text-align:center; justify-content:center;">Launch Web App</a>
                <a class="dock-play-btn" href="{PLAYSTORE_URL}" target="_blank" rel="noopener" style="text-align:center; justify-content:center; padding:10px 18px; border-radius:14px;">
                    {PLAYSTORE_SVG_SMALL}
                    <span>Google Play Store</span>
                </a>
            </div>
        </aside>"""

FOOTER_NAV_REPLACEMENT = f"""<div class="footlinks-nav" style="display:flex; flex-wrap:wrap; align-items:center; gap:16px;">
                        <a href="companion.html" style="font-size:0.88rem; color:var(--ink-2); text-decoration:none; font-weight:500;">AI Companion</a>
                        <a href="discover.html" style="font-size:0.88rem; color:var(--ink-2); text-decoration:none; font-weight:500;">Discover</a>
                        <a href="experts.html" style="font-size:0.88rem; color:var(--ink-2); text-decoration:none; font-weight:500;">For Experts</a>
                        <a href="how-it-works.html" style="font-size:0.88rem; color:var(--ink-2); text-decoration:none; font-weight:500;">How It Works</a>
                        <a href="faq.html" style="font-size:0.88rem; color:var(--ink-2); text-decoration:none; font-weight:500;">FAQ</a>
                        <a href="{WEBAPP_URL}" target="_blank" rel="noopener" style="font-size:0.88rem; color:var(--forest, #263B35); text-decoration:none; font-weight:700; display:inline-flex; align-items:center; gap:4px;">Launch App &rarr;</a>
                        <a href="{PLAYSTORE_URL}" target="_blank" rel="noopener" style="font-size:0.88rem; color:var(--forest, #263B35); text-decoration:none; font-weight:700; display:inline-flex; align-items:center; gap:5px;">
                            {PLAYSTORE_SVG_SMALL}
                            <span>Google Play</span>
                        </a>
                    </div>"""

for page in PAGES:
    filepath = os.path.join(BASE_DIR, page)
    if not os.path.exists(filepath):
        continue
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Update Header Button in <div class="shell bar">
    # Matches: <a class="btn solid" href="...">...</a> before </header>
    content = re.sub(
        r'(<div class="shell bar">.*?<nav class="nav">.*?</nav>\s*)<a class="btn solid"[^>]*>.*?</a>',
        rf'\1<a class="btn solid" href="{WEBAPP_URL}" target="_blank" rel="noopener">Launch App</a>',
        content,
        flags=re.DOTALL
    )

    # 2. Update Drawer
    content = re.sub(
        r'<aside class="drawer" id="drawer"[^>]*>.*?</aside>',
        DRAWER_REPLACEMENT,
        content,
        flags=re.DOTALL
    )

    # 3. Update Footer Navigation
    content = re.sub(
        r'<div class="footlinks-nav">.*?</div>',
        FOOTER_NAV_REPLACEMENT,
        content,
        flags=re.DOTALL
    )

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Updated header, drawer, and footer in {page}")

# Special additions for companion.html:
with open(os.path.join(BASE_DIR, "companion.html"), "r", encoding="utf-8") as f:
    comp_content = f.read()

# Add Launch Character Studio button under the 4 creation steps
if "Launch Character Studio in Web App" not in comp_content:
    comp_content = comp_content.replace(
        '</article>\n                    </div>\n                </div>\n            </section>\n\n            <!-- 4 pillars',
        f'''</article>
                    </div>
                    <div style="text-align:center; margin-top:32px;" class="rv">
                        <a class="btn solid" href="{WEBAPP_URL}" target="_blank" rel="noopener" style="padding:12px 28px; font-size:0.95rem;">
                            Launch Character Studio in Web App &rarr;
                        </a>
                        <a class="dock-play-btn" href="{PLAYSTORE_URL}" target="_blank" rel="noopener" style="padding:11px 22px; font-size:0.92rem; border-radius:18px; margin-left:12px;">
                            {PLAYSTORE_SVG_SMALL}
                            <span>Google Play Store</span>
                        </a>
                    </div>
                </div>
            </section>

            <!-- 4 pillars'''
    )

# Update #start section in companion.html
if "Launch Web App" not in comp_content.split('id="start"')[-1]:
    comp_content = comp_content.replace(
        '<div style="margin-top:20px;">\n                            <a class="btn" href="discover.html" style="font-size:0.88rem; padding:8px 20px;">Explore AI Identities Directory</a>\n                        </div>',
        f'''<div style="display:flex; justify-content:center; gap:12px; flex-wrap:wrap; margin-top:22px;">
                            <a class="btn solid" href="{WEBAPP_URL}" target="_blank" rel="noopener" style="padding:10px 24px; font-size:0.92rem; display:inline-flex; align-items:center; gap:7px;">
                                <span>Launch Web App</span>
                                <svg viewBox="0 0 24 24" width="14" height="14" stroke="currentColor" stroke-width="2.2" fill="none"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"></path><polyline points="15 3 21 3 21 9"></polyline><line x1="10" y1="14" x2="21" y2="3"></line></svg>
                            </a>
                            <a class="dock-play-btn" href="{PLAYSTORE_URL}" target="_blank" rel="noopener" style="padding:10px 22px; font-size:0.92rem; border-radius:18px;">
                                {PLAYSTORE_SVG_SMALL}
                                <span>Google Play Store</span>
                            </a>
                        </div>
                        <div style="margin-top:14px;">
                            <a class="btn" href="discover.html" style="font-size:0.84rem; padding:6px 16px;">Explore AI Identities Directory</a>
                        </div>'''
    )

with open(os.path.join(BASE_DIR, "companion.html"), "w", encoding="utf-8") as f:
    f.write(comp_content)
print("Updated companion.html custom CTAs.")

# Update script.js email signup feedback & redirect
SCRIPT_FILE = os.path.join(BASE_DIR, "templatemo-633-celadon-script.js")
with open(SCRIPT_FILE, "r", encoding="utf-8") as f:
    js_content = f.read()

old_signup_code = """feedbackEl.style.display = "block";
            feedbackEl.style.color = "var(--jade, #2A7A62)";
            feedbackEl.textContent = "Thank you for joining Virtual Human! You're on the early access list.";
            emailInput.value = "";"""

new_signup_code = """feedbackEl.style.display = "block";
            feedbackEl.style.color = "var(--forest, #263B35)";
            feedbackEl.innerHTML = "Welcome to Virtual Human! Opening the live app at <a href='https://univasvh.com' target='_blank' style='text-decoration:underline; font-weight:700;'>univasvh.com</a>...";
            emailInput.value = "";
            setTimeout(function() {
                window.open("https://univasvh.com", "_blank");
            }, 1000);"""

if old_signup_code in js_content:
    js_content = js_content.replace(old_signup_code, new_signup_code)
    with open(SCRIPT_FILE, "w", encoding="utf-8") as f:
        f.write(js_content)
    print("Updated script.js signup feedback and auto-redirect.")
