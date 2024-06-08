CREATE DATABASE sales_dw;

USE sales_dw;

CREATE TABLE aggregated_sales (
    region STRING,
    total_amount DECIMAL(10, 2)
);
