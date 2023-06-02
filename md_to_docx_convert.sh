#!/bin/bash

# Ask for the Markdown directory
echo "Enter the full path to the directory containing the Markdown files you want to convert:"
read -r dir_path

# Ask for the output directory
echo "Enter the full path to the directory where you want to save the converted files (default: ~/Desktop/md_converted):"
read -r output_dir

# If no output directory is provided, use ~/Desktop/md_converted
if [[ -z "$output_dir" ]]; then
  output_dir="$HOME/Desktop/md_converted"
fi

# Create the output directory if it doesn't exist
mkdir -p "$output_dir"

# Call the Python script and pandoc for each .md file in the directory
for file_path in "$dir_path"/*.md; do
  converted_md_file=$(python3 md_to_docx_convert.py "$file_path" "$output_dir")

  # Get the filename without the extension
  filename=$(basename -- "${converted_md_file%.md}")

  # Use pandoc to convert the Markdown file to a .docx file in the output directory
  pandoc "$converted_md_file" -o "${output_dir}/${filename}.docx"
done

# Open the output directory in Finder
open "$output_dir"