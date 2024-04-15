-- This script creates/updates and grants privileges to a user
-- Create or use the db hbnb_dev_db
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- create or update user hbnb_dev with pwd
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
-- grant all privileges
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
-- grant select privileges
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
