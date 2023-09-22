# build_files.sh
echo "Building files"
pip install -r requirements.txt
python3.9 manage.py collectstatic --noinput --clear
echo "Build END"