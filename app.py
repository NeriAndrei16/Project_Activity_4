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



@app.route('/reset_password', methods=['POST'])
def reset_password():
    data = request.json
    username = data.get('username')

    if not username:
        return jsonify({'error': 'Username is required'}), 400

    if username not in users:
        return jsonify({'error': 'User does not exist'}), 404

    # Simulating sending a password reset link (in reality, you'd send an email)
    return jsonify({'message': 'Password reset link sent to your email!'}), 200
