c starts a 'change'
For example cw deletes the current word and puts you into insert mode

ciw - change inside word
ci) - change inside parens
ci" - change inside speachmarks 
ca" - change around speechmarks


The dot command lets us repeat the last _change_.  A change could act at the level of
individual characters, entire lines, or even the whole file.

Find and replace one at a time:
:s/target/replacement, then n to go to next and & if you want to replace it
