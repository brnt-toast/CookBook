# Git Commands 
## Delete Commit
### Last Commit
```sh
	git reset --hard HEAD~^
```
### Nth Number of Commits
```sh
	git reset --hard HEAD~2
```
## Create New Repo From Local repo -- using gitlab
all branches
```sh
	git push --all --set-upstream https://gitlab.example.com/namespace/nonexistent-project.git
```
master branch
```sh 
	# To your own domain
	git push --set-upstream address/your-project.git

	# To gitlab.com with SSH
	git push --set-upstream git@gitlab.example.com:username/new-repo.git master

	# To gitlab.com with HTTP
	git push --set-upstream https://gitlab.example.com/username/new-repo.git master
````