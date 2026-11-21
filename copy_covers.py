import os
import shutil

src_dir = r"C:\Users\singh\Downloads\cover"
base_assets = r"C:\Users\singh\.gemini\antigravity\scratch\academic-portal\assets\pdfs"

mapping = [
    ("cover_CS2303_Development_Tools_Laboratory_Assignment.pdf", os.path.join(base_assets, "dev-tools", "cover_assignment.pdf")),
    ("cover_CS2303_Development_Tools_Laboratory_Practical.pdf", os.path.join(base_assets, "dev-tools", "cover_practical.pdf")),
    ("cover_CS2304_Data_Structures_and_Algorithms_I_Assignment.pdf", os.path.join(base_assets, "dsa", "cover_assignment.pdf")),
    ("cover_CS2304_Data_Structures_and_Algorithms_I_Practical.pdf", os.path.join(base_assets, "dsa", "cover_practical.pdf")),
    ("cover_CS2307_Digital_Logic_Design_Laboratory.pdf", os.path.join(base_assets, "dld", "cover_practical.pdf")),
    ("cover_CS2309_Principles_of_Programming_Languages_Assignment.pdf", os.path.join(base_assets, "ppl", "cover_assignment.pdf")),
    ("cover_CS2309_Principles_of_Programming_Languages_Practical.pdf", os.path.join(base_assets, "ppl", "cover_practical.pdf")),
]

for src_name, dst_path in mapping:
    full_src = os.path.join(src_dir, src_name)
    if os.path.exists(full_src):
        os.makedirs(os.path.dirname(dst_path), exist_ok=True)
        shutil.copy2(full_src, dst_path)
        print(f"Copied: {src_name} -> {dst_path}")
    else:
        print(f"Missing: {full_src}")

print("Cover pages copied successfully.")
