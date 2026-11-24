"""
Full integration script:
1. index.html:
   - Hero "Chat with Persona" href -> https://univasvh.com
   - Hero dock right widget -> Live indicator + Google Play & Web App buttons
   - Top bar & drawer -> Launch App (https://univasvh.com) + Google Play badge
   - Add #download-app section before #start
   - #start section -> Launch Web App + Google Play buttons
   - Footlinks -> Launch Web App + Google Play
2. companion.html, discover.html, how-it-works.html, experts.html, faq.html:
   - Top bar & drawer -> Launch App (https://univasvh.com) + Google Play badge
   - #start section -> Launch Web App + Google Play buttons
   - Footlinks -> Launch Web App + Google Play
3. script.js:
   - When email is submitted, redirect smoothly to https://univasvh.com
"""

import os
import re

BASE_DIR = r"C:\Users\user\Downloads\websites\templatemo_633_celadon"

PLAYSTORE_URL = "https://play.google.com/store/apps/details?id=com.univasos.virtualhuman"
WEBAPP_URL = "https://univasvh.com"

PLAYSTORE_ICON_SVG = """<svg viewBox="0 0 24 24" width="16" height="16" fill="none" style="flex-shrink:0;">
    <path d="M3.6 2.4a1.8 1.8 0 0 0-.4 1.2v16.8a1.8 1.8 0 0 0 .4 1.2l9.8-9.6L3.6 2.4z" fill="#00b0ff"/>
    <path d="M17.4 8.7L13.4 12l4 3.3 2.5-1.4c1-.6 1.6-1.6 1.6-2.8 0-1.1-.6-2.2-1.6-2.8l-2.5-1.4z" fill="#ffc400"/>
    <path d="M3.6 21.6c.6.5 1.5.5 2.3.1l11.5-6.6-4-3.3-9.8 9.8z" fill="#ff3d00"/>
    <path d="M17.4 8.7L5.9 2.1C5.1 1.6 4.2 1.7 3.6 2.2l9.8 9.8 4-3.3z" fill="#00e676"/>
</svg>"""

DOCK_RIGHT_HTML = f"""<div class="dock-widget-right">
                            <div class="dock-live-indicator">
                                <span class="live-pulse-dot"></span>
                                <span>Now Live on Android &amp; Web</span>
                            </div>
                            <div class="dock-app-actions">
                                <a href="{PLAYSTORE_URL}" target="_blank" rel="noopener" class="dock-play-btn" title="Download on Google Play">
                                    {PLAYSTORE_ICON_SVG}
                                    <span>Google Play</span>
                                </a>
                                <a href="{WEBAPP_URL}" target="_blank" rel="noopener" class="dock-web-btn" title="Launch Web App">
                                    <span>Web App &rarr;</span>
                                </a>
                            </div>
                        </div>"""

DOWNLOAD_SECTION_HTML = f"""
            <!-- app download showcase -->
            <section class="pad" id="download-app">
                <div class="shell">
                    <div class="app-download-card rv">
                        <div class="app-download-header">
                            <span class="app-live-status">
                                <span class="live-pulse-dot"></span>
                                Now Live on Android &amp; Web
                            </span>
                            <h2 class="app-download-title">Experience Virtual Human Anywhere.</h2>
                            <p class="app-download-subtitle">
                                Continuous presence right in your pocket. Seamlessly sync your personal companions, lifelike voice dialogue, and long-term memory across your Android phone and desktop browser.
                            </p>
                        </div>

                        <!-- 3 Key Mobile Capabilities -->
                        <div class="app-features-grid">
                            <div class="app-feature-item">
                                <div class="app-feat-icon">
                                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 1a3 3 0 0 0-3 3v8a3 3 0 0 0 6 0V4a3 3 0 0 0-3-3z"></path><path d="M19 10v2a7 7 0 0 1-14 0v-2"></path><line x1="12" y1="19" x2="12" y2="23"></line><line x1="8" y1="23" x2="16" y2="23"></line></svg>
                                </div>
                                <h4>Real-Time Voice Dialogue</h4>
                                <p>Speak freely with your companion during walks, commutes, or evening wind-downs with natural conversational cadence.</p>
                            </div>
                            <div class="app-feature-item">
                                <div class="app-feat-icon">
                                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 8A6 6 0 0 0 6 8c0 7-3 9-3 9h18s-3-2-3-9"></path><path d="M13.73 21a2 2 0 0 1-3.46 0"></path></svg>
                                </div>
                                <h4>Proactive Daily Check-ins</h4>
                                <p>Warm morning greetings and thoughtful evening reflections. Your companion stays aware of your context and mood.</p>
                            </div>
                            <div class="app-feature-item">
                                <div class="app-feat-icon">
                                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path></svg>
                                </div>
                                <h4>Encrypted Episodic Memory</h4>
                                <p>Your relationship history and shared memories sync securely in real time between your Android phone and web app.</p>
                            </div>
                        </div>

                        <!-- Call to Actions -->
                        <div class="app-cta-group">
                            <a href="{PLAYSTORE_URL}" target="_blank" rel="noopener" class="playstore-badge" aria-label="Get it on Google Play">
                                <svg class="playstore-icon" viewBox="0 0 24 24" width="28" height="28" fill="none">
                                    <path d="M3.6 2.4a1.8 1.8 0 0 0-.4 1.2v16.8a1.8 1.8 0 0 0 .4 1.2l9.8-9.6L3.6 2.4z" fill="#00b0ff"/>
                                    <path d="M17.4 8.7L13.4 12l4 3.3 2.5-1.4c1-.6 1.6-1.6 1.6-2.8 0-1.1-.6-2.2-1.6-2.8l-2.5-1.4z" fill="#ffc400"/>
                                    <path d="M3.6 21.6c.6.5 1.5.5 2.3.1l11.5-6.6-4-3.3-9.8 9.8z" fill="#ff3d00"/>
                                    <path d="M17.4 8.7L5.9 2.1C5.1 1.6 4.2 1.7 3.6 2.2l9.8 9.8 4-3.3z" fill="#00e676"/>
                                </svg>
                                <div class="playstore-text">
                                    <span class="playstore-sub">GET IT ON</span>
                                    <span class="playstore-title">Google Play</span>
                                </div>
                            </a>
                            <a href="{WEBAPP_URL}" target="_blank" rel="noopener" class="webapp-badge" aria-label="Launch Web App">
                                <div class="webapp-icon">
                                    <svg viewBox="0 0 24 24" width="24" height="24" stroke="currentColor" stroke-width="2" fill="none">
                                        <circle cx="12" cy="12" r="10"></circle>
                                        <line x1="2" y1="12" x2="22" y2="12"></line>
                                        <path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path>
                                    </svg>
                                </div>
                                <div class="webapp-text">
                                    <span class="webapp-sub">INSTANT ACCESS</span>
                                    <span class="webapp-title">Launch Web App</span>
                                </div>
                                <svg viewBox="0 0 24 24" width="16" height="16" stroke="currentColor" stroke-width="2.5" fill="none" style="margin-left:4px;"><polyline points="9 18 15 12 9 6"></polyline></svg>
                            </a>
                        </div>

                        <p class="app-guarantee-note">
                            <span>Free to download &amp; use</span> &bull; <span>100% Private &amp; Confidential</span> &bull; <span>Virtual Human is a subsidiary of UnivasOS LTD</span>
                        </p>
                    </div>
                </div>
            </section>
"""

