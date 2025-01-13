



Pandoc Templates
===============================================================================

Quick and easy formatting for writers. Start with a plain text markdown-formatted file with a poem and story, and quickly create a PDF or Word doc with [Standard Manuscript Format](http://en.wikipedia.org/wiki/Standard_Manuscript_format).

[Markdown]() is an easy-to-read and easy-to-write syntax for writing in plain text format. It can be easily converted to a variety of output formats (e.g. `.docx`, `.rtf`, `.tex`, `.html`, `.pdf`). For that reason it's often referred to as a swiss army knife for writing. [Pandoc]() is tool to efficiently convert what you've written, from one file format to another.

There are many benefits to writing in Markdown, for example:

**Plain Text Format**: easy to use, non-proprietary, cross-platform, and archival.
**Minimal Workflow:** without distracting buttons to look at, or syntax to think about.
**Version Control**: works seamlessly with Git for collaboration, version control, and Github for tasks, wiki


GETTING STARTED
--------------------------------------------------------------------------------

There are command-line utilities and other apps you'll need to have installed before this kit will be useful.

  - [Courier Prime](https://quoteunquoteapps.com/courierprime/) a better, free Courier font.
  - [Pandoc](https://pandoc.org/) for document conversion
  - [Xelatex](https://www.latex-project.org/get/) for typesetting, and its pacakge:
    - [sectsty](https://ctan.org/pkg/sectsty?lang=en)


USAGE
--------------------------------------------------------------------------------

convert your plain-text story/poem into a variety of file types:

  - PDF
    - `pandoc story.md --pdf-engine=xelatex --template=story.latex --from=markdown_github+yaml_metadata_block --output=story.pdf`
    - `pandoc poem.md --pdf-engine=xelatex --template=poem.latex --from=markdown_github+yaml_metadata_block --output=poem.pdf`
  - Word
    - `pandoc story.md --reference-doc=story-reference.docx --from=markdown_github+yaml_metadata_block --output=manuscript.docx`
  - Open Office?
    - [Pandoc OpenOffice Template](https://github.com/andrewheiss/Global-Pandoc-files/blob/master/templates/odt-manuscript.template)


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
