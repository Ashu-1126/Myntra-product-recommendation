import os

from database.db import init_app
from dotenv import load_dotenv
from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from resources.routes import initialize_routes
from load_data import load_data_into_db

app = Flask(__name__)
CORS(app, origins=["http://localhost:5173"])
api = Api(app)

# Load environment variables before setting config
load_dotenv()

app.config["MONGO_URI"] = os.getenv("MONGO_URI")
init_app(app)
initialize_routes(api)

if __name__ == "__main__":
    # Use app_context to load data on startup
    with app.app_context():
        load_data_into_db()
    app.run(debug=True)