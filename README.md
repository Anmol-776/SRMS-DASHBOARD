# 🚀 Startup Resource Management System

A professional web-based Startup Resource Management System developed using Flask, Python, Bootstrap, JSON Storage, and Multithreading. The system helps startups efficiently manage team members, tasks, resources, and operational monitoring through a centralized dashboard.

## 📌 Features

### Dashboard

* Total Team Members
* Active Tasks
* Completed Tasks
* Resource Availability
* Real-Time Statistics

### Team Management

* Add Members
* View Members
* Delete Members
* Department & Role Tracking

### Task Management

* Create Tasks
* Assign Tasks
* Set Priority Levels
* Mark Tasks as Completed
* Track Task Status

### Resource Management

* Add Resources
* Track Resource Availability
* Monitor Resource Usage

### Reports

* Project Overview
* Team & Task Summary
* Resource Monitoring Summary

## 🧵 Multithreading Implementation

The application uses Python multithreading to perform background operations without affecting UI responsiveness:

* Auto Backup Thread
* Deadline Monitoring Thread
* Resource Monitoring Thread

## 🛠️ Technologies Used

* Python
* Flask
* HTML5
* CSS3
* Bootstrap 5
* JSON
* Python Threading

## 📂 Project Structure

startup-resource-management-system/

├── app.py

├── storage.py

├── threads.py

├── data/

│ ├── employees.json

│ ├── tasks.json

│ └── resources.json

├── templates/

├── static/

└── README.md

## ▶️ How to Run

1. Install Flask

```bash
pip install flask
```

2. Run the application

```bash
python app.py
```

3. Open in browser

```text
http://127.0.0.1:5000
```

## 🔮 Future Enhancements

* User Authentication
* Database Integration (MySQL/PostgreSQL)
* Email Notifications
* PDF Report Generation
* Cloud Deployment
* Advanced Analytics Dashboard

## 👨‍💻 Developed By

Anmol Bansal
