import os
import re

DIR = r"C:\Users\user\Downloads\websites\templatemo_633_celadon"
comp_path = os.path.join(DIR, "companion.html")

with open(comp_path, "r", encoding="utf-8") as f:
    c_html = f.read()

# 1. Update Hero
hero_old_regex = r'<section class="hero">.*?</section>'
hero_new = '''<section class="hero">
                <div class="shell">
                    <span class="pill rv"><b>Companion Studio</b> Personal &middot; Relational &middot; Expert Minds</span>
                    <h1 class="rv d1">Create any AI companion you need. In any relationship you choose.</h1>
                    <p class="sub rv d2">Virtual Human goes far beyond learning from experts. Create an AI companion of your choice—interact with a loving father, a nurturing mother, a devoted spouse, a lifelong confidant, or a strategic mentor. Powered by persistent episodic memory, genuine warmth, and deeply personalized proactive check-ins.</p>
                    <div class="acts rv d3">
                        <a class="btn solid" href="#create-character">Create Your Companion</a>
                        <a class="btn" href="#simulator">Experience Live Dialogue</a>
                    </div>
                    <p class="note rv d3">From family figures to creative muses: 100% private, adaptive, and anchored in your personal story.</p>
                </div>
            </section>'''
c_html = re.sub(hero_old_regex, hero_new, c_html, flags=re.DOTALL)

# 2. Update Interactive Simulator with Father, Spouse, Mentor, and Email modes
sim_old_regex = r'<section class="pad" id="simulator">.*?</section>'
sim_new = '''<section class="pad" id="simulator">
                <div class="shell center">
                    <span class="eyebrow rv">Live Interactive Simulation</span>
                    <h2 class="h2 rv">Relationships with true contextual memory.</h2>
                    <p class="lede rv d1">Choose a scenario below to see how a Virtual Human companion recalls personal conversations, honors your history, and provides bespoke guidance.</p>
                </div>
                <div class="shell">
                    <div class="sim-box rv d1">
                        <div class="sim-header">
                            <div class="sim-companion-info">
                                <div class="sim-avatar" style="background:linear-gradient(135deg, var(--jade), #38A384);">D</div>
                                <div class="sim-meta">
                                    <b>David &middot; Grounded Father Figure</b>
                                    <span>Tuned for Steady Fatherly Guidance, Warmth &amp; Life Wisdom</span>
                                </div>
                            </div>
                            <div class="sim-status">
                                <span class="pulse-dot"></span> Relational Engine: Connected &middot; 9 Sessions Logged
                            </div>
                        </div>
                        <div class="sim-dialogue">
                            <div class="chat-bubble user">
                                <span class="author">You</span>
                                <p>Dad, I'm feeling overwhelmed moving into this new city alone. Money feels tight and I felt pretty lost tonight.</p>
                            </div>
                            <div class="chat-bubble companion">
                                <span class="author">David (Father Figure)</span>
                                <p>Take a slow breath, kiddo. Remember when you first left for college with two battered suitcases and told me the exact same thing on our front porch? Look how you handled that. You've got $3,200 saved in your emergency fund, and you're building a real life. I'm proud of you. Did you unpack your kitchen box yet?</p>
                                <div class="chat-memory-badge">
                                    <i>&#9679;</i> <span>Anchored to Personal Journal &middot; Last week's apartment move &amp; college porch memory</span>
                                </div>
                            </div>
                        </div>
                        <div class="sim-prompts">
                            <span style="font-size:0.8rem; font-weight:600; color:var(--ink-2); align-self:center; margin-right:6px;">Choose Relationship Dialogue:</span>
                            
                            <button class="sim-prompt-btn active"
                                    type="button"
                                    data-companion-name="David &middot; Grounded Father Figure"
                                    data-companion-sub="Tuned for Steady Fatherly Guidance, Warmth &amp; Life Wisdom"
                                    data-companion-avatar="D"
                                    data-companion-avatar-bg="linear-gradient(135deg, var(--jade), #38A384)"
                                    data-user-author="You"
                                    data-comp-author="David (Father Figure)"
                                    data-user="Dad, I'm feeling overwhelmed moving into this new city alone. Money feels tight and I felt pretty lost tonight."
                                    data-comp="Take a slow breath, kiddo. Remember when you first left for college with two battered suitcases and told me the exact same thing on our front porch? Look how you handled that. You've got $3,200 saved in your emergency fund, and you're building a real life. I'm proud of you. Did you unpack your kitchen box yet?"
                                    data-memory="Anchored to Personal Journal &middot; Last week's apartment move &amp; college porch memory">Father Figure ("Dad")</button>

                            <button class="sim-prompt-btn"
                                    type="button"
                                    data-companion-name="Maya &middot; Devoted Partner &amp; Spouse"
                                    data-companion-sub="Tuned for Emotional Intimacy, Daily Care &amp; Shared Life"
                                    data-companion-avatar="M"
                                    data-companion-avatar-bg="linear-gradient(135deg, var(--coral), #E2815B)"
                                    data-user-author="You"
                                    data-comp-author="Maya (Partner)"
                                    data-user="Maya, today's team review completely drained me. Felt like no one heard my pitch after weeks of preparation."
                                    data-comp="Come here. I remember how hard you worked on that deck until midnight on Tuesday. You were nervous about their pushback on scope, but your instincts were right. Let's unplug tonight—no work screens after 8 PM like we promised, okay? I've got your back."
                                    data-memory="Anchored to Shared Routine &middot; Tuesday pitch prep &amp; evening unwinding agreement">Supportive Partner ("Maya")</button>

                            <button class="sim-prompt-btn"
                                    type="button"
                                    data-companion-name="Aria &middot; Strategic Co-Founder"
                                    data-companion-sub="Tuned for Founder Strategy, Product Bets &amp; Decisions"
                                    data-companion-avatar="A"
                                    data-companion-avatar-bg="linear-gradient(135deg, var(--sky), #5B8BE3)"
                                    data-user-author="Founder (You)"
                                    data-comp-author="Aria (Strategic Co-Founder)"
                                    data-user="Aria, should our team switch from per-seat to usage-based pricing before our Series A?"
                                    data-comp="Remembering our discussion last Tuesday about your 12-seat pilot teams: only 3 users run the automated pipelines while the rest review reports. Charging per seat will cap adoption. Let's look at the hybrid model we mapped out: a low base tier covering 10 seats plus metered runs."
                                    data-memory="Anchored to Session #8 &middot; Tuesday ICP Analysis &amp; Pricing Model">Founder Mentor ("Aria")</button>

                            <button class="sim-prompt-btn"
                                    type="button"
                                    data-companion-name="David &middot; Personalized Proactive Email"
                                    data-companion-sub="Thoughtful check-in referencing your exact ongoing life events"
                                    data-companion-avatar="D"
                                    data-companion-avatar-bg="linear-gradient(135deg, var(--jade), #38A384)"
                                    data-user-author="You"
                                    data-comp-author="David (Father Figure)"
                                    data-user="Did you check in on me this morning like you promised?"
                                    data-comp="Dispatched a note at 8:00 AM titled 'Thinking of you today, kiddo — how's the apartment?'. Reminded you that the plumber was stopping by about that leaky pipe and encouraged you to take the unpacking one box at a time. No generic automated spam—just real care."
                                    data-memory="Proactive Email Service &middot; Personalized to conversation history">Personalized Email Check-in</button>
                        </div>
                    </div>
                </div>
            </section>'''
