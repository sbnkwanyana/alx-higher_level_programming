-- Creates the database hbtn_od_2 and user_0d_d if they do not exist. The grants user user_0d_2 select privileges on the hbtn_0d_2 database
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
