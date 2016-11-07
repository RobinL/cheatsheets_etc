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
	git rebase master newbranch
	git checkout master
	git reset HEAD^1 --hard

How to fix it when someone updates remote from under you:

	rm -rf alpha
	rm -rf beta
	rm -rf myremote

	mkdir alpha
	cd alpha
	git init
	echo "1


	3" > myfile.txt
	git add myfile.txt 
	git commit -m "First commit"
	cd ..
	git clone alpha myremote --bare
	git clone myremote beta
	cd alpha/
	git remote add origin ../myremote
	echo "1

	2

	3" > myfile.txt
	git add myfile.txt 
	git commit -m "Second commit"
	git push origin master
	cd ../beta
	echo "1


	3

	4" > myfile.txt
	git fetch origin master
	git add myfile.txt 
	git commit -m "Third commit"

	OPTIONS ARE NOW:

	git rebase origin/master master
	git push origin master

	OR 

	git branch temp
	git reset HEAD^1 --hard
	git merge origin/master
	git merge temp
	git branch -D temp
	git push origin master

	OR

	git branch temp
	git reset HEAD^1 --hard
	git merge origin/master
	git cherry-pick temp
	git branch -D temp
	git push origin master


