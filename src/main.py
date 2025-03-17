from publicise import publicise
from generate_page import generate_page



def main():
    from_path = "./src/content/index.md"
    template_path = "./template.html"
    dest_path = "./static/"
    generate_page(from_path, template_path, dest_path)
    publicise()

if __name__ == "__main__":
    main()
