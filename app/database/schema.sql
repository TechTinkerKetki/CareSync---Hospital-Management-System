CREATE TABLE IF NOT EXISTS departments (
    department_id SERIAL PRIMARY KEY,
    department_name VARCHAR(100) UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS users (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    role VARCHAR(20) NOT NULL
);

CREATE TABLE IF NOT EXISTS doctors (
    doctor_id SERIAL PRIMARY KEY,

    department_id INTEGER NOT NULL,

    name VARCHAR(100) NOT NULL,
    specialization VARCHAR(100) NOT NULL,

    phone VARCHAR(15) UNIQUE,

    consultation_fee DECIMAL(10,2) NOT NULL,

    FOREIGN KEY (department_id)
    REFERENCES departments(department_id)
);

CREATE TABLE IF NOT EXISTS patients (
    patient_id SERIAL PRIMARY KEY,

    name VARCHAR(100) NOT NULL,

    age INTEGER NOT NULL,

    gender VARCHAR(10) NOT NULL,

    phone VARCHAR(15) UNIQUE,

    address TEXT,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS appointments (
    appointment_id SERIAL PRIMARY KEY,

    patient_id INTEGER NOT NULL,
    doctor_id INTEGER NOT NULL,

    appointment_date DATE NOT NULL,
    appointment_time TIME NOT NULL,

    status VARCHAR(20) DEFAULT 'Scheduled',

    FOREIGN KEY (patient_id)
    REFERENCES patients(patient_id),

    FOREIGN KEY (doctor_id)
    REFERENCES doctors(doctor_id)
);

CREATE TABLE IF NOT EXISTS medical_records (
    record_id SERIAL PRIMARY KEY,

    appointment_id INTEGER UNIQUE NOT NULL,

    patient_id INTEGER NOT NULL,

    doctor_id INTEGER NOT NULL,

    diagnosis TEXT NOT NULL,

    prescription TEXT,

    visit_date DATE DEFAULT CURRENT_DATE,

    FOREIGN KEY (appointment_id)
    REFERENCES appointments(appointment_id),

    FOREIGN KEY (patient_id)
    REFERENCES patients(patient_id),

    FOREIGN KEY (doctor_id)
    REFERENCES doctors(doctor_id)
);

CREATE TABLE IF NOT EXISTS rooms (
    room_id SERIAL PRIMARY KEY,

    room_number VARCHAR(20) UNIQUE NOT NULL,

    room_type VARCHAR(50) NOT NULL,

    availability_status VARCHAR(20)
    DEFAULT 'Available'
);

CREATE TABLE IF NOT EXISTS admissions (
    admission_id SERIAL PRIMARY KEY,

    patient_id INTEGER NOT NULL,

    room_id INTEGER NOT NULL,

    admission_date DATE NOT NULL,

    discharge_date DATE,

    FOREIGN KEY (patient_id)
    REFERENCES patients(patient_id),

    FOREIGN KEY (room_id)
    REFERENCES rooms(room_id)
);

CREATE TABLE IF NOT EXISTS bills (
    bill_id SERIAL PRIMARY KEY,

    appointment_id INTEGER UNIQUE NOT NULL,

    amount DECIMAL(10,2) NOT NULL,

    payment_status VARCHAR(20)
    DEFAULT 'Pending',

    payment_method VARCHAR(20),

    generated_at TIMESTAMP
    DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (appointment_id)
    REFERENCES appointments(appointment_id)
);