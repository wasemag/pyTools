import os
import email
from bs4 import BeautifulSoup
import markdownify


# Step 1: Convert MHTML to HTML
def convert_mhtml_to_html(mhtml_file_path, html_file_path):
    if not os.path.exists(mhtml_file_path):
        print(f"Error: MHTML file '{mhtml_file_path}' not found.")
        return False

    with open(mhtml_file_path, 'r', encoding='utf-8', errors='ignore') as file:
        mhtml_content = file.read()

    msg = email.message_from_string(mhtml_content)
    html_content = None
    for part in msg.walk():
        if part.get_content_type() == "text/html":
            html_content = part.get_payload(decode=True)
            break

    if html_content is None:
        print("Error: No HTML content found in the MHTML file.")
        return False

    with open(html_file_path, 'wb') as file:
        file.write(html_content)

    print("Step 1: MHTML to HTML conversion complete.")
    return True


# Step 2: Convert HTML to Markdown
def convert_html_to_markdown(html_file_path, markdown_file_path):
    if not os.path.exists(html_file_path):
        print(f"Error: HTML file '{html_file_path}' not found.")
        return False

    with open(html_file_path, 'r', encoding='utf-8', errors='ignore') as file:
        html_content = file.read()

    if not html_content:
        print("Error: HTML content is empty.")
        return False

    soup = BeautifulSoup(html_content, 'html.parser')
    markdown_content = markdownify.markdownify(str(soup), heading_style="ATX")

    with open(markdown_file_path, 'w', encoding='utf-8') as file:
        file.write(markdown_content)

    print("Step 2: HTML to Markdown conversion complete.")
    return True


# Paths for the files
mhtml_file_path = r'C:\Users\charl\OneDrive\Documents\__TANGRAM\___PARA___\2. Areas\AI Programming\RAG_references_docs\Embeddings - OpenAI API.mhtml'
html_file_path = r'C:\Users\charl\OneDrive\Documents\__TANGRAM\___PARA___\2. Areas\AI Programming\RAG_references_docs\Embeddings - OpenAI API.html'
markdown_file_path = r'C:\Users\charl\OneDrive\Documents\__TANGRAM\___PARA___\2. Areas\AI Programming\RAG_references_docs\Embeddings - OpenAI API.md'
resources_dir = r'C:\Users\charl\OneDrive\Documents\__TANGRAM\___PARA___\2. Areas\AI Programming\RAG_references_docs\resources'

# Convert MHTML to HTML
if convert_mhtml_to_html(mhtml_file_path, html_file_path):
    # Convert HTML to Markdown
    if convert_html_to_markdown(html_file_path, markdown_file_path):
        print(f"Conversion complete. Markdown file saved to {markdown_file_path}")
    else:
        print("Error during HTML to Markdown conversion.")
else:
    print("Error during MHTML to HTML conversion.")
