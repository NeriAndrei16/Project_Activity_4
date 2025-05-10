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
