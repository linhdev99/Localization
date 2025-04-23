import csv
import os

def extract_characters_per_column(csv_file_path, output_folder):
    os.makedirs(output_folder, exist_ok=True)

    with open(csv_file_path, newline="", encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile)
        headers = next(reader)
        char_sets = [set() for _ in headers]
        for row in reader:
            for i, cell in enumerate(row):
                if i < len(char_sets):
                    char_sets[i].update(cell)
        for i, header in enumerate(headers):
            file_name = f"{header.strip()}.txt"
            file_path = os.path.join(output_folder, file_name)
            sorted_chars = sorted(char_sets[i])
            with open(file_path, "w", encoding="utf-8") as f:
                f.write("".join(sorted_chars))
            print(f"Saved {file_name} ({len(sorted_chars)} characters)")

csv_path = "localization.csv"
output_dir = "char_output"

extract_characters_per_column(csv_path, output_dir)