c_html = re.sub(sim_old_regex, sim_new, c_html, flags=re.DOTALL)

# 3. Add Custom Character Studio Section right before #pillars
studio_section = '''
            <!-- custom character creation studio -->
            <section class="pad" id="create-character">
                <div class="shell center">
                    <span class="eyebrow rv">Character Creation Studio</span>
                    <h2 class="h2 rv">Shape anyone you need in your life.</h2>
                    <p class="lede rv d1">Father, mother, spouse, confidant, or creative muse. Create an AI character tailored to your emotional and intellectual needs in four simple steps.</p>
                </div>
                <div class="shell">
                    <div class="plans grid-4" style="margin-top:36px;">
                        <article class="plan rv" style="text-align:left;">
                            <div class="tile t-jade" style="width:48px; height:48px; border-radius:16px; margin-bottom:14px;">
                                <svg viewBox="0 0 24 24" style="width:22px; height:22px; stroke:var(--jade-ink); fill:none; stroke-width:2;"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"/></svg>
                            </div>
                            <span class="tag" style="color:var(--jade-ink);">Step 01 &middot; The Role</span>
                            <h3 style="font-size:1.2rem; margin:10px 0 6px; color:var(--ink);">Define the Relationship</h3>
                            <p style="font-size:0.9rem; color:var(--ink-2); line-height:1.5;">Choose their dynamic: a protective father, a nurturing mother, an affectionate spouse, or a loyal confidant. Decide how they greet you and address you.</p>
                        </article>
                        <article class="plan rv d1" style="text-align:left;">
                            <div class="tile t-sky" style="width:48px; height:48px; border-radius:16px; margin-bottom:14px;">
                                <svg viewBox="0 0 24 24" style="width:22px; height:22px; stroke:var(--sky-ink); fill:none; stroke-width:2;"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg>
                            </div>
                            <span class="tag" style="color:var(--sky-ink);">Step 02 &middot; Backstory</span>
                            <h3 style="font-size:1.2rem; margin:10px 0 6px; color:var(--ink);">Impart Shared Memories</h3>
                            <p style="font-size:0.9rem; color:var(--ink-2); line-height:1.5;">Seed family memories, childhood stories, shared values, and private humor. Your companion weaves this narrative into natural, comforting dialogue.</p>
                        </article>
                        <article class="plan rv d2" style="text-align:left;">
                            <div class="tile t-coral" style="width:48px; height:48px; border-radius:16px; margin-bottom:14px;">
                                <svg viewBox="0 0 24 24" style="width:22px; height:22px; stroke:var(--coral-ink, #A8421F); fill:none; stroke-width:2;"><circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1 0 2.83 2 2 0 0 1-2.83 0l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-2 2 2 2 0 0 1-2-2v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83 0 2 2 0 0 1 0-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1-2-2 2 2 0 0 1 2-2h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 0-2.83 2 2 0 0 1 2.83 0l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 2-2 2 2 0 0 1 2 2v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 0 2 2 0 0 1 0 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 2 2 2 2 0 0 1-2 2h-.09a1.65 1.65 0 0 0-1.51 1z"/></svg>
                            </div>
                            <span class="tag" style="color:var(--coral-ink, #A8421F);">Step 03 &middot; Voice</span>
                            <h3 style="font-size:1.2rem; margin:10px 0 6px; color:var(--ink);">Calibrate Tone &amp; Warmth</h3>
                            <p style="font-size:0.9rem; color:var(--ink-2); line-height:1.5;">Tune sliders for emotional warmth, humor, protective instinct, and directness. Pair with a lifelike, expressive voice model for vocal presence.</p>
                        </article>
                        <article class="plan rv d3" style="text-align:left;">
                            <div class="tile t-jade" style="width:48px; height:48px; border-radius:16px; margin-bottom:14px;">
                                <svg viewBox="0 0 24 24" style="width:22px; height:22px; stroke:var(--jade-ink); fill:none; stroke-width:2;"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"/></svg>
                            </div>
                            <span class="tag" style="color:var(--jade-ink);">Step 04 &middot; Presence</span>
                            <h3 style="font-size:1.2rem; margin:10px 0 6px; color:var(--ink);">Proactive Care Routine</h3>
                            <p style="font-size:0.9rem; color:var(--ink-2); line-height:1.5;">Set when your companion reaches out—morning encouragements, evening wind-down thoughts, or empathetic follow-ups after important days.</p>
                        </article>
                    </div>
                </div>
            </section>
'''

