import os
import re

DIR = r"C:\Users\user\Downloads\websites\templatemo_633_celadon"
exp_path = os.path.join(DIR, "experts.html")

with open(exp_path, "r", encoding="utf-8") as f:
    exp = f.read()

# Update Hero
exp_hero_old = r'<section class="hero">.*?</section>'
exp_hero_new = '''<section class="hero">
                <div class="shell">
                    <span class="pill rv"><b>For Experts &amp; Creators</b> Knowledge Sharing at Scale</span>
                    <h1 class="rv d1">Your experience could be someone's breakthrough.</h1>
                    <p class="sub rv d2">You've learned things others are still trying to figure out. Create an AI identity that shares your knowledge and makes your expertise accessible through conversation.</p>
                    <div class="acts rv d3">
                        <a class="btn solid" href="#apply">Create Your AI Identity</a>
                        <a class="btn" href="#process">See How It Works</a>
                    </div>
                    <p class="note rv d3">You retain 100% intellectual property ownership of your uploaded knowledge.</p>
                </div>
            </section>'''
exp = re.sub(exp_hero_old, exp_hero_new, exp, flags=re.DOTALL)

# Update Process Section with native Celadon .plans grid-4
process_old = r'<section class="pad" id="process">.*?</section>'
process_new = '''<section class="pad" id="process">
                <div class="shell center">
                    <span class="eyebrow rv">Creator Studio</span>
                    <h2 class="h2 rv">From lived experience to an interactive AI identity.</h2>
                    <p class="lede rv d1">Four simple steps to configure, test, and publish your interactive digital counterpart.</p>
                </div>
                <div class="shell">
                    <div class="plans grid-4" style="margin-top:36px;">
                        <article class="plan rv" style="text-align:left;">
                            <div class="tile t-jade" style="width:48px; height:48px; border-radius:16px; margin-bottom:14px;">
                                <svg viewBox="0 0 24 24" style="width:22px; height:22px; stroke:var(--jade-ink); fill:none; stroke-width:2;"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/></svg>
                            </div>
                            <span class="tag" style="color:var(--jade-ink);">Step 01 &middot; Ingest</span>
                            <h3 style="font-size:1.2rem; margin:10px 0 6px; color:var(--ink);">Knowledge Vault</h3>
                            <p style="font-size:0.9rem; color:var(--ink-2); line-height:1.5;">Upload your essays, podcasts, presentations, books, and frameworks. Your AI identity reasons from your actual materials.</p>
                        </article>
                        <article class="plan rv d1" style="text-align:left;">
                            <div class="tile t-sky" style="width:48px; height:48px; border-radius:16px; margin-bottom:14px;">
                                <svg viewBox="0 0 24 24" style="width:22px; height:22px; stroke:var(--sky-ink); fill:none; stroke-width:2;"><circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1 0 2.83 2 2 0 0 1-2.83 0l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-2 2 2 2 0 0 1-2-2v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83 0 2 2 0 0 1 0-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1-2-2 2 2 0 0 1 2-2h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 0-2.83 2 2 0 0 1 2.83 0l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 2-2 2 2 0 0 1 2 2v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 0 2 2 0 0 1 0 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 2 2 2 2 0 0 1-2 2h-.09a1.65 1.65 0 0 0-1.51 1z"/></svg>
                            </div>
                            <span class="tag" style="color:var(--sky-ink);">Step 02 &middot; Calibrate</span>
                            <h3 style="font-size:1.2rem; margin:10px 0 6px; color:var(--ink);">Personality &amp; Guardrails</h3>
                            <p style="font-size:0.9rem; color:var(--ink-2); line-height:1.5;">Define communication rhythm, analytical strictness, and specific boundaries. Set topics you decline to advise on.</p>
                        </article>
                        <article class="plan rv d2" style="text-align:left;">
                            <div class="tile t-coral" style="width:48px; height:48px; border-radius:16px; margin-bottom:14px;">
                                <svg viewBox="0 0 24 24" style="width:22px; height:22px; stroke:var(--coral-ink, #A8421F); fill:none; stroke-width:2;"><path d="M12 1a3 3 0 0 0-3 3v8a3 3 0 0 0 6 0V4a3 3 0 0 0-3-3z"/><path d="M19 10v2a7 7 0 0 1-14 0v-2"/><line x1="12" y1="19" x2="12" y2="23"/><line x1="8" y1="23" x2="16" y2="23"/></svg>
                            </div>
                            <span class="tag" style="color:var(--coral-ink, #A8421F);">Step 03 &middot; Voice</span>
                            <h3 style="font-size:1.2rem; margin:10px 0 6px; color:var(--ink);">Verified Identity</h3>
                            <p style="font-size:0.9rem; color:var(--ink-2); line-height:1.5;">Pair your written identity with a natural voice model. Once verified, receive an authentic creator seal on the directory.</p>
                        </article>
                        <article class="plan rv d3" style="text-align:left;">
                            <div class="tile t-jade" style="width:48px; height:48px; border-radius:16px; margin-bottom:14px;">
                                <svg viewBox="0 0 24 24" style="width:22px; height:22px; stroke:var(--jade-ink); fill:none; stroke-width:2;"><line x1="12" y1="1" x2="12" y2="23"/><path d="M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg>
                            </div>
                            <span class="tag" style="color:var(--jade-ink);">Step 04 &middot; Publish</span>
                            <h3 style="font-size:1.2rem; margin:10px 0 6px; color:var(--ink);">Scale Your Mentorship</h3>
                            <p style="font-size:0.9rem; color:var(--ink-2); line-height:1.5;">Distribute introductory sessions to build audience connection, and offer deeper access with full creator control.</p>
                        </article>
                    </div>
                </div>
            </section>'''
exp = re.sub(process_old, process_new, exp, flags=re.DOTALL)

with open(exp_path, "w", encoding="utf-8") as f:
    f.write(exp)

print("Updated experts.html successfully")
