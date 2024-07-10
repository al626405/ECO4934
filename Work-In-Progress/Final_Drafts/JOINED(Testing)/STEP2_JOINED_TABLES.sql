-- Alexis Leclerc
-- 07/09/2024
--Step 2: Load Data from CSV Files into Temporary Tables

-- Start a transaction to ensure atomicity
START TRANSACTION;

-- Create temporary tables to hold data from the CSV files with prefixed column names
CREATE TEMPORARY TABLE temp_bug_status (
    bug_status_id INT(11),
    bug_status_what ENUM('unconfirmed', 'new', 'assigned', 'reopened', 'ready', 'resolved', 'verified', 'closed'),
    bug_status_when DATETIME,
    bug_status_who INT(11)
);

CREATE TEMPORARY TABLE temp_resolution (
    resolution_id INT(11),
    resolution_what ENUM('DUPLICATE', 'FIXED', 'WORKSFORME', 'INVALID', 'WONTFIX', 'REMIND', 'LATER', 'NOT_ECLIPSE'),
    resolution_when DATETIME,
    resolution_who INT(11)
);

CREATE TEMPORARY TABLE temp_assigned_to (
    assigned_to_id INT(11),
    assigned_to_what VARCHAR(1024),
    assigned_to_when DATETIME,
    assigned_to_who INT(11)
);

CREATE TEMPORARY TABLE temp_priority (
    priority_id INT(11),
    priority_what ENUM('P1', 'P2', 'P3', 'P4', 'P5', 'NONE'),
    priority_when DATETIME,
    priority_who INT(11)
);

CREATE TEMPORARY TABLE temp_severity (
    severity_id INT(11),
    severity_what ENUM('trivial', 'minor', 'normal', 'enhancement', 'major', 'critical', 'blocker'),
    severity_when DATETIME,
    severity_who INT(11)
);

CREATE TEMPORARY TABLE temp_op_sys (
    op_sys_id INT(11),
    op_sys_what ENUM('AIX GTK', 'AIX Motif', 'All', 'HP-UX', 'Linux', 'Linux-GTK', 'Linux-Motif', 'Linux Qt', 'Mac OS', 'Mac OS X', 'MacOS X', 'Mac OS X - Cocoa', 'Neutrino', 'other', 'Other', 'QNX-Photon', 'Solaris', 'Solaris-GTK', 'Solaris-Motif', 'SymbianOS S60', 'SymbianOS-Series 80', 'Symbian Qt', 'Unix All', 'what', 'Windows 2000', 'Windows 2003 Server', 'Windows 7', 'Windows 95', 'Windows 98', 'Windows All', 'Windows CE', 'Windows Me', 'Windows ME', 'Windows Mobile 2003', 'Windows Mobile 5.0', 'Windows NT', 'Windows Server 2003', 'Windows Server 2008', 'Windows Vista', 'Windows Vista Beta 2', 'Windows Vista-WPF', 'Windows XP'),
    op_sys_when DATETIME,
    op_sys_who INT(11)
);

