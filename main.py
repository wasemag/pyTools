import os
from bs4 import BeautifulSoup
import markdownify
import subprocess


# Function to convert MHTML to HTML using MHTMLconverter
def convert_mhtml_to_html(mhtml_file_path, html_file_path, resources_dir):
    # Create the resources directory if it does not exist
    os.makedirs(resources_dir, exist_ok=True)

    # Command to convert MHTML to HTML
    command = [
        "python", "-m", "mhtmlconverter.cli.mhtml2html",
        "-i", mhtml_file_path,
        "-o", html_file_path,
        "-r", resources_dir
    ]
    subprocess.run(command, check=True)


# Function to convert HTML to Markdown
def convert_html_to_markdown(html_file_path, markdown_file_path):
    with open(html_file_path, 'r', encoding='utf-8', errors='ignore') as file:
        html_content = file.read()

    soup = BeautifulSoup(html_content, 'html.parser')
    markdown_content = markdownify.markdownify(str(soup), heading_style="ATX")

    with open(markdown_file_path, 'w', encoding='utf-8') as file:
        file.write(markdown_content)


# Paths for the files
mhtml_file_path = r'C:\Users\charl\OneDrive\Documents\__TANGRAM\___PARA___\2. Areas\AI Programming\RAG_references_docs\API-OpenAI-Reference-COMPLETE.mhtml'
html_file_path = r'C:\Users\charl\OneDrive\Documents\__TANGRAM\___PARA___\2. Areas\AI Programming\RAG_references_docs\API-OpenAI-Reference-COMPLETE.html'
markdown_file_path = r'C:\Users\charl\OneDrive\Documents\__TANGRAM\___PARA___\2. Areas\AI Programming\RAG_references_docs\API-OpenAI-Reference-COMPLETE.md'
resources_dir = r'C:\Users\charl\OneDrive\Documents\__TANGRAM\___PARA___\2. Areas\AI Programming\RAG_references_docs\resources'

# Convert MHTML to HTML
convert_mhtml_to_html(mhtml_file_path, html_file_path, resources_dir)

# Convert HTML to Markdown
convert_html_to_markdown(html_file_path, markdown_file_path)

print(f"Conversion complete. Markdown file saved to {markdown_file_path}")
