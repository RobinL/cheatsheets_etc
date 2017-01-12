c starts a 'change'
For example cw deletes the current word and puts you into insert mode

ciw - change inside word
ci) - change inside parens
ci" - change inside speachmarks 
ca" - change around speechmarks

\* searches for the word under the cursor 

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
