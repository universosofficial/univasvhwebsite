import os
import re

DIR = r"C:\Users\user\Downloads\websites\templatemo_633_celadon"

SHARED_STYLE = """        <style>
            /* ---------- Celadon Claymorphism Multi-page Overrides ---------- */
            .nav a.active {
                color: var(--jade-ink) !important;
                font-weight: 600 !important;
            }
            .plans.grid-2 {
                display: grid !important;
                grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)) !important;
                gap: 24px !important;
            }
            .plans.grid-3 {
                display: grid !important;
                grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)) !important;
                gap: 24px !important;
            }
            .plans.grid-4 {
                display: grid !important;
                grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)) !important;
                gap: 22px !important;
            }
            @media (max-width: 900px) {
                .plans.grid-2, .plans.grid-3, .plans.grid-4 {
                    grid-template-columns: 1fr !important;
                }
            }
            .plan.identity-card {
                display: flex !important;
                flex-direction: column !important;
                min-height: 100% !important;
                text-align: left !important;
                transition: transform 0.28s var(--ease), box-shadow 0.28s var(--ease) !important;
            }
            .plan.identity-card:hover {
                transform: translateY(-6px) !important;
                box-shadow: 0 34px 50px -22px rgba(35, 45, 60, .42), var(--lip) !important;
            }
            .plan.identity-card blockquote {
                margin: 16px 0 !important;
                font-size: 1.02rem !important;
                line-height: 1.52 !important;
                color: var(--ink) !important;
                font-weight: 300 !important;
                font-family: 'Outfit', sans-serif !important;
                flex-grow: 1 !important;
            }
            .matrix-wrapper {
                background: linear-gradient(158deg, #FBFDFF, #F0F5FD 46%, #E6EDFA) !important;
                border-radius: 40px !important;
                box-shadow: 0 40px 60px -28px rgba(35, 45, 60, .42), inset 3px 4px 6px rgba(255, 255, 255, .98), inset -5px -7px 14px rgba(35, 45, 60, .11) !important;
                padding: 44px 36px !important;
                margin-top: 36px !important;
                overflow-x: auto !important;
            }
            .matrix-table {
                width: 100% !important;
                min-width: 620px !important;
                border-collapse: collapse !important;
                text-align: left !important;
                font-size: 0.95rem !important;
                color: var(--ink) !important;
            }
            .matrix-table th {
                font-family: 'Outfit', sans-serif !important;
                font-weight: 600 !important;
                font-size: 1.08rem !important;
                color: var(--ink) !important;
                padding: 18px 20px !important;
                border-bottom: 2px solid rgba(42, 122, 98, 0.22) !important;
            }
            .matrix-table td {
                padding: 16px 20px !important;
                border-bottom: 1px solid rgba(35, 45, 60, 0.08) !important;
                color: var(--ink-2) !important;
            }
            .matrix-table tr:hover td {
                background: rgba(255, 255, 255, 0.45) !important;
            }
            .matrix-table tr:last-child td {
                border-bottom: none !important;
            }
            .matrix-table td.center, .matrix-table th.center {
                text-align: center !important;
            }
            .check-pill {
                display: inline-flex !important;
                align-items: center !important;
                justify-content: center !important;
                width: 28px !important;
                height: 28px !important;
                border-radius: 99px !important;
                background: rgba(42, 122, 98, 0.12) !important;
                color: var(--jade-ink) !important;
                font-weight: 700 !important;
                font-size: 0.9rem !important;
            }
            .cross-pill {
                display: inline-flex !important;
                align-items: center !important;
                justify-content: center !important;
                width: 28px !important;
                height: 28px !important;
                border-radius: 99px !important;
                background: rgba(35, 45, 60, 0.06) !important;
                color: var(--ink-2) !important;
                font-size: 0.95rem !important;
            }
            .sim-box {
                background: linear-gradient(158deg, #FBFDFF, #F0F5FD 46%, #E6EDFA) !important;
                border-radius: 40px !important;
                box-shadow: 0 40px 60px -28px rgba(35, 45, 60, .42), inset 3px 4px 6px rgba(255, 255, 255, .98), inset -5px -7px 14px rgba(35, 45, 60, .11) !important;
                padding: 38px 32px !important;
                margin-top: 36px !important;
                position: relative !important;
                overflow: hidden !important;
            }
            .sim-header {
                display: flex !important;
                align-items: center !important;
                justify-content: space-between !important;
                padding-bottom: 20px !important;
                border-bottom: 1px solid rgba(42, 122, 98, 0.16) !important;
                margin-bottom: 24px !important;
                flex-wrap: wrap !important;
                gap: 14px !important;
            }
            .sim-companion-info {
                display: flex !important;
                align-items: center !important;
                gap: 14px !important;
            }
            .sim-avatar {
                width: 48px !important;
                height: 48px !important;
                border-radius: 18px !important;
                background: linear-gradient(135deg, var(--jade), #38A384) !important;
                color: #fff !important;
                display: flex !important;
                align-items: center !important;
                justify-content: center !important;
                font-weight: 600 !important;
                font-size: 1.2rem !important;
                box-shadow: var(--lift-jade) !important;
            }
            .sim-meta b {
                display: block !important;
                font-size: 1.05rem !important;
                color: var(--ink) !important;
            }
            .sim-meta span {
                font-size: 0.82rem !important;
                color: var(--ink-2) !important;
            }
            .sim-status {
                display: inline-flex !important;
                align-items: center !important;
                gap: 8px !important;
                padding: 7px 16px !important;
                border-radius: 99px !important;
                background: rgba(42, 122, 98, 0.1) !important;
                color: var(--jade-ink) !important;
                font-size: 0.82rem !important;
                font-weight: 500 !important;
            }
            .pulse-dot {
                width: 8px !important;
                height: 8px !important;
                border-radius: 99px !important;
                background: var(--jade) !important;
                box-shadow: 0 0 0 0 rgba(42, 122, 98, 0.5) !important;
                animation: pulse 2s infinite !important;
            }
            @keyframes pulse {
                0% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(42, 122, 98, 0.6); }
                70% { transform: scale(1); box-shadow: 0 0 0 8px rgba(42, 122, 98, 0); }
                100% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(42, 122, 98, 0); }
            }
            .sim-dialogue {
                display: flex !important;
                flex-direction: column !important;
                gap: 20px !important;
                margin-bottom: 28px !important;
            }
            .chat-bubble {
                border-radius: 22px !important;
                padding: 20px 24px !important;
                font-size: 0.95rem !important;
                line-height: 1.55 !important;
                position: relative !important;
            }
            .chat-bubble.user {
                align-self: flex-end !important;
                background: var(--sunk) !important;
                box-shadow: var(--well) !important;
                color: var(--ink) !important;
                max-width: 82% !important;
            }
            .chat-bubble.companion {
                align-self: flex-start !important;
                background: linear-gradient(158deg, #FFFFFF, var(--plate)) !important;
                box-shadow: var(--clay-sm), var(--lip) !important;
                color: var(--ink) !important;
                max-width: 88% !important;
            }
            .chat-bubble .author {
                display: block !important;
                font-size: 0.76rem !important;
                font-weight: 600 !important;
                text-transform: uppercase !important;
                letter-spacing: 0.08em !important;
                margin-bottom: 6px !important;
            }
            .chat-bubble.user .author {
                color: var(--ink-2) !important;
            }
            .chat-bubble.companion .author {
                color: var(--jade-ink) !important;
            }
            .chat-bubble p {
                margin: 0 !important;
                color: var(--ink) !important;
            }
            .chat-memory-badge {
                margin-top: 14px !important;
                display: inline-flex !important;
                align-items: center !important;
                gap: 7px !important;
                padding: 6px 14px !important;
                border-radius: 99px !important;
                background: rgba(42, 122, 98, 0.1) !important;
                color: var(--jade-ink) !important;
                font-size: 0.78rem !important;
                font-weight: 500 !important;
            }
            .sim-prompts {
                display: flex !important;
                flex-wrap: wrap !important;
                align-items: center !important;
                gap: 10px !important;
                padding-top: 20px !important;
                border-top: 1px solid rgba(42, 122, 98, 0.14) !important;
            }
            .sim-prompt-btn {
                border: none !important;
                outline: none !important;
                padding: 10px 18px !important;
                border-radius: 99px !important;
                background: var(--gloss) !important;
                box-shadow: var(--lift), var(--lip) !important;
                color: var(--ink) !important;
                font-family: 'Outfit', sans-serif !important;
                font-weight: 500 !important;
                font-size: 0.88rem !important;
                cursor: pointer !important;
                transition: transform 0.2s var(--ease), box-shadow 0.2s var(--ease), background 0.2s var(--ease) !important;
            }
            .sim-prompt-btn:hover {
                transform: translateY(-2px) !important;
                box-shadow: var(--lift-hi), var(--lip) !important;
            }
            .sim-prompt-btn.active {
                background: var(--jade) !important;
                color: #fff !important;
                box-shadow: var(--lift-jade-hi), var(--lip-jade) !important;
            }
            .email-card {
                background: linear-gradient(160deg, #FFFFFF, var(--plate) 48%, var(--plate-2)) !important;
                border-radius: 32px !important;
                padding: 32px 34px !important;
                box-shadow: var(--clay), var(--lip) !important;
                text-align: left !important;
                margin-top: 32px !important;
            }
            .email-header {
                border-bottom: 1px solid rgba(42, 122, 98, 0.14) !important;
                padding-bottom: 16px !important;
                margin-bottom: 20px !important;
            }
            .email-field {
                display: flex !important;
                gap: 12px !important;
                font-size: 0.88rem !important;
                margin-bottom: 6px !important;
            }
            .email-field b {
                color: var(--ink-2) !important;
                min-width: 65px !important;
            }
            .email-field span {
                color: var(--ink) !important;
            }
            .email-body {
                font-size: 0.94rem !important;
                line-height: 1.65 !important;
                color: var(--ink) !important;
            }
            .email-body p {
                margin: 0 0 14px 0 !important;
            }
        </style>
"""

