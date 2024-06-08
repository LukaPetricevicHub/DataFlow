CREATE DATABASE sales_db;

USE sales_db;

CREATE TABLE sales (
    sale_id INT AUTO_INCREMENT PRIMARY KEY,
    sale_date DATE,
    region VARCHAR(50),
    amount DECIMAL(10, 2)
);

INSERT INTO sales (sale_date, region, amount) VALUES
('2024-01-01', 'North', 1000.00),
('2024-01-02', 'South', 1500.00),
('2024-01-03', 'East', 800.00),
('2024-01-04', 'West', 1200.00);
