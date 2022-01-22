echo "Initialize DVC"
dvc init
git status

echo "Starting to ignore config files now"
echo "\n# Ignoring config files" >> .gitignore
echo "config/*" >> .gitignore
git add .gitignore
git add .dvc/
git commit -m "Initialize DVC"
