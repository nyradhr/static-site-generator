from markdown_to_htmlnode import markdown_to_htmlnode
from extract_title import extract_title
from os.path import dirname, isfile, isdir, join
from os import makedirs, listdir
from pathlib import Path

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, "r", encoding="utf-8") as f:
        markdown = f.read()
    htmlnode = markdown_to_htmlnode(markdown)
    html = htmlnode.to_html()
    title = extract_title(markdown)
    with open(template_path, "r", encoding="utf-8") as t:
        template = t.read()
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)
    directory = dirname(dest_path)
    if directory:
        makedirs(directory, exist_ok = True)
    else:
        dest_path = "public/" + dest_path
    with open(dest_path, "w") as d:
        d.write(template)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    if not isdir(dir_path_content):
        return
    content = listdir(dir_path_content)
    for elem in content:
        if isfile(join(dir_path_content, elem)):
            if Path(elem).suffix == ".md":
                target = Path(join(dest_dir_path, elem)).with_suffix(".html")
                generate_page(join(dir_path_content, elem), template_path, target)
        else:
            generate_pages_recursive(join(dir_path_content, elem), template_path, join(dest_dir_path, elem))