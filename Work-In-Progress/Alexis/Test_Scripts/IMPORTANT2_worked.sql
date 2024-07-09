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

-- Optionally, view the contents of the temporary table
SELECT * FROM temp_reports;

-- Insert data from temp_reports into reports table
INSERT INTO reports (id, current_resolution, current_status, `when`, `who`)
SELECT id, current_resolution, current_status, `when`, `who`
FROM temp_reports;

-- Drop the temporary table
DROP TEMPORARY TABLE temp_reports;














--updated version from above
--Couldnt find an easy way to properly update the table with datetime variable, saved a temp csv and modified old one from the database of incorrect files.
--I decided to start with a database where variables were unintentionally wrong and corrected them as I went along modifying a general script.
--Additionally reports file had duplicates and missing values which lead to double commas (,,) instead of (,).
CREATE TEMPORARY TABLE temp_reports (
    id INT(11),
    current_resolution VARCHAR(100),
    current_status VARCHAR(100),
    `when` DATETIME,
    `who` INT(11)
);


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

DELETE FROM temp_reports
WHERE id IS NULL
   OR current_resolution IS NULL
   OR current_status IS NULL
   OR `when` IS NULL
   OR `who` IS NULL;


SELECT * 
INTO OUTFILE '/var/lib/mysql/Final_Project/UPDATED_FILES/reports.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
FROM temp_reports;
DROP TEMPORARY TABLE temp_reports;








--I couldnt find a way to do this its 3:12AM and I have work tommorow.
-- REPLACING OLD COLUMN IN DATABASE USING NEW CSV
CREATE TEMPORARY TABLE temp_reports (
    id INT(11),
    current_resolution VARCHAR(100),
    current_status VARCHAR(100),
    `when` DATETIME,
    `who` INT(11)
);

LOAD DATA INFILE '/var/lib/mysql/Final_Project/UPDATED_FILES/reports.csv'
INTO TABLE temp_reports
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(id, current_resolution, current_status, @unix_time, who)
SET `when` = FROM_UNIXTIME(@unix_time),
    current_resolution = NULLIF(current_resolution, ''),
    current_status = NULLIF(current_status, ''),
    who = NULLIF(who, '');

-- Start a transaction to ensure atomicity
START TRANSACTION;

-- Delete existing data from reports table
DELETE FROM reports;

-- Insert data from temp_reports into reports table
INSERT INTO reports (id, current_resolution, current_status, `when`, `who`)
SELECT id, current_resolution, current_status, `when`, `who`
FROM temp_reports;

-- Commit the transaction to apply changes
COMMIT;

DROP TEMPORARY TABLE temp_reports;
