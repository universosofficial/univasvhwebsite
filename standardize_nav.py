import glob, re, os

DIR = r"C:\Users\user\Downloads\websites\templatemo_633_celadon"

pages = ["index.html", "discover.html", "how-it-works.html", "experts.html", "pricing.html", "faq.html", "companion.html"]

for fname in pages:
    fpath = os.path.join(DIR, fname)
    if not os.path.exists(fpath): continue
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Standardize navigation to: AI Companion, Discover, How It Works, For Experts, FAQ + CTA
    nav_html = f'''<nav class="nav">
                    <a href="companion.html"{' class="active"' if fname == "companion.html" else ""}>AI Companion</a>
                    <a href="discover.html"{' class="active"' if fname == "discover.html" else ""}>Discover</a>
                    <a href="how-it-works.html"{' class="active"' if fname == "how-it-works.html" else ""}>How It Works</a>
                    <a href="experts.html"{' class="active"' if fname == "experts.html" else ""}>For Experts</a>
                    <a href="faq.html"{' class="active"' if fname == "faq.html" else ""}>FAQ</a>
                </nav>'''
    
    content = re.sub(r'<nav class="nav">.*?</nav>', nav_html, content, flags=re.DOTALL)
    
    drawer_html = f'''<aside class="drawer" id="drawer" aria-label="Menu">
            <span class="dtag">Menu</span>
            <a href="companion.html">AI Companion</a>
            <a href="discover.html">Discover</a>
            <a href="how-it-works.html">How It Works</a>
            <a href="experts.html">For Experts</a>
            <a href="faq.html">FAQ</a>
            <a class="btn solid" href="index.html#start">Get Started</a>
        </aside>'''
    content = re.sub(r'<aside class="drawer" id="drawer" aria-label="Menu">.*?</aside>', drawer_html, content, flags=re.DOTALL)
    
    with open(fpath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Standardized nav in {fname}")

print("All navigation successfully updated with AI Companion across all pages!")
