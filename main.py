import csv
import os
import glob


def extract_chars_from_csv(file_path, char_storage):
    with open(file_path, newline="", encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile)
        headers = next(reader)

        for i, header in enumerate(headers):
            header = header.strip()
            if header not in char_storage:
                char_storage[header] = set()

        for row in reader:
            for i, cell in enumerate(row):
                if i < len(headers):
                    header = headers[i].strip()
                    char_storage[header].update(cell)


def extract_from_all_csvs(folder_path, output_dir):
    os.makedirs(output_dir, exist_ok=True)

    csv_files = glob.glob(os.path.join(folder_path, "*.csv"))
    print(f"📂 Found {len(csv_files)} CSV file(s) in '{folder_path}'.")

    char_storage = dict()

    for csv_file in csv_files:
        print(f"🔍 Reading: {os.path.basename(csv_file)}")
        extract_chars_from_csv(csv_file, char_storage)

    for header, char_set in char_storage.items():
        filename = f"{header.replace('/', '_').replace(' ', '_')}.txt"
        output_path = os.path.join(output_dir, filename)
        with open(output_path, "w", encoding="utf-8") as f:
            f.write("".join(sorted(char_set)))
        print(f"✅ Saved {filename} ({len(char_set)} characters)")


folder_with_csvs = "localization_files"
output_folder = "char_output"

extract_from_all_csvs(folder_with_csvs, output_folder)
