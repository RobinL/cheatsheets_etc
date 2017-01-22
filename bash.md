As a rough analogy, to call a function like `f(x,y = 1)` in the shell, you’d write `f x --y=1` or `f x -y1`.

`>` redirection for `stdout`, creates a new file

`>>` redirection for `stdout`, appends

`stderr` is file descriptor number 2, so we can redirect like this :  `ls . 2> ls-error.txt`

`cat movie.mpeg.0* > movie.mpeg` the wildcards will expand in sorted order
