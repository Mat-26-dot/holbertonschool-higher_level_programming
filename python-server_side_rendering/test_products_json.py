from task_03_files import app

def test_display_all_json_products():
    with app.test_client() as client:
        response = client.get('/products?source=json')
        assert response.status_code == 200
        assert b"Laptop" in response.data  # Adjust if your JSON uses a different product

def test_display_all_csv_products():
    with app.test_client() as client:
        response = client.get('/products?source=csv')
        assert response.status_code == 200
        assert b"Coffee Mug" in response.data  # Adjust to match CSV content

def test_display_specific_product_json():
    with app.test_client() as client:
        response = client.get('/products?source=json&id=1')
        assert response.status_code == 200
        assert b"Laptop" in response.data
        assert b"Coffee Mug" not in response.data

def test_invalid_product_id():
    with app.test_client() as client:
        response = client.get('/products?source=json&id=999')
        assert response.status_code == 200
        assert b"Product not found" in response.data

def test_invalid_source_parameter():
    with app.test_client() as client:
        response = client.get('/products?source=xml')
        assert response.status_code == 200
        assert b"Wrong source" in response.data
