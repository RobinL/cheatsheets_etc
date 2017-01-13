## Rendering a book

The signature of `bookdown::render_book` is as follows:

Render mulitple R Markdown files under the current working directory into a book. It can be used
in the RStudio IDE (specifically, the knit field in YAML).

```
bookdown::render_book(input, output_format = NULL, ..., clean = TRUE, envir = parent.frame(), 
    clean_envir = !interactive(), output_dir = NULL, new_session = NA, preview = FALSE, 
    encoding = "UTF-8")    
``` 

Full documentation is [here](https://cran.r-project.org/web/packages/bookdown/bookdown.pdf).

`input` is an input filename (or multiple filenames). If preview = TRUE, only files specified in this argument are rendered, otherwise all R Markdown files specified by the book are rendered.  

This is quite confusing because you can actually pass any string to this argument, including just '', but you can't leave it empty.  This is the function that the build command actually calls.

### Controlling which `.Rmd` files are rendered

By default, `bookdown` merges all Rmd files by the order of filenames, e.g., `01-intro.Rmd` will appear before `02-literature.Rmd`. Filenames that start with `_` are skipped.

If there exists an Rmd file named `index.Rmd`, it will always be treated as the first file 

This default behaviour is overwritten by the `rmd_files` option in `_bookdown.yml` - see below.

## YAML options for book rendering  `_bookdown.yml`

The`_bookdown.yml` file is the ['book configuration file'](https://github.com/cran/bookdown/blob/36d1b53c9436536019414e0f7c2b599fd4f42a4d/R/utils.R#L271). There is a discussion of the file [here](https://bookdown.org/yihui/bookdown/configuration.html).

I cannot figure out where options in bookdown are passed - but there is a Stackoverflow [here](http://stackoverflow.com/questions/40819213/r-bookdown-bookdown-yml) which if we're lucky will get answered.

There are many options which you can control in the `_bookdown.yml` file.  You can find what they are with [this](output) github search.

```
chapter_name: ""
repo: ""
output_dir: _book
output_dir: "./"
clean: []
rmd_files:
  html: ["index.Rmd", "abstract.Rmd", "intro.Rmd"]
  latex: ["abstract.Rmd", "intro.Rmd"]
exclude: ['other-lessons']
book_filename:
new_session:
before_chapter_script: "code/init/chapter_start.R"
after_chapter_script: "code/init/chapter_end.R"
edit:
  link: https://github.com/UW-POLS503/pols503-notes/edit/gh-pages/%s
  text: "Edit"
language:
  label:
    fig: 'Figur '
    tab: 'Tabel '
    eq: 'Equation '
    thm: 'Theorem '
    lem: 'Lemma '
    def: 'Definition '
    cor: 'Corollary '
    prp: 'Proposition '
    ex: 'Eksempel '
    proof: 'Proof. '
    remark: 'Remark. '
  ui:
    edit: Edit
    chapter: '' 
```


## YAML options for book rendering  `_output.yml`

````
bookdown::gitbook:
  css: style.css
  split_by: chapter
  config:
    toc:
      collapse: subsection
      before: |
        <li><a href="./">A Minimal Bookdown Book</a></li>
      after: |
        <li><a href="https://github.com/rstudio/bookdown" target="blank">Published with bookdown</a></li>
bookdown::pdf_book:
  includes:
    in_header: preamble.tex
  latex_engine: xelatex
  citation_package: natbib
bookdown::epub_book:
  stylesheet: style.css
````



By default, **bookdown** merges all Rmd files by the order of filenames, e.g., `01-intro.Rmd` will appear before `02-literature.Rmd`. Filenames that start with an underscore `_` are skipped. If there exists an Rmd file named `index.Rmd`, it will always be treated as the first file when merging all Rmd files. The reason for this special treatment is that the HTML file `index.html` to be generated from `index.Rmd` is usually the default index file when you view a website, e.g., you are actually browsing http://yihui.name/index.html when you open http://yihui.name/.

You can override the above behavior by including a configuration file named `_bookdown.yml`\index{\_bookdown.yml} in the book directory. It is a YAML\index{YAML} file (https://en.wikipedia.org/wiki/YAML), and R Markdown users should be familiar with this format since it is also used to write the metadata in the beginning of R Markdown documents (you can learn more about YAML in Section \@ref(r-markdown)). You can use a field named `rmd_files` to define your own list and order of Rmd files for the book. For example,

```yaml
rmd_files: ["index.Rmd", "abstract.Rmd", "intro.Rmd"]
```

In this case, **bookdown** will just use whatever you defined in this YAML field without any special treatments of `index.Rmd` or underscores. If you want both HTML and LaTeX/PDF output from the book, and use different Rmd files for HTML and LaTeX output, you may specify these files for the two output formats separately, e.g.,

```yaml
rmd_files:
  html: ["index.Rmd", "abstract.Rmd", "intro.Rmd"]
  latex: ["abstract.Rmd", "intro.Rmd"]
```


More bookdown configuration options in _bookdown.yml are explained in Section 4.4. Besides these configurations, you can also specify some Pandoc-related configurations in the YAML metadata of the first Rmd file of the book, such as the title, author, and date of the book, etc. For example:

--- 
title: "Authoring A Book with R Markdown"
author: "Yihui Xie"
date: "`r Sys.Date()`"
site: "bookdown::bookdown_site"
output:
  bookdown::gitbook: default
documentclass: book
bibliography: ["book.bib", "packages.bib"]
biblio-style: apalike
link-citations: yes
---



Here is a sample _bookdown.yml:

book_filename: "my-book.Rmd"
before_chapter_script: ["script1.R", "script2.R"]
after_chapter_script: "script3.R"
edit: https://github.com/rstudio/bookdown-demo/edit/master/%s
output_dir: "book-output"
clean: ["my-book.bbl", "R-packages.bib"]