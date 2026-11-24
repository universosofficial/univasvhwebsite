# -*- coding: utf-8 -*-
"""
Implement the exact 3D Gallery Hero design from the user's uploaded reference (Halo Lab / Anam)
into Virtual Human's index.html and templatemo-633-celadon-style.css
"""

# 1. Append the 3D Gallery Hero CSS to templatemo-633-celadon-style.css
css_rules = """
/* ==========================================================================
   ANAM / HALO-LAB 3D GALLERY HERO (EXACT REFERENCE REPLICATION)
   ========================================================================== */
.gallery-hero-wrap {
    padding: 16px 20px 48px;
    max-width: 1320px;
    margin: 0 auto;
    position: relative;
}

.gallery-room {
    background: radial-gradient(circle at 50% 30%, #E3DBD2 0%, #D0C6BB 55%, #BFAF9F 100%);
    border-radius: 44px;
    box-shadow: 0 48px 90px -24px rgba(35, 45, 60, 0.32), inset 0 2px 5px rgba(255, 255, 255, 0.8), inset 0 -6px 16px rgba(0, 0, 0, 0.08);
    padding: 36px 48px 36px;
    position: relative;
    overflow: hidden;
    color: #2E2924;
    perspective: 1200px;
}

/* Perspective room lighting & architectural backplate */
.room-backplate {
    position: absolute;
    top: 14%;
    left: 50%;
    transform: translateX(-50%);
    width: 68%;
    height: 62%;
    border: 1px solid rgba(255, 255, 255, 0.35);
    border-radius: 28px;
    box-shadow: inset 0 0 80px rgba(255, 255, 255, 0.22), 0 20px 40px rgba(0, 0, 0, 0.06);
    background: linear-gradient(180deg, rgba(255, 255, 255, 0.14) 0%, rgba(255, 255, 255, 0.04) 100%);
    pointer-events: none;
    z-index: 1;
}

/* Top bar inside the room */
.room-topbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    position: relative;
    z-index: 10;
    margin-bottom: 24px;
}
.room-brand {
    font-size: 1.65rem;
    font-weight: 600;
    font-family: 'Albert Sans', 'Outfit', sans-serif;
    letter-spacing: -0.03em;
    color: #2A241F;
    text-decoration: none;
    display: flex;
    align-items: center;
    gap: 8px;
}
.room-nav {
    display: flex;
    align-items: center;
    gap: 28px;
}
.room-nav a {
    font-size: 0.92rem;
    font-weight: 500;
    color: rgba(42, 36, 31, 0.72);
    text-decoration: none;
    transition: color 0.2s ease;
}
.room-nav a:hover, .room-nav a.active {
    color: #1A1613;
}
.room-cta {
    background: #FFFFFF;
    color: #2A241F !important;
    padding: 10px 24px;
    border-radius: 99px;
    font-size: 0.88rem;
    font-weight: 600;
    text-decoration: none;
    box-shadow: 0 8px 18px rgba(0, 0, 0, 0.08), inset 0 1px 2px rgba(255, 255, 255, 0.95);
    transition: transform 0.2s ease, box-shadow 0.2s ease;
}
.room-cta:hover {
    transform: translateY(-2px);
    box-shadow: 0 12px 24px rgba(0, 0, 0, 0.12);
}

/* Main gallery stage holding the 3D personas */
.gallery-stage {
    position: relative;
    min-height: 560px;
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 2;
    padding: 10px 0 20px;
}

/* Top-left tagline */
.room-tagline {
    position: absolute;
    top: 24px;
    left: 48px;
    max-width: 260px;
    font-size: 0.96rem;
    line-height: 1.45;
    color: rgba(42, 36, 31, 0.78);
    font-weight: 400;
    z-index: 5;
}

/* Top-right floating preview bubble */
.room-badge-bubble {
    position: absolute;
    top: 24px;
    right: 56px;
    width: 68px;
    height: 68px;
    border-radius: 50%;
    background: rgba(255, 255, 255, 0.35);
    backdrop-filter: blur(12px);
    border: 1px solid rgba(255, 255, 255, 0.6);
    box-shadow: 0 14px 28px rgba(0, 0, 0, 0.08);
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: 5;
    cursor: pointer;
    transition: transform 0.24s ease;
}
.room-badge-bubble:hover {
    transform: scale(1.08);
}
.bubble-inner {
    width: 52px;
    height: 52px;
    border-radius: 50%;
    overflow: hidden;
    position: relative;
}
.bubble-inner img {
    width: 100%;
    height: 100%;
    object-fit: cover;
}
.bubble-play {
    position: absolute;
    bottom: -2px;
    right: -2px;
    width: 22px;
    height: 22px;
    border-radius: 50%;
    background: #FFFFFF;
    display: flex;
    align-items: center;
    justify-content: center;
    box-shadow: 0 4px 8px rgba(0,0,0,0.15);
}
.bubble-play svg {
    width: 10px;
    height: 10px;
    fill: #2A241F;
    margin-left: 1px;
}

/* 3D Side Cards */
.side-card {
    position: absolute;
    width: 210px;
    height: 310px;
    border-radius: 20px;
    overflow: hidden;
    box-shadow: 0 24px 44px rgba(0, 0, 0, 0.2);
    border: 1px solid rgba(255, 255, 255, 0.35);
    background: #D1C7BD;
    transition: all 0.45s cubic-bezier(0.2, 0.8, 0.2, 1);
    cursor: pointer;
    z-index: 3;
}
.side-card img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    filter: brightness(0.92) contrast(0.96);
    transition: filter 0.3s ease;
}
.side-card:hover img {
    filter: brightness(1) contrast(1);
}
.side-card.left {
    left: 7%;
    transform: rotateY(26deg) scale(0.88);
    opacity: 0.72;
}
.side-card.left:hover {
    transform: rotateY(20deg) scale(0.94);
    opacity: 0.95;
}
.side-card.right {
    right: 7%;
    transform: rotateY(-26deg) scale(0.88);
    opacity: 0.72;
}
.side-card.right:hover {
    transform: rotateY(-20deg) scale(0.94);
    opacity: 0.95;
}

/* Center Stage with Persona */
.center-persona-wrap {
    position: relative;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: flex-end;
    z-index: 4;
    width: 480px;
    height: 520px;
}

/* Backplate Switcher Arrows */
.persona-switcher {
    position: absolute;
    top: 42%;
    left: -70px;
    right: -70px;
    display: flex;
    justify-content: space-between;
    pointer-events: none;
    z-index: 6;
}
.switcher-btn {
    pointer-events: auto;
    width: 44px;
    height: 44px;
    border-radius: 50%;
    border: 1px solid rgba(255, 255, 255, 0.55);
    background: rgba(255, 255, 255, 0.28);
    backdrop-filter: blur(10px);
    display: flex;
    align-items: center;
    justify-content: center;
    color: #2A241F;
    cursor: pointer;
    box-shadow: 0 10px 20px rgba(0, 0, 0, 0.08);
    transition: all 0.22s ease;
}
.switcher-btn:hover {
    background: #FFFFFF;
    transform: scale(1.1);
    box-shadow: 0 14px 28px rgba(0, 0, 0, 0.14);
}
.switcher-btn svg {
    width: 16px;
    height: 16px;
    stroke: currentColor;
    stroke-width: 2.2;
    fill: none;
}

/* Central Portrait Image */
.center-portrait {
    position: relative;
    width: 380px;
    height: 440px;
    display: flex;
    align-items: flex-end;
    justify-content: center;
}
.center-portrait img {
    max-width: 100%;
    max-height: 100%;
    object-fit: cover;
    border-radius: 28px 28px 0 0;
    filter: drop-shadow(0 20px 30px rgba(0, 0, 0, 0.18));
    transition: opacity 0.35s ease, transform 0.35s ease;
}

/* Iconic Big "Meet Mia / Meet Maya" Title */
.meet-title {
    position: absolute;
    bottom: 58px;
    left: 50%;
    transform: translateX(-50%);
    font-size: 5.6rem;
    font-weight: 400;
    font-family: 'Albert Sans', 'Outfit', sans-serif;
    letter-spacing: -0.04em;
    color: rgba(255, 255, 255, 0.94);
    text-shadow: 0 8px 32px rgba(0, 0, 0, 0.18);
    margin: 0;
    line-height: 0.9;
    white-space: nowrap;
    pointer-events: none;
    z-index: 5;
    transition: opacity 0.25s ease, transform 0.25s ease;
}

/* Chat with Persona CTA button */
.chat-persona-btn {
    position: relative;
    z-index: 7;
    margin-top: 14px;
    background: #1C1814;
    color: #FFFFFF !important;
    padding: 14px 38px;
    border-radius: 99px;
    font-size: 0.98rem;
    font-weight: 500;
    text-decoration: none;
    box-shadow: 0 16px 36px rgba(28, 24, 20, 0.35), inset 0 1px 2px rgba(255, 255, 255, 0.2);
    display: inline-flex;
    align-items: center;
    gap: 10px;
    transition: all 0.25s ease;
}
.chat-persona-btn:hover {
    transform: translateY(-3px) scale(1.02);
    box-shadow: 0 22px 48px rgba(28, 24, 20, 0.45);
    background: #0E0C0A;
}

/* Lower Dock Strip */
.room-dock {
    margin-top: 36px;
    padding-top: 26px;
    border-top: 1px solid rgba(255, 255, 255, 0.3);
    display: grid;
    grid-template-columns: 1fr 1.3fr 1fr;
    gap: 28px;
    align-items: center;
    position: relative;
    z-index: 10;
}

/* Left upload teaser widget */
.dock-widget-left {
    background: rgba(255, 255, 255, 0.32);
    backdrop-filter: blur(10px);
    border: 1px dashed rgba(42, 36, 31, 0.25);
    border-radius: 20px;
    padding: 16px 20px;
    display: flex;
    align-items: center;
    gap: 16px;
    transition: all 0.2s ease;
}
.dock-widget-left:hover {
    background: rgba(255, 255, 255, 0.45);
}
.dock-icon-circle {
    width: 42px;
    height: 42px;
    border-radius: 50%;
    background: rgba(255, 255, 255, 0.65);
    display: flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
}
.dock-icon-circle svg {
    width: 20px;
    height: 20px;
    stroke: #2A241F;
    fill: none;
    stroke-width: 1.8;
}
.dock-widget-info {
    font-size: 0.84rem;
    line-height: 1.35;
    color: #2A241F;
}
.dock-widget-info b {
    display: block;
    font-weight: 600;
    margin-bottom: 2px;
}
.dock-widget-acts {
    display: flex;
    gap: 8px;
    margin-top: 6px;
}
.dock-widget-acts button {
    background: #FFFFFF;
    border: 1px solid rgba(0, 0, 0, 0.1);
    border-radius: 99px;
    padding: 4px 10px;
    font-size: 0.74rem;
    font-weight: 500;
    color: #2A241F;
    cursor: pointer;
    box-shadow: 0 2px 4px rgba(0,0,0,0.05);
}

/* Center statement */
.dock-center-text {
    text-align: center;
    font-size: 1.05rem;
    line-height: 1.5;
    font-weight: 500;
    color: #2A241F;
    font-family: 'Albert Sans', 'Outfit', sans-serif;
    padding: 0 12px;
}

/* Right trust badge */
.dock-widget-right {
    text-align: right;
    display: flex;
    flex-direction: column;
    align-items: flex-end;
    gap: 6px;
}
.dock-widget-right span {
    font-size: 0.78rem;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    color: rgba(42, 36, 31, 0.6);
    font-weight: 600;
}
.dock-trust-tag {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    font-size: 0.95rem;
    font-weight: 600;
    color: #2A241F;
}

/* Responsive adjustments */
@media (max-width: 1040px) {
    .gallery-room { padding: 28px 24px 28px; }
    .side-card { display: none; }
    .meet-title { font-size: 4.2rem; bottom: 50px; }
    .room-dock { grid-template-columns: 1fr; gap: 18px; text-align: center; }
    .dock-widget-right { align-items: center; text-align: center; }
    .room-tagline { position: static; max-width: 100%; margin: 12px 0 20px; text-align: center; }
}
@media (max-width: 640px) {
    .gallery-stage { min-height: 440px; }
    .center-persona-wrap { width: 100%; height: 420px; }
    .center-portrait { width: 280px; height: 340px; }
    .meet-title { font-size: 3.2rem; bottom: 44px; }
    .room-nav { display: none; }
}
"""

