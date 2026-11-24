# -*- coding: utf-8 -*-
"""
VIRTUAL HUMAN — COMPLETE COLOUR HARMONY & BRAND PALETTE IMPLEMENTATION
Brand Palette:
- Warm Ivory: #F5F2EA
- Soft Sage: #E5ECE4
- Muted Sage: #D8E2D8
- Deep Forest Green: #263B35
- Muted Clay: #D6A58D
- Soft Charcoal: #303631
- Warm Sand: #E8E1D6
- White: #FFFFFF
"""

import os, re

BASE_DIR = r"C:\Users\user\Downloads\websites\templatemo_633_celadon"
CSS_PATH = os.path.join(BASE_DIR, "templatemo-633-celadon-style.css")

# 1. Update templatemo-633-celadon-style.css :root tokens and core rules
with open(CSS_PATH, "r", encoding="utf-8") as f:
    css = f.read()

# Replace :root tokens block
old_tokens_pattern = r'/\* ---------- tokens ---------- \*/\s*:root \{.*?\n\}'
new_tokens = '''/* ---------- tokens ---------- */
:root {
    /* Virtual Human Exact Brand Foundation */
    --ivory: #F5F2EA;
    --sage-soft: #E5ECE4;
    --sage-muted: #D8E2D8;
    --forest: #263B35;
    --forest-hover: #1B2A26;
    --clay: #D6A58D;
    --charcoal: #303631;
    --sand: #E8E1D6;
    --white: #FFFFFF;

    /* Semantic Mappings */
    --canvas: #F5F2EA;             /* Warm Ivory page background */
    --plate: #FFFFFF;              /* Crisp White card base */
    --plate-2: #E5ECE4;            /* Soft Sage surface */
    --sunk: #D8E2D8;               /* Muted Sage for insets */
    --ink: #263B35;                /* Deep Forest Green for headings */
    --ink-2: #303631;              /* Soft Charcoal for body text */
    --jade: #D8E2D8;               /* Muted Sage (replacing bright cyan/mint) */
    --jade-ink: #263B35;           /* Deep Forest Green */
    --coral: #D6A58D;              /* Muted Clay (replacing bright coral) */
    --coral-ink: #8F553D;          /* Deep Muted Clay */
    --sky: #E5ECE4;                /* Soft Sage (replacing baby blue) */
    --sky-ink: #263B35;            /* Deep Forest Green */
    --line: rgba(38, 59, 53, 0.12);/* Subtle sage-grey border */
    --bar: 92px;
    --r: 28px;
    --r-sm: 18px;
    --shell: 1180px;
    --ease: cubic-bezier(.19, .86, .22, 1);

    /* Warm Organic Clay Shadows (No blue/black harsh shadows) */
    --clay: 0 20px 38px -18px rgba(38, 59, 53, .16), 0 8px 16px -10px rgba(38, 59, 53, .08), inset 2px 3px 4px 0 rgba(255, 255, 255, .95), inset -3px -5px 9px 0 rgba(38, 59, 53, .04);
    --clay-sm: 0 10px 20px -12px rgba(38, 59, 53, .14), inset 2px 2px 3px 0 rgba(255, 255, 255, .95), inset -2px -3px 6px 0 rgba(38, 59, 53, .04);
    --well: inset 3px 4px 10px -2px rgba(38, 59, 53, .12), inset -2px -3px 6px 0 rgba(255, 255, 255, .9);
    
    /* Harmonious Gradients */
    --gloss: linear-gradient(180deg, #FFFFFF 0%, #FAF8F4 46%, #F5F2EA 46.01%, #EAE5D9 100%);
    --gloss-plate: linear-gradient(180deg, #FFFFFF 0%, #FAF9F5 46%, #F5F2EA 46.01%, #EBE6DA 100%);
    --gloss-down: linear-gradient(180deg, #EAE5D9 0%, #F5F2EA 54%, #FAF8F4 54.01%, #FFFFFF 100%);
    --gloss-jade: linear-gradient(180deg, #324D45 0%, #2B423C 46%, #263B35 46.01%, #1F302B 100%);
    --gloss-jade-down: linear-gradient(180deg, #1F302B 0%, #263B35 54%, #2B423C 54.01%, #324D45 100%);
    --lip: inset 0 1px 0 0 rgba(255, 255, 255, 1), inset 0 -1px 0 0 rgba(38, 59, 53, .08);
    --lip-jade: inset 0 1px 0 0 rgba(255, 255, 255, .3), inset 0 -1px 0 0 rgba(16, 30, 26, .5);
    --lift: 0 8px 18px -10px rgba(38, 59, 53, .25), 0 2px 4px -2px rgba(38, 59, 53, .08);
    --lift-hi: 0 16px 28px -12px rgba(38, 59, 53, .3), 0 4px 8px -3px rgba(38, 59, 53, .12);
    --lift-jade: 0 10px 22px -8px rgba(38, 59, 53, .45), 0 2px 4px -2px rgba(38, 59, 53, .18);
    --lift-jade-hi: 0 18px 30px -10px rgba(38, 59, 53, .55), 0 4px 8px -3px rgba(38, 59, 53, .22);
    --sheen: linear-gradient(100deg, rgba(255, 255, 255, 0) 36%, rgba(255, 255, 255, .75) 48%, rgba(255, 255, 255, 0) 61%);
    --sheen-soft: linear-gradient(100deg, rgba(255, 255, 255, 0) 36%, rgba(255, 255, 255, .35) 48%, rgba(255, 255, 255, 0) 61%);
    --sink: 0 1px 2px -1px rgba(38, 59, 53, .2), inset 0 2px 5px 0 rgba(38, 59, 53, .12);
}'''

