# Live Detection Web App

## 📖 Project Overview

The **Live Detection Web App** is a machine learning project that uses a pre-trained model to classify real-time webcam images. Built using Python, TensorFlow, OpenCV, and Flask, this application allows users to interact with a live webcam feed and classify objects based on an image model.

---

## 🚀 Features

- **Live webcam feed** using OpenCV.
- **Real-time classification** of objects detected in the webcam stream using a pre-trained deep learning model.
- **User-friendly Web Interface** developed using Flask for easy interaction.
- **Optimized performance** using TensorFlow for deep learning model predictions.
- **Flexible design** with customizable CSS for UI enhancements.

---

## ⚙️ Technologies Used

- **Python 3.10**
- **TensorFlow** (Deep Learning)
- **OpenCV** (Computer Vision)
- **Flask** (Web Framework)
- **HTML/CSS** (Frontend)
- **NumPy** (Numerical Computing)

---

## 🛠️ Setup Instructions

### Prerequisites

1. **Python 3.10** or later installed on your machine.
2. **Git** installed for version control.
3. **Virtual environment** recommended for dependency management.

### Steps to Run the Application Locally

1. Clone the repository:

```bash
git clone https://github.com/<your-username>/Live-Detection.git
```
2. Navigate into the project directory:
   
```bash
cd Live-Detection
```

3. Create and activate a virtual environment:
   
```bash
python -m venv .venv
```   
Activate the virtual environment:
   On Windows:
  ```bash
.venv\Scripts\activate
```
4. Install the necessary dependencies:
```bash
pip install -r requirements.txt
```
5. Run the app:
```bash
python app.py
```
---

📑 File Structure
Live-Detection/
│
├── app.py                   # The main Flask application
├── model/                   # Directory containing the model file(s)
│   └── MN.h5                # Pre-trained model file
├── requirements.txt         # List of required Python dependencies
└── README.md                # Project documentation

---

⭐ Google Drive Link For Pre-Trained Model - https://drive.google.com/drive/folders/1u1aHIJMAUUfU83BMaBMsOUzADKuNCusu?usp=drive_link 

---

## 📋 requirements.txt
   Flask==2.1.1
   opencv-python==4.5.5.64
   tensorflow==2.8.0
   numpy==1.22.4

---

📜 License
This project is licensed under the MIT License - see the LICENSE file for details.

---

📝 Acknowledgments

```Thanks to TensorFlow for the powerful deep learning framework.``
```Thanks to Flask for making web development easy.``
```Thanks to OpenCV for enabling real-time image processing.``

---
