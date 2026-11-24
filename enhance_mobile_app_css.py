import os

css_path = r"C:\Users\user\Downloads\websites\templatemo_633_celadon\templatemo-633-celadon-style.css"
with open(css_path, "r", encoding="utf-8") as f:
    css = f.read()

target = """/* Mobile responsive adjustments */
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
}"""

replacement = """/* Mobile responsive adjustments */
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

@media (max-width: 600px) {
    .app-cta-group {
        flex-direction: column;
        align-items: stretch;
        gap: 12px;
        max-width: 320px;
        margin-left: auto;
        margin-right: auto;
    }
    .playstore-badge, .webapp-badge {
        width: 100%;
        justify-content: center;
        padding: 12px 18px;
    }
    .app-download-title {
        font-size: 1.6rem;
    }
    .footlinks-nav {
        justify-content: center;
        gap: 12px 16px;
    }
}"""

if target in css:
    with open(css_path, "w", encoding="utf-8") as f:
        f.write(css.replace(target, replacement))
    print("Enhanced mobile responsive styles in CSS.")
