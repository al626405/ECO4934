-- Drop existing resolution table if it exists
DROP TABLE IF EXISTS resolution;

-- Create the resolution table with `(id, `when`, `who`)` as the primary key
CREATE TABLE resolution (
    id INT(11),
    `what` ENUM('DUPLICATE', 'FIXED', 'WORKSFORME', 'INVALID', 'WONTFIX', 'REMIND', 'LATER', 'NOT_ECLIPSE'),
    `when` DATETIME,
    `who` INT(11),
    PRIMARY KEY (id, `what`, `when`, `who`)
);

-- Start a transaction to ensure atomicity
START TRANSACTION;

-- Create a temporary table to hold the data
CREATE TEMPORARY TABLE temp_resolution (
    id INT(11),
    `what` ENUM('DUPLICATE', 'FIXED', 'WORKSFORME', 'INVALID', 'WONTFIX', 'REMIND', 'LATER', 'NOT_ECLIPSE'),
    `when` DATETIME,
    `who` INT(11)
);

-- Load data from CSV file into the temporary table
LOAD DATA INFILE '/var/lib/mysql/Final_Project/T1/resolution.csv'
INTO TABLE temp_resolution
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(id, `what`, @unix_time, `who`)
SET `when` = FROM_UNIXTIME(@unix_time),
    `what` = NULLIF(`what`, ''),
    `who` = NULLIF(`who`, '');

-- Delete rows with NULL values in key columns from the temporary table
DELETE FROM temp_resolution
WHERE id IS NULL
   OR `what` IS NULL
   OR `when` IS NULL
   OR `who` IS NULL;

-- Remove duplicates in the temporary table
CREATE TEMPORARY TABLE deduped_resolution AS
SELECT DISTINCT id, `what`, `when`, `who`
FROM temp_resolution;

-- Insert data from deduped temporary table into the resolution table
INSERT INTO resolution (id, `what`, `when`, `who`)
SELECT id, `what`, `when`, `who`
FROM deduped_resolution
ON DUPLICATE KEY UPDATE
    `what` = VALUES(`what`);

-- Commit the transaction to apply changes
COMMIT;

-- Drop the temporary tables
DROP TEMPORARY TABLE temp_resolution;
DROP TEMPORARY TABLE deduped_resolution;

SELECT * 
INTO OUTFILE '/var/lib/mysql/Final_Project/Final_CSV-files/resolution_cleaned.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
FROM resolution;

-- Drop existing resolution table if it exists
DROP TABLE IF EXISTS resolution;

-- Create the resolution table with `increment_id` as an AUTO_INCREMENT primary key
CREATE TABLE resolution (
    increment_id INT(11) AUTO_INCREMENT PRIMARY KEY,
    id INT(11),
    `what` ENUM('DUPLICATE', 'FIXED', 'WORKSFORME', 'INVALID', 'WONTFIX', 'REMIND', 'LATER', 'NOT_ECLIPSE'),
    `when` DATETIME,
    `who` INT(11),
    UNIQUE KEY unique_resolution (id, `what`, `when`, `who`)
);

LOAD DATA INFILE '/var/lib/mysql/Final_Project/Final_CSV-files/resolution_cleaned.csv'
INTO TABLE resolution
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
(id, `what`, @unix_time, `who`)
SET `when` = STR_TO_DATE(@unix_time, '%Y-%m-%d %H:%i:%s');

