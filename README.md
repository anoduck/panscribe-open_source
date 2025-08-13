# PanScribe: Pandoc Templates for Writers


PanScribe is a collection of Pandoc templates and configurations designed to help writers to typeset their work quickly. Start with a plain text, markdown-formatted file: a poem or a short story. Use [pandoc](https://pandoc.org/) to create a PDF or Word doc, using [Standard Manuscript Format](http://en.wikipedia.org/wiki/Standard_Manuscript_format).

For background information about this kind of workflow, review the [wiki](https://github.com/dylan-k/panscribe/wiki).

Features:

  - **Multiple Document Types:** Supports poems, short stories, and chapbooks.
  - **Standard Manuscript Formatting:** Adheres to industry-standard formatting for literary submissions.
  - **Customizable Templates:** Easily tweakable LaTeX templates
  - **Chapbook Builder:** A Python script to compile a collection of poems or stories into a single chapbook manuscript.
  - **Word and Line Counting:** Includes Lua filters to automatically count words in stories and lines in poems.
  - **Multiple Output Formats:** Generate PDFs, Word documents, and more.


Getting Started
--------------------------------------------------------------------------------

Some setup is required, but you'll save time spent on formatting documents, so you can focus on writing, editing, or reading instead.

### Prerequisites

Before you can use PanScribe, you'll need:

  - [**Markdown**](https://www.markdownguide.org/): An archival, plain-text format for documents.
  - [**Pandoc**](https://pandoc.org/installing.html): A universal document converter.
  - [**Python**](https://www.python.org/downloads/): Required for the chapbook builder script.
  - [**LaTeX**](https://www.latex-project.org/get/): Required for creating PDF documents. We recommend [MiKTeX](https://miktex.org/) for Windows, [MacTeX](https://www.tug.org/mactex/) for macOS, or [TeX Live](https://www.tug.org/texlive/) for Linux.
  - [**Courier Prime**](https://fontain.org/courier-prime/): A free, open-source font designed for screenplays and manuscripts.

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/dylan-k/panscribe.git
    ```

2. **Place the files in the Pandoc user data directory:**

    To make the templates and other files available to Pandoc, you should store them in the Pandoc user data directory. You can find this directory by running `pandoc --version`.

      - **Windows:** `%APPDATA%\pandoc`
      - **macOS/Linux:** `~/.local/share/pandoc`

    You can either copy the files from this repository into the appropriate subdirectories (`templates`, `filters`, `defaults`) in your Pandoc user data directory, or you can create symbolic links.

    **Example: Creating a symbolic link for the templates on Windows**

    ```cmd
    mklink /D "%APPDATA%\pandoc\templates" "c:\path\to\panscribe\templates"
    ```

    **Example: Creating a symbolic link for the templates on macOS/Linux**

    ```bash
    ln -s /path/to/panscribe/templates ~/.local/share/pandoc/templates
    ```


Usage
--------------------------------------------------------------------------------

Once you have everything set up, you can use Pandoc from your terminal to convert your Markdown files.

### Formatting a Poem

To format a single poem, use the `poem.yml` defaults file:

```bash
pandoc my-poem.md --defaults=poem.yml -o my-poem.pdf
```

This will create a PDF with standard poetry manuscript formatting, including line numbers.

### Formatting a Story

To format a short story, use the `story.yml` defaults file:

```bash
pandoc my-story.md --defaults=story.yml -o my-story.pdf
```

This will create a PDF with standard prose manuscript formatting, including a word count.

### Building a Chapbook

To build a chapbook from a collection of Markdown files, you can use the `chapbook-builder.py` script.

1. **Create a main chapbook file:**

    Create a new Markdown file (e.g., `my-chapbook.md`) and add a YAML frontmatter block that lists the files you want to include in the chapbook.

    ```yaml
    ---
    title: "My Chapbook"
    author: "Your Name"
    contents:
      - poems/poem1.md
      - poems/poem2.md
      - poems/poem3.md
    ---

    This is the introduction to my chapbook.
    ```

2. **Run the chapbook builder script:**

    ```bash
    python scripts/chapbook-builder.py my-chapbook.md
    ```

    This will create a single PDF file named `chapbook-output.pdf` containing all of your poems, formatted as a chapbook manuscript.

### Creating a Word Document

To create a Word document instead of a PDF, you can specify a `.docx` output file and a reference document.

```bash
pandoc my-story.md --reference-doc=reference-story.docx -o my-story.docx
```


Customization
--------------------------------------------------------------------------------

You can customize the output by editing the files in this repository:

  - **Templates:** The `.latex` files in the `templates` directory control the overall layout and formatting of the documents.
  - **Defaults:** The `.yml` files in the `defaults` directory specify the default Pandoc options for each document type.
  - **Metadata:** The `author.yml` file in the `metadata` directory contains your author information.


Contributing
--------------------------------------------------------------------------------

Contributions are welcome! If you have any ideas for improvements or new features, please open an issue or submit a pull request.


License
--------------------------------------------------------------------------------

This project is licensed under the MIT License. See the `LICENSE` file for details.


Related Projects
--------------------------------------------------------------------------------

It's all kinda messy right now, but I use Panscribe along with a few other tools that I've built. You might like to use them too.

  - [Palabra](https://github.com/dylan-k/palabra) is a collection of command-line scripts for writers who want to escape from Microsoft Word format.
  - [Bestrew](https://github.com/dylan-k/bestrew) is a simple database for writers to track their submissions for pulication.
  - [MyVale](https://github.com/dylan-k/MyVale) is my collection of style-guide rules to use with Vale, a grammar and style checker. 
    - One of those rulesets is called [HedgeClipper](https://github.com/dylan-k/MyVale/tree/master/styles/HedgeClipper). It helps to identify and remove overly hesitant, weaker writing.
