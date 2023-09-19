-- Create a MySQL database for the project (if it doesn't already exist) in the development environment
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Create a MySQL user for the project (if it doesn't already exist) in the development environment
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Grant all privileges on the hbnb_dev_db database to the 'hbnb_dev' user in the development environment
GRANT ALL PRIVILEGES ON `hbnb_dev_db`.* TO 'hbnb_dev'@'localhost';

-- Grant SELECT privilege on the performance_schema to the 'hbnb_dev' user in the development environment
GRANT SELECT ON `performance_schema`.* TO 'hbnb_dev'@'localhost';

-- Flush privileges to apply the changes
FLUSH PRIVILEGES;
