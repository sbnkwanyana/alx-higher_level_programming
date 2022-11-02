-- creates the database htbn_0d_usa and table states with id not null that auto increments starting at the default value of 1
-- and sets the id as primary key. Has a name field that doest accept empty (NULL) values
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (id INT NOT NULL AUTO_INCREMENT, name VARCHAR(256) NOT NULL, PRIMARY KEY (id));
