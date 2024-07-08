-- Drop existing severity table (only if you need to recreate it)
DROP TABLE IF EXISTS severity;

-- Create the severity table with the desired structure
CREATE TABLE severity (
    id INT(11),
    `what` ENUM('trivial', 'minor', 'normal', 'enhancement', 'major', 'critical', 'blocker'),
    `when` DATETIME,
    `who` INT(11),
    PRIMARY KEY (id, `when`, `who`)
);

-- Start a transaction to ensure atomicity
START TRANSACTION;

-- Create a temporary table to hold the data
CREATE TEMPORARY TABLE temp_severity (
    id INT(11),
    `what` ENUM('trivial', 'minor', 'normal', 'enhancement', 'major', 'critical', 'blocker'),
    `when` DATETIME,
    `who` INT(11)
);

-- Load data from CSV file into the temporary table
LOAD DATA INFILE '/var/lib/mysql/Final_Project/T1/severity.csv'
INTO TABLE temp_severity
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(id, `what`, @unix_time, `who`)
SET `when` = FROM_UNIXTIME(@unix_time),
    `what` = NULLIF(`what`, ''),
    `who` = NULLIF(`who`, '');

-- Delete rows with NULL values in key columns from the temporary table
DELETE FROM temp_severity
WHERE id IS NULL
   OR `what` IS NULL
   OR `when` IS NULL
   OR `who` IS NULL;

-- Insert data from temporary table into the severity table
INSERT INTO severity (id, `what`, `when`, `who`)
SELECT id,
       CASE
           WHEN `what` NOT IN ('trivial', 'minor', 'normal', 'enhancement', 'major', 'critical', 'blocker') THEN 'NONE'
           ELSE `what`
       END as `what`,
       `when`,
       `who`
FROM temp_severity
GROUP BY id, `when`, `who`;  -- Ensure uniqueness for primary keys

-- Commit the transaction to apply changes
COMMIT;

-- Drop the temporary table
DROP TEMPORARY TABLE temp_severity;
