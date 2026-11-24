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

# discover.html
disc_path = os.path.join(base, "discover.html")
with open(disc_path, "r", encoding="utf-8") as f:
    disc_txt = f.read()

old_disc = """<div style="margin-top:24px;">
                            <a class="btn solid" href="experts.html">Learn About Building Your AI Identity &rarr;</a>
                        </div>"""

new_disc = f"""<div style="margin-top:24px; display:flex; justify-content:center; gap:14px; flex-wrap:wrap;">
                            <a class="btn solid" href="experts.html">Learn About Building Your AI Identity &rarr;</a>
                            <a class="btn" href="{WEBAPP_URL}" target="_blank" rel="noopener">Launch Web App</a>
                            <a class="dock-play-btn" href="{PLAYSTORE_URL}" target="_blank" rel="noopener" style="border-radius:18px; padding:10px 22px;">
                                {PLAYSTORE_SVG_SMALL}
                                <span>Google Play Store</span>
                            </a>
                        </div>"""

if old_disc in disc_txt:
    with open(disc_path, "w", encoding="utf-8") as f:
        f.write(disc_txt.replace(old_disc, new_disc))
    print("Updated discover.html closing section")

# experts.html
exp_path = os.path.join(base, "experts.html")
with open(exp_path, "r", encoding="utf-8") as f:
    exp_txt = f.read()

old_exp = """<div id="signup-feedback" style="display:none; margin-top:14px; font-size:0.92rem; color:var(--jade); font-weight:500;"></div>
                        <p class="note" style="margin-top:16px;">We review each creator application to ensure high-quality knowledge grounding.</p>"""

new_exp = f"""<div id="signup-feedback" style="display:none; margin-top:14px; font-size:0.92rem; color:var(--jade); font-weight:500;"></div>
                        <div style="display:flex; justify-content:center; gap:12px; flex-wrap:wrap; margin-top:22px;">
                            <a class="btn solid" href="{WEBAPP_URL}" target="_blank" rel="noopener" style="padding:10px 24px; font-size:0.92rem;">Launch Web App &rarr;</a>
                            <a class="dock-play-btn" href="{PLAYSTORE_URL}" target="_blank" rel="noopener" style="padding:10px 22px; font-size:0.92rem; border-radius:18px;">
                                {PLAYSTORE_SVG_SMALL}
                                <span>Google Play Store</span>
                            </a>
                        </div>
                        <p class="note" style="margin-top:16px;">We review each creator application to ensure high-quality knowledge grounding.</p>"""

if old_exp in exp_txt:
    with open(exp_path, "w", encoding="utf-8") as f:
        f.write(exp_txt.replace(old_exp, new_exp))
    print("Updated experts.html closing section")
