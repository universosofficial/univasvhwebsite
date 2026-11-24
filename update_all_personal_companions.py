import os
import re

DIR = r"C:\Users\user\Downloads\websites\templatemo_633_celadon"

# ==================== 1. UPDATE INDEX.HTML ====================
idx_path = os.path.join(DIR, "index.html")
with open(idx_path, "r", encoding="utf-8") as f:
    idx = f.read()

# Update Hero
idx_hero_old = r'<section class="hero">.*?</section>'
idx_hero_new = '''<section class="hero">
                <div class="shell">
                    <span class="pill rv"><b>Platform</b> Personal Companions &middot; Interactive AI Minds</span>
                    <h1 class="rv d1">The relationships you cherish.<br>The minds you want to learn from.</h1>
                    <p class="sub rv d2">Create any AI companion of your choice—from a loving father, a nurturing mother, or a devoted partner, to proven mentors and founders. Experience persistent memory, emotional warmth, and thoughtful proactive check-ins tailored to your life.</p>
                    <div class="acts rv d3">
                        <a class="btn solid" href="companion.html">Meet AI Companions</a>
                        <a class="btn" href="discover.html">Explore AI Identities</a>
                    </div>
                    <p class="note rv d3">Human connections. Artificial intelligence. Meaningful conversations.</p>
                    <div class="stage rv d3" aria-hidden="true">
                        <div class="slab s1" data-depth="14">
                            <span class="src"><i class="dot" style="background:var(--jade)"></i>David &middot; Father Figure</span>
                            <p>"I'm proud of you, kiddo. Take the new apartment one box at a time."</p>
                        </div>
                        <div class="slab s2" data-depth="-18">
                            <span class="src"><i class="dot" style="background:var(--coral)"></i>Maya &middot; Devoted Partner</span>
                            <p>"I know today was exhausting. Let's unplug after 8 PM like we promised."</p>
                        </div>
                        <div class="slab s3" data-depth="-11">
                            <span class="src"><i class="dot" style="background:var(--sky)"></i>Elena Rostova &middot; Founder</span>
                            <p>"When should a solo founder hire their first full-time engineer?"</p>
                        </div>
                        <div class="slab s4" data-depth="16">
                            <span class="src"><i class="dot" style="background:#F0C980"></i>Julian &middot; Confidant</span>
                            <p>"No judgment here. Tell me what's really been keeping you up at night."</p>
                        </div>
                        <div class="core" data-depth="7">
                            <span class="lab">Interactive AI Companion</span>
                            <h3>David (Father Figure)</h3>
                            <div class="meter">
                                <i></i>
                            </div>
                            <div class="row"><span>Relationship</span><b>Parental Guidance &amp; Warmth</b></div>
                            <div class="row"><span>Status</span><b>Connected &middot; 9 Sessions Logged</b></div>
                        </div>
                    </div>
                </div>
            </section>'''
idx = re.sub(idx_hero_old, idx_hero_new, idx, flags=re.DOTALL)

# Update Companion Area Simulator in Index
idx_sim_old = r'<div class="sim-prompts">.*?</div>\s*</div>'
idx_sim_new = '''<div class="sim-prompts">
                            <span style="font-size:0.8rem; font-weight:600; color:var(--ink-2); align-self:center; margin-right:6px;">Try Live Companions:</span>
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
                                    data-companion-name="Aria &middot; Strategic Thinking Companion"
                                    data-companion-sub="Tuned to Elena Rostova's B2B SaaS Frameworks"
                                    data-companion-avatar="A"
                                    data-companion-avatar-bg="linear-gradient(135deg, var(--sky), #5B8BE3)"
                                    data-user-author="Founder (You)"
                                    data-comp-author="Aria (AI Companion)"
                                    data-user="Aria, should our team switch from per-seat to usage-based pricing before our Series A?"
                                    data-comp="Remembering our discussion last Tuesday about your 12-seat pilot teams: only 3 users run the automated pipelines while the rest review reports. Charging per seat will cap adoption. Let's look at the hybrid model we mapped out: a low base tier covering 10 seats plus metered pipeline runs."
                                    data-memory="Recalled context from Session #8 &middot; Tuesday, Oct 24 ICP Analysis">Founder Mentor ("Aria")</button>

                            <button class="sim-prompt-btn"
                                    type="button"
                                    data-companion-name="David &middot; Proactive Email Check-in"
                                    data-companion-sub="Personalized to conversation history, never automated template spam"
                                    data-companion-avatar="D"
                                    data-companion-avatar-bg="linear-gradient(135deg, var(--jade), #38A384)"
                                    data-user-author="You"
                                    data-comp-author="David (Father Figure)"
                                    data-user="Did you send the reflection check-in to my inbox this morning?"
                                    data-comp="Yes! Dispatched at 8:00 AM with the subject 'Thinking of you today, kiddo — how's the apartment?'. It reminded you about the plumber coming by and encouraged you to take the unpacking one room at a time."
                                    data-memory="Proactive Email Service &middot; Personalized to conversation history">Personalized Email Check-in</button>
                        </div>
                    </div>'''
