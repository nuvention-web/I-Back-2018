git stash
git pull --rebase=preserve origin master
git stash pop

sudo service gunicorn restart
