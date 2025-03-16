# Create an extract_title(markdown) function.
# It should pull the h1 header from the markdown file (the line that starts with a single #) and return it.
# If there is no h1 header, raise an exception.
# extract_title("# Hello") should return "Hello" (strip the # and any leading or trailing whitespace)

def extract_title(md):
    split_lines = md.splitlines()
    for line in split_lines:
        if line.startswith("# "):
            return line[2:].strip()
    else:
        raise ValueError("No heading")

if __name__ == "__main__":
    file = open("./src/content/index.md").read()

    print(extract_title(file))