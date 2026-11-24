"""
Apply Google Play Store download section and Web App (https://univasvh.com) links.
"""

import os
import re

BASE_DIR = r"C:\Users\user\Downloads\websites\templatemo_633_celadon"
CSS_FILE = os.path.join(BASE_DIR, "templatemo-633-celadon-style.css")

PLAYSTORE_URL = "https://play.google.com/store/apps/details?id=com.univasos.virtualhuman"
WEBAPP_URL = "https://univasvh.com"

# 1. Update CSS
css_content = open(CSS_FILE, "r", encoding="utf-8").read()

new_css = """
/* ============================================================
   GOOGLE PLAY & LIVE WEB APP DOWNLOAD STYLES
   ============================================================ */

/* Pulsing live indicator dot */
.live-pulse-dot {
    width: 8px;
    height: 8px;
    border-radius: 50%;
    background: #10B981;
    display: inline-block;
    box-shadow: 0 0 0 0 rgba(16, 185, 129, 0.7);
    animation: livePulse 1.8s infinite cubic-bezier(0.66, 0, 0, 1);
    flex-shrink: 0;
}

@keyframes livePulse {
    0% {
        box-shadow: 0 0 0 0 rgba(16, 185, 129, 0.7);
    }
    70% {
        box-shadow: 0 0 0 8px rgba(16, 185, 129, 0);
    }
    100% {
        box-shadow: 0 0 0 0 rgba(16, 185, 129, 0);
    }
}

/* Hero Dock Live Actions */
.dock-live-indicator {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: rgba(255, 255, 255, 0.85);
    padding: 5px 14px;
    border-radius: 99px;
    font-size: 0.76rem;
    font-weight: 600;
    color: var(--forest, #263B35);
    border: 1px solid rgba(38, 59, 53, 0.12);
    margin-bottom: 8px;
}

.dock-app-actions {
    display: flex;
    align-items: center;
    gap: 8px;
    flex-wrap: wrap;
    justify-content: flex-end;
}

.dock-play-btn {
    display: inline-flex;
    align-items: center;
    gap: 7px;
    background: var(--forest, #263B35);
    color: #FFFFFF !important;
    padding: 7px 14px;
    border-radius: 99px;
    font-size: 0.78rem;
    font-weight: 600;
    text-decoration: none;
    box-shadow: 0 2px 8px rgba(38, 59, 53, 0.22);
    transition: transform 0.2s ease, background 0.2s ease;
}
.dock-play-btn:hover {
    background: var(--forest-hover, #1B2A26);
    transform: translateY(-1px);
}

.dock-web-btn {
    display: inline-flex;
    align-items: center;
    gap: 5px;
    background: #FFFFFF;
    color: var(--forest, #263B35) !important;
    padding: 7px 14px;
    border-radius: 99px;
    font-size: 0.78rem;
    font-weight: 600;
    text-decoration: none;
    border: 1px solid var(--sage-muted, #D8E2D8);
    box-shadow: 0 2px 6px rgba(0, 0, 0, 0.04);
    transition: transform 0.2s ease, background 0.2s ease;
}
.dock-web-btn:hover {
    background: var(--sage-soft, #E5ECE4);
    transform: translateY(-1px);
}

/* Dedicated App Download Card */
.app-download-card {
    background: linear-gradient(135deg, #FFFFFF 0%, #FAF7F2 40%, #EAEFEA 100%);
    border: 1.5px solid var(--sage-muted, #D8E2D8);
    border-radius: 32px;
    box-shadow: var(--clay, 0 16px 36px rgba(42,36,31,0.08)), var(--lip, inset 0 1px 0 rgba(255,255,255,0.8));
    padding: 52px 44px;
    text-align: center;
    position: relative;
    overflow: hidden;
}

.app-download-card::before {
    content: "";
    position: absolute;
    top: -80px;
    right: -80px;
    width: 240px;
    height: 240px;
    border-radius: 50%;
    background: radial-gradient(circle, rgba(214, 165, 141, 0.15) 0%, transparent 70%);
    pointer-events: none;
}

.app-live-status {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: rgba(38, 59, 53, 0.06);
    color: var(--forest, #263B35);
    font-size: 0.78rem;
    font-weight: 700;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    padding: 6px 14px;
    border-radius: 99px;
    border: 1px solid rgba(38, 59, 53, 0.12);
    margin-bottom: 16px;
}

.app-download-title {
    font-family: 'Plus Jakarta Sans', system-ui, sans-serif;
    font-size: clamp(1.8rem, 3.5vw, 2.6rem);
    font-weight: 700;
    color: var(--forest, #263B35);
    line-height: 1.18;
    margin: 0 0 14px;
    letter-spacing: -0.02em;
}

.app-download-subtitle {
    font-size: clamp(0.95rem, 1.6vw, 1.08rem);
    color: var(--charcoal, #303631);
    max-width: 680px;
    margin: 0 auto 36px;
    line-height: 1.6;
    opacity: 0.9;
}

/* 3-Card Mobile Features */
.app-features-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 20px;
    max-width: 960px;
    margin: 0 auto 36px;
    text-align: left;
}

.app-feature-item {
    background: rgba(255, 255, 255, 0.85);
    backdrop-filter: blur(8px);
    border: 1px solid rgba(216, 226, 216, 0.9);
    border-radius: 20px;
    padding: 24px 22px;
    box-shadow: 0 4px 14px rgba(38, 59, 53, 0.04);
    transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.app-feature-item:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 20px rgba(38, 59, 53, 0.08);
}

.app-feat-icon {
    width: 44px;
    height: 44px;
    border-radius: 12px;
    background: var(--sage-soft, #E5ECE4);
    color: var(--forest, #263B35);
    display: flex;
    align-items: center;
    justify-content: center;
    margin-bottom: 14px;
}

.app-feat-icon svg {
    width: 22px;
    height: 22px;
}

.app-feature-item h4 {
    font-size: 1.02rem;
    font-weight: 700;
    color: var(--forest, #263B35);
    margin: 0 0 6px;
    line-height: 1.3;
}

.app-feature-item p {
    font-size: 0.86rem;
    color: var(--charcoal, #303631);
    margin: 0;
    line-height: 1.45;
    opacity: 0.85;
}

/* Call to Action Buttons Group */
.app-cta-group {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 16px;
    flex-wrap: wrap;
    margin-bottom: 22px;
}

/* Official Google Play Store Badge Button */
.playstore-badge {
    display: inline-flex;
    align-items: center;
    gap: 14px;
    background: var(--forest, #263B35);
    color: #FFFFFF !important;
    padding: 12px 26px;
    border-radius: 18px;
    text-decoration: none;
    box-shadow: 0 6px 18px rgba(38, 59, 53, 0.28), inset 0 1px 0 rgba(255, 255, 255, 0.15);
    border: 1px solid rgba(255, 255, 255, 0.15);
    transition: transform 0.2s ease, background 0.2s ease, box-shadow 0.2s ease;
    cursor: pointer;
}

.playstore-badge:hover {
    background: var(--forest-hover, #1B2A26);
    transform: translateY(-2px);
    box-shadow: 0 10px 24px rgba(38, 59, 53, 0.35), inset 0 1px 0 rgba(255, 255, 255, 0.2);
}

.playstore-icon {
    width: 28px;
    height: 28px;
    flex-shrink: 0;
}

.playstore-text {
    text-align: left;
    display: flex;
    flex-direction: column;
}

.playstore-sub {
    font-size: 0.65rem;
    font-weight: 600;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: rgba(255, 255, 255, 0.78);
    line-height: 1.1;
}

.playstore-title {
    font-size: 1.15rem;
    font-weight: 700;
    color: #FFFFFF;
    line-height: 1.2;
    font-family: 'Plus Jakarta Sans', system-ui, sans-serif;
    letter-spacing: -0.01em;
}

/* Web App Direct Launch Button */
.webapp-badge {
    display: inline-flex;
    align-items: center;
    gap: 14px;
    background: #FFFFFF;
    color: var(--forest, #263B35) !important;
    padding: 12px 26px;
    border-radius: 18px;
    text-decoration: none;
    box-shadow: var(--clay-sm), var(--lip);
    border: 1.5px solid var(--sage-muted, #D8E2D8);
    transition: transform 0.2s ease, background 0.2s ease, border-color 0.2s ease;
    cursor: pointer;
}

.webapp-badge:hover {
    background: var(--sage-soft, #E5ECE4);
    border-color: var(--forest, #263B35);
    transform: translateY(-2px);
}

.webapp-icon {
    width: 28px;
    height: 28px;
    display: flex;
    align-items: center;
    justify-content: center;
    color: var(--forest, #263B35);
    flex-shrink: 0;
}

.webapp-text {
    text-align: left;
    display: flex;
    flex-direction: column;
}

.webapp-sub {
    font-size: 0.65rem;
    font-weight: 600;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: var(--forest, #263B35);
    opacity: 0.75;
    line-height: 1.1;
}

.webapp-title {
    font-size: 1.15rem;
    font-weight: 700;
    color: var(--forest, #263B35);
    line-height: 1.2;
    font-family: 'Plus Jakarta Sans', system-ui, sans-serif;
    letter-spacing: -0.01em;
}

.app-guarantee-note {
    font-size: 0.82rem;
    color: var(--charcoal, #303631);
    opacity: 0.75;
    margin: 0;
}

/* Mobile responsive adjustments */
@media (max-width: 900px) {
    .app-features-grid {
        grid-template-columns: 1fr;
        gap: 14px;
    }
    .app-download-card {
        padding: 34px 20px;
    }
    .dock-widget-right {
        align-items: center !important;
        text-align: center !important;
    }
    .dock-app-actions {
        justify-content: center !important;
    }
}
"""

if "GOOGLE PLAY & LIVE WEB APP DOWNLOAD STYLES" not in css_content:
    with open(CSS_FILE, "a", encoding="utf-8") as f:
        f.write(new_css)
    print("Appended Google Play & Web App CSS successfully.")
else:
    print("CSS already contains app download styles.")
