from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
import joblib
import os
import datetime  # Make sure to import datetime
from pymongo import MongoClient
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app)

# Configure JWT
app.config['JWT_SECRET_KEY'] = os.getenv("JWT_SECRET_KEY")  # Change this to a random secret key
jwt = JWTManager(app)

# Initialize Bcrypt
bcrypt = Bcrypt(app)

# Connect to MongoDB
mongo_uri = os.getenv("MONGODB_URI")
client = MongoClient(mongo_uri)
db = client['VitaVueDB']
users_collection = db['user_data']
users_metric_collection = db['user_metric_data']  # Create a new collection for user data

# Load the trained model
model = joblib.load('glucose_model.pkl')

@app.route('/')
def home():
    return "Welcome to the Glucose Prediction API! Use the /predict endpoint to make predictions."

@app.route('/signup', methods=['POST'])
def signup():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    email = data['email']

    # Check if user already exists
    if users_collection.find_one({"username": username}):
        return jsonify({"msg": "User already exists!"}), 400

    # Hash the password
    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    
    # Store user data
    user = {
        "username": username,
        "password": hashed_password,
        "email": email,
        "createdAt": datetime.datetime.utcnow()
    }
    users_collection.insert_one(user)
    return jsonify({"msg": "User created successfully!"}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    # Check if user exists
    user = users_collection.find_one({"username": username})
    if not user or not bcrypt.check_password_hash(user['password'], password):
        return jsonify({"msg": "Invalid username or password!"}), 401

    # Create JWT token
    access_token = create_access_token(identity={"username": username})
    return jsonify(access_token=access_token), 200

@app.route('/predict', methods=['POST'])
@jwt_required()  # Protect this endpoint with JWT
def predict():
    current_user = get_jwt_identity()  # Get the current user's identity
    data = request.json
    voltage = data.get('nirVoltage')
    bpm = data.get('bpm')  # New field for BPM
    spo2 = data.get('spo2')  # New field for SpO2

    # Make prediction
    prediction = model.predict([[voltage]])
    
    # Store metrics in the database with user identification
    metrics_data = {
        "user": current_user['username'],  # Store the username of the user making the request
        "nirVoltage": voltage,
        "predictedGlucose": prediction[0],
        "bpm": bpm,  # Store BPM
        "spo2": spo2,  # Store SpO2
        "timestamp": datetime.datetime.utcnow()  # Optional: Store timestamp
    }
    users_metric_collection.insert_one(metrics_data)  # Store metrics in MongoDB

    return jsonify({'predictedGlucose': prediction[0]})

@app.route('/metrics', methods=['GET'])
@jwt_required()
def get_metrics():
    current_user = get_jwt_identity()
    metrics = users_metric_collection.find({"user": current_user['username']})
    metrics_list = []
    
    for metric in metrics:
        metrics_list.append({
            "nirVoltage": metric["nirVoltage"],
            "predictedGlucose": metric["predictedGlucose"],
            "bpm": metric.get("bpm"),
            "spo2": metric.get("spo2"),
            "timestamp": metric.get("timestamp")
        })
    
    return jsonify(metrics_list), 200

if __name__ == '__main__':
    app.run(debug=True)