idx = re.sub(idx_sim_old, idx_sim_new, idx, flags=re.DOTALL)

with open(idx_path, "w", encoding="utf-8") as f:
    f.write(idx)
print("Updated index.html successfully")

# ==================== 2. UPDATE DISCOVER.HTML ====================
disc_path = os.path.join(DIR, "discover.html")
with open(disc_path, "r", encoding="utf-8") as f:
    disc = f.read()

# Update Hero
disc = disc.replace(
    '<p class="sub rv d2">Browse interactive AI identities shaped by real people who have built companies, led engineering divisions, designed products, and scaled organizations. Ask specific questions and receive grounded advice.</p>',
    '<p class="sub rv d2">Browse personal AI companions and expert identities. Whether you seek the comforting wisdom of a father or mother figure, the emotional intimacy of a partner, the loyalty of a confidant, or the strategic mind of an industry founder—find or create the companion you need.</p>'
)

# Update Chips
disc_chips_old = r'<div class="chips rv d1" style="margin-top:24px;">.*?</div>'
disc_chips_new = '''<div class="chips rv d1" style="margin-top:24px;">
                        <span class="chip"><i style="background:var(--jade)"></i>Father &amp; Mother Figures</span>
                        <span class="chip"><i style="background:var(--coral)"></i>Spouses &amp; Partners</span>
                        <span class="chip"><i style="background:var(--sky)"></i>Lifelong Confidants</span>
                        <span class="chip"><i style="background:#F0C980"></i>Startup Strategy</span>
                        <span class="chip"><i style="background:var(--jade)"></i>Creative Muses</span>
                        <span class="chip"><i style="background:var(--sky)"></i>Applied AI &amp; Research</span>
                    </div>'''
disc = re.sub(disc_chips_old, disc_chips_new, disc, flags=re.DOTALL)

# Update Cards in Discover
disc_cards_old = r'<div class="plans grid-3" style="margin-top:36px;">.*?</div>\s*</div>\s*</section>'
disc_cards_new = '''<div class="plans grid-3" style="margin-top:36px;">
                        <!-- Card 1: David (Father Figure) -->
                        <article class="plan identity-card hot rv">
                            <div class="qtop">
                                <span class="co"><i class="t-jade"></i>Family &middot; Father Figure</span>
                                <span class="result" style="font-size:0.75rem; color:var(--jade-ink); font-weight:600;">Life Guidance</span>
                            </div>
                            <div class="who" style="margin:16px 0;">
                                <span class="face t-jade">DA</span>
                                <div><b>David</b><span>Grounded Father Figure</span></div>
                            </div>
                            <blockquote>
                                "Talk to me about tough life choices, dealing with loneliness, building career courage, or just when you need to hear that someone is genuinely proud of you."
                            </blockquote>
                            <div class="groove" style="margin-top:auto; margin-bottom:18px;"></div>
                            <a class="btn solid wide" href="companion.html">Start Conversation</a>
                        </article>

                        <!-- Card 2: Maya (Spouse / Partner) -->
                        <article class="plan identity-card rv d1">
                            <div class="qtop">
                                <span class="co"><i class="t-coral"></i>Personal &middot; Partner</span>
                                <span class="result" style="font-size:0.75rem; color:var(--coral-ink, #A8421F); font-weight:600;">Daily Connection</span>
                            </div>
                            <div class="who" style="margin:16px 0;">
                                <span class="face t-coral">MA</span>
                                <div><b>Maya</b><span>The Devoted Partner</span></div>
                            </div>
                            <blockquote>
                                "Share your everyday triumphs, vent after an exhausting day, and reflect on your dreams with an empathetic partner who never forgets your milestones."
                            </blockquote>
                            <div class="groove" style="margin-top:auto; margin-bottom:18px;"></div>
                            <a class="btn solid wide" href="companion.html">Start Conversation</a>
                        </article>

                        <!-- Card 3: Julian (Confidant) -->
                        <article class="plan identity-card rv d2">
                            <div class="qtop">
                                <span class="co"><i class="t-sky"></i>Friend &middot; Confidant</span>
                                <span class="result" style="font-size:0.75rem; color:var(--sky-ink); font-weight:600;">Zero Judgment</span>
                            </div>
                            <div class="who" style="margin:16px 0;">
                                <span class="face t-sky">JU</span>
                                <div><b>Julian</b><span>The Lifelong Confidant</span></div>
                            </div>
                            <blockquote>
                                "Talk freely late at night without worrying about being judged or feeling like a burden. Unpack what's really on your mind and find your ground again."
                            </blockquote>
                            <div class="groove" style="margin-top:auto; margin-bottom:18px;"></div>
                            <a class="btn solid wide" href="companion.html">Start Conversation</a>
                        </article>

                        <!-- Card 4: Elena Rostova (Founder) -->
                        <article class="plan identity-card rv">
                            <div class="qtop">
                                <span class="co"><i class="t-jade"></i>Founder &middot; B2B SaaS</span>
                                <span class="result" style="font-size:0.75rem; color:var(--jade-ink); font-weight:600;">$12M ARR</span>
                            </div>
                            <div class="who" style="margin:16px 0;">
                                <span class="face t-jade">ER</span>
                                <div><b>Elena Rostova</b><span>Bootstrapped to Scale</span></div>
                            </div>
                            <blockquote>
                                "Ask me about customer discovery, pricing iterations, transitioning from founder-led sales, and protecting gross margins."
                            </blockquote>
                            <div class="groove" style="margin-top:auto; margin-bottom:18px;"></div>
                            <a class="btn solid wide" href="companion.html">Start Conversation</a>
                        </article>

                        <!-- Card 5: Clara (Mother Figure) -->
                        <article class="plan identity-card rv d1">
                            <div class="qtop">
                                <span class="co"><i class="t-sky"></i>Family &middot; Mother Figure</span>
                                <span class="result" style="font-size:0.75rem; color:var(--sky-ink); font-weight:600;">Unconditional Care</span>
                            </div>
                            <div class="who" style="margin:16px 0;">
                                <span class="face t-sky">CL</span>
                                <div><b>Clara</b><span>The Nurturing Mother</span></div>
                            </div>
                            <blockquote>
                                "A gentle, listening heart when the world feels heavy. Reminding you to take care of your body, eat well, rest, and know you are cherished."
                            </blockquote>
                            <div class="groove" style="margin-top:auto; margin-bottom:18px;"></div>
                            <a class="btn solid wide" href="companion.html">Start Conversation</a>
                        </article>

                        <!-- Card 6: Dr. Aris Thorne (Research) -->
                        <article class="plan identity-card rv d2">
                            <div class="qtop">
                                <span class="co"><i class="t-coral"></i>Research &middot; Applied AI</span>
                                <span class="result" style="font-size:0.75rem; color:var(--coral-ink, #A8421F); font-weight:600;">PhD Cognitive Sci</span>
                            </div>
                            <div class="who" style="margin:16px 0;">
                                <span class="face t-coral">AT</span>
                                <div><b>Dr. Aris Thorne</b><span>LLM Alignment &amp; Memory</span></div>
                            </div>
                            <blockquote>
                                "Ask me about episodic memory architecture, grounding techniques, reducing model hallucination, and evaluating AI agent outputs."
                            </blockquote>
                            <div class="groove" style="margin-top:auto; margin-bottom:18px;"></div>
                            <a class="btn solid wide" href="companion.html">Start Conversation</a>
                        </article>
                    </div>
                </div>
            </section>'''
