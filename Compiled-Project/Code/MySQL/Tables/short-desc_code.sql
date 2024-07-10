-- Drop existing short_desc table (only if you need to recreate it)
DROP TABLE IF EXISTS short_desc;

-- Create the short_desc table with the desired structure
CREATE TABLE short_desc (
    id INT(11),
    `what` VARCHAR(1024),  -- Change to VARCHAR with a sufficient length
    `when` DATETIME,
    `who` INT(11),
    PRIMARY KEY (id, `when`, `who`)
);

-- Start a transaction to ensure atomicity
START TRANSACTION;

-- Create a temporary table to hold the data
CREATE TEMPORARY TABLE temp_short_desc (
    id INT(11),
    `what` VARCHAR(255),
    `when` DATETIME,
    `who` INT(11)
);

-- Load data from CSV file into the temporary table
LOAD DATA INFILE '/var/lib/mysql/Final_Project/T1/short_desc_reformatted.csv'
INTO TABLE temp_short_desc
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(id, `what`, @unix_time, `who`)
SET `when` = STR_TO_DATE(@unix_time, '%Y-%m-%d %H:%i:%s'),
    `what` = NULLIF(`what`, '');

-- Delete rows with NULL values in key columns or with id value 0 from the temporary table
DELETE FROM temp_short_desc
WHERE id IS NULL
   OR `what` IS NULL
   OR `when` IS NULL
   OR `who` IS NULL
   OR id = 0;

-- Create a deduplicated temporary table with aggregated `what` values
CREATE TEMPORARY TABLE deduped_short_desc AS
SELECT id, GROUP_CONCAT(DISTINCT `what` ORDER BY `what` SEPARATOR ', ') AS `what`, `when`, `who`
FROM temp_short_desc
GROUP BY id, `when`, `who`;

-- Insert data into short_desc table
INSERT INTO short_desc (id, `what`, `when`, `who`)
SELECT id, `what`, `when`, `who`
FROM deduped_short_desc;

-- Commit the transaction to apply changes
COMMIT;

-- Drop the temporary tables
DROP TEMPORARY TABLE temp_short_desc;
DROP TEMPORARY TABLE deduped_short_desc;
