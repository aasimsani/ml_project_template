echo "Initialize DVC"
python3 -m dvc init
git status
git commit -m "Initialize DVC"

echo "Starting to ignore config files now"
echo "#Ignoring config files" >> .gitignore
echo "config/*" >> .gitignore