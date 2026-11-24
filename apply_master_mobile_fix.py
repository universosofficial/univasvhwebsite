import os
import re

CSS_PATH = r"C:\Users\user\Downloads\websites\templatemo_633_celadon\templatemo-633-celadon-style.css"
BASE_DIR = r"C:\Users\user\Downloads\websites\templatemo_633_celadon"

MASTER_MOBILE_CSS = """

/* ==========================================================================
   VIRTUAL HUMAN — MASTER MOBILE RESPONSIVE ENGINE (320px - 768px)
   Engineered for seamless mobile UX, zero horizontal overflow, flawless typography,
   proper touch targets, high contrast, and pristine claymorphic surfaces.
   ========================================================================== */

/* Universal Eyebrow & Pill Contrast Fix across all viewports */
.pill {
    background: #E5ECE4 !important;
    border: 1px solid rgba(38, 59, 53, 0.14) !important;
    color: #263B35 !important;
}
.pill b {
    background: #263B35 !important;
    color: #FFFFFF !important;
    padding: 3px 10px !important;
    border-radius: 99px !important;
    font-weight: 600 !important;
    display: inline-flex !important;
    align-items: center !important;
}

/* Simulator button classes in companion.html */
.sim-prompt-btn, .sim-mode-btn {
    background: #E5ECE4 !important;
    color: #263B35 !important;
    border: 1px solid rgba(38, 59, 53, 0.16) !important;
    padding: 10px 18px !important;
    border-radius: 99px !important;
    font-size: 0.88rem !important;
    font-family: inherit !important;
    cursor: pointer !important;
    transition: all 0.2s ease !important;
}
.sim-prompt-btn:hover, .sim-mode-btn:hover {
    background: #D8E2D8 !important;
    color: #263B35 !important;
}
.sim-prompt-btn.active, .sim-mode-btn.active {
    background: #263B35 !important;
    color: #FFFFFF !important;
    border-color: #263B35 !important;
    font-weight: 600 !important;
    box-shadow: 0 4px 12px rgba(38, 59, 53, 0.25) !important;
}

/* Card Button Alignment Across Columns */
.plan {
    display: flex !important;
    flex-direction: column !important;
    height: 100% !important;
}
.plan .btn, .plan.identity-card .btn {
    margin-top: auto !important;
}

/* Responsive Table & Email wrapping */
.matrix-scroll-hint {
    display: none;
}
.email-field span {
    word-break: break-word !important;
    overflow-wrap: break-word !important;
}

@media (max-width: 900px) {
    /* Staves Accordion Mobile Engine */
    .slabrow {
        flex-direction: column !important;
        height: auto !important;
        gap: 12px !important;
    }
    .stave {
        width: 100% !important;
        border-radius: 24px !important;
        background: #F5F2EA !important;
        border: 1px solid rgba(216, 226, 216, 0.85) !important;
        box-shadow: 0 8px 18px -8px rgba(38, 59, 53, 0.08) !important;
        overflow: hidden !important;
        transition: background 0.3s ease !important;
    }
    .stave.open {
        background: #FFFFFF !important;
        box-shadow: 0 16px 32px -12px rgba(38, 59, 53, 0.12) !important;
    }
    .stave:not(.open) .bodywrap {
        display: none !important;
        height: 0 !important;
        max-height: 0 !important;
        overflow: hidden !important;
        padding: 0 !important;
        margin: 0 !important;
    }
    .stave:not(.open) .bodywrap > .body {
        display: none !important;
        height: 0 !important;
        overflow: hidden !important;
    }
    .spine {
        padding: 16px 18px !important;
        gap: 12px !important;
    }
    .spine .st {
        font-size: 1.05rem !important;
        color: #263B35 !important;
        font-weight: 600 !important;
    }
    .stave.open .bodywrap {
        display: block !important;
        padding: 0 20px 22px !important;
    }
}

@media (max-width: 768px) {
    /* 1. Safe Anchor Scrolling (Header Clearances) */
    section, [id] {
        scroll-margin-top: 88px !important;
    }

    /* Fixed Top Bar on Mobile */
    .bar {
        padding: 10px 14px !important;
        background: rgba(245, 242, 234, 0.96) !important;
        border-bottom: 1px solid rgba(38, 59, 53, 0.12) !important;
    }
    .brand {
        font-size: 1.15rem !important;
    }

    /* Floating UI Controls: avoid collisions */
    .sfx {
        bottom: 16px !important;
        left: 14px !important;
        z-index: 99 !important;
    }
    .scue {
        display: none !important;
    }
    .top {
        bottom: 16px !important;
        right: 14px !important;
        z-index: 99 !important;
    }

    /* Action Buttons in Hero & CTAs (.acts) */
    .acts {
        display: flex !important;
        flex-direction: column !important;
        gap: 12px !important;
        align-items: stretch !important;
        width: 100% !important;
        max-width: 320px !important;
        margin: 22px auto !important;
    }
    .acts .btn {
        width: 100% !important;
        text-align: center !important;
        margin: 0 !important;
        padding: 14px 20px !important;
    }

    /* Grid Stacking for all card collections */
    .plans.grid-2, .plans.grid-3, .plans.grid-4, .plans {
        display: flex !important;
        flex-direction: column !important;
        gap: 18px !important;
        width: 100% !important;
    }
    .plan {
        width: 100% !important;
        padding: 24px 18px !important;
        box-sizing: border-box !important;
    }

    /* 2. Homepage 3D Gallery Hero (index.html) */
    .gallery-hero-wrap {
        padding: 82px 10px 40px !important;
    }
    .gallery-room {
        padding: 20px 14px 22px !important;
        border-radius: 28px !important;
        background: radial-gradient(circle at 50% 25%, #E3DBD2 0%, #D0C6BB 55%, #BFAF9F 100%) !important;
    }
    .room-tagline {
        position: static !important;
        max-width: 100% !important;
        margin: 0 0 14px 0 !important;
        text-align: center !important;
        font-size: 0.9rem !important;
        line-height: 1.45 !important;
        color: #2E2924 !important;
        padding: 0 8px !important;
    }
    .room-badge-bubble {
        position: static !important;
        display: inline-flex !important;
        justify-content: center !important;
        margin: 0 auto 16px !important;
        left: auto !important;
        right: auto !important;
        top: auto !important;
    }
    .gallery-stage {
        min-height: 370px !important;
        height: auto !important;
        margin-top: 6px !important;
        display: flex !important;
        flex-direction: column !important;
        align-items: center !important;
        position: relative !important;
    }
    .room-backplate {
        width: 90% !important;
        height: 58% !important;
        top: 6% !important;
        border-radius: 20px !important;
    }
    .side-card {
        display: none !important;
    }
    .center-persona-wrap {
        width: 100% !important;
        height: auto !important;
        position: relative !important;
        display: flex !important;
        flex-direction: column !important;
        align-items: center !important;
    }
    .center-portrait {
        width: 250px !important;
        height: 310px !important;
        margin: 0 auto !important;
        border-radius: 24px !important;
        overflow: hidden !important;
        box-shadow: 0 20px 36px -12px rgba(35, 45, 60, 0.35) !important;
    }
    .persona-switcher {
        display: flex !important;
        justify-content: space-between !important;
        position: absolute !important;
        top: 38% !important;
        left: 0 !important;
        right: 0 !important;
        width: 100% !important;
        max-width: 310px !important;
        margin: 0 auto !important;
        transform: translateY(-50%) !important;
        z-index: 25 !important;
        pointer-events: none !important;
    }
    .switcher-btn {
        pointer-events: auto !important;
        width: 44px !important;
        height: 44px !important;
        background: rgba(245, 242, 234, 0.95) !important;
        border: 1px solid rgba(38, 59, 53, 0.18) !important;
        color: #263B35 !important;
        border-radius: 99px !important;
        box-shadow: 0 6px 16px rgba(35, 45, 60, 0.2) !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        cursor: pointer !important;
    }
    .meet-title {
        position: relative !important;
        bottom: auto !important;
        left: auto !important;
        transform: none !important;
        font-size: 2.7rem !important;
        margin: -28px auto 14px !important;
        z-index: 20 !important;
        text-align: center !important;
        text-shadow: 0 4px 18px rgba(0, 0, 0, 0.45) !important;
    }
    .chat-persona-btn {
        width: 100% !important;
        max-width: 270px !important;
        margin: 0 auto !important;
        padding: 13px 20px !important;
        font-size: 0.96rem !important;
        border-radius: 99px !important;
        text-align: center !important;
    }
    .room-timeline {
        display: none !important;
    }
    .room-dock {
        grid-template-columns: 1fr !important;
        gap: 16px !important;
        margin-top: 22px !important;
        text-align: center !important;
    }
    .upload-card {
        padding: 14px !important;
        border-radius: 20px !important;
        max-width: 310px !important;
        margin: 0 auto !important;
    }
    .dock-upload-actions {
        display: flex !important;
        gap: 8px !important;
        justify-content: center !important;
    }
    .dock-btn {
        padding: 8px 12px !important;
        font-size: 0.82rem !important;
    }
    .dock-text-center {
        font-size: 0.86rem !important;
        line-height: 1.45 !important;
        padding: 0 6px !important;
    }
    .dock-widget-right {
        align-items: center !important;
        text-align: center !important;
    }

    /* 3. Companion Simulator on Mobile */
    .sim-box {
        padding: 20px 14px !important;
        border-radius: 26px !important;
        margin-top: 22px !important;
    }
    .sim-header {
        flex-direction: column !important;
        align-items: flex-start !important;
        gap: 12px !important;
        padding-bottom: 16px !important;
    }
    .sim-status {
        font-size: 0.78rem !important;
        padding: 5px 10px !important;
        width: 100% !important;
        box-sizing: border-box !important;
    }
    .sim-meta b {
        font-size: 1.05rem !important;
    }
    .sim-meta span {
        font-size: 0.82rem !important;
    }
    .chat-bubble {
        max-width: 95% !important;
        padding: 14px 16px !important;
        font-size: 0.92rem !important;
    }
    .sim-prompt-btn, .sim-mode-btn {
        width: 100% !important;
        margin-bottom: 8px !important;
        text-align: center !important;
    }
    .email-card {
        padding: 20px 14px !important;
        border-radius: 26px !important;
    }
    .email-header {
        font-size: 0.82rem !important;
    }
    .email-field {
        flex-wrap: wrap !important;
        gap: 4px !important;
    }
    .email-body {
        font-size: 0.92rem !important;
        line-height: 1.55 !important;
    }

    /* 4. Pricing Matrix Table on Mobile */
    .matrix-scroll-hint {
        display: inline-flex !important;
        align-items: center !important;
        gap: 6px !important;
        font-size: 0.78rem !important;
        color: #263B35 !important;
        background: #E5ECE4 !important;
        border: 1px solid rgba(38, 59, 53, 0.12) !important;
        padding: 6px 14px !important;
        border-radius: 99px !important;
        margin: 0 auto 14px !important;
    }
    .matrix-wrapper {
        padding: 20px 12px !important;
        border-radius: 26px !important;
        overflow-x: auto !important;
        -webkit-overflow-scrolling: touch !important;
        position: relative !important;
    }
    .matrix-table {
        min-width: 540px !important;
        font-size: 0.86rem !important;
    }
    .matrix-table th, .matrix-table td {
        padding: 12px 10px !important;
    }
    .matrix-table th:first-child, .matrix-table td:first-child {
        position: sticky !important;
        left: 0 !important;
        background: #F5F2EA !important;
        z-index: 5 !important;
        box-shadow: 2px 0 6px rgba(38, 59, 53, 0.08) !important;
        width: 150px !important;
        min-width: 150px !important;
    }

    /* 5. Discover Filter Chips & Cards */
    .chips {
        display: flex !important;
        flex-wrap: wrap !important;
        gap: 8px !important;
        justify-content: center !important;
        padding: 0 4px !important;
    }
    .chip {
        font-size: 0.78rem !important;
        padding: 7px 12px !important;
    }
    .qtop {
        flex-wrap: wrap !important;
        gap: 6px !important;
    }
    .qtop .co {
        font-size: 0.82rem !important;
        max-width: 65% !important;
        white-space: normal !important;
    }
}
"""

