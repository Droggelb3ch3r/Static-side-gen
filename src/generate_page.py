
import os
import shutil
from md_to_html_node import markdown_to_html_node

def copy_static_to_public():
    # Copy static files from the 'static' directory to the 'public' directory
    static_dir = "static"
    output_dir = "public"
    path = os.path.join(os.getcwd(), static_dir)
    print(f"Copying static files from {path} to {output_dir}...")

    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)
        #löschen des public ordners, damit die alten dateien nicht mehr da sind, sonst werden sie nicht überschrieben
    os.makedirs(output_dir)

    #shutil.copytree(static_dir, output_dir, dirs_exist_ok=True) << Die leichte variante, ist aber in der Aufgabe nicht erlaubt, daher die manuelle Variante:
    for root, dirs, files in os.walk(static_dir):
        for file in files:
            src_file = os.path.join(root, file)
            relative_path = os.path.relpath(src_file, static_dir)
            dest_file = os.path.join(output_dir, relative_path)

            # Create the destination directory if it doesn't exist
            os.makedirs(os.path.dirname(dest_file), exist_ok=True)

            shutil.copy2(src_file, dest_file)
            print(f"Copied {src_file} to {dest_file}")


def extract_title(markdown):   
    # Extract the title from the markdown content
    lines = markdown.splitlines()
    for line in lines:
        if line.startswith("# "):
            return line[2:].strip()  # Return the title without the leading '# '
    raise ValueError("No title found in the markdown content")


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} using template {template_path} to {dest_path}...")
    # Read the markdown content from the source file
    with open(from_path, 'r', encoding='utf-8') as f:
        markdown_content = f.read()
    with open(template_path, 'r', encoding='utf-8') as f:
        template_content = f.read()
    html_content = markdown_to_html_node(markdown_content).to_html()
    title = extract_title(markdown_content)
    # Replace the placeholders in the template with the actual content
    final_content = (
        template_content
        .replace("{{ Title }}", title)
        .replace("{{ Content }}", html_content)
        .replace("{{ title }}", title)
        .replace("{{ content }}", html_content)
    )
    # Write the final content to the destination file
    with open(dest_path, 'w', encoding='utf-8') as f:
        f.write(final_content)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    # Generate pages recursively for all markdown files in the content directory
    for root, dirs, files in os.walk(dir_path_content):
        for file in files:
            if file.endswith(".md"):
                from_path = os.path.join(root, file)
                relative_path = os.path.relpath(from_path, dir_path_content)
                dest_path = os.path.join(dest_dir_path, relative_path[:-3] + ".html")  # Change .md to .html
                os.makedirs(os.path.dirname(dest_path), exist_ok=True)  # Create destination directory if it doesn't exist
                generate_page(from_path, template_path, dest_path)