css = re.sub(old_tokens_pattern, new_tokens, css, flags=re.DOTALL)

# Update Master Overrides in CSS to guarantee brand harmony across all components
brand_harmony_css = """
/* ==========================================================================
   VIRTUAL HUMAN MASTER BRAND HARMONY OVERRIDES
   Exact Brand Palette: Warm Ivory, Soft Sage, Muted Sage, Deep Forest Green,
   Muted Clay, Soft Charcoal, Warm Sand, White.
   ========================================================================== */

/* 1. Body & Universal Surfaces */
body {
    background: #F5F2EA !important;
    color: #303631 !important;
}

h1, h2, h3, h4, .h2 {
    color: #263B35 !important;
}

p, .sub, .lede, .desc, blockquote {
    color: #303631 !important;
}

.sub, .lede, .desc, .hint, .note {
    color: #4A544C !important;
}

/* 2. Top Navigation Bar */
.bar {
    background: rgba(245, 242, 234, 0.92) !important;
    border: 1px solid rgba(216, 226, 216, 0.8) !important;
    box-shadow: 0 16px 32px -12px rgba(38, 59, 53, 0.12), inset 0 1px 0 rgba(255, 255, 255, 0.95) !important;
    -webkit-backdrop-filter: blur(14px) !important;
    backdrop-filter: blur(14px) !important;
}
.brand {
    color: #263B35 !important;
}
.mark {
    background: linear-gradient(155deg, #324D45, #263B35 55%, #1B2A26) !important;
    box-shadow: 0 8px 14px -8px rgba(38, 59, 53, .5), inset 1px 2px 3px rgba(255, 255, 255, .4) !important;
}
.mark::after {
    background: rgba(245, 242, 234, 0.6) !important;
}
.nav a {
    color: #303631 !important;
}
.nav a:hover, .nav a.active {
    color: #263B35 !important;
    background: rgba(229, 236, 228, 0.8) !important;
    box-shadow: inset 1px 1px 2px rgba(38, 59, 53, 0.08) !important;
}

/* 3. Primary & Secondary Buttons */
.btn.solid, .chat-persona-btn {
    background: linear-gradient(155deg, #324D45 0%, #263B35 100%) !important;
    color: #FFFFFF !important;
    box-shadow: 0 12px 24px -8px rgba(38, 59, 53, 0.42), var(--lip-jade) !important;
    border: none !important;
}
.btn.solid:hover, .chat-persona-btn:hover {
    background: #1B2A26 !important;
    color: #FFFFFF !important;
    transform: translateY(-2px) !important;
    box-shadow: 0 16px 30px -8px rgba(38, 59, 53, 0.52), var(--lip-jade) !important;
}
.btn {
    background: rgba(245, 242, 234, 0.95) !important;
    color: #263B35 !important;
    border: 1px solid rgba(38, 59, 53, 0.18) !important;
    box-shadow: 0 6px 14px -6px rgba(38, 59, 53, 0.12), var(--lip) !important;
}
.btn:hover {
    background: #D8E2D8 !important;
    color: #1B2A26 !important;
    transform: translateY(-2px) !important;
}

/* 4. 3D Gallery Hero (Refined Warm Sand & Ivory, No Muddy Beige) */
.gallery-room {
    background: radial-gradient(circle at 50% 25%, #F5F2EA 0%, #E8E1D6 60%, #DDD5C8 100%) !important;
    border: 1px solid rgba(216, 226, 216, 0.8) !important;
    box-shadow: 0 44px 84px -24px rgba(38, 59, 53, 0.18), inset 0 2px 4px rgba(255, 255, 255, 0.95), inset 0 -4px 12px rgba(38, 59, 53, 0.04) !important;
    color: #303631 !important;
}
.room-backplate {
    border: 1px solid rgba(216, 226, 216, 0.6) !important;
    background: linear-gradient(180deg, rgba(255, 255, 255, 0.55) 0%, rgba(229, 236, 228, 0.25) 100%) !important;
    box-shadow: inset 0 0 60px rgba(255, 255, 255, 0.55), 0 20px 40px rgba(38, 59, 53, 0.04) !important;
}
.room-tagline {
    color: #4A544C !important;
}
.room-badge-bubble {
    background: rgba(245, 242, 234, 0.88) !important;
    border: 1px solid rgba(216, 226, 216, 0.8) !important;
    box-shadow: 0 12px 24px rgba(38, 59, 53, 0.08) !important;
}
.bubble-play {
    background: #263B35 !important;
}
.bubble-play svg {
    fill: #FFFFFF !important;
}
.switcher-btn {
    border: 1px solid rgba(216, 226, 216, 0.8) !important;
    background: rgba(245, 242, 234, 0.92) !important;
    color: #263B35 !important;
    box-shadow: 0 8px 18px rgba(38, 59, 53, 0.08) !important;
}
.switcher-btn:hover {
    background: #FFFFFF !important;
    color: #1B2A26 !important;
}
.side-card {
    border: 1px solid rgba(216, 226, 216, 0.6) !important;
    background: #E8E1D6 !important;
    box-shadow: 0 20px 36px rgba(38, 59, 53, 0.12) !important;
}
.meet-title {
    color: #FFFFFF !important;
    text-shadow: 0 8px 32px rgba(38, 59, 53, 0.3) !important;
}
.room-dock {
    border-top: 1px solid rgba(216, 226, 216, 0.6) !important;
}
.dock-widget-left {
    background: rgba(255, 255, 255, 0.75) !important;
    border: 1px dashed rgba(38, 59, 53, 0.22) !important;
}
.dock-icon-circle {
    background: #E5ECE4 !important;
}
.dock-icon-circle svg {
    stroke: #263B35 !important;
}
.dock-widget-acts button {
    background: #FFFFFF !important;
    border: 1px solid #D8E2D8 !important;
    color: #263B35 !important;
}
.dock-widget-acts button:hover {
    background: #E5ECE4 !important;
}
.dock-center-text {
    color: #303631 !important;
}
.dock-widget-right span {
    color: #5E6960 !important;
}
.dock-trust-tag {
    color: #263B35 !important;
}

/* 5. Cards & Section Surfaces */
.plan, .identity-card {
    background: #FFFFFF !important;
    border: 1px solid rgba(38, 59, 53, 0.1) !important;
    box-shadow: 0 22px 38px -20px rgba(38, 59, 53, 0.12), inset 2px 3px 4px rgba(255, 255, 255, 0.95) !important;
}
.plan.hot {
    background: linear-gradient(165deg, #FFFFFF 0%, #FAF8F4 50%, #F5F2EA 100%) !important;
    border-top: 4px solid #263B35 !important;
}
.statplate {
    background: #FFFFFF !important;
    border: 1px solid rgba(38, 59, 53, 0.1) !important;
    box-shadow: 0 20px 40px -20px rgba(38, 59, 53, 0.1), inset 0 1px 2px rgba(255, 255, 255, 0.95) !important;
}
.matrix-wrapper {
    background: linear-gradient(158deg, #FFFFFF, #F5F2EA 46%, #E5ECE4) !important;
    border-radius: 40px !important;
    border: 1px solid rgba(216, 226, 216, 0.8) !important;
    box-shadow: 0 36px 54px -24px rgba(38, 59, 53, 0.14), inset 3px 4px 6px rgba(255, 255, 255, .98) !important;
}
.matrix-table th {
    color: #263B35 !important;
    border-bottom: 2px solid rgba(38, 59, 53, 0.18) !important;
}
.matrix-table td {
    color: #303631 !important;
    border-bottom: 1px solid rgba(38, 59, 53, 0.08) !important;
}
.matrix-table tr:hover td {
    background: rgba(255, 255, 255, 0.6) !important;
}
.check-pill {
    background: rgba(38, 59, 53, 0.12) !important;
    color: #263B35 !important;
}
.cross-pill {
    background: rgba(48, 54, 49, 0.06) !important;
    color: #5E6960 !important;
}

/* 6. Email Feature Card */
.email-card {
    background: linear-gradient(160deg, #FFFFFF, #F5F2EA 50%, #E5ECE4) !important;
    border: 1px solid rgba(216, 226, 216, 0.8) !important;
    box-shadow: 0 24px 44px -20px rgba(38, 59, 53, 0.14), inset 2px 3px 4px rgba(255, 255, 255, 0.95) !important;
}
.email-header {
    border-bottom: 1px solid rgba(38, 59, 53, 0.12) !important;
}
.email-field b {
    color: #4A544C !important;
}
.email-field span {
    color: #303631 !important;
}
.email-body {
    color: #303631 !important;
}

/* 7. Simulation Box in companion.html */
.sim-box {
    background: #FFFFFF !important;
    border: 1px solid rgba(216, 226, 216, 0.85) !important;
    box-shadow: 0 32px 56px -24px rgba(38, 59, 53, 0.14), inset 2px 3px 4px rgba(255, 255, 255, 0.95) !important;
}
.sim-header {
    border-bottom: 1px solid rgba(38, 59, 53, 0.1) !important;
}
.sim-meta b {
    color: #263B35 !important;
}
.sim-meta span {
    color: #5E6960 !important;
}
.pulse-dot {
    background: #263B35 !important;
}
.chat-bubble.user {
    background: #E5ECE4 !important;
    color: #303631 !important;
    border: 1px solid rgba(38, 59, 53, 0.08) !important;
}
.chat-bubble.companion {
    background: #F5F2EA !important;
    color: #303631 !important;
    border: 1px solid rgba(38, 59, 53, 0.1) !important;
}
.chat-bubble .author {
    color: #263B35 !important;
    font-weight: 600 !important;
}
.chat-memory-badge {
    background: #E5ECE4 !important;
    color: #263B35 !important;
    border: 1px solid rgba(38, 59, 53, 0.12) !important;
}
.sim-mode-btn {
    background: rgba(245, 242, 234, 0.95) !important;
    color: #263B35 !important;
    border: 1px solid rgba(38, 59, 53, 0.16) !important;
}
.sim-mode-btn.active {
    background: #263B35 !important;
    color: #FFFFFF !important;
    border-color: #263B35 !important;
}

/* 8. Pips, Eyebrows & Accents */
.eyebrow {
    color: #263B35 !important;
    background: #E5ECE4 !important;
    border: 1px solid rgba(38, 59, 53, 0.12) !important;
}
.pill {
    background: #E5ECE4 !important;
    color: #263B35 !important;
    border: 1px solid rgba(38, 59, 53, 0.12) !important;
}
.pill b {
    color: #263B35 !important;
}
.chips .chip {
    background: #FFFFFF !important;
    border: 1px solid rgba(38, 59, 53, 0.12) !important;
    color: #303631 !important;
}
.chips .chip:hover {
    background: #E5ECE4 !important;
    color: #263B35 !important;
}
.tile.t-jade, .tile.t-sky {
    background: #E5ECE4 !important;
    color: #263B35 !important;
}
.tile.t-coral {
    background: rgba(214, 165, 141, 0.22) !important;
    color: #8F553D !important;
}
.face.t-jade, .face.t-sky {
    background: #E5ECE4 !important;
    color: #263B35 !important;
}
.face.t-coral {
    background: rgba(214, 165, 141, 0.25) !important;
    color: #8F553D !important;
}

/* 9. Quotes (Testimonial Rail) */
.quote {
    background: #FFFFFF !important;
    border: 1px solid rgba(38, 59, 53, 0.08) !important;
}
.quote.tint {
    background: #E5ECE4 !important;
}
.qtop .co {
    color: #4A544C !important;
}
.qtop .result {
    color: #263B35 !important;
}

/* 10. Final Conversion Section & Footers */
.close-plate {
    background: linear-gradient(160deg, #FFFFFF 0%, #F5F2EA 50%, #E8E1D6 100%) !important;
    border: 1px solid rgba(38, 59, 53, 0.12) !important;
    box-shadow: 0 34px 60px -24px rgba(38, 59, 53, 0.16) !important;
}
.close-plate .field {
    background: #FFFFFF !important;
    border: 1px solid rgba(38, 59, 53, 0.18) !important;
    color: #303631 !important;
}
.close-plate .field:focus {
    outline: 2px solid #263B35 !important;
}
.footlinks {
    background: #E5ECE4 !important;
    border: 1px solid rgba(38, 59, 53, 0.1) !important;
}
.footlinks a {
    color: #303631 !important;
}
.footlinks a:hover {
    color: #263B35 !important;
}
.footbar p, .footbar a {
    color: #5E6960 !important;
}
.footbar a:hover {
    color: #263B35 !important;
}
.sbtn {
    background: rgba(245, 242, 234, 0.95) !important;
    border: 1px solid rgba(38, 59, 53, 0.18) !important;
    color: #263B35 !important;
}
.scue {
    background: #E5ECE4 !important;
    color: #263B35 !important;
    border: 1px solid rgba(38, 59, 53, 0.12) !important;
}
"""

