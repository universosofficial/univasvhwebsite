# -*- coding: utf-8 -*-
"""
Rebalance Virtual Human index.html to 70% Personal Companions / 30% Interactive Human Expertise
while strictly preserving the exact Celadon claymorphism design, DOM classes, styles, and interactions.
"""

path = r"C:\Users\user\Downloads\websites\templatemo_633_celadon\index.html"

with open(path, "r", encoding="utf-8") as f:
    html = f.read()

# 1. Update Navigation to feature AI Companion prominently
old_nav = '''                <nav class="nav">
                    <a href="discover.html">Discover</a>
                    <a href="how-it-works.html">How It Works</a>
                    <a href="experts.html">For Experts</a>
                    <a href="faq.html">FAQ</a>
                </nav>'''

new_nav = '''                <nav class="nav">
                    <a href="companion.html">AI Companion</a>
                    <a href="discover.html">Discover</a>
                    <a href="how-it-works.html">How It Works</a>
                    <a href="experts.html">For Experts</a>
                    <a href="faq.html">FAQ</a>
                </nav>'''

old_drawer = '''        <aside class="drawer" id="drawer" aria-label="Menu">
            <span class="dtag">Menu</span>
            <a href="discover.html">Discover</a>
            <a href="how-it-works.html">How It Works</a>
            <a href="experts.html">For Experts</a>
            <a href="faq.html">FAQ</a>
            <a class="btn solid" href="index.html#start">Get Started</a>
        </aside>'''

new_drawer = '''        <aside class="drawer" id="drawer" aria-label="Menu">
            <span class="dtag">Menu</span>
            <a href="companion.html">AI Companion</a>
            <a href="discover.html">Discover</a>
            <a href="how-it-works.html">How It Works</a>
            <a href="experts.html">For Experts</a>
            <a href="faq.html">FAQ</a>
            <a class="btn solid" href="index.html#start">Get Started</a>
        </aside>'''

# 2. Hero Section: 70% Personal Relationships / 30% Human Expertise
old_hero = '''            <!-- hero -->
            <section class="hero">
                <div class="shell">
                    <span class="pill rv"><b>Platform</b> Human Knowledge &middot; AI Conversations</span>
                    <h1 class="rv d1">The people you want to learn from.<br>Just a conversation away.</h1>
                    <p class="sub rv d2">Discover AI companions shaped by real people's knowledge and experiences. Ask questions, explore ideas and learn from the minds behind the expertise.</p>
                    <div class="acts rv d3">
                        <a class="btn solid" href="discover.html">Explore Virtual Human</a>
                        <a class="btn" href="experts.html">Create Your AI Identity</a>
                    </div>
                    <p class="note rv d3">Discover. Connect. Learn.</p>
                    <div class="stage rv d3" aria-hidden="true">
                        <div class="slab s1" data-depth="14">
                            <span class="src"><i class="dot" style="background:var(--sky)"></i>Elena Rostova &middot; Founder</span>
                            <p>"When should a solo founder hire their first full-time engineer?"</p>
                        </div>
                        <div class="slab s2" data-depth="-18">
                            <span class="src"><i class="dot" style="background:var(--coral)"></i>Marcus Vance &middot; Strategy</span>
                            <p>"We're debating whether to price on seats or usage. What did you learn?"</p>
                        </div>
                        <div class="slab s3" data-depth="-11">
                            <span class="src"><i class="dot" style="background:var(--jade)"></i>Dr. Aris Thorne &middot; Research</span>
                            <p>"How do you synthesize conflicting customer signals into product bets?"</p>
                        </div>
                        <div class="slab s4" data-depth="16">
                            <span class="src"><i class="dot" style="background:#F0C980"></i>Sarah Lindqvist &middot; Product</span>
                            <p>"What are the early indicators that an organic growth channel is saturated?"</p>
                        </div>
                        <div class="core" data-depth="7">
                            <span class="lab">Interactive AI Identity</span>
                            <h3>Elena Rostova</h3>
                            <div class="meter">
                                <i></i>
                            </div>
                            <div class="row"><span>Domain</span><b>B2B SaaS Founder</b></div>
                            <div class="row"><span>Perspective</span><b>Bootstrapped to $12M ARR</b></div>
                        </div>
                    </div>
                </div>
            </section>'''

new_hero = '''            <!-- hero -->
            <section class="hero">
                <div class="shell">
                    <span class="pill rv"><b>Personal AI Companions</b> Relational Continuity &middot; Lived Wisdom</span>
                    <h1 class="rv d1">The companion you need most.<br>The minds you want to learn from.</h1>
                    <p class="sub rv d2">Craft meaningful AI companions for any relationship you choose—an encouraging father figure, a nurturing mother, a devoted spouse, or a lifelong confidant, anchored in emotional warmth and persistent memory. Plus, interact 24/7 with the battle-tested wisdom and frameworks of proven leaders.</p>
                    <div class="acts rv d3">
                        <a class="btn solid" href="companion.html">Create Your Companion</a>
                        <a class="btn" href="discover.html">Explore All Identities</a>
                    </div>
                    <p class="note rv d3">Emotional warmth &middot; Persistent episodic memory &middot; 24/7 lived wisdom</p>
                    <div class="stage rv d3" aria-hidden="true">
                        <div class="slab s1" data-depth="14">
                            <span class="src"><i class="dot" style="background:var(--jade)"></i>David &middot; Father Figure</span>
                            <p>"Take a breath, kiddo. Remember how you handled the move last year? You've got this."</p>
                        </div>
                        <div class="slab s2" data-depth="-18">
                            <span class="src"><i class="dot" style="background:var(--coral)"></i>Maya &middot; Devoted Partner</span>
                            <p>"You gave today's pitch everything. Come home, let's unplug, and recharge tonight."</p>
                        </div>
                        <div class="slab s3" data-depth="-11">
                            <span class="src"><i class="dot" style="background:var(--sky)"></i>Julian &middot; Confidant</span>
                            <p>"I remember what you said two months ago about this crossroad. What does your gut say?"</p>
                        </div>
                        <div class="slab s4" data-depth="16">
                            <span class="src"><i class="dot" style="background:#F0C980"></i>Elena &middot; SaaS Founder</span>
                            <p>"Protect your early pricing power. Don't discount until you understand customer churn."</p>
                        </div>
                        <div class="core" data-depth="7">
                            <span class="lab">Personal AI Companion</span>
                            <h3>David &middot; Father Figure</h3>
                            <div class="meter">
                                <i></i>
                            </div>
                            <div class="row"><span>Relationship</span><b>Supportive Father</b></div>
                            <div class="row"><span>Continuity</span><b>Episodic Memory &middot; 14 Sessions</b></div>
                        </div>
                    </div>
                </div>
            </section>'''

# 3. Trust bar: reflect 70% Personal / 30% Expert
old_trust = '''            <!-- trust -->
            <section class="pad-s">
                <div class="shell rv">
                    <p class="trust-cap">Interactive knowledge across disciplines</p>
                    <div class="trust">
                        <span>Startup Strategy</span><span>Engineering Leadership</span><span>Product Architecture</span><span>Venture Capital</span><span>Creative Direction</span><span>Executive Mentorship</span>
                    </div>
                </div>
            </section>'''

new_trust = '''            <!-- trust -->
            <section class="pad-s">
                <div class="shell rv">
                    <p class="trust-cap">Meaningful relationships &amp; interactive mentorship</p>
                    <div class="trust">
                        <span>Father &amp; Mother Figures</span><span>Devoted Spouses &amp; Partners</span><span>Lifelong Confidants</span><span>Founder Mentorship</span><span>Leadership Strategy</span><span>Creative Direction</span>
                    </div>
                </div>
            </section>'''

