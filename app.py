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



from flask import Flask, request, jsonify

app = Flask(__name__)

# Simulating user session
active_sessions = {}

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    # Simulate a user checking the username and password
    if username == "john_doe" and password == "password123":
        active_sessions[username] = True  # User is logged in
        return jsonify({"message": "Login successful!"}), 200
    return jsonify({"error": "Invalid credentials"}), 401

@app.route('/logout', methods=['POST'])
def logout():
    data = request.json
    username = data.get("username")

    if username in active_sessions:
        del active_sessions[username]  # Remove user from active sessions (simulating logout)
        return jsonify({"message": f"{username} logged out successfully!"}), 200
    return jsonify({"error": "User is not logged in"}), 400

if __name__ == "__main__":
    app.run(debug=True)
