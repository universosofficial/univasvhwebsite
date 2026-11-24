import os
import re

BASE_DIR = r"C:\Users\user\Downloads\websites\templatemo_633_celadon"

MASTER_MOBILE_CSS_RULE = """
/* ==========================================================================
   VIRTUAL HUMAN — MASTER MOBILE RESPONSIVE ENGINE (320px - 768px)
   ========================================================================== */

/* 0. Header & Drawer Navigation */
header.top {
    z-index: 95 !important;
}
.drawer {
    z-index: 90 !important;
    background: #F5F2EA !important;
    box-shadow: -10px 0 30px rgba(38, 59, 53, 0.18) !important;
}
.drawer a:not(.btn) {
    color: #263B35 !important;
}
.drawer a:not(.btn):hover, .drawer a.active {
    background: #E5ECE4 !important;
    color: #263B35 !important;
}
.drawer-close {
    width: 38px !important;
    height: 38px !important;
    border-radius: 99px !important;
    background: #E5ECE4 !important;
    border: 1px solid rgba(38, 59, 53, 0.16) !important;
    color: #263B35 !important;
    font-size: 1.5rem !important;
    display: inline-flex !important;
    align-items: center !important;
    justify-content: center !important;
    cursor: pointer !important;
    line-height: 1 !important;
    transition: background 0.2s ease !important;
}
.drawer-close:hover {
    background: #D8E2D8 !important;
}

/* Universal Eyebrow & Pill Contrast Fix */
.pill {
    background: #E5ECE4 !important;
    border: 1px solid rgba(38, 59, 53, 0.14) !important;
    color: #263B35 !important;
    display: inline-flex !important;
    align-items: center !important;
    gap: 8px !important;
    padding: 6px 14px 6px 8px !important;
    max-width: 95% !important;
    white-space: normal !important;
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

/* Word-break for email */
.email-field span {
    word-break: break-all !important;
    overflow-wrap: break-word !important;
}
.matrix-scroll-hint {
    display: none;
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

    /* Problem and Opportunity statplate in index.html */
    .statplate, #perspective .statplate {
        grid-template-columns: 1fr !important;
        display: flex !important;
        flex-direction: column !important;
        gap: 16px !important;
        padding: 16px !important;
    }
    .statplate .stat {
        width: 100% !important;
        box-sizing: border-box !important;
        padding: 24px 20px !important;
        border-radius: 24px !important;
    }

    /* 2. Homepage 3D Gallery Hero (index.html) */
    .gallery-hero-wrap {
        padding: 82px 10px 36px !important;
    }
    .gallery-room {
        padding: 20px 14px 22px !important;
        border-radius: 28px !important;
        background: radial-gradient(circle at 50% 25%, #E3DBD2 0%, #D0C6BB 55%, #BFAF9F 100%) !important;
    }
    .room-tagline {
        position: static !important;
        max-width: 100% !important;
        margin: 0 auto 12px !important;
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
        min-height: auto !important;
        height: auto !important;
        margin-top: 6px !important;
        display: flex !important;
        flex-direction: column !important;
        align-items: center !important;
        position: relative !important;
        padding: 0 !important;
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
        padding: 20px 10px !important;
        border-radius: 26px !important;
        overflow-x: auto !important;
        -webkit-overflow-scrolling: touch !important;
        position: relative !important;
    }
    .matrix-table {
        min-width: 530px !important;
        font-size: 0.86rem !important;
    }
    .matrix-table th, .matrix-table td {
        padding: 12px 8px !important;
    }
    .matrix-table th:first-child, .matrix-table td:first-child {
        position: sticky !important;
        left: 0 !important;
        background: #F5F2EA !important;
        z-index: 5 !important;
        box-shadow: 2px 0 6px rgba(38, 59, 53, 0.08) !important;
        width: 145px !important;
        min-width: 145px !important;
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

def update_all_html_files():
    html_files = [
        "index.html",
        "companion.html",
        "discover.html",
        "how-it-works.html",
        "experts.html",
        "pricing.html",
        "faq.html"
    ]
    
    version_str = "v=20261124_mobile_v2"
    
    for fname in html_files:
        fpath = os.path.join(BASE_DIR, fname)
        if not os.path.exists(fpath):
            continue
        with open(fpath, "r", encoding="utf-8") as f:
            html = f.read()
        
        # 1. Update stylesheet version
        html = re.sub(r'templatemo-633-celadon-style\.css\?v=[a-zA-Z0-9_]+', f'templatemo-633-celadon-style.css?{version_str}', html)
        
        # 2. Add or update drawer close button inside <aside class="drawer" ...>
        if '<button class="drawer-close"' not in html:
            html = re.sub(
                r'(<aside class="drawer"[^>]*>)\s*(<span class="dtag">Menu</span>)',
                r'\1\n            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:18px; padding: 0 4px;">\n                \2\n                <button class="drawer-close" id="drawer-close" aria-label="Close menu">&times;</button>\n            </div>',
                html
            )
        
        # 3. Fix #perspective in index.html (remove inline grid-template-columns)
        if fname == "index.html":
            html = re.sub(
                r'<div class="statplate rv d1" style="grid-template-columns:\s*repeat\(3,\s*1fr\);\s*margin-top:36px;">',
                r'<div class="statplate rv d1" style="margin-top:36px;">',
                html
            )
            # Remove any conflicting older media queries in index.html style block
            html = re.sub(r'@media\s*\(max-width:\s*640px\)\s*\{[^}]*\}', '', html)
        
        # 4. Fix experts.html pill text "For Experts & Creators" -> "For Experts"
        if fname == "experts.html":
            html = html.replace('For Experts & Creators', 'For Experts')
        
        # 5. Insert MASTER_MOBILE_CSS_RULE right before </style> in the document
        if "</style>" in html:
            # Check if MASTER_MOBILE_CSS_RULE is already in style
            if "VIRTUAL HUMAN — MASTER MOBILE RESPONSIVE ENGINE" in html:
                # Replace the old one
                pattern = r'/\* ==========================================================================\s+VIRTUAL HUMAN — MASTER MOBILE RESPONSIVE ENGINE.*?</style>'
                html = re.sub(pattern, MASTER_MOBILE_CSS_RULE + "\n</style>", html, flags=re.DOTALL)
            else:
                html = html.replace("</style>", MASTER_MOBILE_CSS_RULE + "\n</style>")
        
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"Applied mobile enhancements to {fname}")

def update_js():
    js_path = os.path.join(BASE_DIR, "templatemo-633-celadon-script.js")
    with open(js_path, "r", encoding="utf-8") as f:
        js = f.read()
    
    if "drawer-close" not in js:
        # Add event listener for drawer-close button
        old_part = 'if (burger && drawer && scrim) {'
        new_part = '''var drawerClose = document.getElementById("drawer-close");
    if (drawerClose && drawer) {
        drawerClose.addEventListener("click", function() {
            setDrawer(false);
        });
    }
    if (burger && drawer && scrim) {'''
        js = js.replace(old_part, new_part)
        with open(js_path, "w", encoding="utf-8") as f:
            f.write(js)
        print("Updated templatemo-633-celadon-script.js with drawer-close event listener.")

if __name__ == "__main__":
    update_all_html_files()
    update_js()
