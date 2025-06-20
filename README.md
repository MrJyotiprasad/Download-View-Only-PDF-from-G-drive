# 📄 View-Only PDF Downloader from Google Drive

This is a Python script that helps you **download view-only PDF files** from Google Drive by extracting base64-encoded images from a `.har` file (captured via browser DevTools) and converting them into a **high-quality PDF**.

---

## 📦 Features

* 🧠 Automatically detects the first `.har` file in the folder
* 📸 Extracts all base64-encoded image responses
* 📁 Saves extracted images locally
* 📄 Converts all images into a single high-resolution (300 DPI) PDF
* 🧹 Option to delete extracted images after PDF is created
* ⚡ Lightweight, offline, and terminal-friendly

---

## 🧰 Requirements

Install required packages using:

```bash
pip install -r requirements.txt
```

Required modules:

* `tqdm` – for progress display
* `pillow` – for image to PDF conversion

---

## 🚀 How to Use

### 1. Capture `.har` File

* Open Google Drive in Chrome
* Inspect → Network → Refresh
* Right-click anywhere in the Network tab → "Save all as HAR with content"
* Save the `.har` file into the same folder as this script

### 2. Run the Script

```bash
python main.py
```

The script will:

* Detect the `.har` file
* Extract all base64 images
* Save them to `extracted_images/`
* Combine them into `final_high_quality_output.pdf`
* Ask if you want to delete the images

---

## 🗂️ Project Structure

```
view-only-pdf-downloader/
├── main.py
├── requirements.txt
├── readme.txt
├── README.md
```

---

## 📝 Notes

* Only processes responses with MIME type `image/*` and `base64` encoding
* Works well with scanned/view-only PDFs displayed as images
* Output PDF is suitable for printing (300 DPI)

---

## 👨‍💻 Author

**Mr. Jyotiprasad**
📺 YouTube Channel: [Gen-Z Security](https://www.youtube.com/@GenZSecurity)
🙏 Please subscribe to support more free tools and projects!

---

> ⚠️ Disclaimer: Use this script for educational purposes only. Do not use it to violate content privacy or copyright policies.
