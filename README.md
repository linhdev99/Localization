# 🌐 Localization Character Extractor

This tool reads a multilingual CSV file and extracts all unique characters from each language column. It generates a separate `.txt` file for each language — useful for font preparation (e.g., TextMeshPro in Unity).

---

## 📁 Input Format

A typical `localization.csv` file should look like this:

| Keys       | English   | Vietnamese | Japanese  | ... |
|------------|-----------|------------|-----------|-----|
| hello      | Hello     | Xin chào   | こんにちは | ... |
| goodbye    | Goodbye   | Tạm biệt   | さようなら | ... |
| ...        | ...       | ...        | ...       | ... |

Each column (excluding `Keys`) represents one language.

---

## 🚀 How to Use

### 1. Install Python (if not already)

You can download from [https://www.python.org](https://www.python.org)

---

### 2. Place your CSV file

Put your `localization.csv` (or any `.csv` file) in the same folder as the script.

---

### 3. Run the Script

```bash
python main.py