# Append master brand harmony overrides to CSS
if "VIRTUAL HUMAN MASTER BRAND HARMONY OVERRIDES" not in css:
    css += "\n\n" + brand_harmony_css
else:
    # Replace existing block
    css = re.sub(r'/\* ==========================================================================\s*VIRTUAL HUMAN MASTER BRAND HARMONY OVERRIDES.*', brand_harmony_css.strip(), css, flags=re.DOTALL)

with open(CSS_PATH, "w", encoding="utf-8") as f:
    f.write(css)
print("Updated templatemo-633-celadon-style.css with exact brand palette and overrides!")

# 2. Update index.html:
# - Replace purple Mia portrait with warm natural light portrait (photo-1573496359142-b8d87734a5a2)
# - Update carousel script with warm natural light portraits for all personas
# - Ensure inline <style> block includes brand harmony overrides
INDEX_PATH = os.path.join(BASE_DIR, "index.html")
with open(INDEX_PATH, "r", encoding="utf-8") as f:
    index_html = f.read()

# Replace purple neon portrait in center-portrait and bubble
index_html = re.sub(
    r'https://images\.unsplash\.com/photo-1534528741775-53994a69daeb\?auto=format&fit=crop&w=800&q=85',
    'https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?auto=format&fit=crop&w=800&q=85',
    index_html
)
index_html = re.sub(
    r'https://images\.unsplash\.com/photo-1534528741775-53994a69daeb\?auto=format&fit=crop&w=150&q=80',
    'https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?auto=format&fit=crop&w=150&q=80',
    index_html
)