# ==================== 1. PRICING.HTML ====================
with open(os.path.join(DIR, "pricing.html"), "r", encoding="utf-8") as f:
    p_content = f.read()

# Update CSS link
p_content = re.sub(r'templatemo-633-celadon-style\.css(?:\?[^"]*)?', 'templatemo-633-celadon-style.css?v=20261123c', p_content)

# Add style if not present
if "/* ---------- Celadon Claymorphism Multi-page Overrides ---------- */" not in p_content:
    p_content = p_content.replace('</head>', f'{SHARED_STYLE}\n    </head>')

# Replace matrix-container with matrix-wrapper
p_content = p_content.replace('<div class="matrix-container rv d1">', '<div class="matrix-wrapper rv d1">')
p_content = p_content.replace('class="check-dot"', 'class="check-pill"')
p_content = p_content.replace('class="cross-dash"', 'class="cross-pill"')

with open(os.path.join(DIR, "pricing.html"), "w", encoding="utf-8") as f:
    f.write(p_content)
print("Updated pricing.html successfully")

# ==================== 2. HOW-IT-WORKS.HTML ====================
with open(os.path.join(DIR, "how-it-works.html"), "r", encoding="utf-8") as f:
    h_content = f.read()

h_content = re.sub(r'templatemo-633-celadon-style\.css(?:\?[^"]*)?', 'templatemo-633-celadon-style.css?v=20261123c', h_content)
if "/* ---------- Celadon Claymorphism Multi-page Overrides ---------- */" not in h_content:
    h_content = h_content.replace('</head>', f'{SHARED_STYLE}\n    </head>')

