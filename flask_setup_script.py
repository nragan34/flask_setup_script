#!/usr/bin/env python3

# Quick Flask Project Starter

echo 'creating virtual environment... ' &&
python3 -m venv venv &&
echo 'activating virtual environment... ' &&
. venv/bin/activate &&
echo 'installing flask... ' &&
pip install flask &&
echo 'making templates and static directories... ' &&
mkdir templates static &&


echo 'writing content to app.py' &&
echo -e "from flask import Flask,render_template\napp = Flask(__name__)\n\n@app.route('/')\ndef index():\n    return render_template('index.html')" > app.py &&
cat app.py &&

echo 'writing boilerplate to index.html' &&
cd templates &&
echo -e "<!DOCTYPE html>\n<html>\n<head>\n<title>Page Title Here</title>\n</head>\n<body>\n\n<h1>My First Heading</h1>\n<p>My first paragraph</p>\n\n</body></html>" > index.html &&
cat index.html &&
cd .. &&

echo 'setting environment variables... ' &&
export FLASK_APP=app.py &&
export FLASK_ENV=development &&


echo 'opening visual studios code... ' &&
code . &&

echo 'opening chrome browser... ' &&
cmd.exe /C start http://localhost:5000 &&
flask run


