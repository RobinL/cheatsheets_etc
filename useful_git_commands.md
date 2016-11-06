To show a given commit without diffs but with tree and parent sha1s:
    
    git cat-file -p sha-1 

To show a given commit including diffs:

    git show sha-1

To show a given tree (blobs and subtrees):

    git ls-tree sha-1

Show the tree recursively (i.e. show sha1 of all files, ignoring folder)

    git ls-tree -r sha-1

Display files in the index (need better description of that)

    git ls-files

Display files in the index with a reference to the blob in the index

    git ls-files -stage

Immediately get rid of unreachable objects e.g. after accidentally commiting a video

    git gc --prune=now
    
How to fix a commit to the wrong branch

	git init
	echo "First edit" > file.txt
	git add file.txt 
	git commit -m "First commit"
	git branch newbranch
	echo "Second edit" >> file.txt
	git add file.txt 
	git commit -m "Second commit, accidentally on master rather than newbranch"
	git checkout newbranch
	git rebase master
	git checkout master
	git reset HEAD^1 --hard
