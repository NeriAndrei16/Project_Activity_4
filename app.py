from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory users store for the demo
users = {}

# Register Route
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

# Profile Update Route
@app.route('/profile', methods=['POST'])
def update_profile():
    data = request.json
    name = data.get("name")
    if not name:
        return jsonify({"error": "Missing name"}), 400
    return jsonify({"message": "Profile updated successfully"})

# Login Route
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


@app.route('/change_password', methods=['POST'])
def change_password():
    data = request.json
    username = data.get('username')
    old_password = data.get('old_password')
    new_password = data.get('new_password')
    confirm_password = data.get('confirm_password')

    # Check if user is logged in
    if username not in logged_in_users:
        return jsonify({'error': 'User not logged in'}), 401

    # Verify old password
    if users[username]['password'] != old_password:
        return jsonify({'error': 'Old password is incorrect'}), 400

    # Check if new password and confirm password match
    if new_password != confirm_password:
        return jsonify({'error': 'New password and confirm password do not match'}), 400

    # Update password
    users[username]['password'] = new_password
    return jsonify({'message': 'Password changed successfully'}), 200

# Main entry point
if __name__ == "__main__":
    app.run(debug=True)