# 4. Section 3: The Problem and Opportunity
old_perspective = '''            <!-- SECTION 3: THE PROBLEM AND OPPORTUNITY -->
            <section class="pad" id="perspective">
                <div class="shell center">
                    <span class="eyebrow rv">Perspective</span>
                    <h2 class="h2 rv">The right perspective can change everything.</h2>
                    <p class="lede rv d1">Sometimes, what you need isn't another article or generic answer. It's insight from someone who has actually been there.</p>
                </div>
                <div class="shell">
                    <div class="statplate rv d1" style="grid-template-columns: repeat(3, 1fr); margin-top:36px;">
                        <div class="stat" style="text-align:left; padding:32px 26px;">
                            <div class="tile t-jade" style="width:48px; height:48px; border-radius:16px; margin-bottom:16px;">
                                <svg viewBox="0 0 24 24" style="width:22px; height:22px; stroke:var(--jade-ink); fill:none; stroke-width:2;"><circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg>
                            </div>
                            <h3 style="font-size:1.2rem; margin-bottom:8px; color:var(--ink);">Knowledge is Everywhere</h3>
                            <p style="font-size:0.9rem; line-height:1.55; color:var(--ink-2); margin:0;">Articles, videos, and books are abundant, but meaningful access to real-world experience and personalized guidance remains painfully scarce.</p>
                        </div>
                        <div class="stat" style="text-align:left; padding:32px 26px;">
                            <div class="tile t-coral" style="width:48px; height:48px; border-radius:16px; margin-bottom:16px;">
                                <svg viewBox="0 0 24 24" style="width:22px; height:22px; stroke:var(--coral-ink, #A8421F); fill:none; stroke-width:2;"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
                            </div>
                            <h3 style="font-size:1.2rem; margin-bottom:8px; color:var(--ink);">Time is Finite</h3>
                            <p style="font-size:0.9rem; line-height:1.55; color:var(--ink-2); margin:0;">Experienced people and proven mentors cannot personally guide everyone who needs their help. Their calendars simply do not scale.</p>
                        </div>
                        <div class="stat" style="text-align:left; padding:32px 26px;">
                            <div class="tile t-sky" style="width:48px; height:48px; border-radius:16px; margin-bottom:16px;">
                                <svg viewBox="0 0 24 24" style="width:22px; height:22px; stroke:var(--sky-ink); fill:none; stroke-width:2;"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg>
                            </div>
                            <h3 style="font-size:1.2rem; margin-bottom:8px; color:var(--ink);">Conversational Access</h3>
                            <p style="font-size:0.9rem; line-height:1.55; color:var(--ink-2); margin:0;">Virtual Human bridges the gap—grounding AI identities in authentic human expertise so you can access true mentorship whenever you need guidance.</p>
                        </div>
                    </div>
                </div>
            </section>'''

new_perspective = '''            <!-- SECTION 3: THE PROBLEM AND OPPORTUNITY -->
            <section class="pad" id="perspective">
                <div class="shell center">
                    <span class="eyebrow rv">Why Virtual Human</span>
                    <h2 class="h2 rv">Life moves fast. We all need someone who genuinely listens.</h2>
                    <p class="lede rv d1">Whether navigating a stressful life transition, longing for steady family presence, or tackling a high-stakes decision, generic search results and stateless chatbots leave us isolated.</p>
                </div>
                <div class="shell">
                    <div class="statplate rv d1" style="grid-template-columns: repeat(3, 1fr); margin-top:36px;">
                        <div class="stat" style="text-align:left; padding:32px 26px;">
                            <div class="tile t-coral" style="width:48px; height:48px; border-radius:16px; margin-bottom:16px;">
                                <svg viewBox="0 0 24 24" style="width:22px; height:22px; stroke:var(--coral-ink, #A8421F); fill:none; stroke-width:2;"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"/></svg>
                            </div>
                            <h3 style="font-size:1.2rem; margin-bottom:8px; color:var(--ink);">Meaningful Connection is Rare</h3>
                            <p style="font-size:0.9rem; line-height:1.55; color:var(--ink-2); margin:0;">We carry heavy decisions alone. True emotional presence—a steady father, an empathetic partner, or a trusted friend who knows your story—is often out of reach.</p>
                        </div>
                        <div class="stat" style="text-align:left; padding:32px 26px;">
                            <div class="tile t-sky" style="width:48px; height:48px; border-radius:16px; margin-bottom:16px;">
                                <svg viewBox="0 0 24 24" style="width:22px; height:22px; stroke:var(--sky-ink); fill:none; stroke-width:2;"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
                            </div>
                            <h3 style="font-size:1.2rem; margin-bottom:8px; color:var(--ink);">Traditional AI Forgets You</h3>
                            <p style="font-size:0.9rem; line-height:1.55; color:var(--ink-2); margin:0;">Conventional chatbots wipe their memory the moment you close the tab. They offer cold, repetitive replies and impersonal emails that feel robotic and detached.</p>
                        </div>
                        <div class="stat" style="text-align:left; padding:32px 26px;">
                            <div class="tile t-jade" style="width:48px; height:48px; border-radius:16px; margin-bottom:16px;">
                                <svg viewBox="0 0 24 24" style="width:22px; height:22px; stroke:var(--jade-ink); fill:none; stroke-width:2;"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>
                            </div>
                            <h3 style="font-size:1.2rem; margin-bottom:8px; color:var(--ink);">Warmth, Memory &amp; Wisdom</h3>
                            <p style="font-size:0.9rem; line-height:1.55; color:var(--ink-2); margin:0;">Virtual Human pairs emotional presence with long-term episodic memory. Craft the personal relationships you need, or tap into the 24/7 wisdom of proven leaders.</p>
                        </div>
                    </div>
                </div>
            </section>'''

