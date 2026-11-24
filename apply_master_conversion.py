import os
import re

DIR = r"C:\Users\user\Downloads\websites\templatemo_633_celadon"
idx_path = os.path.join(DIR, "index.html")

with open(idx_path, "r", encoding="utf-8") as f:
    idx = f.read()

# 1. Update Navigation
nav_old_regex = r'<div class="shell bar">.*?</div>\s*</header>'
nav_new = '''<div class="shell bar">
                <a class="brand" href="index.html"><span class="mark" aria-hidden="true"></span>Virtual Human</a>
                <nav class="nav">
                    <a href="discover.html">Discover</a>
                    <a href="how-it-works.html">How It Works</a>
                    <a href="experts.html">For Experts</a>
                    <a href="faq.html">FAQ</a>
                </nav>
                <a class="btn solid" href="#start">Get Started</a>
                <button class="burger"
                        id="burger"
                        aria-label="Open menu"
                        aria-expanded="false"
                        aria-controls="drawer">
                    <span></span><span></span><span></span>
                </button>
            </div>
        </header>'''
idx = re.sub(nav_old_regex, nav_new, idx, flags=re.DOTALL)

# Update drawer navigation
drawer_old_regex = r'<aside class="drawer" id="drawer" aria-label="Menu">.*?</aside>'
drawer_new = '''<aside class="drawer" id="drawer" aria-label="Menu">
            <span class="dtag">Menu</span>
            <a href="discover.html">Discover</a>
            <a href="how-it-works.html">How It Works</a>
            <a href="experts.html">For Experts</a>
            <a href="faq.html">FAQ</a>
            <a class="btn solid" href="#start">Get Started</a>
        </aside>'''
idx = re.sub(drawer_old_regex, drawer_new, idx, flags=re.DOTALL)

# 2. Update Hero Section
hero_old_regex = r'<section class="hero">.*?</section>'
hero_new = '''<section class="hero">
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
idx = re.sub(hero_old_regex, hero_new, idx, flags=re.DOTALL)

# 3. Section 3: The Problem and Opportunity (replacing companion-area with Problem & Opportunity)
problem_section = '''<!-- SECTION 3: THE PROBLEM AND OPPORTUNITY -->
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

# Replace the companion-area on home with Section 3
comp_area_old = r'<!-- AI VIRTUAL COMPANION SPOTLIGHT AREA -->.*?<!-- features / discover -->'
idx = re.sub(comp_area_old, f'{problem_section}\n\n            <!-- features / discover -->', idx, flags=re.DOTALL)

# 4. Section 4: The Core Value Proposition (The 6 interactive staves)
staves_old_regex = r'<section class="pad" id="discover">.*?</section>'
staves_new = '''<section class="pad" id="discover">
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
idx = re.sub(staves_old_regex, staves_new, idx, flags=re.DOTALL)

# 5. Section 5: How It Works (Three-step process)
how_old_regex = r'<section class="pad" id="how">.*?</section>'
how_new = '''<section class="pad" id="how">
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
idx = re.sub(how_old_regex, how_new, idx, flags=re.DOTALL)

# 6. Section 6: Explore The Possibilities (Chip cluster)
chips_old_regex = r'<section class="pad-s" id="experts">.*?</section>'
chips_new = '''<section class="pad-s" id="possibilities">
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
idx = re.sub(chips_old_regex, chips_new, idx, flags=re.DOTALL)

# 7. Section 7: The Expert Opportunity
stats_old_regex = r'<section class="pad-s">\s*<div class="shell center">\s*<span class="eyebrow rv">Perspective</span>.*?</div>\s*</section>'
stats_new = '''<section class="pad-s" id="expert-opportunity">
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
idx = re.sub(stats_old_regex, stats_new, idx, flags=re.DOTALL)

# 8. Section 8: Social Proof / Illustrative Scenarios (Testimonial rail)
stories_old_regex = r'<section class="pad" id="stories">.*?</section>'
stories_new = '''<section class="pad" id="stories">
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
idx = re.sub(stories_old_regex, stories_new, idx, flags=re.DOTALL)

# 9. Section 9: Pricing / Simple Access
pricing_old_regex = r'<section class="pad" id="pricing">.*?</section>'
pricing_new = '''<section class="pad" id="pricing">
                <div class="shell center">
                    <span class="eyebrow rv">Access</span>
                    <h2 class="h2 rv">Your next conversation starts here.</h2>
                    <p class="lede rv d1">Clear, transparent access. Start for free, upgrade when you want deeper continuity, or publish your own identity.</p>
                    <div class="toggle rv d1">
                        <span class="lbl on" id="lblM">Monthly</span>
                        <div class="switch"
                             id="switch"
                             role="switch"
                             tabindex="0"
                             aria-checked="false"
                             aria-label="Switch to yearly billing">
                            <span class="knob"></span>
                        </div>
                        <span class="lbl" id="lblY">Yearly</span>
                        <span class="save">Save 30%</span>
                    </div>
                </div>
                <div class="shell">
                    <div class="plans">
                        <!-- Explorer -->
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
                        </article>
                    </div>
                    <div style="text-align:center; margin-top:28px;" class="rv d2">
                        <a class="btn" href="pricing.html">Compare All Plan Features &rarr;</a>
                    </div>
                </div>
            </section>'''
idx = re.sub(pricing_old_regex, pricing_new, idx, flags=re.DOTALL)

# 10. Section 10: FAQ (8 questions from brief)
faq_old_regex = r'<section class="pad" id="faq">.*?</section>'
faq_new = '''<section class="pad" id="faq">
                <div class="shell center">
                    <span class="eyebrow rv">Questions</span>
                    <h2 class="h2 rv">A few things you might be wondering.</h2>
                </div>
                <div class="shell">
                    <div class="faq">
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
                    </div>
                    <div style="text-align:center; margin-top:28px;" class="rv d2">
                        <a class="btn" href="faq.html">View Detailed FAQ &rarr;</a>
                    </div>
                </div>
            </section>'''
idx = re.sub(faq_old_regex, faq_new, idx, flags=re.DOTALL)

# 11. Section 11: Final Conversion Section
start_old_regex = r'<section class="pad" id="start">.*?</section>'
start_new = '''<section class="pad" id="start">
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
idx = re.sub(start_old_regex, start_new, idx, flags=re.DOTALL)

with open(idx_path, "w", encoding="utf-8") as f:
    f.write(idx)

print("Applied conversion-first master transformation to index.html successfully!")
