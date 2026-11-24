import os

base = r"C:\Users\user\Downloads\websites\templatemo_633_celadon"

PLAYSTORE_URL = "https://play.google.com/store/apps/details?id=com.univasos.virtualhuman"
WEBAPP_URL = "https://univasvh.com"

PLAYSTORE_SVG_SMALL = """<svg viewBox="0 0 24 24" width="16" height="16" fill="none" style="flex-shrink:0;">
    <path d="M3.6 2.4a1.8 1.8 0 0 0-.4 1.2v16.8a1.8 1.8 0 0 0 .4 1.2l9.8-9.6L3.6 2.4z" fill="#00b0ff"/>
    <path d="M17.4 8.7L13.4 12l4 3.3 2.5-1.4c1-.6 1.6-1.6 1.6-2.8 0-1.1-.6-2.2-1.6-2.8l-2.5-1.4z" fill="#ffc400"/>
    <path d="M3.6 21.6c.6.5 1.5.5 2.3.1l11.5-6.6-4-3.3-9.8 9.8z" fill="#ff3d00"/>
    <path d="M17.4 8.7L5.9 2.1C5.1 1.6 4.2 1.7 3.6 2.2l9.8 9.8 4-3.3z" fill="#00e676"/>
</svg>"""

# 1. how-it-works.html
hw_path = os.path.join(base, "how-it-works.html")
with open(hw_path, "r", encoding="utf-8") as f:
    hw_txt = f.read()

old_hw = """<div style="margin-top:24px; display:flex; justify-content:center; gap:14px; flex-wrap:wrap;">
                            <a class="btn solid" href="companion.html">Meet Your AI Companion</a>
                            <a class="btn" href="discover.html">Explore Identities</a>
                        </div>"""

new_hw = f"""<div style="margin-top:24px; display:flex; justify-content:center; gap:14px; flex-wrap:wrap;">
                            <a class="btn solid" href="{WEBAPP_URL}" target="_blank" rel="noopener">Launch Web App &rarr;</a>
                            <a class="dock-play-btn" href="{PLAYSTORE_URL}" target="_blank" rel="noopener" style="border-radius:18px; padding:10px 22px;">
                                {PLAYSTORE_SVG_SMALL}
                                <span>Google Play Store</span>
                            </a>
                            <a class="btn" href="companion.html">Personal Companions</a>
                            <a class="btn" href="discover.html">Explore Identities</a>
                        </div>"""

if old_hw in hw_txt:
    with open(hw_path, "w", encoding="utf-8") as f:
        f.write(hw_txt.replace(old_hw, new_hw))
    print("Updated how-it-works.html start section")

# 2. faq.html
faq_path = os.path.join(base, "faq.html")
with open(faq_path, "r", encoding="utf-8") as f:
    faq_txt = f.read()

old_faq = """<div style="margin-top:24px;">
                            <a class="btn solid" href="companion.html">Open AI Companion Experience &rarr;</a>
                        </div>"""

new_faq = f"""<div style="margin-top:24px; display:flex; justify-content:center; gap:14px; flex-wrap:wrap;">
                            <a class="btn solid" href="{WEBAPP_URL}" target="_blank" rel="noopener">Launch Web App &rarr;</a>
                            <a class="dock-play-btn" href="{PLAYSTORE_URL}" target="_blank" rel="noopener" style="border-radius:18px; padding:10px 22px;">
                                {PLAYSTORE_SVG_SMALL}
                                <span>Google Play Store</span>
                            </a>
                            <a class="btn" href="companion.html">AI Companions</a>
                        </div>"""

if old_faq in faq_txt:
    with open(faq_path, "w", encoding="utf-8") as f:
        f.write(faq_txt.replace(old_faq, new_faq))
    print("Updated faq.html start section")