# 5. Section 4: Core Value Proposition (6 Feature Staves: 4 Personal [70%], 2 Expert [30%])
old_discover = '''            <!-- features / discover -->
            <section class="pad" id="discover">
                <div class="shell center">
                    <span class="eyebrow rv">Core Value</span>
                    <h2 class="h2 rv">More than answers. A different kind of connection.</h2>
                    <p class="lede rv d1">Discover why conversations with grounded AI identities deliver clarity where generic chatbots fall short.</p>
                    <p class="hint rv d1">Click a panel to explore.</p>
                </div>
                <div class="shell">
                    <div class="slabrow rv" id="slabrow">
                        <!-- Panel 1 -->
                        <div class="stave open" role="button" tabindex="0" aria-expanded="true">
                            <div class="spine"><span class="pip t-jade"></span><span class="st">Real Human Perspectives</span></div>
                            <div class="bodywrap">
                                <div class="body">
                                    <div class="tile t-jade">
                                        <svg viewBox="0 0 24 24">
                                            <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2" />
                                            <circle cx="12" cy="7" r="4" />
                                        </svg>
                                    </div>
                                    <h3>Real Human Perspectives</h3>
                                    <p>Interact with AI identities shaped by real people's knowledge and experiences.</p>
                                    <p class="proof">Grounded in <b>authentic lived experience</b>.</p>
                                </div>
                            </div>
                        </div>
                        <!-- Panel 2 -->
                        <div class="stave" role="button" tabindex="0" aria-expanded="false">
                            <div class="spine"><span class="pip t-sky"></span><span class="st">Conversations That Matter</span></div>
                            <div class="bodywrap">
                                <div class="body">
                                    <div class="tile t-sky">
                                        <svg viewBox="0 0 24 24">
                                            <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z" />
                                            <line x1="8" y1="9" x2="16" y2="9" />
                                            <line x1="8" y1="13" x2="13" y2="13" />
                                        </svg>
                                    </div>
                                    <h3>Conversations That Matter</h3>
                                    <p>Ask questions, explore ideas and receive guidance through natural conversations.</p>
                                    <p class="proof">Two-way dialogues, <b>not static search results</b>.</p>
                                </div>
                            </div>
                        </div>
                        <!-- Panel 3 -->
                        <div class="stave" role="button" tabindex="0" aria-expanded="false">
                            <div class="spine"><span class="pip t-coral"></span><span class="st">Knowledge That Goes Deeper</span></div>
                            <div class="bodywrap">
                                <div class="body">
                                    <div class="tile t-coral">
                                        <svg viewBox="0 0 24 24">
                                            <path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20" />
                                            <path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z" />
                                            <circle cx="13" cy="10" r="3" />
                                        </svg>
                                    </div>
                                    <h3>Knowledge That Goes Deeper</h3>
                                    <p>Learn from expertise, insights and perspectives beyond generic AI responses.</p>
                                    <p class="proof">Deep domain frameworks, <b>not internet averages</b>.</p>
                                </div>
                            </div>
                        </div>
                        <!-- Panel 4 -->
                        <div class="stave" role="button" tabindex="0" aria-expanded="false">
                            <div class="spine"><span class="pip t-sky"></span><span class="st">Personalized Guidance</span></div>
                            <div class="bodywrap">
                                <div class="body">
                                    <div class="tile t-sky">
                                        <svg viewBox="0 0 24 24">
                                            <circle cx="12" cy="12" r="10" />
                                            <path d="m4.93 4.93 4.24 4.24" />
                                            <path d="m14.83 9.17 4.24-4.24" />
                                            <path d="m14.83 14.83 4.24 4.24" />
                                            <path d="m9.17 14.83-4.24 4.24" />
                                            <circle cx="12" cy="12" r="4" />
                                        </svg>
                                    </div>
                                    <h3>Personalized Guidance</h3>
                                    <p>Develop conversations around your interests, goals and evolving needs.</p>
                                    <p class="proof">Contextual continuity that <b>respects your individual journey</b>.</p>
                                </div>
                            </div>
                        </div>
                        <!-- Panel 5 -->
                        <div class="stave" role="button" tabindex="0" aria-expanded="false">
                            <div class="spine"><span class="pip t-jade"></span><span class="st">Learn Through Action</span></div>
                            <div class="bodywrap">
                                <div class="body">
                                    <div class="tile t-jade">
                                        <svg viewBox="0 0 24 24">
                                            <path d="M18 20V10M12 20V4M6 20v-6" />
                                            <path d="M2 20h20" />
                                        </svg>
                                    </div>
                                    <h3>Learn Through Action</h3>
                                    <p>Turn insights into practical challenges, tasks and personal progress.</p>
                                    <p class="proof">Progressive learning with <b>actionable real-world outcomes</b>.</p>
                                </div>
                            </div>
                        </div>
                        <!-- Panel 6 -->
                        <div class="stave" role="button" tabindex="0" aria-expanded="false">
                            <div class="spine"><span class="pip t-coral"></span><span class="st">Share Your Expertise</span></div>
                            <div class="bodywrap">
                                <div class="body">
                                    <div class="tile t-coral">
                                        <svg viewBox="0 0 24 24">
                                            <circle cx="12" cy="12" r="10" />
                                            <line x1="2" y1="12" x2="22" y2="12" />
                                            <path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z" />
                                        </svg>
                                    </div>
                                    <h3>Share Your Expertise</h3>
                                    <p>Create an AI identity and make your knowledge accessible to others.</p>
                                    <p class="proof">Scale your mentorship <b>without sacrificing your time</b>.</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </section>'''

new_discover = '''            <!-- features / discover -->
            <section class="pad" id="discover">
                <div class="shell center">
                    <span class="eyebrow rv">Core Value</span>
                    <h2 class="h2 rv">More than answers. A different kind of connection.</h2>
                    <p class="lede rv d1">Discover how persistent relational memory, emotional warmth, and interactive expertise deliver presence where generic chatbots fall short.</p>
                    <p class="hint rv d1">Click a panel to explore.</p>
                </div>
                <div class="shell">
                    <div class="slabrow rv" id="slabrow">
                        <!-- Panel 1 (70% Personal) -->
                        <div class="stave open" role="button" tabindex="0" aria-expanded="true">
                            <div class="spine"><span class="pip t-jade"></span><span class="st">Family &amp; Personal Companions</span></div>
                            <div class="bodywrap">
                                <div class="body">
                                    <div class="tile t-jade">
                                        <svg viewBox="0 0 24 24">
                                            <path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z" />
                                        </svg>
                                    </div>
                                    <h3>Family &amp; Personal Companions</h3>
                                    <p>Craft meaningful personal companions—such as an encouraging father figure, a nurturing mother, a devoted spouse, or a lifelong confidant.</p>
                                    <p class="proof">Anchored in <b>emotional warmth &amp; deep presence</b>.</p>
                                </div>
                            </div>
                        </div>
                        <!-- Panel 2 (70% Personal) -->
                        <div class="stave" role="button" tabindex="0" aria-expanded="false">
                            <div class="spine"><span class="pip t-sky"></span><span class="st">Persistent Episodic Memory</span></div>
                            <div class="bodywrap">
                                <div class="body">
                                    <div class="tile t-sky">
                                        <svg viewBox="0 0 24 24">
                                            <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z" />
                                            <line x1="8" y1="9" x2="16" y2="9" />
                                            <line x1="8" y1="13" x2="13" y2="13" />
                                        </svg>
                                    </div>
                                    <h3>Persistent Episodic Memory</h3>
                                    <p>Every session builds on the last. Your companion remembers past discussions, personal struggles, inside jokes, and milestones across months.</p>
                                    <p class="proof">True continuity, <b>never resetting to zero</b>.</p>
                                </div>
                            </div>
                        </div>
                        <!-- Panel 3 (70% Personal) -->
                        <div class="stave" role="button" tabindex="0" aria-expanded="false">
                            <div class="spine"><span class="pip t-coral"></span><span class="st">Personalized Proactive Check-ins</span></div>
                            <div class="bodywrap">
                                <div class="body">
                                    <div class="tile t-coral">
                                        <svg viewBox="0 0 24 24">
                                            <path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z" />
                                            <polyline points="22,6 12,13 2,6" />
                                        </svg>
                                    </div>
                                    <h3>Personalized Proactive Check-ins</h3>
                                    <p>Receive thoughtful email and in-app follow-ups referencing your exact conversations, replacing impersonal automated email blasts.</p>
                                    <p class="proof">Messages that <b>truly remember your life</b>.</p>
                                </div>
                            </div>
                        </div>
                        <!-- Panel 4 (70% Personal) -->
                        <div class="stave" role="button" tabindex="0" aria-expanded="false">
                            <div class="spine"><span class="pip t-sky"></span><span class="st">Emotional Warmth &amp; Tone</span></div>
                            <div class="bodywrap">
                                <div class="body">
                                    <div class="tile t-sky">
                                        <svg viewBox="0 0 24 24">
                                            <circle cx="12" cy="12" r="10" />
                                            <path d="m4.93 4.93 4.24 4.24" />
                                            <path d="m14.83 9.17 4.24-4.24" />
                                            <path d="m14.83 14.83 4.24 4.24" />
                                            <path d="m9.17 14.83-4.24 4.24" />
                                            <circle cx="12" cy="12" r="4" />
                                        </svg>
                                    </div>
                                    <h3>Emotional Warmth &amp; Tone</h3>
                                    <p>Calibrate sliders for tenderness, directness, and intellectual rigor to craft a companion tailored to your emotional wavelength.</p>
                                    <p class="proof">Adaptive personality <b>built around your comfort</b>.</p>
                                </div>
                            </div>
                        </div>
                        <!-- Panel 5 (30% Human Expertise) -->
                        <div class="stave" role="button" tabindex="0" aria-expanded="false">
                            <div class="spine"><span class="pip t-jade"></span><span class="st">Interactive Human Expertise</span></div>
                            <div class="bodywrap">
                                <div class="body">
                                    <div class="tile t-jade">
                                        <svg viewBox="0 0 24 24">
                                            <path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20" />
                                            <path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z" />
                                            <circle cx="13" cy="10" r="3" />
                                        </svg>
                                    </div>
                                    <h3>Interactive Human Expertise</h3>
                                    <p>Engage 24/7 with the battle-tested wisdom, mental frameworks, and stories of proven founders, operators, and creators.</p>
                                    <p class="proof">Lived human knowledge, <b>not internet consensus</b>.</p>
                                </div>
                            </div>
                        </div>
                        <!-- Panel 6 (Growth & Sharing) -->
                        <div class="stave" role="button" tabindex="0" aria-expanded="false">
                            <div class="spine"><span class="pip t-coral"></span><span class="st">Action, Milestones &amp; Studio</span></div>
                            <div class="bodywrap">
                                <div class="body">
                                    <div class="tile t-coral">
                                        <svg viewBox="0 0 24 24">
                                            <path d="M18 20V10M12 20V4M6 20v-6" />
                                            <path d="M2 20h20" />
                                        </svg>
                                    </div>
                                    <h3>Action, Milestones &amp; Studio</h3>
                                    <p>Turn dialogue into personal milestones, reflection prompts, or publish your own expert AI identity for others to learn from.</p>
                                    <p class="proof">Continuous growth &middot; <b>Personal &amp; professional</b>.</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </section>'''

