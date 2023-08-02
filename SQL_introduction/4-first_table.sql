-- Script that creates a table in the current database in MySQL
SHOW TABLES LIKE 'first_table';
CREATE TABLE IF NOT EXISTS  first_table  (
   id INT,
   name VARCHAR(256)
);
