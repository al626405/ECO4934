CREATE TABLE Dataset (
    report_id INT(11) PRIMARY KEY,
    current_resolution VARCHAR(100),
    current_status VARCHAR(100),
    priority ENUM('P1', 'P2', 'P3', 'P4', 'P5', 'NONE'),
    product ENUM('Platform', 'JDT', 'CDT', 'EclipseLink'),
    version VARCHAR(10),
    op_sys ENUM('AIX GTK', 'AIX Motif', 'All', 'HP-UX', 'Linux', 'Linux-GTK', 'Linux-Motif', 'Linux Qt', 'Mac OS', 'Mac OS X', 'MacOS X', 'Mac OS X - Cocoa', 'Neutrino', 'other', 'Other', 'QNX-Photon', 'Solaris', 'Solaris-GTK', 'Solaris-Motif', 'SymbianOS S60', 'SymbianOS-Series 80', 'Symbian Qt', 'Unix All', 'what', 'Windows 2000', 'Windows 2003 Server', 'Windows 7', 'Windows 95', 'Windows 98', 'Windows All', 'Windows CE', 'Windows Me', 'Windows ME', 'Windows Mobile 2003', 'Windows Mobile 5.0', 'Windows NT', 'Windows Server 2003', 'Windows Server 2008', 'Windows Vista', 'Windows Vista Beta 2', 'Windows Vista-WPF', 'Windows XP'),
    component ENUM('accservice','AI','alf-core','alf-tools','All','Annotations','Ant','API Tools','App','apps.eclipse.org','APT','Architecture Council','Articles','ASF.Runtime','ATL-UI','Autotools','Bugzilla','Build','Build/Web','bundles','Bundles','Callisto','CDateTime','CDE','cdt-build','cdt-build-managed','cdt-codan','CDT-Contrib','cdt-core','cdt-cppunit','cdt-debug','cdt-debug-cdi','cdt-debug-cdi-gdb','cdt-debug-dsf','cdt-debug-dsf-gdb','cdt-debug-edc','cdt-doc','cdt-editor','cdt-indexer','cdt-launch','cdt-memory','cdt-other','cdt-parser','CDT-parser','cdt-refactoring','cdt-releng','cdt-source-nav','Cell','Chart','CME','Code Assist','Codegen','CommitterTools','Compare','Compendium','Components','CompositeTable','Connection Mgt Framework','Connectivity','core','Core','Cpp-Extensions','cpp-package','Cross-project','Cross-Project','CVS','Data Source Explorer','DataTools','DD','Debug','Debugger','Debug-MI','Debug-UI','Demo','deprecated2','deprecated3','deprecated4','deprecated5','deprecated6','deprecated7','Desktop','DevTools','Doc','DOC','Docs','documentation','Documentation','draw2d','DSF','Dynamic Plugins','e4','ecf.core','ecf.doc','ecf.filetransfer','EclipseBot','EclipseCon','Edit','Editor','EEF','eJFace','EnglishStrings','eSWT','eWorkbench','Examples','Faceted Project Framework','FAQ','Forums and Newsgroups','Foundation','Framework','GDB','geclipse','GEF','General','General UI','Generic-Extensions','Help','Hudson','Hyades','IDE','Incubator','Incubators','Intro','IPZilla','J2EE Standard Tools','Java','Javaco','Java Core','Java Model (JEM)','java-package','jee-package','Jet','JET','JFace','JFC/Swing','Jira','jst.ejb','jst.j2ee','jst.jsp','jst.server','jst.servlet','jst.ws','Launcher','LinuxDistros','LPEX','Mapping','Marketplace','Memory','MI','Models - Graphical','Monitor.UI','Monitor.UI.GLARules','Monitor.UI.SDBEditor','mozide','Mozilla','MTJ projects','newsgroups','Newsgroups','OAW','org.eclipse.stp.bpmn','OSGi','Other','Outline Views','p2','package content','Phoenix','PHP Explorer View','PHP Search','Platform.Analysis','Platform.Collection','Platform.Communication','Platform.Execution','Platform.LineCoverage.Runtime','Platform.Model','Platform.UI','Platform.UI.ProfilingPerspective','Platform.UI.SequenceDiagram','Platform.UI.StatsPerfViewers','PLDT','Plugins','PMC','Portal','Prereq','Problems view','Process','Project Management','RDT','releng','Releng','Report','Report Designer','Report Viewer','Repository','Resources','RSE','Runtime','Runtime Common','Scripting','Search','Security','Server','Server-Side','SQLDevTools','SQL Editor Framework','SWT','SWTBot','Table Data Editor','Tasks','Team','Teneo','Test.Agents','Test.Execution','Test.Execution.JUnitRunner','Test.http','Test.UI','Test.UI.JUnit','Test.UI.Reporting','Text','TM','tools','Tools','Trac','Trace.UI','translations','ufacekit','ui','UI','UI Guidelines','UML','UML2','Unspecified','Update','Update (deprecated - use RT>Equinox>p2)','Updater','Update Site','User','User Assistance','Utils','VCM','Visualization','WebDAV','Web Server (Apache)','Website','Web Standard Tools','what','wizard','Workbench','wst.common','wst.css','wst.html','wst.internet','wst.javascript','wst.jsdt','wst.server','wst.sse','wst.web','wst.ws','wst.wsdl','wtp.inc.jpaeditor','Xtext'),
    severity ENUM('trivial', 'minor', 'normal', 'enhancement', 'major', 'critical', 'blocker'),
    `when` DATETIME,
    who INT(11),
    cc_email TEXT,
    cc_when TEXT,
    cc_who TEXT,
    assigned_to TEXT,
    assigned_when TEXT,
    assigned_who TEXT,
    resolution_update TEXT,
    resolution_when TEXT,
    resolution_who TEXT,
    bug_status_update TEXT,
    bug_status_when TEXT,
    bug_status_who TEXT
);

SET GLOBAL local_infile = 1;

LOAD DATA LOCAL INFILE '/home/Alexis/Database/MySQL_Table_Creation/Final_Project/Final_CSV-files/combine_test/combined_dataset.csv'
INTO TABLE Dataset
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(report_id, current_resolution, current_status, priority, product, version, op_sys, component, severity, `when`, who,
 cc_email, cc_when, cc_who, assigned_to, assigned_when, assigned_who, resolution_update, resolution_when, resolution_who, bug_status_update, bug_status_when, bug_status_who);
