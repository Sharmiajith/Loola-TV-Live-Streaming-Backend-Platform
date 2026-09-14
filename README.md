# Loola TV – Live Streaming Backend

## 📌 Project Overview

Loola TV is a Python-based backend project for managing a live streaming platform. The project uses **Flask** to build REST APIs and **MySQL** to store and manage live stream information.

The backend follows a structured **Route → Controller → Model → Database** architecture, making the application easier to maintain and extend.

## 🚀 Features

* Live stream management
* REST API development using Flask
* MySQL database integration
* Stream information storage and retrieval
* Route, Controller, and Model architecture
* JSON-based API responses
* Modular backend project structure
* Foundation for future RTMP/live-streaming integration

## 🛠️ Technologies Used

* **Python**
* **Flask**
* **MySQL**
* **XAMPP**
* **REST API**
* **VS Code**
* **Git & GitHub**

## 📂 Project Structure

```text
loola_backend/
│
├── app.py
│
├── routes/
│   ├── __init__.py
│   └── stream_routes.py
│
├── controllers/
│   └── stream_controller.py
│
├── models/
│   └── stream_model.py
│
├── database/
│   └── db.py
│
└── README.md
```

## 🔄 Backend Architecture

```text
Client
   │
   ▼
Flask API Routes
   │
   ▼
Controllers
   │
   ▼
Models
   │
   ▼
MySQL Database
```

### Request Flow

1. Client sends an API request.
2. Flask route receives the request.
3. Controller processes the request.
4. Model communicates with the database.
5. MySQL returns the required data.
6. Flask sends a JSON response to the client.

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone <your-github-repository-url>
cd loola_backend
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install flask mysql-connector-python
```

## 🗄️ MySQL Setup

Start **MySQL** from XAMPP.

Open phpMyAdmin and create the database:

```sql
CREATE DATABASE loola_db;
```

Select the database:

```sql
USE loola_db;
```

Create the streams table:

```sql
CREATE TABLE streams (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    status VARCHAR(50) NOT NULL
);
```

Add sample data:

```sql
INSERT INTO streams (title, status)
VALUES
('Gaming Live', 'active'),
('Podcast Live', 'active');
```

## 🔌 Database Configuration

Update `database/db.py` according to your MySQL configuration:

```python
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="loola_db"
)

cursor = conn.cursor()
```

> If you have configured a MySQL password in XAMPP, replace the empty password with your actual local MySQL password.

## ▶️ Run the Application

Start the Flask server:

```bash
python app.py
```

The application will run at:

```text
http://127.0.0.1:5000
```

## 🔗 API Endpoints

### Get All Streams

**Endpoint:**

```text
GET /streams
```

**Example:**

```text
http://127.0.0.1:5000/streams
```

**Example Response:**

```json
{
    "status": "success",
    "data": [
        {
            "id": 1,
            "title": "Gaming Live",
            "status": "active"
        },
        {
            "id": 2,
            "title": "Podcast Live",
            "status": "active"
        }
    ]
}
```

## 🧪 Testing

The API can be tested using:

* Web browser for GET requests
* Postman
* Thunder Client
* cURL

Example:

```bash
curl http://127.0.0.1:5000/streams
```

## 🔮 Future Enhancements

* User registration and authentication
* Stream key generation
* RTMP server integration
* Start/stop stream APIs
* Live viewer management
* Real-time chat
* Stream analytics
* Multi-platform streaming
* Admin dashboard
* JWT authentication
* Docker deployment
* Production WSGI server configuration

## 🎯 Project Objective

The main objective of this project is to develop a modular and scalable backend for a live streaming platform using Python, Flask, and MySQL. The architecture provides a foundation for integrating live video streaming, stream management, authentication, analytics, and other platform services.

## 👩‍💻 Author

**Sharmila SS**

Python | Data Analytics | AI/ML | Backend Development

## 📄 License

This project is intended for learning, development, and demonstration purposes.
