ALTER TABLE reports DROP PRIMARY KEY;

ALTER TABLE reports
    MODIFY COLUMN current_status VARCHAR(100) NULL AFTER current_resolution,
    MODIFY COLUMN `when` BIGINT NOT NULL AFTER current_status;

ALTER TABLE reports ADD PRIMARY KEY (id, `when`, `who`);

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
(id, current_resolution, current_status, `when`, who)
SET current_resolution = NULLIF(current_resolution, ''),
    current_status = NULLIF(current_status, ''),
    `when` = NULLIF(`when`, ''),
    who = NULLIF(who, '');

-- Optionally, view the contents of the temporary table
SELECT * FROM temp_reports;

-- Once done, drop the temporary table
DROP TEMPORARY TABLE temp_reports;


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

-- Once done, drop the temporary table
DROP TEMPORARY TABLE temp_reports;
