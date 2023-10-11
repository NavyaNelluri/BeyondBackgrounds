from flask_pymongo import PyMongo
from flask import Flask, request, jsonify

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017"
mongo = PyMongo(app)

@app.route('/login', methods=['GET','POST'])
def login():
    username = request.form.get('username')  # Use lowercase keys
    password = request.form.get('password')  # Use lowercase keys

    # Find the user in the MongoDB database
    user_data = mongo.db.users.find_one({"username": username})

    if user_data and user_data["password"] == password:
        return jsonify({'message': 'Login successful'})
    else:
        return jsonify({'message': 'Login failed'})

if __name__ == '__main__':
    app.run()

