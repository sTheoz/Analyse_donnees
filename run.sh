[ ! -d "analyze" ] && python -m venv "analyze"

. ./analyze/bin/activate
echo "Loading python packages..."
pip install -r requirements.txt 1> /dev/null
python3 app.py