# Replace the comparison section with authentic Celadon .plans grid and .plan cards
comp_old_regex = r'<section class="pad" id="comparison">.*?</section>'
comp_new = '''<section class="pad" id="comparison">
                <div class="shell center">
                    <span class="eyebrow rv">Architecture Comparison</span>
                    <h2 class="h2 rv">Ordinary Chatbots vs. Virtual Human.</h2>
                    <p class="lede rv d1">Why our approach redefines interactive mentorship.</p>
                </div>
                <div class="shell">
                    <div class="plans grid-2" style="margin-top:36px;">
                        <!-- Conventional Chatbots -->
                        <article class="plan rv" style="border-top: 4px solid var(--coral); text-align:left;">
                            <span class="tag" style="color:var(--coral-ink, #A8421F);">Conventional AI Assistants</span>
                            <h3 style="font-size:1.35rem; margin:14px 0 8px; color:var(--ink);">Stateless &amp; Generic</h3>
                            <p style="font-size:0.92rem; color:var(--ink-2); margin-bottom:20px;">Built on ephemeral sessions that forget context the moment you close the tab.</p>
                            <div class="groove" style="margin-bottom:20px;"></div>
                            <ul class="feat">
                                <li style="align-items:flex-start; gap:12px;">
                                    <span class="cross-pill" style="color:var(--coral); font-weight:700;">&#10005;</span>
                                    <div><b>Memory Resets:</b> Forgets who you are and what you decided as soon as the session closes.</div>
                                </li>
                                <li style="align-items:flex-start; gap:12px;">
                                    <span class="cross-pill" style="color:var(--coral); font-weight:700;">&#10005;</span>
                                    <div><b>Unanchored Advice:</b> Answers with generic internet consensus rather than battle-tested domain frameworks.</div>
                                </li>
                                <li style="align-items:flex-start; gap:12px;">
                                    <span class="cross-pill" style="color:var(--coral); font-weight:700;">&#10005;</span>
                                    <div><b>Canned Check-ins:</b> Dispatches impersonal automated email blasts that ignore your actual conversation history.</div>
                                </li>
                                <li style="align-items:flex-start; gap:12px;">
                                    <span class="cross-pill" style="color:var(--coral); font-weight:700;">&#10005;</span>
                                    <div><b>No Accountability:</b> Never checks whether you completed the tasks or resolved the dilemma you discussed.</div>
                                </li>
                            </ul>
                        </article>

                        <!-- Virtual Human System -->
                        <article class="plan hot rv d1" style="border-top: 4px solid var(--jade); text-align:left;">
                            <span class="tag" style="color:var(--jade-ink);">Virtual Human System</span>
                            <h3 style="font-size:1.35rem; margin:14px 0 8px; color:var(--ink);">Relational &amp; Grounded</h3>
                            <p style="font-size:0.92rem; color:var(--ink-2); margin-bottom:20px;">Anchored in persistent cognitive graphs that evolve across weeks and months.</p>
                            <div class="groove" style="margin-bottom:20px;"></div>
                            <ul class="feat">
                                <li style="align-items:flex-start; gap:12px;">
                                    <span class="check-pill" style="color:var(--jade-ink); font-weight:700;">&#10003;</span>
                                    <div><b>Episodic Continuity:</b> Retains your business context, team dynamics, and personal milestones over months.</div>
                                </li>
                                <li style="align-items:flex-start; gap:12px;">
                                    <span class="check-pill" style="color:var(--jade-ink); font-weight:700;">&#10003;</span>
                                    <div><b>Grounded Expertise:</b> Powered by verified frameworks, documents, and private methodologies uploaded by proven mentors.</div>
                                </li>
                                <li style="align-items:flex-start; gap:12px;">
                                    <span class="check-pill" style="color:var(--jade-ink); font-weight:700;">&#10003;</span>
                                    <div><b>Tailored Proactive Email:</b> Follows up with personalized reflections referencing the specific trade-offs of your last conversation.</div>
                                </li>
                                <li style="align-items:flex-start; gap:12px;">
                                    <span class="check-pill" style="color:var(--jade-ink); font-weight:700;">&#10003;</span>
                                    <div><b>Adaptive Sparring:</b> Calibrates directness and challenge level to push your critical thinking forward.</div>
                                </li>
                            </ul>
                        </article>
                    </div>
                </div>
            </section>'''

