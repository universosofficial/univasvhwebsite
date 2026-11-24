import os
import re

BASE_DIR = r"C:\Users\user\Downloads\websites\templatemo_633_celadon"

def process_file(fname):
    fpath = os.path.join(BASE_DIR, fname)
    if not os.path.exists(fpath):
        return
    with open(fpath, "r", encoding="utf-8") as f:
        html = f.read()

    # 1. Remove TemplateMo/Tooplate comments at top
    html = re.sub(r'<!--\s*Celadon Template\s*https://templatemo\.com/tm-633-celadon\s*-->', '', html)
    html = re.sub(r'<!--\s*Celadon Soft, a claymorphism SaaS landing template.*?attribution links kept in the footer\.\s*-->', '', html, flags=re.DOTALL)

    # 2. Remove Pricing link from footlinks-nav
    html = re.sub(r'<a\s+href="pricing\.html"[^>]*>Pricing</a>\s*', '', html)

    # 3. Remove Pricing link from top nav and drawer if present
    html = re.sub(r'<a\s+href="pricing\.html"[^>]*>Pricing</a>\s*', '', html)

    # 4. Update footlinks brand paragraph with UnivasOS LTD
    old_p1 = r'<p style="font-size:0\.88rem;\s*color:var\(--ink-2\);\s*max-width:480px;\s*margin:6px 0 0;">An interactive AI identity and companion platform making human knowledge, experience and expertise accessible through meaningful conversations\.</p>'
    new_p1 = '<p style="font-size:0.88rem; color:var(--ink-2); max-width:480px; margin:6px 0 0;">An interactive AI companion and human identity platform. Virtual Human is a subsidiary of <b>UnivasOS LTD</b>.</p>'
    html = re.sub(old_p1, new_p1, html)

    # 5. Remove TemplateMo / Tooplate credits and add UnivasOS LTD subsidiary note to footbar
    old_footbar_pattern = r'<div class="footbar">\s*<p>&copy;\s*2026\s*Virtual Human\.\s*All rights reserved\.</p>\s*<p>Design by\s*<a[^>]*>TemplateMo</a>\s*<a[^>]*>Tooplate</a></p>\s*</div>'
    new_footbar = '''<div class="footbar">
                    <p>&copy; 2026 Virtual Human. A subsidiary of UnivasOS LTD. All rights reserved.</p>
                </div>'''
    html = re.sub(old_footbar_pattern, new_footbar, html, flags=re.DOTALL)

    # Also handle if footbar was already slightly different
    html = re.sub(r'<p>Design by\s*<a[^>]*>TemplateMo</a>.*?Tooplate</a></p>', '', html, flags=re.DOTALL)
    if "UnivasOS LTD" not in html and '<div class="footbar">' in html:
        html = re.sub(
            r'<div class="footbar">\s*<p>&copy;\s*2026\s*Virtual Human\.\s*All rights reserved\.</p>',
            '<div class="footbar">\n                    <p>&copy; 2026 Virtual Human. A subsidiary of UnivasOS LTD. All rights reserved.</p>',
            html
        )

    # 6. Specific page adjustments
    if fname == "index.html":
        # Remove entire #pricing section
        html = re.sub(r'<!-- pricing -->\s*<section class="pad" id="pricing">.*?</section>', '', html, flags=re.DOTALL)
        # Change testimonial "Pricing Strategy" to "Growth Strategy"
        html = html.replace('<span class="result">Pricing Strategy</span>', '<span class="result">Growth Strategy</span>')
        # Update FAQ Q1 to mention UnivasOS LTD
        html = re.sub(
            r'(<div class="qh">\s*<h3>What is Virtual Human\?</h3>\s*<span class="plus"></span>\s*</div>\s*<div class="qb">\s*<div>\s*<p>)(Virtual Human is an interactive AI identity and companion platform)',
            r'\1Virtual Human is an interactive AI identity and companion platform developed by <b>UnivasOS LTD</b>. It',
            html
        )

    elif fname == "companion.html":
        # Update Aria prompt mentioning pricing
        html = html.replace(
            'data-user="Aria, should our team switch from per-seat to usage-based pricing before our Series A?"',
            'data-user="Aria, should our team switch from a direct sales model to product-led onboarding before our Series A?"'
        )
        html = html.replace(
            'data-memory="Anchored to Session #8 &middot; Tuesday ICP Analysis &amp; Pricing Model"',
            'data-memory="Anchored to Session #8 &middot; Tuesday ICP Analysis &amp; Go-to-Market Model"'
        )

    elif fname == "discover.html":
        # Elena's quote
        html = html.replace("pricing iterations,", "market positioning,")

    elif fname == "how-it-works.html":
        html = html.replace("or a mentor reviewing your pricing model.", "or a mentor reviewing your launch roadmap.")

    elif fname == "faq.html":
        # Update FAQ Q1 to mention UnivasOS LTD
        html = re.sub(
            r'(<div class="qh">\s*<h3>What is Virtual Human\?</h3>\s*<span class="plus"></span>\s*</div>\s*<div class="qb">\s*<div>\s*<p>)(Virtual Human is an interactive AI identity and companion platform)',
            r'\1Virtual Human is an interactive AI identity and companion platform developed and operated by <b>UnivasOS LTD</b>. It',
            html
        )

    with open(fpath, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Updated {fname}")

def replace_pricing_page():
    fpath = os.path.join(BASE_DIR, "pricing.html")
    redirect_html = """<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="refresh" content="0; url=index.html">
        <title>Virtual Human — A subsidiary of UnivasOS LTD</title>
        <script>window.location.replace("index.html");</script>
    </head>
    <body style="font-family:'Albert Sans', sans-serif; background:#F5F2EA; color:#263B35; display:flex; flex-direction:column; align-items:center; justify-content:center; height:100vh; margin:0; text-align:center;">
        <h1 style="font-weight:600; margin-bottom:12px;">Virtual Human</h1>
        <p style="color:#5E6960; margin-bottom:20px;">A subsidiary of UnivasOS LTD.</p>
        <p>Redirecting to <a href="index.html" style="color:#263B35; font-weight:600; text-decoration:underline;">Virtual Human Home</a>...</p>
    </body>
</html>
"""
    with open(fpath, "w", encoding="utf-8") as f:
        f.write(redirect_html)
    print("Replaced pricing.html with clean redirect to index.html")

if __name__ == "__main__":
    pages = ["index.html", "companion.html", "discover.html", "how-it-works.html", "experts.html", "faq.html"]
    for p in pages:
        process_file(p)
    replace_pricing_page()