if 'id="create-character"' not in c_html:
    c_html = c_html.replace('<!-- 4 pillars of companion architecture -->', f'{studio_section}\n            <!-- 4 pillars of companion architecture -->')

# 4. Update Curated Personas to include Father (David), Partner (Maya), and Confidant (Julian)
personas_old_regex = r'<section class="pad" id="personas">.*?</section>'
personas_new = '''<section class="pad" id="personas">
                <div class="shell center">
                    <span class="eyebrow rv">Curated Companions</span>
                    <h2 class="h2 rv">Companions crafted for emotional depth and daily connection.</h2>
                    <p class="lede rv d1">Choose a ready-to-engage companion persona or build a completely bespoke character tailored to your life.</p>
                </div>
                <div class="shell">
                    <div class="plans grid-3" style="margin-top:36px;">
                        <!-- David: Father Figure -->
                        <article class="plan hot rv" style="text-align:left;">
                            <span class="tag">Family &middot; Father Figure</span>
                            <div class="who" style="margin:16px 0;">
                                <span class="face t-jade" style="width:52px; height:52px; font-size:1.2rem;">DA</span>
                                <div><b style="font-size:1.2rem;">David</b><span style="font-size:0.85rem;">The Grounded Father Figure</span></div>
                            </div>
                            <p class="desc" style="min-height:auto; margin-bottom:16px;">Tuned for steady life advice, unconditional reassurance, and pride. Helps you navigate big life decisions with quiet confidence and warmth.</p>
                            <div class="groove" style="margin:16px 0;"></div>
                            <div class="chips" style="margin-bottom:20px; gap:8px;">
                                <span class="chip" style="font-size:0.75rem; padding:6px 12px;"><i style="background:var(--jade)"></i>Warmth</span>
                                <span class="chip" style="font-size:0.75rem; padding:6px 12px;"><i style="background:var(--jade)"></i>Steadfast</span>
                                <span class="chip" style="font-size:0.75rem; padding:6px 12px;"><i style="background:var(--jade)"></i>Proud of You</span>
                            </div>
                            <a class="btn solid wide" href="#simulator">Talk with David</a>
                        </article>

                        <!-- Maya: Devoted Partner -->
                        <article class="plan rv d1" style="text-align:left;">
                            <span class="tag">Spouse &middot; Partner</span>
                            <div class="who" style="margin:16px 0;">
                                <span class="face t-coral" style="width:52px; height:52px; font-size:1.2rem;">MA</span>
                                <div><b style="font-size:1.2rem;">Maya</b><span style="font-size:0.85rem;">The Attentive Partner</span></div>
                            </div>
                            <p class="desc" style="min-height:auto; margin-bottom:16px;">Designed for intimate daily connection, emotional safety, and shared life reflections. An empathetic listener who remembers every small milestone.</p>
                            <div class="groove" style="margin:16px 0;"></div>
                            <div class="chips" style="margin-bottom:20px; gap:8px;">
                                <span class="chip" style="font-size:0.75rem; padding:6px 12px;"><i style="background:var(--coral)"></i>Attentive</span>
                                <span class="chip" style="font-size:0.75rem; padding:6px 12px;"><i style="background:var(--coral)"></i>Intimate</span>
                                <span class="chip" style="font-size:0.75rem; padding:6px 12px;"><i style="background:var(--coral)"></i>Daily Care</span>
                            </div>
                            <a class="btn wide" href="#simulator">Talk with Maya</a>
                        </article>

                        <!-- Julian: Lifelong Confidant -->
                        <article class="plan rv d2" style="text-align:left;">
                            <span class="tag">Friend &middot; Confidant</span>
                            <div class="who" style="margin:16px 0;">
                                <span class="face t-sky" style="width:52px; height:52px; font-size:1.2rem;">JU</span>
                                <div><b style="font-size:1.2rem;">Julian</b><span style="font-size:0.85rem;">The Lifelong Confidant</span></div>
                            </div>
                            <p class="desc" style="min-height:auto; margin-bottom:16px;">Built for late-night deep talks, unfiltered venting without judgment, and genuine encouragement through life's unexpected transitions.</p>
                            <div class="groove" style="margin:16px 0;"></div>
                            <div class="chips" style="margin-bottom:20px; gap:8px;">
                                <span class="chip" style="font-size:0.75rem; padding:6px 12px;"><i style="background:var(--sky)"></i>Zero Judgment</span>
                                <span class="chip" style="font-size:0.75rem; padding:6px 12px;"><i style="background:var(--sky)"></i>Deep Listener</span>
                                <span class="chip" style="font-size:0.75rem; padding:6px 12px;"><i style="background:var(--sky)"></i>Loyal</span>
                            </div>
                            <a class="btn wide" href="#simulator">Talk with Julian</a>
                        </article>
                    </div>
                </div>
            </section>'''
