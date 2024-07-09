-- Drop existing resolution table (only if you need to recreate it)
DROP TABLE IF EXISTS resolution;

-- Create the resolution table with the desired structure
CREATE TABLE resolution (
    id INT(11),
    `what` ENUM('fixed', 'invalid', 'wontfix', 'duplicate', 'worksforme', 'incomplete'),
    `when` DATETIME,
    `who` INT(11),
    PRIMARY KEY (id, `when`, `who`)
);

-- Start a transaction to ensure atomicity
START TRANSACTION;

-- Create a temporary table to hold the data
CREATE TEMPORARY TABLE temp_resolution (
    id INT(11),
    `what` VARCHAR(100),
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

-- Insert data from temporary table into the resolution table
INSERT INTO resolution (id, `what`, `when`, `who`)
SELECT id,
       CASE
           WHEN `what` NOT IN ('fixed', 'invalid', 'wontfix', 'duplicate', 'worksforme', 'incomplete') THEN 'NONE'
           ELSE `what`
       END as `what`,
       `when`,
       `who`
FROM temp_resolution
ON DUPLICATE KEY UPDATE
   `what` = VALUES(`what`),
   `when` = VALUES(`when`),
   `who` = VALUES(`who`);

-- Commit the transaction to apply changes
COMMIT;

-- Drop the temporary table
DROP TEMPORARY TABLE temp_resolution;
