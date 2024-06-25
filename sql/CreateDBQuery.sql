DROP DATABASE IF EXISTS urban_fields;
CREATE DATABASE urban_fields;
USE urban_fields;

CREATE TABLE users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(80) NOT NULL UNIQUE,
    password VARCHAR(120) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    phone_number VARCHAR(20) NOT NULL UNIQUE,
    user_document VARCHAR(255),
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
    city VARCHAR(100) NOT NULL,
    address VARCHAR(100) NOT NULL,
    street_address VARCHAR(100),
    image_url VARCHAR(255) NOT NULL,
    image_url2 VARCHAR(255) NOT NULL,
    image_url3 VARCHAR(255) NOT NULL,
    price_per_hour INT(10) NOT NULL,
    opening_time TIME NOT NULL,
    closing_time TIME NOT NULL,
    FOREIGN KEY (type_id) REFERENCES field_types(id)
);

CREATE TABLE facilities (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    icon VARCHAR(255) NOT NULL
);

CREATE TABLE field_facility (
    id INT PRIMARY KEY AUTO_INCREMENT,
    field_id INT NOT NULL,
    facility_id INT NOT NULL,
    FOREIGN KEY (field_id) REFERENCES fields(id),
    FOREIGN KEY (facility_id) REFERENCES facilities(id)
);

CREATE TABLE field_review (
    id INT PRIMARY KEY AUTO_INCREMENT,
    field_id INT NOT NULL,
    user_id INT NOT NULL,
    rating INT NOT NULL,
    review TEXT NOT NULL,
    FOREIGN KEY (field_id) REFERENCES fields(id),
    FOREIGN KEY (user_id) REFERENCES users(id)
);

CREATE TABLE payment_methods (
    id INT PRIMARY KEY AUTO_INCREMENT,
    method VARCHAR(50) NOT NULL,
    icon VARCHAR(255) NOT NULL
);

CREATE TABLE bookings (
    id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT NOT NULL,
    field_id INT NOT NULL,
    date DATETIME NOT NULL,
    time TIME NOT NULL,
    payment_method_id INT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (field_id) REFERENCES fields(id),
    FOREIGN KEY (payment_method_id) REFERENCES payment_methods(id)
);