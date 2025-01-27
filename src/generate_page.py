from markdown_to_htmlnode import markdown_to_htmlnode
from extract_title import extract_title
from os.path import dirname, join
from os import makedirs

def generate_page(from_path, template_path, dest_path): #check if with open works as intended
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    #extract content and title from starting path
    with open(from_path, "r", encoding="utf-8") as f:
        markdown = f.read()
    htmlnode = markdown_to_htmlnode(markdown)
    html = htmlnode.to_html()
    title = extract_title(markdown)
    #replace title and content placeholders in template
    with open(template_path, "r", encoding="utf-8") as t:
        template = t.read()
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)
    #check if dest_path exists and if not, create it
    directory = dirname(dest_path)
    if directory:
        makedirs(directory, exist_ok = True)
    else:
        dest_path = "public/" + dest_path
    with open(dest_path, "w") as d:
        d.write(template)