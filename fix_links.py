import os
import re

base_dir = r"C:\Users\singh\.gemini\antigravity\scratch\academic-portal"

updated_count = 0

for root, dirs, files in os.walk(base_dir):
    for f in files:
        if f.endswith(".html"):
            fpath = os.path.join(root, f)
            with open(fpath, "r", encoding="utf-8") as file:
                content = file.read()

            def fix_href(match):
                attr = match.group(1)
                quote = match.group(2)
                url = match.group(3)
                if url.startswith("http") or url.startswith("#") or url.startswith("mailto:") or url.startswith("tel:"):
                    return match.group(0)
                if url.endswith(".pdf") or url.endswith(".css") or url.endswith(".js") or url.endswith(".html"):
                    return match.group(0)
                if url.endswith("/"):
                    return f'{attr}={quote}{url}index.html{quote}'
                return f'{attr}={quote}{url}/index.html{quote}'

            new_content = re.sub(r'(href)=(["\'])([^"\'>]+)\2', fix_href, content)

            if new_content != content:
                with open(fpath, "w", encoding="utf-8") as file:
                    file.write(new_content)
                updated_count += 1
                print(f"Updated links in: {os.path.relpath(fpath, base_dir)}")

print(f"Total files updated: {updated_count}")
