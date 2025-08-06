from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

def load_json_products(filepath='products.json'):
    try:
        with open(filepath, 'r') as f:
            data = json.load(f)
            # Ensure all fields are correct type
            for item in data:
                item['id'] = int(item['id'])
                item['price'] = float(item['price'])
            return data
    except Exception as e:
        return None

def load_csv_products(filepath='products.csv'):
    try:
        data = []
        with open(filepath, newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                item = {
                    'id': int(row['id']),
                    'name': row['name'],
                    'category': row['category'],
                    'price': float(row['price'])
                }
                data.append(item)
        return data
    except Exception as e:
        return None

@app.route('/products')
def show_products():
    source = request.args.get('source', '').lower()
    id_filter = request.args.get('id', None)
    error = None
    products = []

    if source == 'json':
        products = load_json_products()
        if products is None:
            error = "Failed to read JSON data."
    elif source == 'csv':
        products = load_csv_products()
        if products is None:
            error = "Failed to read CSV data."
    else:
        error = "Wrong source"
        products = None

    # Only filter if no file error and if there's an 'id'
    if not error and id_filter is not None:
        try:
            id_filter = int(id_filter)
        except ValueError:
            products = []
            error = "Invalid id value: must be an integer."
        else:
            filtered = [p for p in products if p['id'] == id_filter]
            if filtered:
                products = filtered
            else:
                products = []
                error = "Product not found"

    return render_template('product_display.html', products=products, error=error)

if __name__ == '__main__':
    app.run(debug=True)
