# The relationship between R Markdown, Knitr, Pandocs, and Bookdown

# Pandocs

Pandocs is a document converter.    It can convert from a number of different markup formats to many other formats, such as `.doc`, `.pdf` etc.  

Pandocs is a command line tool with no GUI.    It is an independent piece of software, separate from R.  However, it comes bundled with R Studio because `rmarkdown` relies on it for document conversion. 

Pandocs not only converts documents, but it also adds functionality on top of the base markdown language to enable it to support more complex outputs.

# R Markdown

R Markdown is based on markdown:

### Markdown (markup language)

Markdown is a lightweight markup language with plain text formatting syntax designed so that it can be converted to HTML and many other formats. A markdown file is a plain text file that is typically given the extension `.md`.

Like other markup languages like HTML and Latex, it is completely independent from R.

There is no clearly defined Markdown standard. This has led to fragmentation as different vendors write their own variants of the language to correct flaws or add missing features.

### Markdown (R package)

[`markdown`](https://cran.r-project.org/web/packages/markdown/index.html) is an R package which converts `.Rmd` files into HTML.  It is the predecessor of [`rmarkdown`](https://cran.r-project.org/web/packages/rmarkdown/index.html), which offers much more functionality.  It is no longer recommended for use.

### R Markdown (markup language)

R Markdown is an extension of the markdown syntax.  R Markdown files are plain text files that typically have the file extension `.Rmd`.  They are written using an extension of markdown syntax that enables R code to be embedded in them in a way which can later be executed.  

Because they are expected to be processed by the `rmarkdown` package, it is possible to use [Pandocs markdown syntax](http://pandoc.org/MANUAL.html#pandocs-markdown) as part of a R markdown file.  This is an extension to the original markdown syntax that provides additional functionality like raw HTML/Latex and tables.

### R Markdown (package)

The R package `rmarkdown` is a library which proceses and converts `.Rmd` files into a number of different formats.

The core function is `rmarkdown::render` which [stands on the shoulders of pandoc](https://blog.rstudio.org/2014/06/18/r-markdown-v2/).   This function ['renders the input file to the specified output format using pandoc. If the input requires knitting then `knitr::knit` is called prior to pandoc.](https://www.rdocumentation.org/packages/rmarkdown/versions/0.1.2/topics/render?)

The RMarkdown package's aim is simply [to provide reasonably good defaults and an R-friendly interface to customize Pandoc options.](https://blog.rstudio.org/2014/06/18/r-markdown-v2/).

The YAML metadata seen at the top of RMarkdown files is specificially to pass options to `rmarkdown::render`, to guide the build process


# Knitr

Knitr takes a plain text document with embedded code, executes the code and 'knits' the results back into the document.

For for example, it converts 

- An [R Markdown (`.Rmd`)](https://github.com/yihui/knitr-examples/blob/master/001-minimal.Rmd) file into a standard markdown file (`.md`) 
- An [`.Rnw` (Sweave)](https://github.com/yihui/knitr/blob/master/inst/examples/knitr-minimal.Rnw) file into to `.tex` format.  
- An [`.Rhtml`](https://github.com/yihui/knitr-examples/blob/master/003-minimal.Rhtml) file into to html.

The core function is `knitr::knit` and by default this will look at the input document and try and guess what type it is - Rnw, Rmd etc.

This core function performs three roles:
- A source parser, which looks at the input document and detects which parts are code that the user wants to be evaluated.
- A code evaluator, which evaluates this code
- An output renderer, which writes the results of evaluation back to the document in a format which is interpretable by the raw output type.  For instance, if the input file is an `.Rmd`, the output render marks up the output of code evaluation in `.md` format.

###Converting between document formats

Knitr does _not_ convert between document formats - such as converting a `.md` into a `.html`.  It does, however, provide some convenience functions to help you use other libraries to do this.  *If you are using the `rmarkdown` package, you should ignore this functionality because it has been superceded by `rmarkdown::render`.*

An example is `knitr:knit2pdf` which will: ['Knit the input Rnw or Rrst document, and compile to PDF using texi2pdf or rst2pdf'.](https://www.rforge.net/doc/packages/knitr/knit2pdf.html)

A potential source of confusion is `knitr::knit2html`, which ["is a convenience function to knit the input markdown source and call `markdown::markdownToHTML` to convert the result to HTML."](https://rforge.net/doc/packages/knitr/knit2html.html)  This is now legacy functionality because the `markdown` package has been superceded by the `rmarkdown` package.  See [this note](https://rforge.net/doc/packages/knitr/knit2html.html).


#Bookdown

The bookdown package is built on top of R Markdown, and inherits the simplicity of the Markdown syntax , as well as the possibility of multiple types of output formats (PDF/HTML/Word/…). 

It offers features like multi-page HTML output, numbering and cross-referencing figures/tables/sections/equations, inserting parts/appendices, and imported the GitBook style (https://www.gitbook.com) to create elegant and appealing HTML book pages. 

