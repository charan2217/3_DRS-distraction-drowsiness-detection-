# 3DRS: Driver Distraction Detection and Recovery System 🚗🧠

An AI-powered system for real-time detection and feedback of driver distraction using computer vision and audio. Built to enhance road safety by identifying behaviors like drowsiness and phone usage, and responding with alerts and violation tracking.

---

## 📌 Features

- 🔍 **Drowsiness Detection** using Eye Aspect Ratio (EAR) via facial landmarks
- 📱 **Phone Usage Detection** using YOLOv8-based object detection
- 🔊 **Speech Alerts & Visual Feedback** with pyttsx3 and Streamlit
- 📈 **Violation Counters** for tracking distraction types
- 🎛️ **Interactive Streamlit GUI** for real-time monitoring
- 🚫 No external CSV logs – counters update live in GUI

---

## 🎯 Use Case

Designed for integration into **ADAS (Advanced Driver Assistance Systems)** or in-cabin safety modules for:

- Commercial fleet safety monitoring
- Research in cognitive state estimation
- Driver fatigue monitoring systems

---

## 📁 Project Structure

```bash
3DRS/
├── models/
│   └── yolov8_custom_phone.pt        # YOLOv8 model for phone detection
├── haarcascades/
│   └── haarcascade_frontalface.xml   # Face detection
├── drowsiness_detection.py
├── phone_detection.py
├── streamlit_app.py                  # Main GUI app
├── requirements.txt
└── README.md
#⚙️ Tech Stack
Languages: Python

Libraries: OpenCV, dlib, pyttsx3, Streamlit, YOLOv8 (Ultralytics)

Models: EAR for drowsiness, YOLOv8 for phone detection

#🚀 How to Run
1. Clone the repository
bash
Copy
Edit
git clone https://github.com/yourusername/3DRS.git
cd 3DRS
2. Install requirements
bash
Copy
Edit
pip install -r requirements.txt
3. Run the Streamlit GUI
bash
Copy
Edit
streamlit run streamlit_app.py
##🧠 Methodology
Drowsiness Detection:
Uses dlib to detect facial landmarks

Calculates Eye Aspect Ratio (EAR)

If EAR < threshold for a sustained time, triggers alert

##Phone Detection:
Custom-trained YOLOv8 model

Detects phone in hand or near ear

On detection, GUI shows warning and increments phone violation counter


##📌 Future Work
Integrate voice emotion detection (optional)

Add ROS2 support for automotive-grade deployment

Use vehicle CAN data (speed, RPM, etc.) for state-aware alerts

Export logs and violation summaries to cloud dashboard

##👤 Author
Parava Charan

📫 paravacharanreddy4@gmail.com
