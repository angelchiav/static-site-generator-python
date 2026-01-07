from textnode import TextNode, TextType
from copy_static import copy_directory
from generate_page_recursive import generate_page_recursive

def main():
    copy_directory("static", "public")
    generate_page_recursive("content", "template.html", "public")

if __name__ == "__main__":
    main()