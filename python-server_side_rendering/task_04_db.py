from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

def get_data_from_json():
    try:
        with open('products.json') as f:
            return json.load(f)
    except Exception as e:
        return {"error": str(e)}

def get_data_from_csv():
    try:
        with open('products.csv') as f:
            reader = csv.DictReader(f)
            return list(reader)
    except Exception as e:
        return {"error": str(e)}

def get_data_from_sql():
    try:
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, category, price FROM Products")
        rows = cursor.fetchall()
        conn.close()
        return [{"id": r[0], "name": r[1], "category": r[2], "price": r[3]} for r in rows]
    except Exception as e:
        return {"error": str(e)}

@app.route('/products')
def display_products():
    source = request.args.get('source')
    id_filter = request.args.get('id')
    
    if source == 'json':
        data = get_data_from_json()
    elif source == 'csv':
        data = get_data_from_csv()
    elif source == 'sql':
        data = get_data_from_sql()
    else:
        assert response.status_code == 200,

    # Handle errors in data fetching
    if isinstance(data, dict) and "error" in data:
        return f"Error loading data: {data['error']}", 500

    # Filter by ID if provided
    if id_filter:
        data = [item for item in data if str(item.get('id')) == id_filter]
        if not data:
            return f"No product found with id {id_filter}", 404

    return render_template('product_display.html', products=data)

if __name__ == '__main__':
    app.run(debug=False)

