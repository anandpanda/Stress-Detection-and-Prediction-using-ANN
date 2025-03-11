# 🧘‍♂️ Chill Check: Stress Detection and Prediction Using ANN

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Flask](https://img.shields.io/badge/Flask-2.3.2-green)
![SQLite](https://img.shields.io/badge/SQLite-3-lightgrey)

Chill Check is a web application designed to detect and predict stress levels using an **Artificial Neural Network (ANN)**. The app provides **AI generated personalized stress analysis** and **actionable tips** to help users manage their stress effectively. The app also features **chart visualizations** to help users track their stress trends over time.

It is built with **Flask** for the backend, **SQLite** for the database. 


## 🎥 Demo
https://github.com/user-attachments/assets/f7ea1dd1-ea97-43ac-b9dd-0bc7607e6dda


## 🌟 Features

- **🧠 Stress Prediction**  
  Predicts stress levels using an **ANN model** trained on physiological data such as **heart rate, snoring rate, and respiratory rate**.  

- **🔐 User Authentication**  
  Secure login and registration system using **Flask-Login** to protect user data.  

- **📊 Stress Trend Analysis**  
  Visualizes stress trends over time using **beautiful charts** powered by Chart.js, allowing users to track their stress levels and identify patterns.  

- **📌 Personalized Suggestions**  
  Provides **AI generated personalized actionable tips** based on the user's stress levels, including **breathing exercises, sleep hygiene tips, and relaxation techniques**.  

- **📱 Responsive Design**  
  Works seamlessly on **both desktop and mobile devices**, ensuring a smooth user experience.  


## 🔄 How the System Works

1. **📥 Data Input**  
   Users enter physiological data (**heart rate, snoring rate, respiratory rate**) through an intuitive web interface.  

2. **🧠 Stress Prediction**  
   The **ANN model** processes input data and predicts whether the user is **Stressed** or **Not Stressed**.  

3. **📊 Trend Analysis**  
   The system visualizes user **stress trends over time** using **cool charts**, helping them identify patterns and triggers.  

4. **📌 Personalized Suggestions**  
   Based on predictions and trends, the app provides **tailored suggestions via GEMINI** to help users manage stress more effectively.  


## 🚀 Future Scope

- **📡 Integration with Wearable Devices :**  Real-time data collection from **smartwatches** and **fitness trackers**.  

- **📊 Advanced Analytics & AI :** Deeper insights into stress patterns using **predictive analytics** and **AI-driven recommendations**.  


## 🛠️ Technologies Used

- **🐍 Python**: Backend language for implementing core logic and machine learning models.  
- **🌐 Flask**: Lightweight web framework for backend and API development.  
- **🗄️ SQLite**: Embedded database for storing user data and stress predictions.  
- **🧠 TensorFlow/Keras**: Libraries for building and training the **Artificial Neural Network (ANN)** model.  
- **📊 Chart.js**: JavaScript library for interactive stress trend visualizations.  
- **💻 HTML/CSS/JavaScript**: Technologies for building the user interface.  
- **🔐 Flask-Login**: Library for user authentication and session management.  
- **🔄 Flask-Migrate**: Handles database migrations.


## 📥 Installation & Setup

### **1️⃣ Clone the Repository**
```sh
https://github.com/anandpanda/Stress-Detection-and-Prediction-using-ANN.git
cd Stress-Detection-and-Prediction-using-ANN
```

### **2️⃣ Run the Setup Script**
```sh
chmod +x setup.sh
./setup.sh
```

This will:

- Create & activate a virtual environment
- Install dependencies
- Apply database migrations
- Start the application

**The app will be available at `http://127.0.0.1:10000`🎉**