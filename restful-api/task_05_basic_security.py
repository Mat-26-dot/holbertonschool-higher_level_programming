from flask import Flask, jsonify, request
from werkzeug.security import generate_password_hash, check_password_hash
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager, create_access_token, 
    jwt_required, get_jwt_identity, get_jwt
)

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'super-secret-key'  # Change in production
auth = HTTPBasicAuth()
jwt = JWTManager(app)

# User storage with hashed passwords and roles
users = {
    "user1": {
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}

# Basic Authentication setup
@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users[username]['password'], password):
        return username

# JWT Error Handlers (return 401 for all auth errors)
@jwt.unauthorized_loader
def missing_token_callback(error):
    return jsonify({"error": "Authorization required"}), 401

@jwt.invalid_token_loader
def invalid_token_callback(error):
    return jsonify({"error": "Invalid token"}), 401

@jwt.expired_token_loader
def expired_token_callback(jwt_header, jwt_payload):
    return jsonify({"error": "Token expired"}), 401

# Basic Auth Protected Route
@app.route('/basic-protected', methods=['GET'])
@auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted", 200

# JWT Login Route
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    if username not in users or not check_password_hash(users[username]['password'], password):
        return jsonify({"error": "Invalid credentials"}), 401
    
    # Include role in JWT claims
    access_token = create_access_token(
        identity=username,
        additional_claims={"role": users[username]['role']}
    )
    return jsonify (access_token=access_token)

# JWT Protected Route
@app.route('/jwt-protected', methods=['GET'])
@jwt_required()
def jwt_protected():
    return "JWT Auth: Access Granted", 200

# Admin-only Route
@app.route('/admin-only', methods=['GET'])
@jwt_required()
def admin_only():
    claims = get_jwt()
    if claims['role'] != 'admin':
        return jsonify({"error": "Admin access required"}), 403
    return "Admin Access: Granted", 200

if __name__ == '__main__':
    app.run()
