-- Drop existing version table (only if you need to recreate it)
DROP TABLE IF EXISTS version;

-- Create the version table with the desired structure
CREATE TABLE version (
    id INT(11),
    `what` VARCHAR(10),
    `when` DATETIME,
    `who` INT(11),
    PRIMARY KEY (id, `when`, `who`)
);

-- Start a transaction to ensure atomicity
START TRANSACTION;

-- Create a temporary table to hold the data
CREATE TEMPORARY TABLE temp_version (
    id INT(11),
    `what` VARCHAR(10),
    `when` DATETIME,
    `who` INT(11)
);

-- Load data from CSV file into the temporary table
LOAD DATA INFILE '/var/lib/mysql/Final_Project/T1/version.csv'
INTO TABLE temp_version
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(id, `what`, @unix_time, `who`)
SET `when` = FROM_UNIXTIME(@unix_time),
    `what` = NULLIF(`what`, ''),
    `who` = NULLIF(`who`, '');

-- Delete rows with NULL values in key columns from the temporary table
DELETE FROM temp_version
WHERE id IS NULL
   OR `what` IS NULL
   OR `when` IS NULL
   OR `who` IS NULL;

-- Insert unique data from temporary table into the version table
INSERT INTO version (id, `what`, `when`, `who`)
SELECT id,
       CASE
           WHEN `what` IS NULL THEN 'NONE'
           ELSE `what`
       END as `what`,
       `when`,
       `who`
FROM temp_version
GROUP BY id, `when`, `who`;  -- Ensure uniqueness for primary keys

-- Commit the transaction to apply changes
COMMIT;

-- Drop the temporary table
DROP TEMPORARY TABLE temp_version;
