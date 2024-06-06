import os
import markdown
import argparse


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
                html_file_path = os.path.join(
                    folder_path, os.path.splitext(file)[0] + ".html"
                )
                convert_md_to_html(md_file_path, html_file_path)
                print(f"Converted: {md_file_path} to {html_file_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert Markdown files to HTML.")
    parser.add_argument(
        "folder_path", type=str, help="Path to the folder containing Markdown files"
    )
    args = parser.parse_args()

    traverse_and_convert(args.folder_path)
