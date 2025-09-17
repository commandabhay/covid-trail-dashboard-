COVID-19 Clinical Trials Interactive Dashboard
This project is an interactive web dashboard designed to visualize key insights from a dataset of COVID-19 clinical trials. The dashboard is built with a decoupled architecture, using a Python backend to serve data to a modern, interactive web frontend.

Features
Interactive Data Visualization: Explore trial data through dynamic charts, including stacked bar charts, doughnut charts, and line charts.

Country-Specific Analysis: Filter the dashboard to view data for specific countries, allowing for detailed, regional insights.

Real-time Data Fetching: The frontend fetches data from a running backend API, ensuring the dashboard is always up-to-date with the latest information.

Modern UI/UX: The dashboard features a clean, professional design with a built-in dark mode for a better user experience.

Project Structure
The project is organized into two main components:

backend/: Contains the Python Flask API that serves the data.

frontend/: Contains all the web files (HTML, CSS, JavaScript) for the dashboard.

Getting Started
To run this project, you need to set up both the backend and the frontend.

1. Backend Setup
Navigate to the backend directory:

cd backend

Install the required Python packages:

pip install Flask Flask-Cors

Run the Flask server:

python app.py

The server will start and run on http://127.0.0.1:5000. Keep this terminal window open.

2. Frontend Setup
Navigate to the frontend directory:

cd frontend

Open the dashboard in your browser:
Simply open the index.html file with your preferred web browser (e.g., Chrome, Firefox).

The dashboard will automatically connect to the running backend and display the data.

Technologies Used
Frontend: HTML, CSS (Tailwind CSS), JavaScript, D3.js, and Chart.js

Backend: Python, Flask, and Flask-CORS
