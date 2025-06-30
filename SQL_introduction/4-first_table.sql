-- creates a table called first_table in the current database

USE hbtn_test_db_4;

CREATE TABLE IF NOT EXISTS first_table (

    id INT
    name VARCHAR(256)

INSERT INTO first_table (id, name) VALUES (1, 'Alice'), (2, 'Bob');
SELECT COUNT(id) FROM first_table;
);

