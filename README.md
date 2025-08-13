



PanScribe: Pandoc Templates for Writers
===============================================================================

Quick formatting for writers. Start with a plain text, markdown-formatted file: a poem or a short story. Use [pandoc](https://pandoc.org/) to create a PDF or Word doc, using [Standard Manuscript Format](http://en.wikipedia.org/wiki/Standard_Manuscript_format).

Some setup is required, but you'll save time spent on formatting documents, so you can focus on writing, editing, or reading instead.

format different types of writing...
  - poem
  - story
  - novel
  - poetry collection (WIP)
  - stories collection (TODO)

... into standard manuscript format, in a variety of file-types:
  - PDF
  - Word
  - epub
  - mobi / kindle


USAGE
--------------------------------------------------------------------------------

This kit helps you transform your plain-text (Markdown) writing—such as poems, stories, or novels—into Standard Manuscript Format for a variety of output file types. Below are examples for PDF and Word. You can adapt these commands for other formats (ePub, MOBI, etc.) by changing the relevant pandoc parameters.

### Prose Markdown to PDF

```
pandoc story.md --pdf-engine=xelatex --template=story.latex --from=markdown_github+yaml_metadata_block --output=story.pdf
```

### Verse Markdown to PDF

```
pandoc --pdf-engine=lualatex --template=poem.latex --metadata-file=author.yml --lua-filter=linecount.lua --from=gfm+hard_line_breaks "poem.md" --output=output.pdf
```

...or, a shorter command thanks to the `defaults/poem.yml` file

```
pandoc --defaults=poem.yml "poem.md" -o output.pdf
```

Breakdown of Flags:

  - `story.md` or `poem.md`: The input Markdown file
  - `--pdf-engine=lualatex`: Specifies the LaTeX engine
  - `--template=story.latex`: Points to your LaTeX template, which implements the Standard Manuscript Format.
  - `--from=markdown_github+yaml_metadata_block`: Tells Pandoc to expect GitHub-flavored Markdown with YAML metadata blocks.
  - `--output=story.pdf`: Specifies the output file name and format (PDF).

### Chapbook to PDF


The  directory contains a script to generate a PDF chapbook from multiple markdown files using Pandoc.

Directory Structure:


```
writing/
├─ chapbooks/
│  ├─ build.py
│  ├─ chapbook1.md
│  ├─ chapbook2.md
│  └─ README.md
├─ poems/
│  ├─ poem2.md
│  ├─ poem1.md
```



### Convert to  Word

```
pandoc story.md --reference-doc=story-reference.docx --from=markdown_github+yaml_metadata_block --output=manuscript.docx
```

Pandoc supports a variety of other formats, including .epub, .mobi, and .html. Just adjust the --to or --output flags.

### Tips for Best Results

Use YAML Metadata
Include a YAML header in your Markdown (e.g., title, author) so Pandoc can automatically fill those fields in the final document.

Place Templates in Pandoc's Data Directory
If you put your LaTeX templates and Word references in Pandoc's data directory, you won't need to specify full paths each time.

Tweak As Needed
Modify .latex templates or .docx references to fine-tune margins, headers, spacing, or any other manuscript elements.

With PanScribe, you can focus on crafting your writing rather than fiddling with formatting. Happy writing!


GETTING STARTED
--------------------------------------------------------------------------------

You'll want to be familiar with a few **key concepts**, to begin.

  - [Markdown](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax), an easy-to-read and easy-to-write syntax for writing in plain text format that's non-proprietary, cross-platform, and archival, to help with re-use. collaboration, version control, and more...

  - [Standard Manuscript Format](http://en.wikipedia.org/wiki/Standard_Manuscript_format) is a formatting style for manuscripts of short stories, novels, poems and other literary works submitted by authors to publishers.

  - [Pandoc](https://pandoc.org/) is tool to efficiently convert what you've written, from one file format to another. (e.g. `.docx`, `.rtf`, `.tex`, `.html`, `.pdf`)

You'll need to **install some prerequisites** before this kit will be useful.

  - [Courier Prime](https://fontain.org/courier-prime/) a better, free Courier font. (the 2015 version is available as .otf)
  - [Pandoc](https://pandoc.org/) for document conversion
  - [lualatex](https://www.luatex.org/) for typesetting. ([docs](https://mirrors.ibiblio.org/CTAN/systems/doc/luatex/luatex.pdf))


INSTALLATION
--------------------------------------------------------------------------------

For the best experience, it's recommended to clone this repository to your main projects folder (e.g., `s:\Portfolio\panscribe`) and then create a symbolic link (symlink) from your Pandoc data directory to it. This keeps your project organized without duplicating files.

1. **Clone the repository** to your preferred location:

    ```bash
    git clone https://github.com/dylan-k/panscribe.git s:/Portfolio/panscribe
    ```

2. **Find your Pandoc data directory** by running `pandoc --version`. It will be in a location like:
    - **Windows**: `%APPDATA%\pandoc`
    - **macOS/Linux**: `~/.local/share/pandoc`

    *(If this directory doesn't exist, you'll need to create it.)*

3. **Create the symbolic link**.
    - **On Windows (in Command Prompt run as Administrator):**

        ```cmd
        mklink /D "%APPDATA%\pandoc\templates" "s:\Portfolio\panscribe\templates"
        ```

    - **On macOS/Linux:**

        ```bash
        ln -s "s:/Portfolio/panscribe/templates" "$HOME/.local/share/pandoc/templates"
        ```

By using a symlink, any updates you make in the `panscribe` repository are automatically available to Pandoc.


