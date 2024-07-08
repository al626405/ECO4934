-- Drop existing cc table (only if you need to recreate it)
DROP TABLE IF EXISTS cc;

-- Create the cc table with the desired structure
CREATE TABLE cc (
    id INT(11),
    `what` VARCHAR(255),
    `when` DATETIME,
    `who` INT(11),
    PRIMARY KEY (id, `what`, `when`, `who`)
);

-- Start a transaction to ensure atomicity
START TRANSACTION;

-- Create a temporary table to hold the data
CREATE TEMPORARY TABLE temp_cc (
    id INT(11),
    `what` VARCHAR(255),
    `when` DATETIME,
    `who` INT(11)
);

-- Load data from CSV file into the temporary table
LOAD DATA INFILE '/var/lib/mysql/Final_Project/T1/cc.csv'
INTO TABLE temp_cc
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(id, `what`, @unix_time, `who`)
SET `when` = FROM_UNIXTIME(@unix_time),
    `what` = NULLIF(`what`, ''),
    `who` = NULLIF(`who`, '');

-- Delete rows with NULL values in key columns from the temporary table
DELETE FROM temp_cc
WHERE id IS NULL
   OR `what` IS NULL
   OR `when` IS NULL
   OR `who` IS NULL;

-- Remove duplicates in the temporary table
CREATE TEMPORARY TABLE deduped_cc AS
SELECT DISTINCT id, `what`, `when`, `who`
FROM temp_cc;

-- Insert data from deduped temporary table into the cc table
INSERT INTO cc (id, `what`, `when`, `who`)
SELECT id, `what`, `when`, `who`
FROM deduped_cc;

-- Commit the transaction to apply changes
COMMIT;

-- Drop the temporary tables
DROP TEMPORARY TABLE temp_cc;
DROP TEMPORARY TABLE deduped_cc;
