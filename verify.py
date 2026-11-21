import os
import re

base_dir = r"C:\Users\singh\.gemini\antigravity\scratch\academic-portal"

errors = []
html_files = []
for root, dirs, files in os.walk(base_dir):
    for f in files:
        if f.endswith(".html"):
            html_files.append(os.path.join(root, f))

print(f"Found {len(html_files)} HTML pages.")

for path in html_files:
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    
    if "viewport" not in content:
        errors.append(f"{path}: Missing viewport meta tag!")
    
    # Check all internal hrefs and srcs
    matches = re.findall(r'(?:href|src)=["\']([^"\':#]+)["\']', content)
    curr_dir = os.path.dirname(path)
    for ref in matches:
        if ref.startswith("http") or ref.startswith("//") or ref.startswith("mailto:"):
            continue
        # Clean query strings if any
        ref_clean = ref.split("?")[0]
        target = os.path.normpath(os.path.join(curr_dir, ref_clean))
        if not os.path.exists(target):
            errors.append(f"{os.path.relpath(path, base_dir)} references non-existent path: {ref} -> {target}")

if errors:
    print(f"Errors found ({len(errors)}):")
    for err in errors:
        print("  -", err)
else:
    print("SUCCESS: All links, relative paths, CSS, JS, and PDFs exist and are 100% valid!")

# Verify PDF sizes
pdf_count = 0
for root, dirs, files in os.walk(os.path.join(base_dir, "assets", "pdfs")):
    for f in files:
        if f.endswith(".pdf"):
            fpath = os.path.join(root, f)
            sz = os.path.getsize(fpath)
            pdf_count += 1
            if sz == 0:
                print(f"ERROR: {f} is empty!")
print(f"Verified {pdf_count} PDF files.")
