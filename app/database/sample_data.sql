INSERT INTO departments (department_name)
VALUES
('Cardiology'),
('Orthopedics'),
('Neurology'),
('Pediatrics');

INSERT INTO users (username, password_hash, role)
VALUES
('reception1', 'dummy_hash', 'Receptionist'),
('doctor1', 'dummy_hash', 'Doctor');

INSERT INTO doctors
(department_id, name, specialization, phone, consultation_fee)
VALUES
(1, 'Dr. Sharma', 'Cardiologist', '9876543210', 500),
(2, 'Dr. Patel', 'Orthopedic Surgeon', '9876543211', 700);

INSERT INTO patients
(name, age, gender, phone, address)
VALUES
('Rahul Verma', 25, 'Male', '9876543200', 'Mumbai'),
('Priya Singh', 30, 'Female', '9876543201', 'Delhi');