h_content = re.sub(comp_old_regex, comp_new, h_content, flags=re.DOTALL)

with open(os.path.join(DIR, "how-it-works.html"), "w", encoding="utf-8") as f:
    f.write(h_content)
print("Updated how-it-works.html successfully")

# ==================== 3. COMPANION.HTML ====================
with open(os.path.join(DIR, "companion.html"), "r", encoding="utf-8") as f:
    c_content = f.read()

c_content = re.sub(r'templatemo-633-celadon-style\.css(?:\?[^"]*)?', 'templatemo-633-celadon-style.css?v=20261123c', c_content)
if "/* ---------- Celadon Claymorphism Multi-page Overrides ---------- */" not in c_content:
    c_content = c_content.replace('</head>', f'{SHARED_STYLE}\n    </head>')

# Replace #pillars
pillars_old_regex = r'<section class="pad" id="pillars">.*?</section>'
pillars_new = '''<section class="pad" id="pillars">
                <div class="shell center">
                    <span class="eyebrow rv">Core Architecture</span>
                    <h2 class="h2 rv">Why Virtual Human companions feel profoundly different.</h2>
                    <p class="lede rv d1">Engineered from the ground up for long-term relationships, intellectual depth, and actionable growth.</p>
                </div>
                <div class="shell">
                    <div class="plans grid-2" style="margin-top:36px;">
                        <!-- Pillar 1 -->
                        <article class="plan rv" style="text-align:left;">
                            <div class="tile t-jade" style="width:52px; height:52px; border-radius:18px; margin-bottom:16px;">
                                <svg viewBox="0 0 24 24" style="width:24px; height:24px; stroke:var(--jade-ink); fill:none; stroke-width:2;"><path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg>
                            </div>
                            <span class="tag" style="color:var(--jade-ink); margin-bottom:8px;">01 &middot; Episodic Memory</span>
                            <h3 style="font-size:1.3rem; margin:8px 0; color:var(--ink);">Relational Continuity</h3>
                            <p style="font-size:0.92rem; line-height:1.55; color:var(--ink-2); margin-top:8px;">Every session builds on the last. Your companion keeps track of team dynamics, recurring challenges, personal principles, and project milestones across months of collaboration.</p>
                        </article>
                        <!-- Pillar 2 -->
                        <article class="plan rv d1" style="text-align:left;">
                            <div class="tile t-sky" style="width:52px; height:52px; border-radius:18px; margin-bottom:16px;">
                                <svg viewBox="0 0 24 24" style="width:24px; height:24px; stroke:var(--sky-ink); fill:none; stroke-width:2;"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg>
                            </div>
                            <span class="tag" style="color:var(--sky-ink); margin-bottom:8px;">02 &middot; Proactive Check-ins</span>
                            <h3 style="font-size:1.3rem; margin:8px 0; color:var(--ink);">Personalized Follow-ups</h3>
                            <p style="font-size:0.92rem; line-height:1.55; color:var(--ink-2); margin-top:8px;">Users hate generic automated emails. Virtual Human companions dispatch thoughtful, tailored messages referencing the exact ideas, metrics, and challenges you discussed in your last session.</p>
                        </article>
                        <!-- Pillar 3 -->
                        <article class="plan rv d2" style="text-align:left;">
                            <div class="tile t-coral" style="width:52px; height:52px; border-radius:18px; margin-bottom:16px;">
                                <svg viewBox="0 0 24 24" style="width:24px; height:24px; stroke:var(--coral-ink, #A8421F); fill:none; stroke-width:2;"><circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1 0 2.83 2 2 0 0 1-2.83 0l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-2 2 2 2 0 0 1-2-2v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83 0 2 2 0 0 1 0-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1-2-2 2 2 0 0 1 2-2h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 0-2.83 2 2 0 0 1 2.83 0l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 2-2 2 2 0 0 1 2 2v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 0 2 2 0 0 1 0 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 2 2 2 2 0 0 1-2 2h-.09a1.65 1.65 0 0 0-1.51 1z"/></svg>
                            </div>
                            <span class="tag" style="color:var(--coral-ink, #A8421F); margin-bottom:8px;">03 &middot; Cognitive Calibration</span>
                            <h3 style="font-size:1.3rem; margin:8px 0; color:var(--ink);">Adaptive Personality &amp; Tone</h3>
                            <p style="font-size:0.92rem; line-height:1.55; color:var(--ink-2); margin-top:8px;">Tune your companion's voice to your style. Adjust sliders for directness, analytical rigor, warmth, and challenging pushback to create the ideal intellectual sparring partner.</p>
                        </article>
                        <!-- Pillar 4 -->
                        <article class="plan rv d3" style="text-align:left;">
                            <div class="tile t-jade" style="width:52px; height:52px; border-radius:18px; margin-bottom:16px;">
                                <svg viewBox="0 0 24 24" style="width:24px; height:24px; stroke:var(--jade-ink); fill:none; stroke-width:2;"><polyline points="9 11 12 14 22 4"/><path d="M21 12v7a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11"/></svg>
                            </div>
                            <span class="tag" style="color:var(--jade-ink); margin-bottom:8px;">04 &middot; Action &amp; Reflection</span>
                            <h3 style="font-size:1.3rem; margin:8px 0; color:var(--ink);">Practical Milestones</h3>
                            <p style="font-size:0.92rem; line-height:1.55; color:var(--ink-2); margin-top:8px;">Transform dialogue into measurable progress. Your companion assigns relevant reflection prompts, decision journals, and accountability milestones to keep you advancing.</p>
                        </article>
                    </div>
                </div>
            </section>'''