def update_css():
    with open(CSS_PATH, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Check if master mobile css is already present
    if "VIRTUAL HUMAN — MASTER MOBILE RESPONSIVE ENGINE" in content:
        # Replace existing master mobile block
        idx = content.find("/* ==========================================================================\n   VIRTUAL HUMAN — MASTER MOBILE RESPONSIVE ENGINE")
        content = content[:idx] + MASTER_MOBILE_CSS.strip() + "\n"
    else:
        content = content + "\n" + MASTER_MOBILE_CSS.strip() + "\n"
    
    with open(CSS_PATH, "w", encoding="utf-8") as f:
        f.write(content)
    print("Updated templatemo-633-celadon-style.css with master mobile responsive engine.")

def update_html_files():
    html_files = [
        "index.html",
        "companion.html",
        "discover.html",
        "how-it-works.html",
        "experts.html",
        "pricing.html",
        "faq.html"
    ]
    
    version_str = "v=20261124_mobile_v1"
    
    for fname in html_files:
        fpath = os.path.join(BASE_DIR, fname)
        if not os.path.exists(fpath):
            continue
        with open(fpath, "r", encoding="utf-8") as f:
            html = f.read()
        
        # 1. Update stylesheet version
        html = re.sub(r'templatemo-633-celadon-style\.css\?v=[a-zA-Z0-9_]+', f'templatemo-633-celadon-style.css?{version_str}', html)
        
        # 2. Add scroll hint to pricing.html if not already present
        if fname == "pricing.html" and "matrix-scroll-hint" not in html:
            html = html.replace(
                '<div class="matrix-wrapper rv d1">',
                '<div class="center" style="margin-bottom:12px;"><span class="matrix-scroll-hint">&larr; Swipe horizontally to compare tiers &rarr;</span></div>\n                    <div class="matrix-wrapper rv d1">'
            )
        
        # 3. Fix .pill b contrast in inline styles if present
        html = re.sub(r'\.pill b\s*\{\s*color:\s*#263B35\s*!important;\s*\}', '.pill b { background: #263B35 !important; color: #FFFFFF !important; padding: 3px 10px !important; border-radius: 99px !important; }', html)
        
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"Updated {fname} with {version_str}")

if __name__ == "__main__":
    update_css()
    update_html_files()
