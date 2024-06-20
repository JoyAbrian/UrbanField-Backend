CREATE DATABASE urban_fields;
USE urban_fields;

CREATE TABLE users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(80) NOT NULL UNIQUE,
    password VARCHAR(120) NOT NULL,
    role ENUM('admin', 'customer') NOT NULL
);

CREATE TABLE field_types (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL
);

CREATE TABLE fields (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    type_id INT NOT NULL,
    location VARCHAR(100) NOT NULL,
    size VARCHAR(50) NOT NULL,
    price_per_hour FLOAT NOT NULL,
    status ENUM('available', 'booked') NOT NULL,
    FOREIGN KEY (type_id) REFERENCES field_types(id)
);

CREATE TABLE bookings (
    id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT NOT NULL,
    field_id INT NOT NULL,
    start_date DATETIME NOT NULL,
    end_date DATETIME NOT NULL,
    total_price FLOAT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (field_id) REFERENCES fields(id)
);

CREATE TABLE payments (
    id INT PRIMARY KEY AUTO_INCREMENT,
    booking_id INT NOT NULL,
    amount FLOAT NOT NULL,
    payment_date DATETIME NOT NULL,
    FOREIGN KEY (booking_id) REFERENCES bookings(id)
);

CREATE TABLE facilities (
    id INT PRIMARY KEY AUTO_INCREMENT,
    field_id INT NOT NULL,
    name VARCHAR(100) NOT NULL,
    description VARCHAR(255),
    FOREIGN KEY (field_id) REFERENCES fields(id)
);

CREATE TABLE user_document (
    id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT NOT NULL,
    document_number VARCHAR(50) NOT NULL,
    expiry_date DATETIME NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id)
);