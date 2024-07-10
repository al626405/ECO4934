-- Drop existing severity table if it exists
DROP TABLE IF EXISTS severity;

-- Create the severity table with `id`, `when`, and `who` as primary keys
CREATE TABLE severity (
    id INT(11),
    `what` ENUM('trivial', 'minor', 'normal', 'enhancement', 'major', 'critical', 'blocker'),
    `when` DATETIME,
    `who` INT(11),
    PRIMARY KEY (id, `when`, `who`)
);

-- Load data from CSV file into the severity table
LOAD DATA INFILE '/var/lib/mysql/Final_Project/Final_CSV-files/severity.csv'
INTO TABLE severity
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(id, `what`, @unix_time, `who`)
SET `when` = STR_TO_DATE(@unix_time, '%Y-%m-%d %H:%i:%s');
