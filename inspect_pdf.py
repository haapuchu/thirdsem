import os
import pypdf

pdf_path = r"C:\Users\singh\Downloads\Telegram Desktop\DLD 2nd assignment Set I & Set II.pdf"

print("Checking:", pdf_path)
print("File exists:", os.path.exists(pdf_path))
print("Size in bytes:", os.path.getsize(pdf_path))

try:
    reader = pypdf.PdfReader(pdf_path)
    print(f"Total pages: {len(reader.pages)}")
    for i, p in enumerate(reader.pages):
        print(f"\n================ PAGE {i+1} ================")
        text = p.extract_text()
        print(text if text else "[No text extracted - could be scanned image]")
except Exception as e:
    print("Error:", e)
