



PanScribe: Pandoc Templates for Standard Manuscript Format
===============================================================================

Quick formatting for writers. Start with a plain text, markdown-formatted file: a poem or a short story, and use [pandoc](https:) to quickly create a PDF or Word doc, using [Standard Manuscript Format](http://en.wikipedia.org/wiki/Standard_Manuscript_format).

Some setup is required, but you'll save time spent on formatting documents, so you can focus on writing, editing, or reading instead.

format different types of writing...
  - poem
  - story
  - novel
  - poetry collection
  - stories collection

... into standard manuscript format, in a variety of file-types:
  - PDF
  - Word
  - epub
  - mobi / kindle


GETTING STARTED
--------------------------------------------------------------------------------

You'll want to be familiar with a few **key concepts**, to begin.

  - [Markdown]([Basic writing and formatting syntax - GitHub Docs](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)) is an easy-to-read and easy-to-write syntax for writing in plain text format. There are many benefits to writing in Markdown, for example: the **Plain Text Format**: easy to use, non-proprietary, cross-platform, and archival **Minimal Workflow:** without distracting buttons to look at, or syntax to think about. **Version Control**: works seamlessly with Git for collaboration, version control, and Github for tasks, wiki...

  - [Standard Manuscript Format](http://en.wikipedia.org/wiki/Standard_Manuscript_format) is a formatting style for manuscripts of short stories, novels, poems and other literary works submitted by authors to publishers.

  - [Pandoc]([Pandoc - index](https://pandoc.org/)) is tool to efficiently convert what you've written, from one file format to another. (e.g. `.docx`, `.rtf`, `.tex`, `.html`, `.pdf`)

You'll need to **install some prerequisites** before this kit will be useful.

  - [Courier Prime](https://quoteunquoteapps.com/courierprime/) a better, free Courier font.
  - [Pandoc](https://pandoc.org/) for document conversion
  - [Xelatex](https://www.latex-project.org/get/) for typesetting, and its pacakge:
    - [sectsty](https://ctan.org/pkg/sectsty?lang=en)


INSTALLATION
--------------------------------------------------------------------------------

  - Download or `git clone` the files in this repository
  - Save (or symlink) them into your [pandoc data directory](https://pandoc.org/MANUAL.html#option--data-dir). (create it if it doesn't exist already)
    - Windows: `%APPDATA%\pandoc`
    - Mac/Unix: `$HOME/.local/share/pandoc`.

> You can find the default user data directory on your system by looking at the output of `pandoc --version`.

> Data files placed in this directory (for example, `reference.odt`, `reference.docx`, `epub.css`, `templates/`) will override pandoc's normal defaults. (Note that the user data directory is not created by pandoc, so you will need to create it yourself if you want to make use of it.)


USAGE
--------------------------------------------------------------------------------

This kit helps you transform your plain-text (Markdown) writing—such as poems, stories, or novels—into Standard Manuscript Format for a variety of output file types. Below are examples for PDF and Word. You can adapt these commands for other formats (ePub, MOBI, etc.) by changing the relevant pandoc parameters.

### Convert to PDF

for prose:

```
pandoc story.md \
  --pdf-engine=xelatex \
  --template=story.latex \
  --from=markdown_github+yaml_metadata_block \
  --output=story.pdf
```

or for verse

```
pandoc poem.md \
  --pdf-engine=xelatex \
  --template=poem.latex \
  --from=markdown_github+yaml_metadata_block \
  --output=poem.pdf

```

Breakdown of Flags:

  - `story.md`: The input Markdown file containing your story, or `poem.md` for a poem.
  - `--pdf-engine=xelatex`: Specifies the LaTeX engine; XeLaTeX is preferred if you want to use custom fonts like Courier Prime.
  - `--template=story.latex`: Points to your LaTeX template, which implements the Standard Manuscript Format.
  - `--from=markdown_github+yaml_metadata_block`: Tells Pandoc to expect GitHub-flavored Markdown with YAML metadata blocks.
  - `--output=story.pdf`: Specifies the output file name and format (PDF).

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


Resources
--------------------------------------------------------------------------------

  - [Pandoc Templates Documentation](http://johnmacfarlane.net/pandoc/README.html#templates)
  - [Official Pandoc Templates](https://github.com/jgm/pandoc-templates)
  - [Community Pandoc Templates](https://github.com/jgm/pandoc/wiki/User-contributed-templates#notable-forks-of-pandoc-templates-for-pandoctemplates)
  - [Pandoc: A Markdown publishing tool workflow | OU Libraries](https://libraries.ou.edu/content/pandoc-markdown-publishing-tool-workflow)
  - [GitHub - kjhealy/pandoc-templates: Some templates for Pandoc.](https://github.com/kjhealy/pandoc-templates)
  - [GitHub - dpwiese/.pandoc: Set of Pandoc configuration, including CSL files for references, Lua filters, and themes and templates for making Pandoc output look nice.](https://github.com/dpwiese/.pandoc)
  - [GitHub - seananderson/pandoc-template: An example manuscript setup in Pandoc](https://github.com/seananderson/pandoc-template)


References
--------------------------------------------------------------------------------

  - [A Word about Word](https://kdheepak.com/blog/writing-papers-with-markdown/#a-word-about-word)
  - [Plain Text, Papers, Pandoc](http://kieranhealy.org/blog/archives/2014/01/23/plain-text/)
  - [pandoc-novel: Markdown text to a novel in ePub and PDF.](https://github.com/jp-fosterson/pandoc-novel)
  - [Sustainable Authorship in Plain Text using Pandoc and Markdown](https://programminghistorian.org/en/lessons/sustainable-authorship-in-plain-text-using-pandoc-and-markdown)
  - Academic Writing:
    - [academic-pandoc: Framework for Academic Writing with Pandoc + Markdown](https://github.com/danprince/academic-pandoc)
    - [Git-Pandoc Academic Workflow](https://www.goodthoughts.blog/p/git-pandoc-academic-workflow)
    - [Writing Academic Papers in Markdown](https://brainbaking.com/post/2021/02/writing-academic-papers-in-markdown/)
    - [GitHub - maehr/academic-pandoc-template: Write beautifully typeset academic texts with distraction-free Markdown and Pandoc.](https://github.com/maehr/academic-pandoc-template)
    - [GitHub - pandoc-scholar/pandoc-scholar: Create beautiful and semantically meaningful articles with pandoc.](https://github.com/pandoc-scholar/pandoc-scholar)
    - [GitHub - peterdalle/academic-article-template: Templates for pandoc converting an academic article written in markdown to pdf](https://github.com/peterdalle/academic-article-template)
    - [Using Pandoc to publish a book](https://brainbaking.com/post/2020/05/using-pandoc/)


Related Projects
--------------------------------------------------------------------------------

[Palabra](https://github.com/dylan-k/palabra) is a collection of command-line scripts for writers who want to escape from Microsoft Word format.

[Bestrew](https://github.com/dylan-k/bestrew) is a simple database for writers to track their submissions for pulication.

[MyVale](https://github.com/dylan-k/MyVale) is my collection of style-guide rules to use with Vale, a grammar and style checker. One of those rulesets is called [HedgeClipper](https://github.com/dylan-k/MyVale/tree/master/styles/HedgeClipper). It helps to identify and remove overly hesitant, weaker writing.

[Textplay](https://github.com/overvale/Textplay) is a simple command-line script that converts screenplays written in Fountain formatted plain-text to HTML, XML, and FDX (Final Draft).
