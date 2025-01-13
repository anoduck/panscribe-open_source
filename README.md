



PanScribe: Pandoc Templates for Standard Manuscript Format
===============================================================================

Quick and easy formatting for writers. Start with a plain text markdown-formatted file with a poem and story, and quickly create a PDF or Word doc with [Standard Manuscript Format](http://en.wikipedia.org/wiki/Standard_Manuscript_format).


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
    - ``pandoc story.md --pdf-engine=xelatex --template=story.latex --from=markdown_github+yaml_metadata_block --output=story.pdf``
    - ``pandoc poem.md --pdf-engine=xelatex --template=poem.latex --from=markdown_github+yaml_metadata_block --output=poem.pdf``
  - Word
    - ``pandoc story.md --reference-doc=story-reference.docx --from=markdown_github+yaml_metadata_block --output=manuscript.docx``
  - Open Office?
    - https://github.com/andrewheiss/Global-Pandoc-files/blob/master/templates/odt-manuscript.template


References
--------------------------------------------------------------------------------

  - http://kieranhealy.org/blog/archives/2014/01/23/plain-text/
  - http://johnmacfarlane.net/pandoc/README.html#templates
  - https://github.com/jgm/pandoc-templates
  - https://github.com/jgm/pandoc/wiki/User-contributed-templates


See Also
--------------------------------------------------------------------------------

[Palabra](https://github.com/dylan-k/palabra) is a collection of command-line scripts for writers who want to escape from Microsoft Word format.

[Bestrew](https://github.com/dylan-k/bestrew) is a simple database for writers to track their submissions for pulication.

[MyVale](https://github.com/dylan-k/MyVale) is my collection of style-guide rules to use with Vale, a grammar and style checker. One of those rulesets is called [HedgeClipper](https://github.com/dylan-k/MyVale/tree/master/styles/HedgeClipper). It helps to identify and remove overly hesitant, weaker writing.

[Textplay](https://github.com/overvale/Textplay) is a simple command-line script that converts screenplays written in Fountain formatted plain-text to HTML, XML, and FDX (Final Draft).
