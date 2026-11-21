import os
import shutil

base_assets = r"C:\Users\singh\.gemini\antigravity\scratch\academic-portal\assets\pdfs"

copies = [
    # PPL
    (r"C:\Users\singh\Downloads\james ppl assignment.pdf", os.path.join(base_assets, "ppl", "james_ppl_assignment.pdf")),
    (r"C:\Users\singh\Downloads\ppl\lab record\ppl CPP_Lab_Record_Complete.pdf", os.path.join(base_assets, "ppl", "ppl_CPP_Lab_Record_Complete.pdf")),
    (r"C:\Users\singh\Downloads\ppl\lab record\ppl output print.pdf", os.path.join(base_assets, "ppl", "ppl_output_print.pdf")),

    # Dev Tools
    (r"C:\Users\singh\Downloads\deve tools\lab copy\adit dev tools 1 to 5 lab copy output and code.pdf", os.path.join(base_assets, "dev-tools", "adit_dev_tools_1_to_5_lab_copy_output_and_code.pdf")),
    (r"C:\Users\singh\Downloads\deve tools\lab copy\dev tools 6 7.pdf", os.path.join(base_assets, "dev-tools", "dev_tools_6_7.pdf")),
    (r"C:\Users\singh\Downloads\deve tools\lab copy\dev 6 7 output.pdf", os.path.join(base_assets, "dev-tools", "dev_6_7_output.pdf")),

    # DSA
    (r"C:\Users\singh\Downloads\dsa assignment.pdf", os.path.join(base_assets, "dsa", "dsa_assignment.pdf")),
    (r"C:\Users\singh\Downloads\dsa\lab ccopy\dsa practical.pdf", os.path.join(base_assets, "dsa", "dsa_practical.pdf")),
    (r"C:\Users\singh\Downloads\dsa\lab ccopy\Linked_List_and_C_Programs_Outputs_Only.pdf", os.path.join(base_assets, "dsa", "Linked_List_and_C_Programs_Outputs_Only.pdf")),

    # Discrete
    (r"C:\Users\singh\Downloads\discrete_assignment.pdf", os.path.join(base_assets, "discrete", "discrete_assignment.pdf")),
]

for src, dst in copies:
    if os.path.exists(src):
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        shutil.copy2(src, dst)
        print(f"Copied: {os.path.basename(src)} -> {dst}")
    else:
        print(f"NOT FOUND: {src}")

# Copy DLD lab record directory
dld_src = r"C:\Users\singh\Downloads\Telegram Desktop\dld lab record"
dld_dst = os.path.join(base_assets, "dld", "lab_record")
if os.path.exists(dld_src):
    if os.path.exists(dld_dst):
        shutil.rmtree(dld_dst)
    shutil.copytree(dld_src, dld_dst)
    print("Copied DLD lab record directory successfully.")

print("Asset copying complete.")
