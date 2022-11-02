-- creates the database if it does not exist
-- creates the table cities if it does not exist with the fields id auto generated and not null and is the primary key
-- with field integer state_id not null and the foregin key field from the states table
-- with field name of type string and not null
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities (id INT NOT NULL AUTO_INCREMENT, state_id INT NOT NULL,name VARCHAR(256) NOT NULL, PRIMARY KEY (id), FOREIGN KEY (state_id) REFERENCES states(id));
