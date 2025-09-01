**🛍️ Myntra Product Recommendation System**
This is a full-stack e-commerce application that provides personalized product recommendations based on user and item features. 
The project consists of a ReactJS frontend, a Flask-based backend, and a machine learning model for content-based recommendations.

**✨ Features**
-------Content-Based Recommendations: The system provides product suggestions based on a user's browsing history and interests, powered by a TF-IDF vectorization and cosine similarity model.

-------Full-Stack Architecture: The application is built with a decoupled architecture, using a modern ReactJS frontend and a robust Flask backend.

-------Scalable Backend: The backend is built using Flask-Restful and connected to a MongoDB database, ensuring efficient handling of product data.

-------Responsive User Interface: The frontend is designed for a seamless user experience across various devices.

**💻 Technologies Used**
**Category**	               **Technologies**
Frontend	                   ReactJS
Backend	                     Python, Flask, Gunicorn
Database	                   MongoDB
Machine Learning	           Scikit-learn, Pandas, NumPy, Jupyter
Deployment	                 Vercel (Frontend), Render (Backend)
DevOps	                     Git, GitHub, Git LFS

**🚀 Getting Started
Follow these instructions to set up the project on your local machine.
**
Prerequisites: Python 3.10 or higher, Node.js and npm, MongoDB Atlas account or a local MongoDB instance

1. Backend Setup
Clone the repository:

Bash

git clone https://github.com/Ashu-1126/Myntra-product-recommendation.git
cd Myntra-product-recommendation/backend
Create a virtual environment and install dependencies:

Bash

python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
pip install -r requirements.txt
Set up environment variables:
Create a .env file in the backend directory with your MongoDB URI.

MONGO_URI=mongodb://localhost:27017/myntra_local_db


# You can also use a MongoDB Atlas URI for remote connection
SECRET_KEY=your_secret_key
Run the backend server:

Bash
python app.py


2. Frontend Setup
Navigate to the frontend directory and install dependencies:

Bash
cd ../frontend
npm install


Set up environment variables:
Create a .env file in the frontend directory. Make sure VITE_BACKEND_BASE_URL points to your backend URL (e.g., http://localhost:5000/api).

VITE_BACKEND_BASE_URL=http://localhost:5000/***


Start the frontend application:

Bash
npm run dev