c_content = re.sub(pillars_old_regex, pillars_new, c_content, flags=re.DOTALL)

# Replace #personas
personas_old_regex = r'<section class="pad" id="personas">.*?</section>'
personas_new = '''<section class="pad" id="personas">
                <div class="shell center">
                    <span class="eyebrow rv">Curated Companions</span>
                    <h2 class="h2 rv">Minds crafted for specific cognitive journeys.</h2>
                    <p class="lede rv d1">Choose a dedicated companion persona or craft a tailored AI identity tuned to your exact goals.</p>
                </div>
                <div class="shell">
                    <div class="plans grid-3" style="margin-top:36px;">
                        <!-- Aria -->
                        <article class="plan hot rv" style="text-align:left;">
                            <span class="tag">Founder Strategy</span>
                            <div class="who" style="margin:16px 0;">
                                <span class="face t-jade" style="width:52px; height:52px; font-size:1.2rem;">AR</span>
                                <div><b style="font-size:1.2rem;">Aria</b><span style="font-size:0.85rem;">The Strategic Co-Founder</span></div>
                            </div>
                            <p class="desc" style="min-height:auto; margin-bottom:16px;">Specialized in early-stage validation, go-to-market strategy, unit economics, and decisive prioritization for founders and operators.</p>
                            <div class="groove" style="margin:16px 0;"></div>
                            <div class="chips" style="margin-bottom:20px; gap:8px;">
                                <span class="chip" style="font-size:0.75rem; padding:6px 12px;"><i style="background:var(--jade)"></i>Direct</span>
                                <span class="chip" style="font-size:0.75rem; padding:6px 12px;"><i style="background:var(--jade)"></i>Analytical</span>
                                <span class="chip" style="font-size:0.75rem; padding:6px 12px;"><i style="background:var(--jade)"></i>Uncompromising</span>
                            </div>
                            <a class="btn solid wide" href="#simulator">Engage Aria</a>
                        </article>

                        <!-- Kaelen -->
                        <article class="plan rv d1" style="text-align:left;">
                            <span class="tag">Deep Focus</span>
                            <div class="who" style="margin:16px 0;">
                                <span class="face t-sky" style="width:52px; height:52px; font-size:1.2rem;">KA</span>
                                <div><b style="font-size:1.2rem;">Kaelen</b><span style="font-size:0.85rem;">The Deep Focus Architect</span></div>
                            </div>
                            <p class="desc" style="min-height:auto; margin-bottom:16px;">Designed for engineers, researchers, and technical leaders who need calm, distraction-free thinking and structured architecture reviews.</p>
                            <div class="groove" style="margin:16px 0;"></div>
                            <div class="chips" style="margin-bottom:20px; gap:8px;">
                                <span class="chip" style="font-size:0.75rem; padding:6px 12px;"><i style="background:var(--sky)"></i>Methodical</span>
                                <span class="chip" style="font-size:0.75rem; padding:6px 12px;"><i style="background:var(--sky)"></i>Systems</span>
                                <span class="chip" style="font-size:0.75rem; padding:6px 12px;"><i style="background:var(--sky)"></i>Minimalist</span>
                            </div>
                            <a class="btn wide" href="#simulator">Engage Kaelen</a>
                        </article>

                        <!-- Lyra -->
                        <article class="plan rv d2" style="text-align:left;">
                            <span class="tag">Creative Direction</span>
                            <div class="who" style="margin:16px 0;">
                                <span class="face t-coral" style="width:52px; height:52px; font-size:1.2rem;">LY</span>
                                <div><b style="font-size:1.2rem;">Lyra</b><span style="font-size:0.85rem;">The Creative Catalyst</span></div>
                            </div>
                            <p class="desc" style="min-height:auto; margin-bottom:16px;">Built for creative directors, writers, and product visionaries seeking lateral thinking, metaphor exploration, and breakthrough storytelling.</p>
                            <div class="groove" style="margin:16px 0;"></div>
                            <div class="chips" style="margin-bottom:20px; gap:8px;">
                                <span class="chip" style="font-size:0.75rem; padding:6px 12px;"><i style="background:var(--coral)"></i>Imaginative</span>
                                <span class="chip" style="font-size:0.75rem; padding:6px 12px;"><i style="background:var(--coral)"></i>Empathic</span>
                                <span class="chip" style="font-size:0.75rem; padding:6px 12px;"><i style="background:var(--coral)"></i>Lateral Ideation</span>
                            </div>
                            <a class="btn wide" href="#simulator">Engage Lyra</a>
                        </article>
                    </div>
                </div>
            </section>

            <!-- personalized email check-in showcase -->
            <section class="pad" id="email-feature">
                <div class="shell center">
                    <span class="eyebrow rv">No Generic Spam</span>
                    <h2 class="h2 rv">Proactive emails tailored to your exact dialogues.</h2>
                    <p class="lede rv d1">Users hate repetitive automated reminders. Virtual Human companions dispatch thoughtful, context-anchored follow-ups that pick up the thread of your last conversation.</p>
                </div>
                <div class="shell">
                    <div class="email-card rv d1">
                        <div class="email-header">
                            <div class="email-field">
                                <b>From:</b> <span>Aria &middot; Strategic Thinking Companion &lt;aria@virtualhuman.ai&gt;</span>
                            </div>
                            <div class="email-field">
                                <b>To:</b> <span>Elena (Founder) &lt;elena@acme-saas.com&gt;</span>
                            </div>
                            <div class="email-field">
                                <b>Subject:</b> <span><b>[Reflection] Your gross margin trade-off &amp; the 12-seat pilot rollout</b></span>
                            </div>
                            <div class="email-field">
                                <b>Anchored:</b> <span style="color:var(--jade-ink); font-weight:500;">Conversation #14 &middot; Yesterday at 4:15 PM</span>
                            </div>
                        </div>
                        <div class="email-body">
                            <p>Hi Elena,</p>
                            <p>In our session yesterday, you mentioned feeling torn between shipping the redesign or preparing for your enterprise partner demo on Nov 30th. You uncovered that <b>42% of funnel drop-off happened at the team invite step</b>, yet a full redesign risked postponing that demo.</p>
                            <p>Here are the two core questions to reflect on before your morning standup:</p>
                            <ul style="margin: 0 0 16px 20px; padding:0; line-height:1.6;">
                                <li><b>1.</b> Can you test the single inline modal for the invite step with your 3 pilot teams this Thursday?</li>
                                <li><b>2.</b> Does preserving the Nov 30th demo date protect your committed $36K ARR pipeline more than delaying for a visual polish?</li>
                            </ul>
                            <p>Whenever you're ready to review the conversion data from Thursday's pilot test, just open Virtual Human—I'll have our session notes loaded.</p>
                            <p style="margin-top:20px; font-weight:500; color:var(--ink-2);">&mdash; Aria</p>
                        </div>
                    </div>
                </div>
            </section>'''

