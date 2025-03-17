# Chapbook Manuscript Generator
# Combines markdown files, then runs Pandoc.
# Usage: Run this script with the command: python build.py <input_file>

import sys  # Provides access to command-line arguments
import yaml  # Library for parsing YAML data from files
import subprocess  # Used to run external commands, like Pandoc

def read_file(file_path):
    """
    Read the entire content of a file.

    :param file_path: Path to the file to be read.
    :return: A string containing the file's content.
    """
    with open(file_path, 'r') as file:
        return file.read()

def split_frontmatter_body(content):
    """
    Split the content into YAML frontmatter and body.

    :param content: The complete text content of a markdown file.
    :return: A tuple (frontmatter, body) with separated content sections.
    """
    frontmatter, body = content.split('---', 2)[1:]
    return frontmatter, body

def parse_frontmatter(frontmatter):
    """
    Parse the YAML frontmatter string into a dictionary.

    :param frontmatter: A string containing the YAML frontmatter.
    :return: A dictionary with parsed metadata.
    """
    return yaml.safe_load(frontmatter)

def format_content(metadata, body):
    """
    Format markdown content with title and body for the main document.

    :param metadata: A dictionary with metadata such as title, author, and date.
    :param body: The main body text of the markdown file.
    :return: A formatted markdown string for the main document.
    """
    title = metadata.get('title', 'Untitled')
    author = metadata.get('author', 'Unknown')
    date = metadata.get('date', '')
    content = f"\n\n\n# {title}\n\n"
    content += body
    return content

def compile_content_bodies(contents):
    """
    Compile all content bodies from file paths in the contents list.

    :param contents: List of file paths to additional markdown content.
    :return: A string containing all compiled content bodies, marked for new pages.
    """
    content_bodies = []
    for content_file in contents:
        content_text = read_file(content_file.replace('\\', '/'))
        content_frontmatter, content_body = split_frontmatter_body(content_text)
        content_metadata = parse_frontmatter(content_frontmatter)
        content_title = content_metadata.get('title', 'Untitled')
        content_bodies.append(f"# {content_title}\n\n{content_body}")
    return "\n\n\n".join(content_bodies)

def write_temp_file(main_content, additional_content):
    """
    Write the main content and additional content to a temporary markdown file.

    :param main_content: The main section of the markdown document.
    :param additional_content: The additional contents to be appended after the main content.
    """
    with open('temp.md', 'w') as temp_file:
        temp_file.write(main_content + "\n\n\n" + additional_content)

def execute_pandoc():
    """
    Execute the Pandoc command to convert markdown to PDF.
    """
    pandoc_command = [
        'pandoc',
        '--defaults=chapbook-manuscript.yml',
        'temp.md'
    ]
    print("Running Pandoc with command:")
    print(" ".join(pandoc_command))
    subprocess.run(pandoc_command, shell=True)

def generate_pdf(input_file):
    """
    Main function to generate a PDF from the input markdown file.

    :param input_file: The path to the input markdown file.
    """
    file_content = read_file(input_file)
    frontmatter, body = split_frontmatter_body(file_content)
    metadata = parse_frontmatter(frontmatter)

    main_content = format_content(metadata, body)
    additional_content = compile_content_bodies(metadata.get('contents', []))

    write_temp_file(main_content, additional_content)
    execute_pandoc()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python build.py <input_file>")
        sys.exit(1)
    input_file = sys.argv[1]
    generate_pdf(input_file)
