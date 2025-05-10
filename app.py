from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/profile', methods=['POST'])
def update_profile():
    data = request.json
    name = data.get("name")
    if not name:
        return jsonify({"error": "Missing name"}), 400
    return jsonify({"message": "Profile updated successfully"})

if __name__ == '__main__':
    app.run(debug=True)


@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")
    
    if not username or not password:
        return jsonify({"error": "Missing username or password"}), 400

    # Pretend authentication
    if username == "john_doe" and password == "password123":
        return jsonify({"message": "Login successful!"})
    else:
        return jsonify({"error": "Invalid credentials"}), 401

users = {}  # This will act as a simple in-memory store

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    email = data.get('email', '')  # Optional email field

    if not username or not password:
        return jsonify({'error': 'Username and password are required'}), 400

    if username in users:
        return jsonify({'error': 'User already exists'}), 400

    users[username] = {'password': password, 'email': email}
    return jsonify({'message': 'User registered successfully!'}), 201

if name == "main":
    app.run(debug=True)
from flask import Flask, request, jsonify

app = Flask(_name_)

# In-memory user store (acts as a database)
users = {
    "john": {"password": "1234", "email": "john@example.com"},
    "jane": {"password": "abcd", "email": "jane@example.com"},
    "alex": {"password": "xyz", "email": "alex@example.com"},
}

# User registration route
@app.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    email = data.get('email', '')  # Optional email field

    if not username or not password:
        return jsonify({'error': 'Username and password are required'}), 400

    if username in users:
        return jsonify({'error': 'User already exists'}), 400

    users[username] = {'password': password, 'email': email}
    return jsonify({'message': 'User registered successfully!'}), 201

# Search users route (search bar feature)
@app.route('/search', methods=['GET'])
def search_users():
    query = request.args.get('username', '').lower()  # Get the username query from URL
    results = {}

    # Search for users in the store (case-insensitive search)
    for username, user_info in users.items():
        if query in username.lower():  # Match the username (case-insensitive)
            results[username] = user_info

    if not results:
        return jsonify({'message': 'No users found matching that username.'}), 404
    
    return jsonify(results), 200

if _name_ == "_main_":
    app.run(debug=True)