# Also update Elena portrait in right side card to warm natural light Elena
index_html = re.sub(
    r'https://images\.unsplash\.com/photo-1580489944761-15a19d654956\?auto=format&fit=crop&w=400&q=80',
    'https://images.unsplash.com/photo-1573497019940-1c28c88b4f3e?auto=format&fit=crop&w=400&q=80',
    index_html
)

# Update personas array in index.html script
old_script_personas = r'const personas = \[.*?\];'
new_script_personas = '''const personas = [
                {
                    name: "Mia",
                    role: "Devoted Partner",
                    image: "https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?auto=format&fit=crop&w=800&q=85",
                    bubble: "https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?auto=format&fit=crop&w=150&q=80",
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
                    image: "https://images.unsplash.com/photo-1567532939604-b6b5b0db2604?auto=format&fit=crop&w=800&q=85",
                    bubble: "https://images.unsplash.com/photo-1567532939604-b6b5b0db2604?auto=format&fit=crop&w=150&q=80",
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
                    image: "https://images.unsplash.com/photo-1573497019940-1c28c88b4f3e?auto=format&fit=crop&w=800&q=85",
                    bubble: "https://images.unsplash.com/photo-1573497019940-1c28c88b4f3e?auto=format&fit=crop&w=150&q=80",
                    btnText: "Chat with Elena"
                }
            ];'''