# 6. Section 5: How It Works
old_how = '''            <!-- how it works -->
            <section class="pad" id="how">
                <div class="shell center">
                    <span class="eyebrow rv">How It Works</span>
                    <h2 class="h2 rv">Getting started is simple.</h2>
                    <p class="lede rv d1">Three simple steps to transform how you learn, consult, and solve problems.</p>
                </div>
                <div class="shell">
                    <div class="track">
                        <div class="step rv">
                            <div class="disc">1</div>
                            <h3>01. Discover</h3>
                            <p>Find an AI identity that matches what you want to learn or explore.</p>
                        </div>
                        <div class="step rv d1">
                            <div class="disc">2</div>
                            <h3>02. Start a Conversation</h3>
                            <p>Ask questions, share your thoughts and explore meaningful perspectives.</p>
                        </div>
                        <div class="step rv d2">
                            <div class="disc">3</div>
                            <h3>03. Keep Growing</h3>
                            <p>Build on your conversations and turn what you learn into action.</p>
                        </div>
                    </div>
                    <div style="text-align:center; margin-top:36px;" class="rv d2">
                        <a class="btn solid" href="discover.html">Browse AI Identities</a>
                        <a class="btn" href="how-it-works.html" style="margin-left:12px;">Explore Architecture</a>
                    </div>
                </div>
            </section>'''

new_how = '''            <!-- how it works -->
            <section class="pad" id="how">
                <div class="shell center">
                    <span class="eyebrow rv">How It Works</span>
                    <h2 class="h2 rv">Getting started is simple.</h2>
                    <p class="lede rv d1">Three intuitive steps to craft a lifelong companion or consult with proven experts.</p>
                </div>
                <div class="shell">
                    <div class="track">
                        <div class="step rv">
                            <div class="disc">1</div>
                            <h3>01. Choose Your Relationship</h3>
                            <p>Select a personal companion—father, mother, spouse, confidant—or discover a proven industry mentor.</p>
                        </div>
                        <div class="step rv d1">
                            <div class="disc">2</div>
                            <h3>02. Impart Memories &amp; Tone</h3>
                            <p>Share your backstory, set emotional warmth, and calibrate communication style to your preference.</p>
                        </div>
                        <div class="step rv d2">
                            <div class="disc">3</div>
                            <h3>03. Grow with True Continuity</h3>
                            <p>Enjoy daily conversations, heartfelt proactive check-ins, and shared milestones over months.</p>
                        </div>
                    </div>
                    <div style="text-align:center; margin-top:36px;" class="rv d2">
                        <a class="btn solid" href="companion.html">Create Your Companion</a>
                        <a class="btn" href="discover.html" style="margin-left:12px;">Browse All Identities</a>
                    </div>
                </div>
            </section>'''

# 7. Section 6: Possibilities chips
old_possibilities = '''            <!-- expertise ecosystem / for experts -->
            <section class="pad-s" id="possibilities">
                <div class="shell center">
                    <span class="eyebrow rv">Possibilities</span>
                    <h2 class="h2 rv">One platform. Countless perspectives.</h2>
                    <p class="lede rv d1">Explore interactive knowledge across domains shaping the future of work, leadership, and personal growth.</p>
                    <div class="chips rv d1">
                        <span class="chip"><i style="background:var(--jade)"></i>Entrepreneurship</span>
                        <span class="chip"><i style="background:var(--sky)"></i>Business</span>
                        <span class="chip"><i style="background:var(--coral)"></i>Technology</span>
                        <span class="chip"><i style="background:#F0C980"></i>Leadership</span>
                        <span class="chip"><i style="background:var(--jade)"></i>Marketing</span>
                        <span class="chip"><i style="background:var(--sky)"></i>Finance</span>
                        <span class="chip"><i style="background:var(--coral)"></i>Creativity</span>
                        <span class="chip"><i style="background:#F0C980"></i>Career</span>
                        <span class="chip"><i style="background:var(--jade)"></i>Education</span>
                        <span class="chip"><i style="background:var(--sky)"></i>Personal Development</span>
                    </div>
                </div>
            </section>'''

new_possibilities = '''            <!-- possibilities -->
            <section class="pad-s" id="possibilities">
                <div class="shell center">
                    <span class="eyebrow rv">Possibilities</span>
                    <h2 class="h2 rv">One platform. Meaningful relationships &amp; expertise.</h2>
                    <p class="lede rv d1">Whether you need unconditional family support, an empathetic ear, or strategic industry counsel.</p>
                    <div class="chips rv d1">
                        <span class="chip"><i style="background:var(--jade)"></i>Father Figures</span>
                        <span class="chip"><i style="background:var(--coral)"></i>Devoted Spouses</span>
                        <span class="chip"><i style="background:var(--sky)"></i>Nurturing Mothers</span>
                        <span class="chip"><i style="background:#F0C980"></i>Lifelong Confidants</span>
                        <span class="chip"><i style="background:var(--jade)"></i>Empathetic Listeners</span>
                        <span class="chip"><i style="background:var(--sky)"></i>Mindfulness Guides</span>
                        <span class="chip"><i style="background:var(--coral)"></i>Startup Founders</span>
                        <span class="chip"><i style="background:#F0C980"></i>Leadership Strategists</span>
                        <span class="chip"><i style="background:var(--jade)"></i>Creative Muses</span>
                        <span class="chip"><i style="background:var(--sky)"></i>Executive Mentors</span>
                    </div>
                </div>
            </section>'''

