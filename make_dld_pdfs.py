import os
from PIL import Image

dld_dir = r"C:\Users\singh\.gemini\antigravity\scratch\academic-portal\assets\pdfs\dld"
record_dir = os.path.join(dld_dir, "lab_record")

# Exp 3
exp3_dir = os.path.join(record_dir, "exp 3")
if os.path.exists(exp3_dir):
    files = sorted([os.path.join(exp3_dir, f) for f in os.listdir(exp3_dir) if f.lower().endswith(('.jpg', '.jpeg', '.png'))])
    if files:
        images = [Image.open(f).convert('RGB') for f in files]
        out_exp3 = os.path.join(dld_dir, "dld_exp3_lab_record.pdf")
        images[0].save(out_exp3, save_all=True, append_images=images[1:])
        print(f"Created {out_exp3} with {len(images)} pages.")

# Exp 4
exp4_dir = os.path.join(record_dir, "exp 4")
if os.path.exists(exp4_dir):
    files = sorted([os.path.join(exp4_dir, f) for f in os.listdir(exp4_dir) if f.lower().endswith(('.jpg', '.jpeg', '.png'))])
    if files:
        images = [Image.open(f).convert('RGB') for f in files]
        out_exp4 = os.path.join(dld_dir, "dld_exp4_lab_record.pdf")
        images[0].save(out_exp4, save_all=True, append_images=images[1:])
        print(f"Created {out_exp4} with {len(images)} pages.")

print("DLD PDF compilation complete.")
