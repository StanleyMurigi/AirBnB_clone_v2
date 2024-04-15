--creating and or updating a db
--create or update hbnb_text_db
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
--add a user if they dont exist
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
--grant all privileges
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
--grant selected privileges
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';

