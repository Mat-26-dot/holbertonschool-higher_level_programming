from flask import Flask, render_template, request
import csv
import json
import sqlite3

app = Flask(__name__)

def get_products_from_json(filename):
    try:
        with open(filename) as f:
            data = json.load(f)
            return data['products'], None
    except Exception as e:
        return None, f"JSON error: {e}"

def get_products_from_csv(filename):
    try:
        with open(filename) as f:
            reader = csv.DictReader(f)
            return list(reader), None
    except Exception as e:
        return None, f"CSV error: {e}"

def get_products_from_sqlite(db_file):
    try:
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, category, price FROM Products")
        rows = cursor.fetchall()
        conn.close()
        products = [{"id": r[0], "name": r[1], "category": r[2], "price": r[3]} for r in rows]
        return products, None
    except Exception as e:
        return None, f"Database error: {e}"

@app.route('/products')
def show_products():
    source = request.args.get('source')

    if source == "json":
        products, error = get_products_from_json("products.json")
    elif source == "csv":
        products, error = get_products_from_csv("products.csv")
    elif source == "sql":
        products, error = get_products_from_sqlite("products.db")
    else:
        products = None
        error = "Wrong source"

    return render_template(
        "product_display.html",
        products=products,
        error=error
    )

if __name__ == "__main__":
    app.run(debug=True)