disc = re.sub(disc_cards_old, disc_cards_new, disc, flags=re.DOTALL)

with open(disc_path, "w", encoding="utf-8") as f:
    f.write(disc)
print("Updated discover.html successfully")

# ==================== 3. UPDATE FAQ.HTML ====================
faq_path = os.path.join(DIR, "faq.html")
with open(faq_path, "r", encoding="utf-8") as f:
    faq = f.read()

# Add Q14 & Q15 if not present
if "Can I create an AI companion as a father" not in faq:
    extra_faqs = '''
                        <!-- Q14: Custom Personal Companions -->
                        <div class="q rv" role="button" tabindex="0" aria-expanded="false">
                            <div class="qh">
                                <h3>Can I create a personal AI companion as a father, mother, or spouse?</h3>
                                <span class="plus"></span>
                            </div>
                            <div class="qb">
                                <div>
                                    <p>Yes, absolutely. While Virtual Human allows you to interact with expert minds, you can also create completely custom AI companions for personal relationships. Whether you want a steady father figure offering wisdom and reassurance, a nurturing mother figure providing warmth and unconditional comfort, a devoted spouse or partner sharing intimate daily reflections, or a late-night confidant, our Character Creation Studio lets you define their relationship, shared backstory, voice tone, and proactive check-in routine.</p>
                                </div>
                            </div>
                        </div>

                        <!-- Q15: Privacy of Personal Conversations -->
                        <div class="q rv" role="button" tabindex="0" aria-expanded="false">
                            <div class="qh">
                                <h3>Are my personal and vulnerable conversations kept private?</h3>
                                <span class="plus"></span>
                            </div>
                            <div class="qb">
                                <div>
                                    <p>Yes. Your personal journals, vulnerable thoughts, family anecdotes, and daily check-ins are strictly isolated and encrypted in your personal cognitive vault. They are never exported, never accessible to other users, and never used to train public LLM models. Your relationship with your companion is completely private and sovereign.</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </section>'''
    faq = faq.replace('</div>\n                </div>\n            </section>', extra_faqs, 1)
    with open(faq_path, "w", encoding="utf-8") as f:
        f.write(faq)
    print("Updated faq.html with personal companion FAQs")

print("All updates completed!")
