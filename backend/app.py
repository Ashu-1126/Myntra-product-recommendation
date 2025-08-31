import os
from database.db import init_app
from dotenv import load_dotenv
from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_restful import Api
from resources.routes import initialize_routes
from load_data import load_data_into_db
from ml_model import load_model_and_data, give_recommendation

app = Flask(__name__)
CORS(app, origins=["http://localhost:5173"])
api = Api(app)

# Load environment variables before setting config
load_dotenv()

app.config["MONGO_URI"] = os.getenv("MONGO_URI")

# Define global variables for the model and data
model_data = None
app_ready = False

# A simple endpoint to check if the app is running
@app.route('/', methods=['GET'])
def health_check():
    return jsonify({"status": "running"}), 200

# A new endpoint for recommendations that lazy-loads the model
@app.route('/recommendations/<int:p_id>', methods=['GET'])
def get_recommendations(p_id):
    global model_data
    if model_data is None:
        # Lazy load the model and data on the first request
        try:
            model_data = load_model_and_data()
        except FileNotFoundError:
            return jsonify({"error": "Model files not found. Please run ml_model.py locally to train and save the model."}), 500
    
    recommendations = give_recommendation(p_id, model_data)
    return jsonify(recommendations), 200

def run_app():
    global app_ready
    with app.app_context():
        # Only load data into DB if it doesn't exist
        load_data_into_db()
        app_ready = True
    app.run(debug=True)

if __name__ == "__main__":
    run_app()