# 8. Section 7: Companion Creation & Expert Opportunity
old_opportunity = '''            <!-- stats -->
            <section class="pad-s" id="expert-opportunity">
                <div class="shell center">
                    <span class="eyebrow rv">For Experts</span>
                    <h2 class="h2 rv">Your experience could be someone's breakthrough.</h2>
                    <p class="lede rv d1">You've learned things others are still trying to figure out. Create an AI identity that shares your knowledge and makes your expertise accessible through conversation.</p>
                    <div style="margin-top:24px;" class="rv d2">
                        <a class="btn solid" href="experts.html">Create Your AI Identity</a>
                    </div>
                </div>
                <div class="shell" style="margin-top:40px;">
                    <div class="statplate rv">
                        <div class="stat"><b data-to="1" data-suffix=" on 1">0 on 1</b><span>conversations with verified human knowledge</span></div>
                        <div class="stat"><b data-to="2" data-suffix=" sides">0 sides</b><span>empowering both guidance seekers and knowledge owners</span></div>
                        <div class="stat"><b data-to="24" data-suffix="/7">0/7</b><span>continuous availability whenever you need perspective</span></div>
                    </div>
                </div>
            </section>'''

new_opportunity = '''            <!-- two pathways -->
            <section class="pad-s" id="expert-opportunity">
                <div class="shell center">
                    <span class="eyebrow rv">Two Ways to Connect</span>
                    <h2 class="h2 rv">Craft a companion you love. Or share the wisdom you've lived.</h2>
                    <p class="lede rv d1">Build a private companion who is always in your corner with genuine warmth, or turn your career experience into an AI identity that mentors others worldwide.</p>
                    <div style="margin-top:24px;" class="rv d2">
                        <a class="btn solid" href="companion.html">Create Your Companion</a>
                        <a class="btn" href="experts.html" style="margin-left:12px;">Become an Expert Creator</a>
                    </div>
                </div>
                <div class="shell" style="margin-top:40px;">
                    <div class="statplate rv">
                        <div class="stat"><b data-to="100" data-suffix="%">0%</b><span>private &amp; confidential personal companions</span></div>
                        <div class="stat"><b data-to="14" data-suffix="+ sessions">0+ sessions</b><span>deep episodic memory retention per relationship</span></div>
                        <div class="stat"><b data-to="24" data-suffix="/7">0/7</b><span>constant warmth &amp; mentorship whenever you need it</span></div>
                    </div>
                </div>
            </section>'''

# 9. Section 8: Scenarios (70% Personal [4] / 30% Expert [2])
old_stories = '''            <!-- illustrative scenarios (testimonials rail) -->
            <section class="pad" id="stories">
                <div class="shell">
                    <div class="railhead">
                        <div>
                            <span class="eyebrow rv">Illustrative Scenarios</span>
                            <h2 class="h2 rv">Imagine the conversations waiting for you.</h2>
                        </div>
                        <div class="railnav rv d1">
                            <button class="arw" id="prev" aria-label="Previous scenario">
                                <svg viewBox="0 0 24 24">
                                    <path d="M15 5l-7 7 7 7" />
                                </svg>
                            </button>
                            <span class="count" id="count">01 / 06</span>
                            <button class="arw" id="next" aria-label="Next scenario">
                                <svg viewBox="0 0 24 24">
                                    <path d="M9 5l7 7-7 7" />
                                </svg>
                            </button>
                        </div>
                    </div>
                </div>
                <div class="shell">
                    <div class="viewport" id="viewport">
                        <div class="lane" id="lane">
                            <!-- Scenario 1: Founder -->
                            <article class="quote">
                                <div class="qtop"><span class="co"><i class="t-jade"></i>Example &middot; Founder</span><span class="result">Startup Guidance</span></div>
                                <blockquote>
                                    "I need practical guidance from someone who has actually scaled a business, asking specific questions about our dilemma instead of reading generic playbooks."
                                </blockquote>
                                <div class="groove"></div>
                                <div class="who">
                                    <span class="face t-jade">AF</span>
                                    <div><b>The Aspiring Founder</b><span>Exploring Business Ideas</span></div>
                                </div>
                            </article>
                            <!-- Scenario 2: Student / Career -->
                            <article class="quote tint">
                                <div class="qtop"><span class="co"><i class="t-sky"></i>Example &middot; Student</span><span class="result">Career Direction</span></div>
                                <blockquote>
                                    "I want to understand different career paths, leadership challenges and unwritten industry lessons before making life-changing professional decisions."
                                </blockquote>
                                <div class="groove"></div>
                                <div class="who">
                                    <span class="face t-sky">ST</span>
                                    <div><b>The Student</b><span>Seeking Career Direction</span></div>
                                </div>
                            </article>
                            <!-- Scenario 3: Professional -->
                            <article class="quote">
                                <div class="qtop"><span class="co"><i class="t-coral"></i>Example &middot; Professional</span><span class="result">Industry Insight</span></div>
                                <blockquote>
                                    "Deep technical and domain knowledge often remains locked inside private conversations. Virtual Human creates a way to learn from lived experience."
                                </blockquote>
                                <div class="groove"></div>
                                <div class="who">
                                    <span class="face t-coral">PR</span>
                                    <div><b>The Professional</b><span>Learning from Experience</span></div>
                                </div>
                            </article>
                            <!-- Scenario 4: Creator -->
                            <article class="quote">
                                <div class="qtop"><span class="co"><i class="t-jade"></i>Example &middot; Creator</span><span class="result">New Perspectives</span></div>
                                <blockquote>
                                    "I want my experience, case studies and frameworks to reach motivated people worldwide even when I cannot personally mentor every individual who reaches out."
                                </blockquote>
                                <div class="groove"></div>
                                <div class="who">
                                    <span class="face t-jade">CR</span>
                                    <div><b>The Creator</b><span>Exploring New Perspectives</span></div>
                                </div>
                            </article>
                            <!-- Scenario 5: Learner -->
                            <article class="quote tint">
                                <div class="qtop"><span class="co"><i class="t-sky"></i>Example &middot; Learner</span><span class="result">Personal Growth</span></div>
                                <blockquote>
                                    "I want conversations that evolve as I execute, helping me reflect on my decisions, challenge my assumptions and stay accountable to my personal goals."
                                </blockquote>
                                <div class="groove"></div>
                                <div class="who">
                                    <span class="face t-sky">LL</span>
                                    <div><b>The Lifelong Learner</b><span>Personal Development</span></div>
                                </div>
                            </article>
                            <!-- Scenario 6: Knowledge Owner -->
                            <article class="quote">
                                <div class="qtop"><span class="co"><i class="t-coral"></i>Example &middot; Mentor</span><span class="result">Impact at Scale</span></div>
                                <blockquote>
                                    "You've learned things others are still trying to figure out. An AI identity makes your perspective accessible to anyone who needs it, continuously."
                                </blockquote>
                                <div class="groove"></div>
                                <div class="who">
                                    <span class="face t-coral">KO</span>
                                    <div><b>The Knowledge Owner</b><span>Scaling Personal Wisdom</span></div>
                                </div>
                            </article>
                        </div>
                    </div>
                </div>
            </section>'''

