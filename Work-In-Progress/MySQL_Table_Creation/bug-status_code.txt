-- Drop existing bug_status table (only if you need to recreate it)
DROP TABLE IF EXISTS bug_status;

-- Create the bug_status table with the desired structure
CREATE TABLE bug_status (
    id INT(11),
    `what` ENUM('unconfirmed', 'new', 'assigned', 'reopened', 'ready', 'resolved', 'verified'),
    `when` DATETIME,
    `who` INT(11),
    PRIMARY KEY (id)
);

-- Start a transaction to ensure atomicity
START TRANSACTION;

-- Create a temporary table to hold the data
CREATE TEMPORARY TABLE temp_bug_status (
    id INT(11),
    `what` ENUM('unconfirmed', 'new', 'assigned', 'reopened', 'ready', 'resolved', 'verified'),
    `when` DATETIME,
    `who` INT(11)
);

-- Load data from CSV file into the temporary table
LOAD DATA INFILE '/var/lib/mysql/Final_Project/T1/bug_status.csv'
INTO TABLE temp_bug_status
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(id, `what`, @unix_time, `who`)
SET `when` = FROM_UNIXTIME(@unix_time),
    `what` = NULLIF(`what`, ''),
    `who` = NULLIF(`who`, '');

-- Delete rows with NULL values in key columns from the temporary table
DELETE FROM temp_bug_status
WHERE id IS NULL
   OR `what` IS NULL
   OR `when` IS NULL
   OR `who` IS NULL;

-- Insert data from temporary table into the bug_status table
INSERT INTO bug_status (id, `what`, `when`, `who`)
SELECT id,
       CASE
           WHEN `what` NOT IN ('unconfirmed', 'new', 'assigned', 'reopened', 'ready', 'resolved', 'verified')
           THEN 'NONE'
           ELSE `what`
       END as `what`,
       `when`,
       `who`
FROM temp_bug_status
ON DUPLICATE KEY UPDATE
   `what` = VALUES(`what`),
   `when` = VALUES(`when`),
   `who` = VALUES(`who`);

-- Commit the transaction to apply changes
COMMIT;

-- Drop the temporary table
DROP TEMPORARY TABLE temp_bug_status;
-- Drop existing bug_status table (only if you need to recreate it)
DROP TABLE IF EXISTS bug_status;

-- Create the bug_status table with the desired structure
CREATE TABLE bug_status (
    id INT(11),
    `what` ENUM('unconfirmed', 'new', 'assigned', 'reopened', 'ready', 'resolved', 'verified'),
    `when` DATETIME,
    `who` INT(11),
    PRIMARY KEY (id, `when`, `who`)
);

-- Start a transaction to ensure atomicity
START TRANSACTION;

-- Create a temporary table to hold the data
CREATE TEMPORARY TABLE temp_bug_status (
    id INT(11),
    `what` VARCHAR(255), -- Use VARCHAR to accommodate all possible values before transformation
    `when` DATETIME,
    `who` INT(11)
);

-- Load data from CSV file into the temporary table
LOAD DATA INFILE '/var/lib/mysql/Final_Project/T1/bug_status.csv'
INTO TABLE temp_bug_status
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(id, `what`, @unix_time, `who`)
SET `when` = FROM_UNIXTIME(@unix_time),
    `what` = NULLIF(`what`, ''),
    `who` = NULLIF(`who`, '');

-- Delete rows with NULL values in key columns from the temporary table
DELETE FROM temp_bug_status
WHERE id IS NULL
   OR `what` IS NULL
   OR `when` IS NULL
   OR `who` IS NULL;

-- Insert data from temporary table into the bug_status table
INSERT INTO bug_status (id, `what`, `when`, `who`)
SELECT id,
       CASE
           WHEN `what` NOT IN ('unconfirmed', 'new', 'assigned', 'reopened', 'ready', 'resolved', 'verified')
           THEN 'unconfirmed'
           ELSE `what`
       END as `what`,
       `when`,
       `who`
FROM temp_bug_status
ON DUPLICATE KEY UPDATE
   `what` = VALUES(`what`),
   `when` = VALUES(`when`),
   `who` = VALUES(`who`);

-- Commit the transaction to apply changes
COMMIT;

-- Drop the temporary table
DROP TEMPORARY TABLE temp_bug_status;
