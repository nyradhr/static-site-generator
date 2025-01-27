from copy_src_to_dst import copy_src_to_dst
from generate_page import generate_page

def main():
    copy_src_to_dst("./static", "./public")
    generate_page("./content/index.md", "template.html", "./public/index.html")

main()
