import os

DIR = r"C:\Users\user\Downloads\websites\templatemo_633_celadon"

rule = """
/* Reset playful organic stagger jitter for chips inside cards */
.plan .chips .chip,
.plan .chip,
.identity-card .chips .chip {
    transform: none !important;
}
.plan .chips .chip:hover,
.plan .chip:hover,
.identity-card .chips .chip:hover {
    transform: translateY(-2px) !important;
}
"""

# Update CSS
css_path = os.path.join(DIR, "templatemo-633-celadon-style.css")
with open(css_path, "r", encoding="utf-8") as f:
    css = f.read()

if "/* Reset playful organic stagger jitter" not in css:
    css += rule
    with open(css_path, "w", encoding="utf-8") as f:
        f.write(css)
    print("Updated CSS with jitter reset")

# Update HTML files
for fname in ["companion.html", "discover.html", "index.html", "pricing.html", "how-it-works.html", "experts.html", "faq.html"]:
    fpath = os.path.join(DIR, fname)
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
    if "/* Reset playful organic stagger jitter" not in content and "</style>" in content:
        content = content.replace("</style>", f"{rule}\n        </style>")
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated {fname}")

print("Stagger jitter reset applied everywhere!")
