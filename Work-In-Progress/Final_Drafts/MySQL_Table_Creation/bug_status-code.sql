-- Drop existing bug_status table if it exists
DROP TABLE IF EXISTS bug_status;

-- Create the bug_status table with `(id, `when`, `who`)` as the primary key
CREATE TABLE bug_status (
    id INT(11),
    `what` ENUM('unconfirmed', 'new', 'assigned', 'reopened', 'ready', 'resolved', 'verified','closed'),
    `when` DATETIME,
    `who` INT(11),
    PRIMARY KEY (id, `what`, `when`, `who`)
);

-- Start a transaction to ensure atomicity
START TRANSACTION;

-- Create a temporary table to hold the data
CREATE TEMPORARY TABLE temp_bug_status (
    id INT(11),
    `what` ENUM('unconfirmed', 'new', 'assigned', 'reopened', 'ready', 'resolved', 'verified','closed'),
    `when` DATETIME,
    `who` INT(11)
);

-- Load data from CSV file into the temporary table
LOAD DATA INFILE '/var/lib/mysql/Final_Project/T1/bug_status.csv'
INTO TABLE temp_bug_status
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(id, `what`, @unix_time, `who`)
SET `when` = FROM_UNIXTIME(@unix_time),
    `what` = NULLIF(`what`, ''),
    `who` = NULLIF(`who`, '');

-- Delete rows with NULL values in key columns from the temporary table
DELETE FROM temp_bug_status
WHERE id IS NULL
   OR `what` IS NULL
   OR `when` IS NULL
   OR `who` IS NULL;

-- Remove duplicates in the temporary table
CREATE TEMPORARY TABLE deduped_bug_status AS
SELECT DISTINCT id, `what`, `when`, `who`
FROM temp_bug_status;

-- Insert data from deduped temporary table into the bug_status table
INSERT INTO bug_status (id, `what`, `when`, `who`)
SELECT id, `what`, `when`, `who`
FROM deduped_bug_status
ON DUPLICATE KEY UPDATE
    `what` = VALUES(`what`);

-- Commit the transaction to apply changes
COMMIT;

-- Drop the temporary tables
DROP TEMPORARY TABLE temp_bug_status;
DROP TEMPORARY TABLE deduped_bug_status;





SELECT * 
INTO OUTFILE '/var/lib/mysql/Final_Project/Final_CSV-files/bug_status_cleaned.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
FROM bug_status;




-- Drop existing bug_status table if it exists
DROP TABLE IF EXISTS bug_status;

-- Create the bug_status table with `increment_id` as an AUTO_INCREMENT primary key
CREATE TABLE bug_status (
    increment_id INT(11) AUTO_INCREMENT PRIMARY KEY,
    id INT(11),
    `what` ENUM('unconfirmed', 'new', 'assigned', 'reopened', 'ready', 'resolved', 'verified','closed'),
    `when` DATETIME,
    `who` INT(11),
    UNIQUE KEY unique_bug_status (id, `what`, `when`, `who`)
);

LOAD DATA INFILE '/var/lib/mysql/Final_Project/Final_CSV-files/bug_status_cleaned.csv'
INTO TABLE bug_status
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
(id, `what`, @unix_time, `who`)
SET `when` = STR_TO_DATE(@unix_time, '%Y-%m-%d %H:%i:%s');

