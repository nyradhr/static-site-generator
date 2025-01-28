from copy_src_to_dst import copy_src_to_dst
from generate_page import generate_pages_recursive

def main():
    copy_src_to_dst("./static", "./public")
    generate_pages_recursive("./content", "template.html", "./public")

main()