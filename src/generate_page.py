from markdown_to_html_node import markdown_to_html_node
from extract_title import extract_title

# Print a message like "Generating page from from_path to dest_path using template_path". ✔️

# Read the markdown file at from_path and store the contents in a variable. ✔️

# Read the template file at template_path and store the contents in a variable. ✔️

# Use your markdown_to_html_node function and .to_html() method to convert the markdown file to an HTML string. ✔️

# Use the extract_title function to grab the title of the page. ✔️

# Replace the {{ Title }} and {{ Content }} placeholders in the template with the HTML and title you generated. ✔️

# TODO: Write the new full HTML page to a file at dest_path. Be sure to create any necessary directories if they don't exist.
# TODO: Write tests for generate_page


def generate_page(from_path, template_path, dest_path):
    print("-----GENERATING HTML-----")
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path) as f:
        content = f.read()
    with open(template_path) as f:
        template = f.read()
    title = extract_title(content) 
    to_html = markdown_to_html_node(content).to_html()
    html = template.replace("{{ Title }}", title).replace("{{ Content }}", to_html)
    with open("./static/index.html", "w") as f:
        f.write(html)


if __name__ == "__main__":
    from_path = "./src/content/index.md"
    template_path = "./template.html"
    dest_path = "./static/"

    generate_page(from_path, template_path, dest_path)
