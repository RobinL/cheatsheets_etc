c starts a 'change'
For example cw deletes the current word and puts you into insert mode

ciw - change inside word
ci) - change inside parens
ci" - change inside speachmarks 
ca" - change around speechmarks

In insert mode the following will work
`Ctrl h` - delete back one character
`Ctrl w` - delete back one word
`Ctrl u` - delete back to the start of the line 

`*` searches for the word under the cursor 

The dot command lets us repeat the last _change_.  A change could act at the level of
individual characters, entire lines, or even the whole file.

Find and replace one at a time:
:s/target/replacement, then n to go to next and & if you want to replace it

If you have a couple lines of python code in your file that you want to execute eg

````
  for i in range(10):
    print i
````

you can execute them and get the output in your current file (buffer) with `:1,2 !python`

:b hello.py to change buffers

mM to set a global marker called M, 'M to recall it

Insert normal mode activated using `ctrl o` - fire off a single command
You can paste from a register in insert mode using `<C-r>0`

`<C-r>=100+100` to use the expression register in insert mode
In normal mode type `"2+2p`

`gv` reselect the last visual selection

The `o` key toggles the end of the selection in visual mode
`<C-v>` enable visual block mode

You can use visual block mode to enter multiple commands
e.g. `<C-v>jj$A;<Esc>` will add a semi colon after each line

Find and replace:
`:7,9s/hello/hiya/`
`:%s/hello/hiya`
`/<html>/,/<\/html>/s/<p>/<div>/

Copy line 52 to line 53
`:52t53`

Running normal mode commands across a range:
use `:normal`


`:nohlsearch` to get rid of highlight on search

`{}` move to the beginning or end of a para.

`ma` create a marker called a
`d'a` delete to the marker called a


