-- Drop existing assigned_to table (only if you need to recreate it)
DROP TABLE IF EXISTS assigned_to;

-- Create the assigned_to table with the desired structure
CREATE TABLE assigned_to (
    id INT(11),
    `what` VARCHAR(255),
    `when` DATETIME,
    `who` INT(11),
    PRIMARY KEY (id, `what`, `when`, `who`)
);

-- Start a transaction to ensure atomicity
START TRANSACTION;

-- Create a temporary table to hold the data
CREATE TEMPORARY TABLE temp_assigned_to (
    id INT(11),
    `what` VARCHAR(255),
    `when` DATETIME,
    `who` INT(11)
);

-- Load data from CSV file into the temporary table
LOAD DATA INFILE '/var/lib/mysql/Final_Project/T1/assigned_to.csv'
INTO TABLE temp_assigned_to
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(id, `what`, @unix_time, `who`)
SET `when` = FROM_UNIXTIME(@unix_time),
    `what` = NULLIF(`what`, ''),
    `who` = NULLIF(`who`, '');

-- Delete rows with NULL values in key columns from the temporary table
DELETE FROM temp_assigned_to
WHERE id IS NULL
   OR `what` IS NULL
   OR `when` IS NULL
   OR `who` IS NULL;

-- Remove duplicates in the temporary table
CREATE TEMPORARY TABLE deduped_assigned_to AS
SELECT DISTINCT id, `what`, `when`, `who`
FROM temp_assigned_to;

-- Insert data from deduped temporary table into the assigned_to table
INSERT INTO assigned_to (id, `what`, `when`, `who`)
SELECT id, `what`, `when`, `who`
FROM deduped_assigned_to;
ON DUPLICATE KEY UPDATE
   `what` = VALUES(`what`),
   `when` = VALUES(`when`),
   `who` = VALUES(`who`);
-- Commit the transaction to apply changes
COMMIT;

-- Drop the temporary tables
DROP TEMPORARY TABLE temp_assigned_to;
DROP TEMPORARY TABLE deduped_assigned_to;
