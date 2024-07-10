-- Drop existing op_sys table if it exists
DROP TABLE IF EXISTS op_sys;

-- Create the op_sys table with `id`, `when`, and `who` as primary keys
CREATE TABLE op_sys (
    id INT(11),
    `what` ENUM('AIX GTK', 'AIX Motif', 'All', 'HP-UX', 'Linux', 'Linux-GTK', 'Linux-Motif', 'Linux Qt', 'Mac OS', 'Mac OS X', 'MacOS X', 'Mac OS X - Cocoa', 'Neutrino', 'other', 'Other', 'QNX-Photon', 'Solaris', 'Solaris-GTK', 'Solaris-Motif', 'SymbianOS S60', 'SymbianOS-Series 80', 'Symbian Qt', 'Unix All', 'what', 'Windows 2000', 'Windows 2003 Server', 'Windows 7', 'Windows 95', 'Windows 98', 'Windows All', 'Windows CE', 'Windows Me', 'Windows ME', 'Windows Mobile 2003', 'Windows Mobile 5.0', 'Windows NT', 'Windows Server 2003', 'Windows Server 2008', 'Windows Vista', 'Windows Vista Beta 2', 'Windows Vista-WPF', 'Windows XP'),
    `when` DATETIME,
    `who` INT(11),
    PRIMARY KEY (id, `when`, `who`)
);

-- Load data from CSV file into the op_sys table
LOAD DATA INFILE '/var/lib/mysql/Final_Project/Final_CSV-files/op_sys.csv'
INTO TABLE op_sys
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(id, `what`, @unix_time, `who`)
SET `when` = STR_TO_DATE(@unix_time, '%Y-%m-%d %H:%i:%s');