index_html = re.sub(old_script_personas, new_script_personas, index_html, flags=re.DOTALL)

# Inline the brand_harmony_css in index.html <style> block as well
if "VIRTUAL HUMAN MASTER BRAND HARMONY OVERRIDES" not in index_html:
    idx = index_html.find("</style>")
    if idx != -1:
        index_html = index_html[:idx] + "\n\n" + brand_harmony_css + "\n" + index_html[idx:]
        print("Inlined brand harmony overrides into index.html <style> block")

# Bump cache buster
index_html = re.sub(r'templatemo-633-celadon-style\.css\?v=[^\"]+', 'templatemo-633-celadon-style.css?v=20261124_harmony', index_html)

with open(INDEX_PATH, "w", encoding="utf-8") as f:
    f.write(index_html)
print("Updated index.html with natural lighting portraits and harmonious styles!")

# 3. Update all other HTML pages (companion.html, discover.html, how-it-works.html, experts.html, pricing.html, faq.html)
# with the inline brand harmony overrides and cache buster
other_pages = ["companion.html", "discover.html", "how-it-works.html", "experts.html", "pricing.html", "faq.html"]
for p in other_pages:
    fpath = os.path.join(BASE_DIR, p)
    if not os.path.exists(fpath): continue
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Bump cache buster
    content = re.sub(r'templatemo-633-celadon-style\.css\?v=[^\"]+', 'templatemo-633-celadon-style.css?v=20261124_harmony', content)
    
    # Inline brand harmony overrides in <style>
    if "VIRTUAL HUMAN MASTER BRAND HARMONY OVERRIDES" not in content:
        idx = content.find("</style>")
        if idx != -1:
            content = content[:idx] + "\n\n" + brand_harmony_css + "\n" + content[idx:]
    else:
        content = re.sub(r'/\* ==========================================================================\s*VIRTUAL HUMAN MASTER BRAND HARMONY OVERRIDES.*?(?=</style>)', brand_harmony_css.strip() + "\n", content, flags=re.DOTALL)
    
    with open(fpath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Updated brand harmony in {p}")

print("Complete brand harmony applied across entire website!")
