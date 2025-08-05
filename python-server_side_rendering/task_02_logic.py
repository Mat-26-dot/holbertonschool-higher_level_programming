from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Welcome to the Flask App!</h1><p>Go to <a href="/items">/items</a> to see the item list.</p>'

@app.route('/items')
def show_items():
    try:
        with open('items.json') as f:
           data = json.load(f)
           items = data.get("items", [])
    except (FileNotFoundError, json.JSONDecodeError):
        items = [] # fallback if the file is missing or broken
       
       
    return render_template('items.html', items=items)

if __name__ == '__main__':
    app.run(debug=True)