CREATE TEMPORARY TABLE temp_component (
    component_id INT(11),
    component_what ENUM('accservice','AI','alf-core','alf-tools','All','Annotations','Ant','API Tools','App','apps.eclipse.org','APT','Architecture Council','Articles','ASF.Runtime','ATL-UI','Autotools','Bugzilla','Build','Build/Web','bundles','Bundles','Callisto','CDateTime','CDE','cdt-build','cdt-build-managed','cdt-codan','CDT-Contrib','cdt-core','cdt-cppunit','cdt-debug','cdt-debug-cdi','cdt-debug-cdi-gdb','cdt-debug-dsf','cdt-debug-dsf-gdb','cdt-debug-edc','cdt-doc','cdt-editor','cdt-indexer','cdt-launch','cdt-memory','cdt-other','cdt-parser','CDT-parser','cdt-refactoring','cdt-releng','cdt-source-nav','Cell','Chart','CME','Code Assist','Codegen','CommitterTools','Compare','Compendium','Components','CompositeTable','Connection Mgt Framework','Connectivity','core','Core','Cpp-Extensions','cpp-package','Cross-project','Cross-Project','CVS','Data Source Explorer','DataTools','DD','Debug','Debugger','Debug-MI','Debug-UI','Demo','deprecated2','deprecated3','deprecated4','deprecated5','deprecated6','deprecated7','Desktop','DevTools','Doc','DOC','Docs','documentation','Documentation','draw2d','DSF','Dynamic Plugins','e4','ecf.core','ecf.doc','ecf.filetransfer','EclipseBot','EclipseCon','Edit','Editor','EEF','eJFace','EnglishStrings','eSWT','eWorkbench','Examples','Faceted Project Framework','FAQ','Forums and Newsgroups','Foundation','Framework','GDB','geclipse','GEF','General','General UI','Generic-Extensions','Help','Hudson','Hyades','IDE','Incubator','Incubators','Intro','IPZilla','J2EE Standard Tools','Java','Javaco','Java Core','Java Model (JEM)','java-package','jee-package','Jet','JET','JFace','JFC/Swing','Jira','jst.ejb','jst.j2ee','jst.jsp','jst.server','jst.servlet','jst.ws','Launcher','LinuxDistros','LPEX','Mapping','Marketplace','Memory','MI','Models - Graphical','Monitor.UI','Monitor.UI.GLARules','Monitor.UI.SDBEditor','mozide','Mozilla','MTJ projects','newsgroups','Newsgroups','OAW','org.eclipse.stp.bpmn','OSGi','Other','Outline Views','p2','package content','Phoenix','PHP Explorer View','PHP Search','Platform.Analysis','Platform.Collection','Platform.Communication','Platform.Execution','Platform.LineCoverage.Runtime','Platform.Model','Platform.UI','Platform.UI.ProfilingPerspective','Platform.UI.SequenceDiagram','Platform.UI.StatsPerfViewers','PLDT','Plugins','PMC','Portal','Prereq','Problems view','Process','Project Management','RDT','releng','Releng','Report','Report Designer','Report Viewer','Repository','Resources','RSE','Runtime','Runtime Common','Runtime Diagram','Scripting','Search','Security','Server','Server-Side','SQLDevTools','SQL Editor Framework','SWT','SWTBot','Table Data Editor','Tasks','Team','Teneo','Test.Agents','Test.Execution','Test.Execution.JUnitRunner','Test.http','Test.UI','Test.UI.JUnit','Test.UI.Reporting','Text','TM','tools','Tools','Trac','Trace.UI','translations','ufacekit','ui','UI','UI Guidelines','UML','UML2','Unspecified','Update','Update (deprecated - use RT>Equinox>p2)','Updater','Update Site','User','User Assistance','Utils','VCM','Visualization','WebDAV','Web Server (Apache)','Website','Web Standard Tools','what','wizard','Workbench','wst.common','wst.css','wst.html','wst.internet','wst.javascript','wst.jsdt','wst.server','wst.sse','wst.web','wst.ws','wst.wsdl','wtp.inc.jpaeditor','Xtext'),
    component_when DATETIME,
    component_who INT(11)
);

CREATE TEMPORARY TABLE temp_product (
    product_id INT(11),
    product_what ENUM('Platform', 'JDT', 'CDT', 'EclipseLink'),
    product_when DATETIME,
    product_who INT(11)
);

CREATE TEMPORARY TABLE temp_cc (
    cc_id INT(11),
    cc_what VARCHAR(1024),
    cc_when DATETIME,
    cc_who INT(11)
);

CREATE TEMPORARY TABLE temp_short_desc (
    short_desc_id INT(11),
    short_desc_what VARCHAR(1024),
    short_desc_when DATETIME,
    short_desc_who INT(11)
);

CREATE TEMPORARY TABLE temp_reports (
    reports_id INT(11),
    reports_current_resolution VARCHAR(100),
    reports_current_status VARCHAR(100),
    reports_when DATETIME,
    reports_who INT(11)
);

CREATE TEMPORARY TABLE temp_version (
    version_id INT(11),
    version_what VARCHAR(10),
    version_when DATETIME,
    version_who INT(11)
);

-- Load data into temporary tables from CSV files
LOAD DATA INFILE '/var/lib/mysql/Final_Project/Final_CSV-files/bug_status.csv'
INTO TABLE temp_bug_status
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(bug_status_id, bug_status_what, bug_status_when, bug_status_who);

LOAD DATA INFILE '/var/lib/mysql/Final_Project/Final_CSV-files/resolution.csv'
INTO TABLE temp_resolution
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(resolution_id, resolution_what, resolution_when, resolution_who);

LOAD DATA INFILE '/var/lib/mysql/Final_Project/Final_CSV-files/assigned_to.csv'
INTO TABLE temp_assigned_to
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(assigned_to_id, assigned_to_what, assigned_to_when, assigned_to_who);

LOAD DATA INFILE '/var/lib/mysql/Final_Project/Final_CSV-files/priority.csv'
INTO TABLE temp_priority
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(priority_id, priority_what, priority_when, priority_who);

LOAD DATA INFILE '/var/lib/mysql/Final_Project/Final_CSV-files/severity.csv'
INTO TABLE temp_severity
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(severity_id, severity_what, severity_when, severity_who);