css_path = r"C:\Users\user\Downloads\websites\templatemo_633_celadon\templatemo-633-celadon-style.css"
with open(css_path, "r", encoding="utf-8") as f:
    css_content = f.read()

if ".gallery-room" not in css_content:
    css_content += "\n" + css_rules
    with open(css_path, "w", encoding="utf-8") as f:
        f.write(css_content)
    print("Added 3D Gallery Hero CSS to templatemo-633-celadon-style.css")
else:
    print("CSS already contains .gallery-room")

# 2. Update index.html with the new 3D Gallery Hero
html_path = r"C:\Users\user\Downloads\websites\templatemo_633_celadon\index.html"
with open(html_path, "r", encoding="utf-8") as f:
    html = f.read()

new_hero_html = '''            <!-- HERO: EXACT ANAM / HALO-LAB 3D GALLERY REPLICATION -->
            <section class="gallery-hero-wrap">
                <div class="gallery-room">
                    <!-- Perspective Room Backplate with Subtle Illumination -->
                    <div class="room-backplate" aria-hidden="true"></div>

                    <!-- Top Bar Inside Gallery Room -->
                    <div class="room-topbar">
                        <a class="room-brand" href="index.html">
                            <span class="mark" style="width:24px; height:24px; border-radius:8px; background:linear-gradient(135deg, #1C1814, #423A33); display:inline-block;"></span>
                            Virtual Human
                        </a>
                        <nav class="room-nav">
                            <a href="companion.html">AI Companion</a>
                            <a href="discover.html">Discover</a>
                            <a href="how-it-works.html">How It Works</a>
                            <a href="experts.html">For Experts</a>
                            <a href="pricing.html">Pricing</a>
                            <a href="faq.html">FAQ</a>
                        </nav>
                        <a class="room-cta" href="companion.html">Get Started</a>
                    </div>

                    <!-- Room Tagline (Top Left) -->
                    <div class="room-tagline">
                        Create lifelike, customizable AI companions—anchored in warmth, episodic memory, and human wisdom.
                    </div>

                    <!-- Live Voice / Video Preview Badge (Top Right) -->
                    <a class="room-badge-bubble" href="companion.html#simulator" title="Listen to AI Companion live voice sample">
                        <div class="bubble-inner">
                            <img id="bubble-avatar-img" src="https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&w=150&q=80" alt="Companion audio preview">
                            <div class="bubble-play">
                                <svg viewBox="0 0 24 24"><polygon points="5 3 19 12 5 21 5 3"></polygon></svg>
                            </div>
                        </div>
                    </a>

                    <!-- Main 3D Gallery Stage -->
                    <div class="gallery-stage">
                        <!-- Left Angled 3D Perspective Card (David - Father Figure) -->
                        <div class="side-card left" id="side-card-left" title="Click to view David (Father Figure)">
                            <img id="left-card-img" src="https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?auto=format&fit=crop&w=400&q=80" alt="David - Father Figure">
                        </div>

                        <!-- Center Persona Focus -->
                        <div class="center-persona-wrap">
                            <!-- Switcher Arrows (< and >) -->
                            <div class="persona-switcher">
                                <button class="switcher-btn" id="btn-persona-prev" aria-label="Previous Persona">
                                    <svg viewBox="0 0 24 24"><polyline points="15 18 9 12 15 6"></polyline></svg>
                                </button>
                                <button class="switcher-btn" id="btn-persona-next" aria-label="Next Persona">
                                    <svg viewBox="0 0 24 24"><polyline points="9 18 15 12 9 6"></polyline></svg>
                                </button>
                            </div>

                            <!-- Central Portrait Image -->
                            <div class="center-portrait">
                                <img id="center-persona-img" src="https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&w=800&q=85" alt="Mia / Maya - Devoted Partner">
                            </div>

                            <!-- Massive Overlapping Headline "Meet Mia" -->
                            <h1 class="meet-title" id="meet-persona-title">Meet Mia</h1>

                            <!-- Central "Chat with Persona" Button -->
                            <a class="chat-persona-btn" id="chat-persona-link" href="companion.html">
                                <span id="chat-persona-text">Chat with Persona</span>
                                <svg viewBox="0 0 24 24" style="width:16px; height:16px; stroke:currentColor; stroke-width:2.2; fill:none;"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
                            </a>
                        </div>

                        <!-- Right Angled 3D Perspective Card (Elena - Founder Mentor) -->
                        <div class="side-card right" id="side-card-right" title="Click to view Elena (Founder Mentor)">
                            <img id="right-card-img" src="https://images.unsplash.com/photo-1580489944761-15a19d654956?auto=format&fit=crop&w=400&q=80" alt="Elena - SaaS Founder">
                        </div>
                    </div>

                    <!-- Bottom Widget Strip / Room Dock -->
                    <div class="room-dock">
                        <!-- Left: Upload photo / Camera teaser -->
                        <div class="dock-widget-left">
                            <div class="dock-icon-circle">
                                <svg viewBox="0 0 24 24"><path d="M23 19a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h4l2-3h6l2 3h4a2 2 0 0 1 2 2z"></path><circle cx="12" cy="13" r="4"></circle></svg>
                            </div>
                            <div class="dock-widget-info">
                                <b>Upload a photo or backstory</b>
                                <span>Create from image or memory</span>
                                <div class="dock-widget-acts">
                                    <button type="button" onclick="location.href='companion.html#create-character'">Browse Files</button>
                                    <button type="button" onclick="location.href='companion.html#create-character'">Use Studio</button>
                                </div>
                            </div>
                        </div>

                        <!-- Center: Clear value statement -->
                        <div class="dock-center-text">
                            Create an AI persona for any relationship or choose from our curated library of personal &amp; expert minds.
                        </div>

                        <!-- Right: Trust Signals -->
                        <div class="dock-widget-right">
                            <span>Platform Security</span>
                            <div class="dock-trust-tag">
                                <svg viewBox="0 0 24 24" style="width:18px; height:18px; stroke:var(--jade-ink, #1F6B56); fill:none; stroke-width:2;"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path></svg>
                                100% Private &middot; Episodic Memory
                            </div>
                        </div>
                    </div>
                </div>
            </section>'''

