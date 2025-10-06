🛡️ Network Security Phishing Prediction API
This project implements a machine learning-based Phishing Detection API using FastAPI. It provides a robust, asynchronous endpoint for classifying URLs to predict whether they are legitimate or potential phishing attempts, leveraging the power of Python, a trained model, and MongoDB for data management.

✨ Features
Real-time Prediction: Offers a high-performance endpoint for instant phishing prediction. (the /predict_route/predict_post endpoint)

Machine Learning Integration: Utilizes a trained model (based on the Kaggle Phishing Dataset) for accurate URL classification.

Data Persistence: Uses MongoDB to store data (e.g., predicted results, user input, or model training data).

Interactive Documentation: Automatically generated and interactive API documentation (Swagger UI/ReDoc) thanks to FastAPI.

Scalable Architecture: Built on modern, asynchronous Python (FastAPI/Uvicorn) for high throughput.

🛠️ Technology Stack

Framework-	FastAPI	High-performance API development and routing.
Server-	Uvicorn	Asynchronous Server Gateway Interface (ASGI) server to run FastAPI.
Database-	MongoDB	NoSQL database for flexible data storage.
Programming-	Python 3.x	Core development language.
Machine Learning-	Scikit-learn/TensorFlow Model training and prediction logic.
Dataset-	Kaggle Phishing Dataset,	data source for training the model.

Export to Sheets
🚀 Getting Started
Follow these steps to get your API up and running locally.

1. Prerequisites
Python 3.8+

pip (Python package installer)

A running MongoDB instance (local or hosted).

2. Clone the Repository
Bash

git clone <REPO_URL>
cd <PROJECT_FOLDER>
3. Set Up Virtual Environment
It is highly recommended to use a virtual environment.

Bash

python -m venv venv
source venv/bin/activate  # On Linux/macOS
# venv\Scripts\activate  # On Windows
4. Install Dependencies
Install all required Python libraries.

Bash

pip install -r requirements.txt
(You will need to create a requirements.txt file listing all libraries like fastapi, uvicorn, pymongo, pandas, scikit-learn, etc.)

5. Configure Environment Variables
Create a .env file or set environment variables for your MongoDB connection string and other settings.

Bash

# Example .env content
MONGO_URI="mongodb://localhost:27017/"
DATABASE_NAME="phishing_db"
6. Run the Application
Start the FastAPI application using Uvicorn.

Bash

uvicorn main:app --reload --host 0.0.0.0 --port 8000
The application will now be running at http://0.0.0.0:8000.

📄 API Documentation & Usage
Interactive Docs (Swagger UI): Access the interactive documentation and test the endpoints directly at: http://127.0.0.1:8000/docs

Alternative Docs (ReDoc): View the alternative documentation at: http://127.0.0.1:8000/redoc

Key Endpoint
Method	Path	Description
POST	/predict_route/predict_post	Predicts the security status of a given input (e.g., a URL).

Export to Sheets
Example Usage (Request Body):

JSON

{
  "url_features": "..." // The input data your model expects (e.g., URL string or extracted features)
}
Why FastAPI?

FastAPI is a modern, fast (high-performance) web framework for building APIs with Python 3.7+ based on standard Python type hints.

Why FastAPI for this Project?
Speed (Performance): It is one of the fastest Python frameworks available, comparable to Node.js and Go. This is crucial for a real-time prediction service where latency must be minimal.

Developer Experience: It dramatically simplifies API development. By leveraging standard Python type hints, it automatically provides:

Data Validation: Ensures incoming data matches the expected structure.

Serialization: Converts Python objects to JSON and vice-versa.

Automatic Docs: Generates comprehensive and interactive API documentation (Swagger UI and ReDoc) right out of the box, as you showed in your screenshot. This makes testing and integration easy.

Asynchronous Support: It fully supports asynchronous programming (async and await), which, when combined with an ASGI server like Uvicorn, allows the API to handle many concurrent requests efficiently—a must-have for a scalable service.

Standard Compliance: It's built upon open standards for APIs, including OpenAPI (formerly Swagger) for documentation and JSON Schema for data definition.

