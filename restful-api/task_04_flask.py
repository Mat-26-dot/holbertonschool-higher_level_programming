from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory user storage
users = {}

# Root endpoint
@app.route('/')
def home():
    return "Welcome to the Flask API!"

# /status endpoint
@app.route('/status')
def status():
    return "OK"

# /data endpoint: returns list of usernames
@app.route('/data')
def data():
    return jsonify(list(users.keys()))

# /users/<username> endpoint: returns user data or error
@app.route('/users/<username>')
def get_user(username):
    user = users.get(username)
    if user:
        # Include username in the returned object
        result = user.copy()
        result['username'] = username
        return jsonify(result)
    else:
        return jsonify({"error": "User not found"}), 404

# /add_user endpoint: handles POST to add a new user
@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()
    if not data or 'username' not in data:
        return jsonify({"error": "Username is required"}), 400
    username = data['username']
    # Prepare user data (excluding username from the value, as it's the key)
    user_data = {
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city")
    }
    users[username] = user_data
    # Include username in the response
    response = {
        "message": "User added",
        "user": {
            "username": username,
            "name": user_data["name"],
            "age": user_data["age"],
            "city": user_data["city"]
        }
    }
    return jsonify(response), 201

if __name__ == "__main__":
    app.run()

