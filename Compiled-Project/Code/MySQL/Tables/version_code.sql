-- Drop existing version table if it exists
DROP TABLE IF EXISTS version;

-- Create the version table with `id`, `when`, and `who` as primary keys
CREATE TABLE version (
    id INT(11),
    `what` VARCHAR(10),
    `when` DATETIME,
    `who` INT(11),
    PRIMARY KEY (id, `when`, `who`)
);

-- Load data from CSV file into the version table
LOAD DATA INFILE '/var/lib/mysql/Final_Project/Final_CSV-files/version.csv'
INTO TABLE version
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(id, `what`, @unix_time, `who`)
SET `when` = STR_TO_DATE(@unix_time, '%Y-%m-%d %H:%i:%s');
