#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('unchained.db')
print "Opened database successfully";

##########################################################
#Creation of a table using these features
##########################################################

conn.execute('''CREATE TABLE UNCHAINED
         (ID              INT PRIMARY KEY,
         ORIGIN           TEXT,
	 GOOD  		  TEXT,
	 CL               INTEGER,
	 FL               INTEGER);''')
print "Database creted successfully";
conn.close()