LOAD DATA INFILE '/var/lib/mysql/Final_Project/Final_CSV-files/op_sys.csv'
INTO TABLE temp_op_sys
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(op_sys_id, op_sys_what, op_sys_when, op_sys_who);

LOAD DATA INFILE '/var/lib/mysql/Final_Project/Final_CSV-files/component.csv'
INTO TABLE temp_component
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(component_id, component_what, component_when, component_who);

LOAD DATA INFILE '/var/lib/mysql/Final_Project/Final_CSV-files/product.csv'
INTO TABLE temp_product
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(product_id, product_what, product_when, product_who);

LOAD DATA INFILE '/var/lib/mysql/Final_Project/Final_CSV-files/cc.csv'
INTO TABLE temp_cc
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(cc_id, cc_what, cc_when, cc_who);

LOAD DATA INFILE '/var/lib/mysql/Final_Project/Final_CSV-files/short_desc.csv'
INTO TABLE temp_short_desc
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(short_desc_id, short_desc_what, short_desc_when, short_desc_who);

LOAD DATA INFILE '/var/lib/mysql/Final_Project/Final_CSV-files/reports.csv'
INTO TABLE temp_reports
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(reports_id, reports_current_resolution, reports_current_status, reports_when, reports_who);

LOAD DATA INFILE '/var/lib/mysql/Final_Project/Final_CSV-files/version.csv'
INTO TABLE temp_version
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(version_id, version_what, version_when, version_who);

-- Commit the transaction to save data in temporary tables
COMMIT;


-- Start Transaction

-- Start a new transaction for inserting into the Dataset table
START TRANSACTION;

-- Insert data from temporary tables into the Dataset table
INSERT INTO Dataset (
    bug_status_id, bug_status_what, bug_status_when, bug_status_who,
    resolution_id, resolution_what, resolution_when, resolution_who,
    assigned_to_id, assigned_to_what, assigned_to_when, assigned_to_who,
    priority_id, priority_what, priority_when, priority_who,
    severity_id, severity_what, severity_when, severity_who,
    op_sys_id, op_sys_what, op_sys_when, op_sys_who,
    component_id, component_what, component_when, component_who,
    product_id, product_what, product_when, product_who,
    cc_id, cc_what, cc_when, cc_who,
    short_desc_id, short_desc_what, short_desc_when, short_desc_who,
    reports_id, reports_current_resolution, reports_current_status, reports_when, reports_who,
    version_id, version_what, version_when, version_who
)
SELECT
    b.bug_status_id, b.bug_status_what, b.bug_status_when, b.bug_status_who,
    r.resolution_id, r.resolution_what, r.resolution_when, r.resolution_who,
    a.assigned_to_id, a.assigned_to_what, a.assigned_to_when, a.assigned_to_who,
    p.priority_id, p.priority_what, p.priority_when, p.priority_who,
    s.severity_id, s.severity_what, s.severity_when, s.severity_who,
    o.op_sys_id, o.op_sys_what, o.op_sys_when, o.op_sys_who,
    c.component_id, c.component_what, c.component_when, c.component_who,
    pd.product_id, pd.product_what, pd.product_when, pd.product_who,
    cc.cc_id, cc.cc_what, cc.cc_when, cc.cc_who,
    sd.short_desc_id, sd.short_desc_what, sd.short_desc_when, sd.short_desc_who,
    rp.reports_id, rp.reports_current_resolution, rp.reports_current_status, rp.reports_when, rp.reports_who,
    v.version_id, v.version_what, v.version_when, v.version_who
FROM
    temp_bug_status b
    LEFT JOIN temp_resolution r ON b.bug_status_id = r.resolution_id
    LEFT JOIN temp_assigned_to a ON b.bug_status_id = a.assigned_to_id
    LEFT JOIN temp_priority p ON b.bug_status_id = p.priority_id
    LEFT JOIN temp_severity s ON b.bug_status_id = s.severity_id
    LEFT JOIN temp_op_sys o ON b.bug_status_id = o.op_sys_id
    LEFT JOIN temp_component c ON b.bug_status_id = c.component_id
    LEFT JOIN temp_product pd ON b.bug_status_id = pd.product_id
    LEFT JOIN temp_cc cc ON b.bug_status_id = cc.cc_id
    LEFT JOIN temp_short_desc sd ON b.bug_status_id = sd.short_desc_id
    LEFT JOIN temp_reports rp ON b.bug_status_id = rp.reports_id
    LEFT JOIN temp_version v ON b.bug_status_id = v.version_id;

-- Commit the transaction to save data in the Dataset table
COMMIT;
