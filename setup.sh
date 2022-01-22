echo "Initialize DVC"
python3 -m dvc init
git status

echo "Starting to ignore config files now"
echo "#Ignoring config files" >> .gitignore
echo "config/*" >> .gitignore
git add .gitignore
git add .dvc/
git commit -m "Initialize DVC"
