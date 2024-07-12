-- Drop existing resolution table (only if you need to recreate it)
DROP TABLE IF EXISTS resolution;

-- Create the resolution table with the desired structure
CREATE TABLE resolution (
    id INT(11) AUTO_INCREMENT PRIMARY KEY,
    `what` ENUM('fixed', 'invalid', 'wontfix', 'duplicate', 'worksforme', 'incomplete'),
    `when` DATETIME,
    `who` INT(11)
);

-- Load data from CSV file into the resolution table
LOAD DATA INFILE '/var/lib/mysql/Final_Project/Final_CSV-files/resolution.csv'
INTO TABLE resolution
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(id, `what`, @unix_time, `who`)
SET `when` = STR_TO_DATE(@unix_time, '%Y-%m-%d %H:%i:%s');
