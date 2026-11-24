import os

DIR = r"C:\Users\user\Downloads\websites\templatemo_633_celadon"

SHARED_STYLE = """
        <style>
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
        </style>
"""

# ----------------- DISCOVER.HTML -----------------
discover_html = f"""<!DOCTYPE html>
<!--
  Celadon Template
  https://templatemo.com/tm-633-celadon
-->
<!-- Celadon Soft, a claymorphism SaaS landing template adapted for Virtual Human. Free to use with attribution links kept in the footer. -->
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Discover AI Identities — Virtual Human</title>
        <meta name="description"
              content="Discover interactive AI identities representing founders, mentors, and specialists. Explore their mental models and start a personalized conversation.">
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@200;300;400;500&family=Albert+Sans:wght@400;500;600&display=swap"
              rel="stylesheet">
        <link rel="stylesheet" href="templatemo-633-celadon-style.css?v=20261123c">
{SHARED_STYLE}
    </head>
    <body>
        <header class="top" id="top">
            <div class="shell bar">
                <a class="brand" href="index.html"><span class="mark" aria-hidden="true"></span>Virtual Human</a>
                <nav class="nav">
                    <a href="index.html">Home</a>
                    <a href="companion.html">AI Companion</a>
                    <a href="discover.html" class="active">Discover</a>
                    <a href="experts.html">For Experts</a>
                    <a href="how-it-works.html">How It Works</a>
                    <a href="pricing.html">Pricing</a>
                    <a href="faq.html">FAQ</a>
                </nav>
                <a class="btn solid" href="index.html#start">Get Started</a>
                <button class="burger"
                        id="burger"
                        aria-label="Open menu"
                        aria-expanded="false"
                        aria-controls="drawer">
                    <span></span><span></span><span></span>
                </button>
            </div>
        </header>
        <div class="scrim" id="scrim"></div>
        <aside class="drawer" id="drawer" aria-label="Menu">
            <span class="dtag">Menu</span>
            <a href="index.html">Home</a>
            <a href="companion.html">AI Companion</a>
            <a href="discover.html">Discover</a>
            <a href="experts.html">For Experts</a>
            <a href="how-it-works.html">How It Works</a>
            <a href="pricing.html">Pricing</a>
            <a href="faq.html">FAQ</a>
            <a class="btn solid" href="index.html#start">Get Started</a>
        </aside>
        <main id="discover-page">
            <!-- discover hero -->
            <section class="hero">
                <div class="shell">
                    <span class="pill rv"><b>Directory</b> Curated Knowledge Network</span>
                    <h1 class="rv d1">Meet the minds behind the expertise.</h1>
                    <p class="sub rv d2">Browse interactive AI identities shaped by real people who have built companies, led engineering divisions, designed products, and scaled organizations. Ask specific questions and receive grounded advice.</p>
                    <div class="acts rv d3">
                        <a class="btn solid" href="#directory">Browse Identities</a>
                        <a class="btn" href="experts.html">Create Your Identity</a>
                    </div>
                    <p class="note rv d3">Every identity is anchored in verified documents, frameworks, and personal methodologies.</p>
                </div>
            </section>

            <!-- directory -->
            <section class="pad" id="directory">
                <div class="shell center">
                    <span class="eyebrow rv">Featured Identities</span>
                    <h2 class="h2 rv">Explore by domain and discipline.</h2>
                    <p class="lede rv d1">Choose an identity to engage in a structured, conversational exploration of their knowledge.</p>
                    <div class="chips rv d1" style="margin-top:24px;">
                        <span class="chip"><i style="background:var(--jade)"></i>Startup Strategy</span>
                        <span class="chip"><i style="background:var(--sky)"></i>Product Architecture</span>
                        <span class="chip"><i style="background:var(--coral)"></i>Engineering Leadership</span>
                        <span class="chip"><i style="background:#F0C980"></i>Applied AI</span>
                        <span class="chip"><i style="background:var(--jade)"></i>Design Systems</span>
                        <span class="chip"><i style="background:var(--sky)"></i>Capital Allocation</span>
                    </div>
                </div>
                <div class="shell">
                    <div class="plans grid-3" style="margin-top:36px;">
                        <!-- Card 1 -->
                        <article class="plan identity-card rv">
                            <div class="qtop">
                                <span class="co"><i class="t-jade"></i>Founder &middot; B2B SaaS</span>
                                <span class="result" style="font-size:0.75rem; color:var(--jade-ink); font-weight:600;">$12M ARR</span>
                            </div>
                            <div class="who" style="margin:16px 0;">
                                <span class="face t-jade">ER</span>
                                <div><b>Elena Rostova</b><span>Bootstrapped to Scale</span></div>
                            </div>
                            <blockquote>
                                "Ask me about customer discovery, pricing iterations, transitioning from founder-led sales, and protecting gross margins."
                            </blockquote>
                            <div class="groove" style="margin-top:auto; margin-bottom:18px;"></div>
                            <a class="btn solid wide" href="companion.html">Start Conversation</a>
                        </article>

                        <!-- Card 2 -->
                        <article class="plan identity-card rv d1">
                            <div class="qtop">
                                <span class="co"><i class="t-sky"></i>Strategy &middot; Growth</span>
                                <span class="result" style="font-size:0.75rem; color:var(--sky-ink); font-weight:600;">Ex-VP Growth</span>
                            </div>
                            <div class="who" style="margin:16px 0;">
                                <span class="face t-sky">MV</span>
                                <div><b>Marcus Vance</b><span>Product Loops &amp; Compounding</span></div>
                            </div>
                            <blockquote>
                                "Ask me about viral coefficient mechanics, cohort retention curves, user activation friction, and organic compounding channels."
                            </blockquote>
                            <div class="groove" style="margin-top:auto; margin-bottom:18px;"></div>
                            <a class="btn solid wide" href="companion.html">Start Conversation</a>
                        </article>

                        <!-- Card 3 -->
                        <article class="plan identity-card rv d2">
                            <div class="qtop">
                                <span class="co"><i class="t-coral"></i>Research &middot; Applied AI</span>
                                <span class="result" style="font-size:0.75rem; color:var(--coral-ink, #A8421F); font-weight:600;">PhD Cognitive Sci</span>
                            </div>
                            <div class="who" style="margin:16px 0;">
                                <span class="face t-coral">AT</span>
                                <div><b>Dr. Aris Thorne</b><span>LLM Alignment &amp; Memory</span></div>
                            </div>
                            <blockquote>
                                "Ask me about episodic memory architecture, grounding techniques, reducing model hallucination, and evaluating AI agent outputs."
                            </blockquote>
                            <div class="groove" style="margin-top:auto; margin-bottom:18px;"></div>
                            <a class="btn solid wide" href="companion.html">Start Conversation</a>
                        </article>

                        <!-- Card 4 -->
                        <article class="plan identity-card rv">
                            <div class="qtop">
                                <span class="co"><i class="t-jade"></i>Engineering &middot; Scale</span>
                                <span class="result" style="font-size:0.75rem; color:var(--jade-ink); font-weight:600;">Cloud Systems</span>
                            </div>
                            <div class="who" style="margin:16px 0;">
                                <span class="face t-jade">SL</span>
                                <div><b>Sarah Lindqvist</b><span>VP Engineering</span></div>
                            </div>
                            <blockquote>
                                "Ask me about technical debt management, hiring high-performing engineers, decoupling monoliths, and building resilient distributed systems."
                            </blockquote>
                            <div class="groove" style="margin-top:auto; margin-bottom:18px;"></div>
                            <a class="btn solid wide" href="companion.html">Start Conversation</a>
                        </article>

                        <!-- Card 5 -->
                        <article class="plan identity-card rv d1">
                            <div class="qtop">
                                <span class="co"><i class="t-sky"></i>Creative &middot; Systems</span>
                                <span class="result" style="font-size:0.75rem; color:var(--sky-ink); font-weight:600;">Brand Identity</span>
                            </div>
                            <div class="who" style="margin:16px 0;">
                                <span class="face t-sky">KS</span>
                                <div><b>Kenji Sato</b><span>Design Director</span></div>
                            </div>
                            <blockquote>
                                "Ask me about tactile claymorphic interfaces, cohesive multi-platform design systems, typography hierarchy, and emotional UI design."
                            </blockquote>
                            <div class="groove" style="margin-top:auto; margin-bottom:18px;"></div>
                            <a class="btn solid wide" href="companion.html">Start Conversation</a>
                        </article>

                        <!-- Card 6 -->
                        <article class="plan identity-card rv d2">
                            <div class="qtop">
                                <span class="co"><i class="t-coral"></i>Venture &middot; Capital</span>
                                <span class="result" style="font-size:0.75rem; color:var(--coral-ink, #A8421F); font-weight:600;">Seed Allocator</span>
                            </div>
                            <div class="who" style="margin:16px 0;">
                                <span class="face t-coral">AD</span>
                                <div><b>Amara Diallo</b><span>Managing Partner</span></div>
                            </div>
                            <blockquote>
                                "Ask me about pitching pre-seed investors, cap table governance, convertible notes vs SAFE dynamics, and navigating market downturns."
                            </blockquote>
                            <div class="groove" style="margin-top:auto; margin-bottom:18px;"></div>
                            <a class="btn solid wide" href="companion.html">Start Conversation</a>
                        </article>
                    </div>
                </div>
            </section>

            <!-- creator invite plate -->
            <section class="pad" id="create-invite">
                <div class="shell">
                    <div class="close-plate rv">
                        <span class="eyebrow">For Mentors &amp; Experts</span>
                        <h2>Have valuable experience to share with the world?</h2>
                        <p class="lede">Transform your frameworks, articles, and lessons into an interactive AI identity that provides continuous mentorship while respecting your boundaries.</p>
                        <div style="margin-top:24px;">
                            <a class="btn solid" href="experts.html">Learn About Building Your AI Identity &rarr;</a>
                        </div>
                    </div>
                </div>
            </section>
        </main>
        <footer class="foot">
            <div class="shell">
                <div class="footlinks rv" style="display:flex; flex-wrap:wrap; justify-content:space-between; align-items:center; gap:20px; padding:24px 30px; margin-bottom:18px; background:var(--plate); border-radius:28px; box-shadow:var(--clay-sm), var(--lip);">
                    <div>
                        <a class="brand" href="index.html" style="margin-bottom:6px;"><span class="mark" aria-hidden="true"></span>Virtual Human</a>
                        <p style="font-size:0.88rem; color:var(--ink-2); max-width:480px; margin:6px 0 0;">An interactive AI identity and companion platform making human knowledge, experience and expertise accessible through meaningful conversations.</p>
                    </div>
                    <div class="footlinks-nav">
                        <a href="companion.html" style="font-size:0.88rem; color:var(--ink-2); text-decoration:none; font-weight:500;">AI Companion</a>
                        <a href="discover.html" style="font-size:0.88rem; color:var(--ink-2); text-decoration:none; font-weight:500;">Discover</a>
                        <a href="experts.html" style="font-size:0.88rem; color:var(--ink-2); text-decoration:none; font-weight:500;">For Experts</a>
                        <a href="how-it-works.html" style="font-size:0.88rem; color:var(--ink-2); text-decoration:none; font-weight:500;">How It Works</a>
                        <a href="pricing.html" style="font-size:0.88rem; color:var(--ink-2); text-decoration:none; font-weight:500;">Pricing</a>
                        <a href="faq.html" style="font-size:0.88rem; color:var(--ink-2); text-decoration:none; font-weight:500;">FAQ</a>
                    </div>
                </div>
                <div class="footbar">
                    <p>&copy; 2026 Virtual Human. All rights reserved.</p>
                    <p>Design by <a rel="nofollow noopener" href="https://templatemo.com" target="_blank">TemplateMo</a> <a rel="nofollow noopener"
    href="https://www.tooplate.com"
    target="_blank">Tooplate</a></p>
                </div>
            </div>
        </footer>
        <div class="sfx" id="sfx">
            <button class="sbtn"
                    id="sbtn"
                    aria-pressed="true"
                    aria-label="Sound on"
                    title="Sound on">
                <svg viewBox="0 0 24 24" aria-hidden="true">
                    <path class="cone" d="M3.5 9.4v5.2h3.4l4.6 3.8V5.6L6.9 9.4H3.5z" />
                    <path class="w1" d="M14.6 9.3a3.7 3.7 0 0 1 0 5.4" />
                    <path class="w2" d="M17.3 6.6a7.4 7.4 0 0 1 0 10.8" />
                    <path class="slash" d="M4.5 19.5L19.5 4.5" />
                </svg>
            </button>
            <span class="scue" id="scue">Click once to wake the sound</span>
        </div>
        <button class="up" id="up" aria-label="Back to top">
            <svg viewBox="0 0 24 24">
                <path d="M12 19V6M6 12l6-6 6 6" />
            </svg>
        </button>
        <script src="templatemo-633-celadon-script.js"></script>
    </body>
</html>
"""

with open(os.path.join(DIR, "discover.html"), "w", encoding="utf-8") as f:
    f.write(discover_html)
print("Updated discover.html successfully")
