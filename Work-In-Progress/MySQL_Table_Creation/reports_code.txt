-- Drop existing reports table (only if you need to recreate it)
DROP TABLE IF EXISTS reports;

-- Create the reports table with the desired structure
CREATE TABLE reports (
    id INT(11),
    current_resolution VARCHAR(100),
    current_status VARCHAR(100),
    `when` DATETIME,
    `who` INT(11),
    PRIMARY KEY (id, `when`, `who`)
);

-- Create the temporary table with appropriate column definitions
CREATE TEMPORARY TABLE temp_reports (
    id INT(11),
    current_resolution VARCHAR(100),
    current_status VARCHAR(100),
    `when` DATETIME,
    `who` INT(11)
);

-- Load data from CSV file into the temporary table, handling empty values
LOAD DATA INFILE '/var/lib/mysql/Final_Project/T1/reports.csv'
INTO TABLE temp_reports
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(id, current_resolution, current_status, @unix_time, who)
SET `when` = FROM_UNIXTIME(@unix_time),
    current_resolution = NULLIF(current_resolution, ''),
    current_status = NULLIF(current_status, ''),
    who = NULLIF(who, '');

-- Delete rows with NULL values in key columns from the temporary table
DELETE FROM temp_reports
WHERE id IS NULL
   OR `when` IS NULL
   OR `who` IS NULL;

-- Insert data from temporary table into the reports table
INSERT INTO reports (id, current_resolution, current_status, `when`, `who`)
SELECT id,
       current_resolution,
       current_status,
       `when`,
       `who`
FROM temp_reports
ON DUPLICATE KEY UPDATE
   current_resolution = VALUES(current_resolution),
   current_status = VALUES(current_status),
   `when` = VALUES(`when`),
   `who` = VALUES(`who`);

-- Commit the transaction to apply changes
COMMIT;

-- Optionally, view the contents of the temporary table
SELECT * FROM temp_reports;

-- Once done, drop the temporary table
DROP TEMPORARY TABLE temp_reports;