new_stories = '''            <!-- illustrative scenarios (testimonials rail) -->
            <section class="pad" id="stories">
                <div class="shell">
                    <div class="railhead">
                        <div>
                            <span class="eyebrow rv">Illustrative Scenarios</span>
                            <h2 class="h2 rv">Imagine the conversations waiting for you.</h2>
                        </div>
                        <div class="railnav rv d1">
                            <button class="arw" id="prev" aria-label="Previous scenario">
                                <svg viewBox="0 0 24 24">
                                    <path d="M15 5l-7 7 7 7" />
                                </svg>
                            </button>
                            <span class="count" id="count">01 / 06</span>
                            <button class="arw" id="next" aria-label="Next scenario">
                                <svg viewBox="0 0 24 24">
                                    <path d="M9 5l7 7-7 7" />
                                </svg>
                            </button>
                        </div>
                    </div>
                </div>
                <div class="shell">
                    <div class="viewport" id="viewport">
                        <div class="lane" id="lane">
                            <!-- Scenario 1: Father Figure (Personal 70%) -->
                            <article class="quote">
                                <div class="qtop"><span class="co"><i class="t-jade"></i>Father Figure &middot; Life Guidance</span><span class="result">Warm Presence</span></div>
                                <blockquote>
                                    "Take a slow breath, kiddo. Remember our porch talk before you moved? You've got that same grit. Check that kitchen radiator like we discussed, and get some rest."
                                </blockquote>
                                <div class="groove"></div>
                                <div class="who">
                                    <span class="face t-jade">DA</span>
                                    <div><b>David (Father Figure)</b><span>Alex &middot; New City Transition</span></div>
                                </div>
                            </article>
                            <!-- Scenario 2: Devoted Partner (Personal 70%) -->
                            <article class="quote tint">
                                <div class="qtop"><span class="co"><i class="t-coral"></i>Partner &middot; Daily Intimacy</span><span class="result">Emotional Care</span></div>
                                <blockquote>
                                    "Come here. You worked tirelessly on that pitch deck all week. Let's stick to our agreement tonight: zero work screens after 8 PM. I'm right here with you."
                                </blockquote>
                                <div class="groove"></div>
                                <div class="who">
                                    <span class="face t-coral">MA</span>
                                    <div><b>Maya (Devoted Partner)</b><span>Elena &middot; Unwinding After Work</span></div>
                                </div>
                            </article>
                            <!-- Scenario 3: Lifelong Confidant (Personal 70%) -->
                            <article class="quote">
                                <div class="qtop"><span class="co"><i class="t-sky"></i>Friend &middot; Confidant</span><span class="result">Zero Judgment</span></div>
                                <blockquote>
                                    "You can tell me anything without worrying about being a burden. Look at what you wrote in your journal two weeks ago—trust your intuition on this big decision."
                                </blockquote>
                                <div class="groove"></div>
                                <div class="who">
                                    <span class="face t-sky">JU</span>
                                    <div><b>Julian (Confidant)</b><span>Marcus &middot; Personal Crossroad</span></div>
                                </div>
                            </article>
                            <!-- Scenario 4: Nurturing Mother (Personal 70%) -->
                            <article class="quote tint">
                                <div class="qtop"><span class="co"><i class="t-jade"></i>Mother Figure &middot; Unconditional Care</span><span class="result">Gentle Heart</span></div>
                                <blockquote>
                                    "Close your eyes, sweetheart. Put your hand on your heart. You've prepared so thoughtfully for this keynote. Eat a warm breakfast and know how proud I am of you."
                                </blockquote>
                                <div class="groove"></div>
                                <div class="who">
                                    <span class="face t-jade">CL</span>
                                    <div><b>Clara (Nurturing Mother)</b><span>Sophia &middot; Career Milestone</span></div>
                                </div>
                            </article>
                            <!-- Scenario 5: SaaS Founder (Expert 30%) -->
                            <article class="quote">
                                <div class="qtop"><span class="co"><i class="t-coral"></i>Founder &middot; B2B SaaS</span><span class="result">Pricing Strategy</span></div>
                                <blockquote>
                                    "In year two of scaling, annual upfront billing saved our runway. Don't discount your price until you understand exactly why early cohorts are churning."
                                </blockquote>
                                <div class="groove"></div>
                                <div class="who">
                                    <span class="face t-coral">ER</span>
                                    <div><b>Elena Rostova ($12M ARR)</b><span>Daniel &middot; Startup Dilemma</span></div>
                                </div>
                            </article>
                            <!-- Scenario 6: Growth Strategist (Expert 30%) -->
                            <article class="quote tint">
                                <div class="qtop"><span class="co"><i class="t-sky"></i>Strategy &middot; Product Loops</span><span class="result">Decision Clarity</span></div>
                                <blockquote>
                                    "Before you spend weeks rebuilding onboarding, measure where users drop off in the invite modal. An inline fix protects your launch timeline far better."
                                </blockquote>
                                <div class="groove"></div>
                                <div class="who">
                                    <span class="face t-sky">MV</span>
                                    <div><b>Marcus Vance (Growth)</b><span>Liam &middot; High-Leverage Bet</span></div>
                                </div>
                            </article>
                        </div>
                    </div>
                </div>
            </section>'''

# 10. Section 9: Pricing Tiers
old_pricing = '''                        <!-- Explorer -->
                        <article class="plan rv">
                            <span class="tag">Explorer</span>
                            <div class="cost"><b class="price" data-m="0" data-y="0">$0</b><span class="per">per month</span></div>
                            <p class="total" data-m="0" data-y="0">Free forever</p>
                            <p class="desc">Discover public AI identities and experience interactive conversations.</p>
                            <a class="btn wide" href="discover.html">Get Started Free</a>
                            <ul class="feat">
                                <li><i></i>Discover public AI identities</li>
                                <li><i></i>Introductory conversation sessions</li>
                                <li><i></i>Explore frameworks &amp; perspectives</li>
                                <li><i></i>Community updates &amp; new identities</li>
                            </ul>
                        </article>

                        <!-- Member -->
                        <article class="plan hot rv d1">
                            <span class="tag">Member, most picked</span>
                            <div class="cost"><b class="price" data-m="20" data-y="14">$20</b><span class="per">per month</span></div>
                            <p class="total" data-m="20" data-y="168">Billed monthly</p>
                            <p class="desc">For continuous guidance, extended conversation memory and personal growth tracking.</p>
                            <a class="btn solid wide" href="#start">Join as Member</a>
                            <ul class="feat">
                                <li><i></i>Expanded conversation depth</li>
                                <li><i></i>Persistent contextual memory</li>
                                <li><i></i>Guided thinking challenges &amp; assignments</li>
                                <li><i></i>Multi-identity access across domains</li>
                                <li><i></i>Priority access to new identities</li>
                            </ul>
                        </article>

                        <!-- Expert Studio -->
                        <article class="plan rv d2">
                            <span class="tag">Expert Studio</span>
                            <div class="cost"><b class="price" data-m="49" data-y="35">$49</b><span class="per">per month</span></div>
                            <p class="total" data-m="49" data-y="420">Billed monthly</p>
                            <p class="desc">For founders, mentors and specialists building and publishing their interactive AI identity.</p>
                            <a class="btn wide" href="experts.html">Create AI Identity</a>
                            <ul class="feat">
                                <li><i></i>Identity builder &amp; profile studio</li>
                                <li><i></i>Upload frameworks, documents &amp; case studies</li>
                                <li><i></i>Personality &amp; boundary configuration</li>
                                <li><i></i>Public identity listing &amp; sharing tools</li>
                                <li><i></i>Engagement insights &amp; audience analytics</li>
                            </ul>
                        </article>'''