c_content = re.sub(personas_old_regex, personas_new, c_content, flags=re.DOTALL)

with open(os.path.join(DIR, "companion.html"), "w", encoding="utf-8") as f:
    f.write(c_content)
print("Updated companion.html successfully")

# ==================== 4. EXPERTS.HTML ====================
with open(os.path.join(DIR, "experts.html"), "r", encoding="utf-8") as f:
    e_content = f.read()

e_content = re.sub(r'templatemo-633-celadon-style\.css(?:\?[^"]*)?', 'templatemo-633-celadon-style.css?v=20261123c', e_content)
if "/* ---------- Celadon Claymorphism Multi-page Overrides ---------- */" not in e_content:
    e_content = e_content.replace('</head>', f'{SHARED_STYLE}\n    </head>')

# In #steps
steps_old_regex = r'<div class="clay-grid-4">.*?</div>\s*</div>\s*</section>'
steps_new = '''<div class="plans grid-4" style="margin-top:36px;">
                        <article class="plan rv" style="text-align:left;">
                            <div class="tile t-jade" style="width:48px; height:48px; border-radius:16px; margin-bottom:14px;">
                                <svg viewBox="0 0 24 24" style="width:22px; height:22px; stroke:var(--jade-ink); fill:none; stroke-width:2;"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/></svg>
                            </div>
                            <span class="tag" style="color:var(--jade-ink);">Step 01 &middot; Ingest</span>
                            <h3 style="font-size:1.25rem; margin:10px 0 6px; color:var(--ink);">Knowledge Vault</h3>
                            <p style="font-size:0.9rem; color:var(--ink-2); line-height:1.5;">Upload your essays, frameworks, podcasts, books, and decision logs into an encrypted vault. Your AI identity reasons from your actual materials.</p>
                        </article>
                        <article class="plan rv d1" style="text-align:left;">
                            <div class="tile t-sky" style="width:48px; height:48px; border-radius:16px; margin-bottom:14px;">
                                <svg viewBox="0 0 24 24" style="width:22px; height:22px; stroke:var(--sky-ink); fill:none; stroke-width:2;"><circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1 0 2.83 2 2 0 0 1-2.83 0l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-2 2 2 2 0 0 1-2-2v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83 0 2 2 0 0 1 0-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1-2-2 2 2 0 0 1 2-2h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 0-2.83 2 2 0 0 1 2.83 0l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 2-2 2 2 0 0 1 2 2v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 0 2 2 0 0 1 0 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 2 2 2 2 0 0 1-2 2h-.09a1.65 1.65 0 0 0-1.51 1z"/></svg>
                            </div>
                            <span class="tag" style="color:var(--sky-ink);">Step 02 &middot; Calibrate</span>
                            <h3 style="font-size:1.25rem; margin:10px 0 6px; color:var(--ink);">Tone &amp; Guardrails</h3>
                            <p style="font-size:0.9rem; color:var(--ink-2); line-height:1.5;">Define your communication rhythm, analytical strictness, and boundaries. Set topics you refuse to advise on, and instruct how to challenge users.</p>
                        </article>
                        <article class="plan rv d2" style="text-align:left;">
                            <div class="tile t-coral" style="width:48px; height:48px; border-radius:16px; margin-bottom:14px;">
                                <svg viewBox="0 0 24 24" style="width:22px; height:22px; stroke:var(--coral-ink, #A8421F); fill:none; stroke-width:2;"><path d="M12 1a3 3 0 0 0-3 3v8a3 3 0 0 0 6 0V4a3 3 0 0 0-3-3z"/><path d="M19 10v2a7 7 0 0 1-14 0v-2"/><line x1="12" y1="19" x2="12" y2="23"/><line x1="8" y1="23" x2="16" y2="23"/></svg>
                            </div>
                            <span class="tag" style="color:var(--coral-ink, #A8421F);">Step 03 &middot; Voice</span>
                            <h3 style="font-size:1.25rem; margin:10px 0 6px; color:var(--ink);">Verified Identity</h3>
                            <p style="font-size:0.9rem; color:var(--ink-2); line-height:1.5;">Pair your written identity with an expressive voice model. Once verified, your identity receives an authentic creator seal on the directory.</p>
                        </article>
                        <article class="plan rv d3" style="text-align:left;">
                            <div class="tile t-jade" style="width:48px; height:48px; border-radius:16px; margin-bottom:14px;">
                                <svg viewBox="0 0 24 24" style="width:22px; height:22px; stroke:var(--jade-ink); fill:none; stroke-width:2;"><line x1="12" y1="1" x2="12" y2="23"/><path d="M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg>
                            </div>
                            <span class="tag" style="color:var(--jade-ink);">Step 04 &middot; Monetize</span>
                            <h3 style="font-size:1.25rem; margin:10px 0 6px; color:var(--ink);">Subscriptions</h3>
                            <p style="font-size:0.9rem; color:var(--ink-2); line-height:1.5;">Distribute free introductory sessions to build audience trust, then gate advanced reasoning behind monthly subscriptions with expert pricing.</p>
                        </article>
                    </div>
                </div>
            </section>'''
