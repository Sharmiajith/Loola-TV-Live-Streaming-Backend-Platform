# Loola TV – Live Streaming Backend

## 📌 Project Overview

Loola TV is a Python-based backend project for managing a live streaming platform. The project uses **Flask** to build REST APIs, **MySQL** to store and manage live stream information, **WebSocket** for real-time communication, and **FFmpeg** for video and audio stream processing.

The backend follows a structured **Route → Controller → Model → Database** architecture, making the application easier to maintain and extend.

## 🚀 Features

* Live stream management
* REST API development using Flask
* MySQL database integration
* Stream information storage and retrieval
* Route, Controller, and Model architecture
* JSON-based API responses
* **WebSocket-based real-time communication**
* **Real-time viewer count and stream status updates**
* **FFmpeg-based video and audio processing**
* **RTMP stream processing foundation**
* Modular backend project structure

## 🛠️ Technologies Used

* **Python** – Backend programming
* **Flask** – REST API development
* **MySQL** – Database management
* **XAMPP** – Local MySQL server environment
* **WebSocket / Flask-SocketIO** – Real-time communication
* **FFmpeg** – Video and audio processing
* **REST API** – Client-server communication
* **VS Code** – Development environment
* **Git & GitHub** – Version control

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
├── streaming/
│   └── ffmpeg_service.py
│
├── websocket/
│   └── socket_service.py
│
└── README.md
```

## 🔄 Backend Architecture

```text
                         Client
                           │
                           ▼
                    Flask REST API
                           │
                           ▼
                         Routes
                           │
                           ▼
                      Controllers
                           │
                           ▼
                         Models
                           │
                           ▼
                    MySQL Database


                    LIVE STREAMING
                         
Streamer / OBS
      │
      │ RTMP
      ▼
Streaming Server
      │
      ▼
    FFmpeg
      │
      ├── Video Processing
      ├── Audio Processing
      └── Stream Conversion
      │
      ▼
   Live Stream
      │
      ▼
    Viewers


                    REAL-TIME DATA

Viewer / Streamer
        │
        ▼
     WebSocket
        │
        ├── Live Chat
        ├── Viewer Count
        ├── Stream Status
        └── Notifications
```

### Request Flow

1. Client sends an API request.
2. Flask route receives the request.
3. Controller processes the request.
4. Model communicates with the database.
5. MySQL returns the required data.
6. Flask sends a JSON response to the client.

### Live Streaming Flow

1. Streamer sends a live video using OBS or another streaming application.
2. The stream is received through an RTMP endpoint.
3. FFmpeg processes the video and audio stream.
4. The processed stream is prepared for delivery to viewers.
5. WebSocket handles real-time events such as viewer count, chat, and stream status.

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
pip install flask
pip install mysql-connector-python
pip install flask-socketio
```

## 🎥 FFmpeg Installation

FFmpeg is used for processing live video and audio streams.

After installing FFmpeg, verify the installation:

```bash
ffmpeg -version
```

If FFmpeg is installed correctly, the terminal will display the FFmpeg version and configuration details.

### Example FFmpeg Command

```bash
ffmpeg -re -i input.mp4 -c:v libx264 -c:a aac -f flv rtmp://localhost/live/test
```

This command reads a video file, processes the video and audio, and sends the output to an RTMP streaming endpoint.

### Python FFmpeg Integration

```python
import subprocess

def start_stream(input_file, rtmp_url):

    command = [
        "ffmpeg",
        "-re",
        "-i", input_file,
        "-c:v", "libx264",
        "-c:a", "aac",
        "-f", "flv",
        rtmp_url
    ]

    process = subprocess.Popen(command)

    return process
```

## 🔌 WebSocket

WebSocket provides a persistent connection between the client and server for real-time communication.

In the Loola TV backend, WebSocket can be used for:

* Live chat
* Real-time viewer count
* Stream status updates
* Notifications
* Live interaction events

### Flask-SocketIO Example

```python
from flask_socketio import SocketIO

socketio = SocketIO(app)

@socketio.on("message")
def handle_message(data):

    print("Message received:", data)

    socketio.emit(
        "message",
        data
    )
```

The WebSocket connection allows the server to send updates to connected clients without requiring continuous HTTP requests.

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

Start **MySQL** from XAMPP and make sure FFmpeg is available in your system PATH.

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

## 📡 WebSocket Events

Example WebSocket events that can be implemented:

| Event            | Purpose                             |
| ---------------- | ----------------------------------- |
| `message`        | Send and receive chat messages      |
| `viewer_update`  | Update live viewer count            |
| `stream_started` | Notify clients when a stream starts |
| `stream_stopped` | Notify clients when a stream stops  |
| `notification`   | Send real-time notifications        |

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

WebSocket functionality can be tested using a compatible WebSocket client or a frontend application connected to the Flask-SocketIO server.

## 🔮 Future Enhancements

* User registration and authentication
* JWT authentication
* Stream key generation
* RTMP server integration
* Start/stop stream APIs
* Live viewer management
* Real-time chat
* Stream analytics
* Multi-platform streaming
* YouTube/Facebook/Twitch integration
* Stream recording using FFmpeg
* Multiple video quality/transcoding support
* Admin dashboard
* Docker deployment
* Production WSGI server configuration

## 🎯 Project Objective

The main objective of this project is to develop a modular and scalable backend for a live streaming platform using **Python, Flask, MySQL, WebSocket, and FFmpeg**.

The architecture provides a foundation for integrating **live video streaming, stream management, real-time communication, authentication, analytics, multimedia processing, and other platform services**.

## 👩‍💻 Author

**Sharmila SS**

Python | Data Analytics | AI/ML | Backend Development

## 📄 License

This project is intended for learning, development, and demonstration purposes.