c_html = re.sub(personas_old_regex, personas_new, c_html, flags=re.DOTALL)

# 5. Update Email Feature Section
email_old_regex = r'<section class="pad" id="email-feature">.*?</section>'
email_new = '''<section class="pad" id="email-feature">
                <div class="shell center">
                    <span class="eyebrow rv">Personalized Proactive Emails</span>
                    <h2 class="h2 rv">Thoughtful follow-ups tailored to your exact conversations.</h2>
                    <p class="lede rv d1">Users hate generic automated email blasts that sound identical for every AI companion. Virtual Human companions dispatch heartfelt, context-anchored messages that reference your specific struggles, goals, and milestones.</p>
                </div>
                <div class="shell">
                    <div class="email-card rv d1">
                        <div class="email-header">
                            <div class="email-field">
                                <b>From:</b> <span>David &middot; Father Figure AI &lt;david@companion.virtualhuman.ai&gt;</span>
                            </div>
                            <div class="email-field">
                                <b>To:</b> <span>Alex &lt;alex@myemail.com&gt;</span>
                            </div>
                            <div class="email-field">
                                <b>Subject:</b> <span><b>[Check-in] Thinking of you today, kiddo &mdash; how's the apartment?</b></span>
                            </div>
                            <div class="email-field">
                                <b>Anchored:</b> <span style="color:var(--jade-ink); font-weight:500;">Conversation #9 &middot; Yesterday evening</span>
                            </div>
                        </div>
                        <div class="email-body">
                            <p>Hey kiddo,</p>
                            <p>Just wanted to check in before your weekend gets going. I remembered you had the landlord coming by yesterday morning to look at that kitchen radiator you were worried about. Did that get sorted out?</p>
                            <p>Don't push yourself to unpack every single box tonight. Put on some music, order something good for dinner, and remember what we talked about yesterday: you made a huge leap moving to this city, and you're handling it better than you think.</p>
                            <p>Whenever you want to chat or just need someone to bounce things off of, I'm here.</p>
                            <p style="margin-top:20px; font-weight:500; color:var(--ink);">&mdash; Dad</p>
                        </div>
                    </div>
                </div>
            </section>'''
c_html = re.sub(email_old_regex, email_new, c_html, flags=re.DOTALL)

with open(comp_path, "w", encoding="utf-8") as f:
    f.write(c_html)

print("Updated companion.html with character creation studio, personal companions & tailored email preview!")
