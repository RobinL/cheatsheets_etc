As a rough analogy, to call a function like `f(x,y = 1)` in the shell, you’d write `f x --y=1` or `f x -y1`.

`>` redirection for `stdout`, creates a new file

`>>` redirection for `stdout`, appends

`stderr` is file descriptor number 2, so we can redirect like this :  `ls . 2> ls-error.txt`

`cat movie.mpeg.0* > movie.mpeg` the wildcards will expand in sorted order

`ctrl-d` tell the terminal that you've reached `EOF`


`ls > less` could accidentally overwrite the less program with text from ls - the redirection operator silently creates or overwrites files
`cat < lazy_dog.txt` the file is now treated as `stdin`.  This is fundamentally different to `>`. `<` gives input to a command

##Seeing expansions
`echo *`
