import os

DIR = r"C:\Users\user\Downloads\websites\templatemo_633_celadon"
css_path = os.path.join(DIR, "templatemo-633-celadon-style.css")

with open(css_path, "r", encoding="utf-8") as f:
    css = f.read()

append_css = """

/* ---------- Virtual Human Multi-page & Claymorphism Final Enhancements ---------- */

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
"""

if ".matrix-wrapper" not in css:
    css += append_css
    with open(css_path, "w", encoding="utf-8") as f:
        f.write(css)
    print("Updated templatemo-633-celadon-style.css")
else:
    print("CSS already contains matrix-wrapper")
