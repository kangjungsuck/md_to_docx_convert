import re
import os
from datetime import datetime
import sys
import logging

def convert_notion_footnotes(file_path, output_dir):
    # Set up the logging
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    log_file_path = os.path.join(output_dir, f'app_{timestamp}.log')
    logging.basicConfig(filename=log_file_path, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    with open(file_path, 'r') as file:
        data = file.read()
    logging.info(f"Read data from file: {file_path}")

    # Remove the unnecessary string between the Notion URL and footnote
    data = re.sub(r'\(notion:\/\/www\.notion\.so\/[^#]*#', '(notion://www.notion.so/#', data)
    logging.info(f"Removed unnecessary strings in the Notion URLs")

    # Find all footnotes and references in this file
    footnotes_and_refs = list(re.findall(r'\[\[(\d+)\]\]\(notion:\/\/www\.notion\.so\/#_ftn(ref)?\d+\)', data))
    logging.info(f"Found footnotes and references: {footnotes_and_refs}")

    for pair in footnotes_and_refs:
        if pair[1] == 'ref':  # This is the footnote
            # Replace footnote with correct Markdown syntax
            data = re.sub(r'\[\[' + pair[0] + r'\]\]\(notion:\/\/www\.notion\.so\/#_ftnref' + pair[0] + r'\)', '[^' + pair[0] + ']:', data)
            logging.info(f"Replaced footnote: {pair[0]}")
        else:  # This is the reference
            # Replace reference with correct Markdown syntax
            data = re.sub(r'\[\[' + pair[0] + r'\]\]\(notion:\/\/www\.notion\.so\/#_ftn' + pair[0] + r'\)', '[^' + pair[0] + ']', data)
            logging.info(f"Replaced reference: {pair[0]}")

    # Save to new file
    new_file_path = os.path.join(output_dir, os.path.basename(file_path).rsplit('.', 1)[0] + '_edited_' + timestamp + '.md')
    with open(new_file_path, 'w') as file:
        file.write(data)

    logging.info(f"Converted file saved as {new_file_path}")
    return new_file_path

# Use the function
md_file_path = convert_notion_footnotes(sys.argv[1], sys.argv[2])
# return md_file_path for further use in shell script
print(md_file_path)