e_content = re.sub(steps_old_regex, steps_new, e_content, flags=re.DOTALL)

# In #guarantees
guar_old_regex = r'<div class="clay-grid-3">.*?</div>\s*</div>\s*</section>'
guar_new = '''<div class="plans grid-3" style="margin-top:36px;">
                        <article class="plan rv" style="text-align:left;">
                            <span class="tag" style="color:var(--jade-ink);">Zero Training</span>
                            <h3 style="font-size:1.25rem; margin:12px 0 8px; color:var(--ink);">No Public LLM Training</h3>
                            <p style="font-size:0.9rem; color:var(--ink-2); line-height:1.55;">Your uploaded documents and case studies are strictly used to serve your identity's retrieval engine. They are never exported or used to train open LLM models.</p>
                        </article>
                        <article class="plan rv d1" style="text-align:left;">
                            <span class="tag" style="color:var(--sky-ink);">Data Privacy</span>
                            <h3 style="font-size:1.25rem; margin:12px 0 8px; color:var(--ink);">Granular Privacy Controls</h3>
                            <p style="font-size:0.9rem; color:var(--ink-2); line-height:1.55;">Flag sensitive files as internal reasoning context only—your AI identity can synthesize principles without quoting proprietary figures or client names.</p>
                        </article>
                        <article class="plan rv d2" style="text-align:left;">
                            <span class="tag" style="color:var(--coral-ink, #A8421F);">Calendar Sync</span>
                            <h3 style="font-size:1.25rem; margin:12px 0 8px; color:var(--ink);">Live Escalation Option</h3>
                            <p style="font-size:0.9rem; color:var(--ink-2); line-height:1.55;">Enable users who hit complex, high-stakes decisions to request a direct, paid consultation on your live calendar directly through the conversation window.</p>
                        </article>
                    </div>
                </div>
            </section>'''
e_content = re.sub(guar_old_regex, guar_new, e_content, flags=re.DOTALL)

with open(os.path.join(DIR, "experts.html"), "w", encoding="utf-8") as f:
    f.write(e_content)
print("Updated experts.html successfully")

# ==================== 5. INDEX.HTML & FAQ.HTML ====================
for fname in ["index.html", "faq.html"]:
    with open(os.path.join(DIR, fname), "r", encoding="utf-8") as f:
        content = f.read()
    content = re.sub(r'templatemo-633-celadon-style\.css(?:\?[^"]*)?', 'templatemo-633-celadon-style.css?v=20261123c', content)
    if "/* ---------- Celadon Claymorphism Multi-page Overrides ---------- */" not in content:
        content = content.replace('</head>', f'{SHARED_STYLE}\n    </head>')
    with open(os.path.join(DIR, fname), "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Updated {fname} successfully")

print("All HTML files updated!")
