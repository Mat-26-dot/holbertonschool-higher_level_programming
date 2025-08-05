import json
import csv

def read_json_products(filename='products.json'):
    with open(filename, 'r') as file:
        return json.load(file)

def read_csv_products(filename='products.csv'):
    products = []
    with open(filename, newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            products.append({
                'id': int(row['id']),
                'name': row['name'],
                'category': row['category'],
                'price': float(row['price'])
            })
    return products

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/products')
def display_products():
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)

    if source == 'json':
        products = read_json_products()
    elif source == 'csv':
        products = read_csv_products()
    else:
        return render_template("product_display.html", error="Wrong source", products=None)

    if product_id:
        products = [product for product in products if product['id'] == product_id]
        if not products:
            return render_template("product_display.html", error="Product not found", products=None)

    return render_template("product_display.html", products=products, error=None)


import json
import csv

def read_json_products(filename='products.json'):
    with open(filename, 'r') as file:
        return json.load(file)
