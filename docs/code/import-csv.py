import csv
import os

# Define file paths
input_file = os.path.join("..", "data", "KJV.csv")
output_file = os.path.join("..", "bible", "KJV.tex")

# Open the CSV file and read its contents
with open(input_file, "r", encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    with open(output_file, "w", encoding="utf-8") as texfile:
        texfile.write("% Auto-generated file\n\n")
        # Generate individual verse commands
        for row in reader:
            book = row["Book"].replace(" ", "")
            chapter = row["Chapter"]
            verse = row["Verse"]
            text = row["Text"].replace("&", "\\&")  # Escape special characters
            command = f"\\expandafter\\newcommand\\csname verse{book}{chapter}v{verse}\\endcsname{{{text}}}\n"
            texfile.write(command)
print(f"LaTeX file generated at: {output_file}")
