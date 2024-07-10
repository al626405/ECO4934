-- Drop existing product table (only if you need to recreate it)
DROP TABLE IF EXISTS product;

-- Create the product table with the desired structure
CREATE TABLE product (
    id INT(11),
    `what` ENUM('Platform', 'JDT', 'CDT', 'EclipseLink'),
    `when` DATETIME,
    `who` INT(11),
    PRIMARY KEY (id, `when`, `who`)
);

-- Start a transaction to ensure atomicity
START TRANSACTION;

-- Create a temporary table to hold the data
CREATE TEMPORARY TABLE temp_product (
    id INT(11),
    `what` VARCHAR(100),
    `when` DATETIME,
    `who` INT(11)
);

-- Load data from CSV file into the temporary table
LOAD DATA INFILE '/var/lib/mysql/Final_Project/T1/product.csv'
INTO TABLE temp_product
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(id, `what`, @unix_time, `who`)
SET `when` = FROM_UNIXTIME(@unix_time),
    `what` = NULLIF(`what`, ''),
    `who` = NULLIF(`who`, '');

-- Delete rows with NULL values in key columns from the temporary table
DELETE FROM temp_product
WHERE id IS NULL
   OR `what` IS NULL
   OR `when` IS NULL
   OR `who` IS NULL;

-- Insert data from temporary table into the product table
INSERT INTO product (id, `what`, `when`, `who`)
SELECT id,
       CASE
           WHEN `what` NOT IN ('Platform', 'JDT', 'CDT', 'EclipseLink') THEN 'NONE'
           ELSE `what`
       END as `what`,
       `when`,
       `who`
FROM temp_product
ON DUPLICATE KEY UPDATE
   `what` = VALUES(`what`),
   `when` = VALUES(`when`),
   `who` = VALUES(`who`);

-- Commit the transaction to apply changes
COMMIT;

-- Drop the temporary table
DROP TEMPORARY TABLE temp_product;
