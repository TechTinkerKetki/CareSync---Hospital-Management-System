# 🏥 CareSync

CareSync is a Hospital Management System built using **Python, FastAPI, PostgreSQL, and NeonDB** to digitize and streamline core hospital workflows. The system provides a centralized backend for managing patients, doctors, appointments, medical records, admissions, room allocation, billing, and administrative operations through a modular REST API architecture.

---

## ✨ Key Features

* Centralized management of patients, doctors, appointments, admissions, and billing
* Normalized relational database with 9 interconnected entities and foreign-key relationships
* RESTful API architecture built using FastAPI
* Medical record tracking with diagnosis and prescription management
* Automated room occupancy and patient admission workflows
* Billing and payment status management
* User authentication and role-based user records
* Hospital analytics dashboard with aggregated operational statistics

---

## 🛠️ Tech Stack

**Python • FastAPI • PostgreSQL • NeonDB • psycopg2 • Pydantic • Uvicorn • Git**

---

## 📊 Entity Relationship Diagram

```text
                    ┌──────────────┐
                    │ Departments  │
                    └──────┬───────┘
                           │
                           │
                    ┌──────▼───────┐
                    │   Doctors    │
                    └──────┬───────┘
                           │
                           │
         ┌─────────────────┴─────────────────┐
         │                                   │
         │                                   │
┌────────▼────────┐                ┌────────▼────────┐
│  Appointments   │───────────────►│ Medical Records │
└────────┬────────┘                └─────────────────┘
         │
         │
         │
┌────────▼────────┐
│    Patients     │
└────────┬────────┘
         │
         │
 ┌───────▼────────┐
 │   Admissions   │
 └───────┬────────┘
         │
         │
 ┌───────▼────────┐
 │     Rooms      │
 └────────────────┘

Appointments
      │
      │
      ▼
┌──────────────┐
│    Bills     │
└──────────────┘

Users → Authentication & Access Management
```

---

## 📁 Project Structure

```text
CareSync
│
├── app
│   ├── database
│   │   ├── db.py
│   │   ├── schema.sql
│   │   └── sample_data.sql
│   │
│   ├── routers
│   │   ├── auth.py
│   │   ├── patients.py
│   │   ├── doctors.py
│   │   ├── appointments.py
│   │   ├── medical_records.py
│   │   ├── rooms.py
│   │   ├── admissions.py
│   │   ├── bills.py
│   │   └── hospital.py
│   │
│   ├── config.py
│   └── main.py
│
├── requirements.txt
└── README.md
```

---

## 🚀 Getting Started

### Clone the Repository

```bash
git clone <repository-url>
cd CareSync
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Database

Update PostgreSQL credentials in:

```text
app/config.py
```

### Initialize Database

Execute:

```text
app/database/schema.sql
```

### Load Sample Data

Execute:

```text
app/database/sample_data.sql
```

### Run the Application

```bash
uvicorn app.main:app --reload
```

Server:

```text
http://127.0.0.1:8000
```

Interactive API Documentation:

```text
http://127.0.0.1:8000/docs
```

---

## 🔮 Scope for Improvement

### JWT-Based Authentication & Role-Based Access Control

Implement secure token-based authentication with role-specific permissions for administrators, doctors, and reception staff, ensuring controlled access to sensitive hospital data.

### Appointment Rescheduling & Notification System

Extend appointment workflows by supporting rescheduling, automated reminders, and status updates through email or SMS notifications.

### Analytics & Reporting Module

Introduce advanced hospital analytics such as patient trends, room occupancy rates, appointment statistics, and revenue reports to support operational decision-making.

```
```
