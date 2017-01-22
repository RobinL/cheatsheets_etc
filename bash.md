As a rough analogy, to call a function like `f(x,y = 1)` in the shell, you’d write `f x --y=1` or `f x -y1`.

`>` redirection for `stdout`, creates a new file

`>>` redirection for `stdout`, appends

`stderr` is file descriptor number 2, so we can redirect like this :  `ls . 2> ls-error.txt`

`cat movie.mpeg.0* > movie.mpeg` the wildcards will expand in sorted order

`ctrl-d` tell the terminal that you've reached `EOF`


`ls > less` could accidentally overwrite the less program with text from ls - the redirection operator silently creates or overwrites files
`cat < lazy_dog.txt` the file is now treated as `stdin`.  This is fundamentally different to `>`. `<` gives input to a command

##Seeing expansions
`echo *` - note that hidden files are not echoed

`echo Front-{A,B,C}-Back` expands to Front-A-Back etc.
`echo Number_{1..5}` expands to Number_1 etc..  You can do ranges of letters, zero padded numbers
`echo a{A{1,2},B{3,4}}b` expands to aA1b aA2b etc
`mkdir {2007..2009}-{01-12}`

`echo $USER`

`printenv less`
