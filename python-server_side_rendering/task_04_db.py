from flask import Flask, render_template, request
import json
import csv
import sqlite3
import os

app = Flask(__name__)

def read_json():
    try:
        with open('products.json') as f:
            data = json.load(f)
        return data
    except Exception as e:
        return None

def read_csv():
    data = []
    try:
        with open('products.csv', newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                row['id'] = int(row['id'])
                row['price'] = float(row['price'])
                data.append(row)
        return data
    except Exception as e:
        return None

def read_sql():
    if not os.path.exists('products.db'):
        return None
    try:
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()
        cursor.execute('SELECT id, name, category, price FROM Products')
        rows = cursor.fetchall()
        products = []
        for row in rows:
            products.append({'id': row[0], 'name': row[1], 'category': row[2], 'price': row[3]})
        conn.close()
        return products
    except Exception as e:
        return None

@app.route('/products')
def display_products():
    source = request.args.get('source')
    products = None
    error = None

    if source == 'json':
        products = read_json()
        if products is None:
            error = "Could not read JSON data."
    elif source == 'csv':
        products = read_csv()
        if products is None:
            error = "Could not read CSV data."
    elif source == 'sql':
        products = read_sql()
        if products is None:
            error = "Could not read from SQL database."
    else:
        error = "Wrong source"

    return render_template('product_display.html', products=products, error=error)

if __name__ == '__main__':
    app.run(debug=True)
