🛡️ IDS-IoT: Intrusion Detection System for IoT Devices
🔍 Overview

IDS-IoT is a machine learning–based Intrusion Detection System designed to detect and classify cyber attacks in IoT networks.
It uses an ensemble learning approach combining LightGBM, CatBoost, and Random Forest models to achieve high detection accuracy with minimal false positives.
The system features a clean, interactive web interface built with Flask, allowing users to monitor real-time alerts, view attack analytics, and analyze threat trends efficiently.

🚀 Features

🧠 Multi-class attack detection — Detects and classifies attacks such as:

DDoS

Brute Force

Infiltration

Botnet,etc

⚡ Real-time monitoring — Processes incoming IoT network logs and raises instant alerts.

📊 Analytical dashboard — Displays attack trends, frequency, and model performance graphs.

🧩 Ensemble model architecture — Combines multiple models for improved accuracy.

🔔 Alert system — Generates notifications upon detection of suspicious traffic.

🌐 User-friendly interface — Clean and responsive Flask-based web UI.

🧱 System Architecture
 ┌────────────────────────────┐
 │        IoT Devices         │
 └────────────┬───────────────┘
              │
       (Network Traffic)
              │
 ┌────────────▼───────────────┐
 │   Data Preprocessing Unit  │
 │ (Feature extraction, SMOTE)│
 └────────────┬───────────────┘
              │
       (Processed Data)
              │
 ┌────────────▼───────────────┐
 │   Ensemble ML Model        │
 │ (LightGBM + CatBoost + RF) │
 └────────────┬───────────────┘
              │
       (Predicted Class)
              │
 ┌────────────▼───────────────┐
 │     Flask Web Interface    │
 │ (Dashboard + Alert System) │
 └────────────────────────────┘

🧩 Tech Stack
Component	Technology Used
Programming Language	Python
Machine Learning	Scikit-learn, LightGBM, CatBoost, Random Forest
Web Framework	Flask
Visualization	Plotly, Matplotlib, Chart.js
Dataset	CIC IDS 2018
Deployment	Flask Server / Docker (optional)
⚙️ Installation & Setup
1️⃣ Clone the repository
git clone https://github.com/yourusername/IDS-IoT.git
cd IDS-IoT

2️⃣ Create and activate a virtual environment
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Run the Flask application
python app.py

5️⃣ Open your browser

Visit → http://127.0.0.1:5000

📊 Dataset Details

Dataset Used: CIC IDS 2018

Contains realistic IoT network traffic labeled for multiple attack types.

Used for training, testing, and evaluation of ensemble models.

🧠 Model Training

The system uses a hybrid ensemble model combining:

LightGBM for gradient boosting,

CatBoost for handling categorical data efficiently, and

Random Forest for robust generalization.

Each model’s prediction is aggregated using weighted voting to improve classification accuracy and minimize false alarms.


🖥️ User Interface

The interface provides:

Real-time attack alerts

Visual analytics (attack frequency, type distribution, trends)

System logs and threat reports

(Add screenshots here if available)

/static/
   ├── css/
   ├── js/
   └── images/

📦 Folder Structure
IDS-IoT/
│
├── app.py                  # Flask main application
├── models/                 # Trained ML models
├── static/                 # CSS, JS, and images
├── templates/              # HTML templates
├── utils/                  # Helper scripts (data preprocessing, feature extraction)
├── dataset/                # CIC IDS 2018 dataset (or link)
├── requirements.txt        # Dependencies
└── README.md               # Project documentation

🌍 Future Enhancements

Integration with MQTT or Kafka for real-time IoT data streaming

Containerized deployment using Docker / Kubernetes

Integration with SIEM tools for enterprise monitoring

Automated model retraining pipeline with new attack data

🤝 Contributors

[Your Name] – Developer & Researcher

Open for collaboration! Feel free to submit PRs or suggest enhancements.

🪪 License

This project is licensed under the MIT License — see the LICENSE
 file for details.

⭐ Acknowledgements

Dataset: Canadian Institute for Cybersecurity (CIC IDS 2018)

Libraries: LightGBM, CatBoost, Scikit-learn, Flask