# Replace the existing <section class="hero">...</section> in index.html
import re
hero_pattern = r'<!-- hero -->\s*<section class="hero">.*?</section>'
if re.search(hero_pattern, html, flags=re.DOTALL):
    html = re.sub(hero_pattern, new_hero_html, html, flags=re.DOTALL)
    print("Replaced existing hero with exact Anam/Halo-Lab 3D Gallery Hero!")
else:
    # Try alternate match
    hero_pattern_2 = r'<section class="hero">.*?</section>'
    if re.search(hero_pattern_2, html, flags=re.DOTALL):
        html = re.sub(hero_pattern_2, new_hero_html, html, flags=re.DOTALL)
        print("Replaced hero using fallback pattern!")
    else:
        print("ERROR: Could not find hero section in index.html!")

# 3. Add the Carousel Switching Script before </body>
script_carousel = '''        <script>
        // Interactive Persona Carousel for Anam / Halo-Lab 3D Gallery Hero
        (function() {
            const personas = [
                {
                    name: "Mia",
                    role: "Devoted Partner",
                    image: "https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&w=800&q=85",
                    bubble: "https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&w=150&q=80",
                    btnText: "Chat with Mia"
                },
                {
                    name: "David",
                    role: "Grounded Father Figure",
                    image: "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?auto=format&fit=crop&w=800&q=85",
                    bubble: "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?auto=format&fit=crop&w=150&q=80",
                    btnText: "Chat with David"
                },
                {
                    name: "Clara",
                    role: "Nurturing Mother",
                    image: "https://images.unsplash.com/photo-1544005313-94ddf0286df2?auto=format&fit=crop&w=800&q=85",
                    bubble: "https://images.unsplash.com/photo-1544005313-94ddf0286df2?auto=format&fit=crop&w=150&q=80",
                    btnText: "Chat with Clara"
                },
                {
                    name: "Julian",
                    role: "Lifelong Confidant",
                    image: "https://images.unsplash.com/photo-1500648767791-00dcc994a43e?auto=format&fit=crop&w=800&q=85",
                    bubble: "https://images.unsplash.com/photo-1500648767791-00dcc994a43e?auto=format&fit=crop&w=150&q=80",
                    btnText: "Chat with Julian"
                },
                {
                    name: "Elena",
                    role: "SaaS Founder ($12M ARR)",
                    image: "https://images.unsplash.com/photo-1580489944761-15a19d654956?auto=format&fit=crop&w=800&q=85",
                    bubble: "https://images.unsplash.com/photo-1580489944761-15a19d654956?auto=format&fit=crop&w=150&q=80",
                    btnText: "Chat with Elena"
                }
            ];

            let currentIndex = 0;
            const titleEl = document.getElementById("meet-persona-title");
            const imgEl = document.getElementById("center-persona-img");
            const btnTextEl = document.getElementById("chat-persona-text");
            const bubbleEl = document.getElementById("bubble-avatar-img");
            const leftImgEl = document.getElementById("left-card-img");
            const rightImgEl = document.getElementById("right-card-img");
            const prevBtn = document.getElementById("btn-persona-prev");
            const nextBtn = document.getElementById("btn-persona-next");

            function updatePersona(index) {
                if (!titleEl || !imgEl) return;
                currentIndex = (index + personas.length) % personas.length;
                const p = personas[currentIndex];

                imgEl.style.opacity = "0";
                titleEl.style.opacity = "0";
                titleEl.style.transform = "translateX(-50%) translateY(10px)";

                setTimeout(() => {
                    imgEl.src = p.image;
                    titleEl.innerText = "Meet " + p.name;
                    btnTextEl.innerText = p.btnText;
                    if (bubbleEl) bubbleEl.src = p.bubble;

                    // Update side cards to reflect adjacent personas
                    const leftIndex = (currentIndex - 1 + personas.length) % personas.length;
                    const rightIndex = (currentIndex + 1) % personas.length;
                    if (leftImgEl) leftImgEl.src = personas[leftIndex].image;
                    if (rightImgEl) rightImgEl.src = personas[rightIndex].image;

                    imgEl.style.opacity = "1";
                    titleEl.style.opacity = "1";
                    titleEl.style.transform = "translateX(-50%) translateY(0)";
                }, 200);
            }

            if (prevBtn) prevBtn.addEventListener("click", () => updatePersona(currentIndex - 1));
            if (nextBtn) nextBtn.addEventListener("click", () => updatePersona(currentIndex + 1));

            // Also click side cards to switch
            const sideLeft = document.getElementById("side-card-left");
            const sideRight = document.getElementById("side-card-right");
            if (sideLeft) sideLeft.addEventListener("click", () => updatePersona(currentIndex - 1));
            if (sideRight) sideRight.addEventListener("click", () => updatePersona(currentIndex + 1));
        })();
        </script>
'''

if "Interactive Persona Carousel" not in html:
    html = html.replace("</body>", script_carousel + "\n</body>")
    print("Added interactive carousel script to index.html")

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html)

print("Updated index.html successfully with the exact Anam/Halo-Lab 3D Gallery Hero!")
