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
LOAD DATA INFILE '/var/lib/mysql/Final_Project/Final_CSV-files/reports.csv'
INTO TABLE temp_reports
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(id, current_resolution, current_status, @unix_time, who)
SET `when` = STR_TO_DATE(@unix_time, '%Y-%m-%d %H:%i:%s'),
    current_resolution = NULLIF(current_resolution, ''),
    current_status = NULLIF(current_status, ''),
    `who` = NULLIF(`who`, '');

-- Delete rows with NULL values in key columns from the temporary table
DELETE FROM temp_reports
WHERE id IS NULL
   OR `when` IS NULL
   OR `who` IS NULL;

-- Create deduped_reports as a temporary table to hold deduplicated data
CREATE TEMPORARY TABLE deduped_reports AS
SELECT DISTINCT id, current_resolution, current_status, `when`, `who`
FROM temp_reports;

-- Insert data from deduped temporary table into the reports table
INSERT INTO reports (id, current_resolution, current_status, `when`, `who`)
SELECT id,
       current_resolution,
       current_status,
       `when`,
       `who`
FROM deduped_reports
ON DUPLICATE KEY UPDATE
   current_resolution = VALUES(current_resolution),
   current_status = VALUES(current_status),
   `when` = VALUES(`when`),
   `who` = VALUES(`who`);

-- Commit the transaction to apply changes
COMMIT;

-- Optionally, view the contents of the temporary table for debugging
SELECT * FROM temp_reports LIMIT 10;

-- Once done, drop the temporary tables
DROP TEMPORARY TABLE temp_reports;
DROP TEMPORARY TABLE deduped_reports;
