from generate_page import copy_static_to_public, generate_pages_recursive
import sys





def main():

    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    else:
        basepath = "/"

    copy_static_to_public("static", "docs")
    generate_pages_recursive("content", "template.html", "docs", basepath)






if __name__ == "__main__":
    main()