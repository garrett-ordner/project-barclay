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
        
        # Define a command for fetching a single verse
        texfile.write("\\newcommand{\\getBibleText}[3]{%\n")
        texfile.write("  \\ifcsname verse#1#2v#3\\endcsname%\n")
        texfile.write("    \\csname verse#1#2v#3\\endcsname%\n")
        texfile.write("  \\else%\n")
        texfile.write("    [Verse not found: #1 #2:#3]%\n")
        texfile.write("  \\fi%\n")
        texfile.write("}\n\n")
        
        # Define a command for fetching a range of verses
        texfile.write("\\newcommand{\\getBibleRange}[4]{%\n")
        texfile.write("  \\foreach \\v in {#3,...,#4} {%\n")
        texfile.write("    \\getBibleText{#1}{#2}{\\v} %\n")
        texfile.write("  }%\n")
        texfile.write("}\n\n")
        
        # Generate individual verse commands
        for row in reader:
            book = row["Book"].replace(" ", "")
            chapter = row["Chapter"]
            verse = row["Verse"]
            text = row["Text"].replace("&", "\\&")  # Escape special characters
            command = f"\\expandafter\\newcommand\\csname verse{book}{chapter}v{verse}\\endcsname{{{text}}}\n"
            texfile.write(command)
print(f"LaTeX file generated at: {output_file}")
