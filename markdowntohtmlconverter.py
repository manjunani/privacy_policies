# Python code to traverse through a folder and convert the markdown files to html files
import os
import markdown


def convert_md_to_html(md_file_path, html_file_path):
    """Convert a markdown file to an HTML file."""
    with open(md_file_path, "r", encoding="utf-8") as md_file:
        md_content = md_file.read()
        html_content = markdown.markdown(md_content)

    with open(html_file_path, "w", encoding="utf-8") as html_file:
        html_file.write(html_content)


def traverse_and_convert(folder_path):
    """Traverse through the folder and convert markdown files to HTML files."""
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".md"):
                md_file_path = os.path.join(root, file)
                html_file_path = os.path.splitext(md_file_path)[0] + ".html"
                convert_md_to_html(md_file_path, html_file_path)
                print(f"Converted: {md_file_path} to {html_file_path}")


# Replace 'your_folder_path' with the path to the folder you want to traverse
folder_path = "mosaicmerch/"
traverse_and_convert(folder_path)