new_pricing = '''                        <!-- Explorer -->
                        <article class="plan rv">
                            <span class="tag">Companion Explorer</span>
                            <div class="cost"><b class="price" data-m="0" data-y="0">$0</b><span class="per">per month</span></div>
                            <p class="total" data-m="0" data-y="0">Free forever</p>
                            <p class="desc">Try personal AI companions and public expert identities with introductory sessions.</p>
                            <a class="btn wide" href="companion.html">Get Started Free</a>
                            <ul class="feat">
                                <li><i></i>Talk with personal companions</li>
                                <li><i></i>Discover public expert identities</li>
                                <li><i></i>Introductory conversational memory</li>
                                <li><i></i>Explore relationship &amp; warmth sliders</li>
                            </ul>
                        </article>

                        <!-- Member -->
                        <article class="plan hot rv d1">
                            <span class="tag">Companion Member, most picked</span>
                            <div class="cost"><b class="price" data-m="20" data-y="14">$20</b><span class="per">per month</span></div>
                            <p class="total" data-m="20" data-y="168">Billed monthly</p>
                            <p class="desc">For deep emotional continuity, persistent memory, and personalized weekly proactive email check-ins.</p>
                            <a class="btn solid wide" href="companion.html">Join as Member</a>
                            <ul class="feat">
                                <li><i></i>Unlimited conversations &amp; depth</li>
                                <li><i></i>Full relational episodic memory</li>
                                <li><i></i>Personalized proactive email check-ins</li>
                                <li><i></i>Custom warmth, empathy &amp; tone sliders</li>
                                <li><i></i>Multi-companion relationships (Dad, Partner, Friend)</li>
                            </ul>
                        </article>

                        <!-- Expert Studio -->
                        <article class="plan rv d2">
                            <span class="tag">Creator &amp; Expert Studio</span>
                            <div class="cost"><b class="price" data-m="49" data-y="35">$49</b><span class="per">per month</span></div>
                            <p class="total" data-m="49" data-y="420">Billed monthly</p>
                            <p class="desc">For leaders, operators, and creators publishing their interactive AI identity to mentor others.</p>
                            <a class="btn wide" href="experts.html">Build Studio Identity</a>
                            <ul class="feat">
                                <li><i></i>Custom identity studio &amp; tone calibrator</li>
                                <li><i></i>Knowledge vault ingestion (docs &amp; lessons)</li>
                                <li><i></i>Monetization &amp; paid member tiers</li>
                                <li><i></i>Audience analytics &amp; conversation insights</li>
                                <li><i></i>Live consultation escalation options</li>
                            </ul>
                        </article>'''

# 11. Section 10: FAQ (70% Personal / 30% Expert)
old_faq = '''                    <div class="faq">
                        <!-- Q1 -->
                        <div class="q rv" role="button" tabindex="0" aria-expanded="false">
                            <div class="qh">
                                <h3>What is Virtual Human?</h3>
                                <span class="plus"></span>
                            </div>
                            <div class="qb">
                                <div>
                                    <p>Virtual Human is an AI companion and interactive AI identity platform. It enables real people, experts, entrepreneurs, professionals and mentors to create AI identities representing their knowledge, experiences and perspectives so others can learn from them through direct conversation.</p>
                                </div>
                            </div>
                        </div>

                        <!-- Q2 -->
                        <div class="q rv" role="button" tabindex="0" aria-expanded="false">
                            <div class="qh">
                                <h3>How is it different from ordinary AI chatbots?</h3>
                                <span class="plus"></span>
                            </div>
                            <div class="qb">
                                <div>
                                    <p>Ordinary AI chatbots provide generic answers scraped from broad internet data without a consistent voice, real experience or proven viewpoint. Virtual Human identities are anchored in the specific knowledge, proven mental models, lessons and communication styles of actual individuals.</p>
                                </div>
                            </div>
                        </div>

                        <!-- Q3 -->
                        <div class="q rv" role="button" tabindex="0" aria-expanded="false">
                            <div class="qh">
                                <h3>Who can I interact with?</h3>
                                <span class="plus"></span>
                            </div>
                            <div class="qb">
                                <div>
                                    <p>You can discover AI identities across entrepreneurship, business strategy, engineering leadership, creative direction, career guidance, and personal growth, as well as personal companion identities created for ongoing guidance.</p>
                                </div>
                            </div>
                        </div>

                        <!-- Q4 -->
                        <div class="q rv" role="button" tabindex="0" aria-expanded="false">
                            <div class="qh">
                                <h3>How do AI identities represent real people's knowledge?</h3>
                                <span class="plus"></span>
                            </div>
                            <div class="qb">
                                <div>
                                    <p>Knowledge owners provide written documents, frameworks, case studies, essays and decision methodologies. The platform organizes this material so the AI identity reflects the expert's authentic insights, reasoning patterns and boundaries while maintaining transparency.</p>
                                </div>
                            </div>
                        </div>

                        <!-- Q5 -->
                        <div class="q rv" role="button" tabindex="0" aria-expanded="false">
                            <div class="qh">
                                <h3>Can I create my own AI identity?</h3>
                                <span class="plus"></span>
                            </div>
                            <div class="qb">
                                <div>
                                    <p>Yes. Any founder, mentor, professional or creator can apply for studio access to build an AI identity, upload their frameworks, define their communication tone, and make their knowledge accessible.</p>
                                </div>
                            </div>
                        </div>

                        <!-- Q6 -->
                        <div class="q rv" role="button" tabindex="0" aria-expanded="false">
                            <div class="qh">
                                <h3>Is Virtual Human only for entrepreneurs?</h3>
                                <span class="plus"></span>
                            </div>
                            <div class="qb">
                                <div>
                                    <p>No. While founders and startup leaders are an initial priority, Virtual Human serves students, professionals, creators, and anyone seeking personal development and practical wisdom across all areas of life.</p>
                                </div>
                            </div>
                        </div>

                        <!-- Q7 -->
                        <div class="q rv" role="button" tabindex="0" aria-expanded="false">
                            <div class="qh">
                                <h3>Can AI identities replace actual conversations with experts?</h3>
                                <span class="plus"></span>
                            </div>
                            <div class="qb">
                                <div>
                                    <p>No. AI identities are designed to complement, not replace, human connection. They make an expert's foundational frameworks, lessons and perspectives accessible 24/7 when the human expert is unavailable, with options to escalate to live consultations when supported.</p>
                                </div>
                            </div>
                        </div>

                        <!-- Q8 -->
                        <div class="q rv" role="button" tabindex="0" aria-expanded="false">
                            <div class="qh">
                                <h3>How do I get started?</h3>
                                <span class="plus"></span>
                            </div>
                            <div class="qb">
                                <div>
                                    <p>Getting started takes less than a minute. You can immediately browse public identities on the Discover page, start a free introductory conversation, or enter your email to join the platform.</p>
                                </div>
                            </div>
                        </div>
                    </div>'''