# Process index.html
with open(os.path.join(BASE_DIR, "index.html"), "r", encoding="utf-8") as f:
    idx_content = f.read()

# 1. Update Chat with Persona link to https://univasvh.com
idx_content = re.sub(
    r'<a\s+class="chat-persona-btn"\s+id="chat-persona-link"\s+href="[^"]*"',
    f'<a class="chat-persona-btn" id="chat-persona-link" href="{WEBAPP_URL}" target="_blank" rel="noopener"',
    idx_content
)

# 2. Update dock-widget-right in hero
dock_right_pattern = r'<div class="dock-widget-right">.*?</div>\s*</div>\s*</div>\s*</section>'
old_dock_right_match = re.search(r'<div class="dock-widget-right">.*?</div>\s*(?=</div>\s*</div>\s*</section>)', idx_content, re.DOTALL)
if old_dock_right_match:
    idx_content = idx_content[:old_dock_right_match.start()] + DOCK_RIGHT_HTML + idx_content[old_dock_right_match.end():]
    print("Updated dock-widget-right in hero.")

# 3. Add #download-app section before #start
if 'id="download-app"' not in idx_content:
    start_sec_match = re.search(r'(<!-- closing cta -->\s*<section class="pad" id="start">)', idx_content)
    if start_sec_match:
        idx_content = idx_content[:start_sec_match.start()] + DOWNLOAD_SECTION_HTML + "\n            " + idx_content[start_sec_match.start():]
        print("Inserted #download-app section before #start.")

# 4. Enhance #start section actions
start_actions_old = """<div style="margin-top:20px;">
                            <a class="btn" href="companion.html" style="font-size:0.88rem; padding:8px 20px;">Create Your Companion</a>
                            <a class="btn" href="experts.html" style="font-size:0.88rem; padding:8px 20px; margin-left:10px;">Become an Expert</a>
                        </div>"""

start_actions_new = f"""<div style="display:flex; justify-content:center; gap:12px; flex-wrap:wrap; margin-top:22px;">
                            <a class="btn solid" href="{WEBAPP_URL}" target="_blank" rel="noopener" style="padding:10px 24px; font-size:0.92rem; display:inline-flex; align-items:center; gap:7px;">
                                <span>Launch Web App</span>
                                <svg viewBox="0 0 24 24" width="14" height="14" stroke="currentColor" stroke-width="2.2" fill="none"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"></path><polyline points="15 3 21 3 21 9"></polyline><line x1="10" y1="14" x2="21" y2="3"></line></svg>
                            </a>
                            <a class="dock-play-btn" href="{PLAYSTORE_URL}" target="_blank" rel="noopener" style="padding:10px 22px; font-size:0.92rem; border-radius:18px;">
                                {PLAYSTORE_ICON_SVG}
                                <span>Google Play Store</span>
                            </a>
                        </div>
                        <div style="margin-top:14px;">
                            <a class="btn" href="companion.html" style="font-size:0.84rem; padding:6px 16px;">Create Your Companion</a>
                            <a class="btn" href="experts.html" style="font-size:0.84rem; padding:6px 16px; margin-left:8px;">Become an Expert</a>
                        </div>"""

if start_actions_old in idx_content:
    idx_content = idx_content.replace(start_actions_old, start_actions_new)
    print("Enhanced #start section actions.")

with open(os.path.join(BASE_DIR, "index.html"), "w", encoding="utf-8") as f:
    f.write(idx_content)

print("Updated index.html successfully.")
