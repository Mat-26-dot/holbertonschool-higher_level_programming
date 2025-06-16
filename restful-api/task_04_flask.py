from flask import Flask, jsonify

app = Flask(__name__)  # creates your Flask app

@app.route("/")  # defines the home route
def home():
    return "Welcome to the Flask API!"

# In-memory user store (declared before the route)
users = {
    "jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"},
    "john": {"username": "john", "name": "John", "age": 30, "city": "New York"}
}

@app.route("/data")
def get_usernames():
    return jsonify(list(users.keys()))  # returns ["jane", "john"]

@app.route("/status")
def status():
    return "OK"

@app.route("/users/<username>")
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

if __name__ == "__main__":
    app.run()
