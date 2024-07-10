-- Drop existing priority table if it exists
DROP TABLE IF EXISTS priority;

-- Create the priority table with `id`, `when`, and `who` as primary keys
CREATE TABLE priority (
    id INT(11),
    `what` ENUM('P1', 'P2', 'P3', 'P4', 'P5', 'NONE'),
    `when` DATETIME,
    `who` INT(11),
    PRIMARY KEY (id, `when`, `who`)
);

-- Load data from CSV file into the priority table
LOAD DATA INFILE '/var/lib/mysql/Final_Project/Final_CSV-files/priority.csv'
INTO TABLE priority
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(id, `what`, @unix_time, `who`)
SET `when` = STR_TO_DATE(@unix_time, '%Y-%m-%d %H:%i:%s');