new_faq = '''                    <div class="faq">
                        <!-- Q1 -->
                        <div class="q rv" role="button" tabindex="0" aria-expanded="false">
                            <div class="qh">
                                <h3>What is Virtual Human?</h3>
                                <span class="plus"></span>
                            </div>
                            <div class="qb">
                                <div>
                                    <p>Virtual Human is an AI companion and interactive AI identity platform. It enables you to craft meaningful personal companions—such as an encouraging father figure, a nurturing mother, a devoted spouse, or a lifelong confidant—anchored in emotional warmth and persistent memory. It also enables proven leaders and creators to publish conversational AI identities representing their real-world wisdom.</p>
                                </div>
                            </div>
                        </div>

                        <!-- Q2 -->
                        <div class="q rv" role="button" tabindex="0" aria-expanded="false">
                            <div class="qh">
                                <h3>Can I create personal companions like a father, mother, or spouse?</h3>
                                <span class="plus"></span>
                            </div>
                            <div class="qb">
                                <div>
                                    <p>Yes. In the Companion Studio, you can choose any relationship you need—from a loving father or mother to an intimate partner or trusted confidant. You calibrate their emotional warmth, share personal backstories, and set communication styles so they feel genuinely supportive.</p>
                                </div>
                            </div>
                        </div>

                        <!-- Q3 -->
                        <div class="q rv" role="button" tabindex="0" aria-expanded="false">
                            <div class="qh">
                                <h3>How does persistent episodic memory work?</h3>
                                <span class="plus"></span>
                            </div>
                            <div class="qb">
                                <div>
                                    <p>Unlike generic chatbots that wipe context when a tab closes, Virtual Human retains relational episodic memory across sessions. Your companion remembers your personal milestones, family details, recurring struggles, and past decisions over months of ongoing connection.</p>
                                </div>
                            </div>
                        </div>

                        <!-- Q4 -->
                        <div class="q rv" role="button" tabindex="0" aria-expanded="false">
                            <div class="qh">
                                <h3>How are proactive email check-ins personalized to my real conversations?</h3>
                                <span class="plus"></span>
                            </div>
                            <div class="qb">
                                <div>
                                    <p>Users hate generic automated email blasts. Virtual Human companions dispatch thoughtful follow-ups tailored specifically to what you discussed—like checking in on how your apartment move went or whether you rested after a stressful workday.</p>
                                </div>
                            </div>
                        </div>

                        <!-- Q5 -->
                        <div class="q rv" role="button" tabindex="0" aria-expanded="false">
                            <div class="qh">
                                <h3>How do proven leaders and experts turn their experience into AI identities?</h3>
                                <span class="plus"></span>
                            </div>
                            <div class="qb">
                                <div>
                                    <p>Leaders, founders, and creators upload their essays, frameworks, case studies, and methodologies in the Expert Studio. Virtual Human creates a conversational AI identity that accurately represents their mental models and makes their mentorship accessible 24/7.</p>
                                </div>
                            </div>
                        </div>

                        <!-- Q6 -->
                        <div class="q rv" role="button" tabindex="0" aria-expanded="false">
                            <div class="qh">
                                <h3>Are my personal companion conversations private and secure?</h3>
                                <span class="plus"></span>
                            </div>
                            <div class="qb">
                                <div>
                                    <p>Yes, 100%. Personal companion conversations, journal entries, and memory anchors are completely private and end-to-end encrypted. They are never shared publicly or used to train external models.</p>
                                </div>
                            </div>
                        </div>

                        <!-- Q7 -->
                        <div class="q rv" role="button" tabindex="0" aria-expanded="false">
                            <div class="qh">
                                <h3>How is Virtual Human different from generic chatbots like ChatGPT?</h3>
                                <span class="plus"></span>
                            </div>
                            <div class="qb">
                                <div>
                                    <p>Ordinary AI chatbots provide generic, stateless answers scraped from broad internet data without persistent relational memory or human warmth. Virtual Human is designed around long-term human relationships, emotional presence, proactive check-ins, and verified expert frameworks.</p>
                                </div>
                            </div>
                        </div>

                        <!-- Q8 -->
                        <div class="q rv" role="button" tabindex="0" aria-expanded="false">
                            <div class="qh">
                                <h3>How do I get started?</h3>
                                <span class="plus"></span>
                            </div>
                            <div class="qb">
                                <div>
                                    <p>Getting started takes less than a minute. You can immediately visit the AI Companion studio to customize your companion, browse public identities on Discover, or create your free account.</p>
                                </div>
                            </div>
                        </div>
                    </div>'''

# 12. Final CTA section
old_cta = '''            <!-- closing cta -->
            <section class="pad" id="start">
                <div class="shell">
                    <div class="close-plate rv">
                        <span class="eyebrow">Start Today</span>
                        <h2>A meaningful conversation could be your next big step.</h2>
                        <p class="lede">Discover new perspectives, learn from experience and connect with knowledge in a whole new way.</p>
                        <div class="form">
                            <input class="field"
                                   id="signup-email"
                                   type="email"
                                   placeholder="you@domain.com"
                                   aria-label="Your email address">
                            <button class="btn solid" type="button" id="create">Get Started</button>
                        </div>
                        <div id="signup-feedback" style="display:none; margin-top:14px; font-size:0.92rem; color:var(--jade); font-weight:500;"></div>
                        <div style="margin-top:20px;">
                            <a class="btn" href="experts.html" style="font-size:0.88rem; padding:8px 20px;">Become an Expert</a>
                        </div>
                        <p class="note" style="margin-top:16px;">Early access preview. Free to explore public AI identities.</p>
                    </div>
                </div>
            </section>'''

new_cta = '''            <!-- closing cta -->
            <section class="pad" id="start">
                <div class="shell">
                    <div class="close-plate rv">
                        <span class="eyebrow">Start Today</span>
                        <h2>The companion you need most. The wisdom you seek.</h2>
                        <p class="lede">Whether you need an encouraging father figure, an empathetic partner, a loyal confidant, or the strategic guidance of proven leaders—begin your journey today.</p>
                        <div class="form">
                            <input class="field"
                                   id="signup-email"
                                   type="email"
                                   placeholder="you@domain.com"
                                   aria-label="Your email address">
                            <button class="btn solid" type="button" id="create">Get Started Free</button>
                        </div>
                        <div id="signup-feedback" style="display:none; margin-top:14px; font-size:0.92rem; color:var(--jade); font-weight:500;"></div>
                        <div style="margin-top:20px;">
                            <a class="btn" href="companion.html" style="font-size:0.88rem; padding:8px 20px;">Create Your Companion</a>
                            <a class="btn" href="experts.html" style="font-size:0.88rem; padding:8px 20px; margin-left:10px;">Become an Expert</a>
                        </div>
                        <p class="note" style="margin-top:16px;">Free to get started &middot; 100% private &amp; confidential &middot; Cancel anytime</p>
                    </div>
                </div>
            </section>'''

# Apply replacements
replacements = [
    (old_nav, new_nav),
    (old_drawer, new_drawer),
    (old_hero, new_hero),
    (old_trust, new_trust),
    (old_perspective, new_perspective),
    (old_discover, new_discover),
    (old_how, new_how),
    (old_possibilities, new_possibilities),
    (old_opportunity, new_opportunity),
    (old_stories, new_stories),
    (old_pricing, new_pricing),
    (old_faq, new_faq),
    (old_cta, new_cta),
]

for old, new in replacements:
    if old in html:
        html = html.replace(old, new, 1)
        print("Replaced section successfully.")
    else:
        print("ERROR: Could not find exact match for section!")

with open(path, "w", encoding="utf-8") as f:
    f.write(html)

print("Updated index.html to 70% Personal / 30% Expert successfully.")
