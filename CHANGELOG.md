# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).


[Unreleased]
--------------------------------------------------------------------------------

  - Improved documentation
  - [Open Office export template](https://github.com/andrewheiss/Global-Pandoc-files/blob/master/templates/odt-manuscript.template)?


2025-03-14
--------------------------------------------------------------------------------

 - Add pandoc template `chapbook-manuscript.latex` for multi-poem manuscripts.
 - Experimented with [Quarto](https://quarto.org/) for chapbooks, but I didn't like being required to maintain so many extra files.
 - My first templates for pandoc and LaTeX were built using the `scrartcl` document class, becuase I had to pick something and I didn't know where to start. Some years later, I revised my templates to use the default `article` class, mostly as a learning exercise. Of the two, I thought `scrartcl` was a bit easier to work with. When it came time to build a manuscript chapbook template, I chose its sibling from the KOMA-Script bundle, `scrbook`. I might experiment with alternatives, though. The KOMA documentation is hard to work with for its unclear examples, circular rambling, and even its visual design leave a lot to be desired for writing and design. 


2025-01-12
--------------------------------------------------------------------------------

  - Project moved apart from my "Palabra" project, which remains a collection of scrips for converting away from Microsoft Word format.
  - This is now its own, distinct, repository/project, called "Panscribe" with a focus specifically on templates for converting markdown into standard manuscript format, for submissions, editing, etc.
  - I'm no longer storing my templates as part of a (private) repository of writings, so I can share the templates and their development.
  - These templates are no longer a part of my dotfiles repository, though they could be included as a submodule there.


2024-06-25
--------------------------------------------------------------------------------

  - Add pandoc template for exporting to Microsoft Word files
  - Working templates for both `poem.latex` and `story.latex`


2018-06-14
--------------------------------------------------------------------------------

  - Add `chapbook-layout.latex` template for printing a book of multiple poems


2015-01-31
-------------------------------------------------------------------------------

  - Project began as a .latex template for short stories in Standard Manuscript Format: a GitHub gist [standard-manuscript.latex](https://gist.github.com/dylan-k/c596ca65098ac3f61ce2/revisions#diff-26afb7209a0eeb6d257edf1994c569134db4ff154c6b22cb7b404184972c8add)
