import re

CSS_ADDITIONS = '''
/* ==========================================================================
   VIRTUAL HUMAN — CELADON CLAYMORPHISM ENHANCEMENTS
   ========================================================================== */

/* Active Navigation */
.nav a.active {
    color: var(--jade-ink) !important;
    font-weight: 600 !important;
}

/* Grid Layout Extensions using Celadon's native .plans pattern */
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
    .plans.grid-2,
    .plans.grid-3,
    .plans.grid-4 {
        grid-template-columns: 1fr !important;
    }
}

/* Plan Identity Card for Discover Directory */
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

/* Comparison Feature Matrix Table in Pricing */
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

/* Dialogue Simulation Plate in AI Companion */
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

/* Proactive Email Preview Card */
.email-preview-card {
    background: #FFFFFF !important;
    border-radius: 24px !important;
    box-shadow: var(--clay-sm), var(--lip) !important;
    padding: 28px 30px !important;
    border: 1px solid rgba(42, 122, 98, 0.14) !important;
    text-align: left !important;
}
.email-header-row {
    display: flex !important;
    justify-content: space-between !important;
    align-items: center !important;
    padding-bottom: 14px !important;
    border-bottom: 1px solid rgba(35, 45, 60, 0.08) !important;
    margin-bottom: 16px !important;
    font-size: 0.85rem !important;
    color: var(--ink-2) !important;
}
'''
print("CSS Additions prepared")
