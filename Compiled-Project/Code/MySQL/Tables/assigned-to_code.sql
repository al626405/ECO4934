-- Drop existing assigned_to table if it exists
DROP TABLE IF EXISTS assigned_to;

CREATE TABLE assigned_to (
    increment_id INT(11) AUTO_INCREMENT PRIMARY KEY,
    id INT(11),
    `what` VARCHAR(1024),
    `when` DATETIME,
    `who` INT(11),
    UNIQUE KEY unique_when_who (id, `when`, `who`)
);

-- Load data from CSV file into the assigned_to table
LOAD DATA INFILE '/var/lib/mysql/Final_Project/Final_CSV-files/assigned_to.csv'
INTO TABLE assigned_to
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(id, `what`, @unix_time, `who`)
SET `when` = STR_TO_DATE(@unix_time, '%Y-%m-%d %H:%i:%s');