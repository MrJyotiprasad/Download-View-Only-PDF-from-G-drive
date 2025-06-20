import json
import os
import base64
from tqdm import tqdm
from PIL import Image
import shutil

# === CREDIT ===
print("=" * 60)
print("🛠️  This tool is coded by Mr Jyotiprasad")
print("📺 YouTube Channel : Gen-Z Security")
print("🙏 Please subscribe to support more such tools!")
print("=" * 60 + "\n")

# === AUTO-DETECT .HAR FILE ===
har_file = None
for file in os.listdir():
    if file.lower().endswith(".har"):
        har_file = file
        break

if not har_file:
    print("❌ No .har file found in the current directory.")
    exit()

print(f"📦 Using HAR file: {har_file}")

# === CONFIG ===
image_folder = "extracted_images"
output_pdf = "final_high_quality_output.pdf"

# === Ensure Output Folder Exists ===
os.makedirs(image_folder, exist_ok=True)

# === LOAD HAR FILE ===
with open(har_file, "r", encoding="utf-8") as file:
    har_data = json.load(file)

entries = har_data.get("log", {}).get("entries", [])
print(f"[*] Total entries in HAR: {len(entries)}")

img_count = 0

# === PARSE HAR ENTRIES AND SAVE IMAGES ===
for entry in tqdm(entries, desc="Extracting Images from HAR"):
    try:
        res = entry.get("response", {})
        content = res.get("content", {})
        mime = content.get("mimeType", "")
        encoding = content.get("encoding", "")
        raw_data = content.get("text", "")

        if "image/" in mime and encoding == "base64":
            ext = mime.split("/")[1].split(";")[0]
            img_count += 1
            file_name = f"page_{img_count:03}.{ext}"
            file_path = os.path.join(image_folder, file_name)
            with open(file_path, "wb") as out:
                out.write(base64.b64decode(raw_data))
    except Exception as e:
        print(f"[!] Error parsing entry: {e}")

print(f"\n✅ Extracted {img_count} images to: {image_folder}/")

# === CONVERT IMAGES TO PDF ===
image_files = sorted([
    f for f in os.listdir(image_folder)
    if f.lower().endswith((".jpg", ".jpeg", ".png"))
])

images = []
for file in image_files:
    img_path = os.path.join(image_folder, file)
    img = Image.open(img_path).convert("RGB")
    images.append(img)

if images:
    print(f"[*] Saving {len(images)} pages to PDF...")
    images[0].save(output_pdf, save_all=True, append_images=images[1:])
    print(f"✅ High-quality PDF created: {output_pdf}")

    # === CLEANUP OPTION ===
    clean = input("🧹 Do you want to clean extracted images? (Y/N): ").strip().lower()
    if clean != "y":
        shutil.rmtree(image_folder)
        print(f"🗑️  Deleted folder: {image_folder}")
    else:
        print(f"📁 Images retained in: {image_folder}/")

else:
    print("❌ No images found to convert.")
