#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('index.db')
print "Opened database successfully";

##########################################################
#Creation of a table using these features
##########################################################

conn.execute('''CREATE TABLE COMPANY
         (ID              INT PRIMARY KEY,
         COMPANY          TEXT,
         CATEGORY         TEXT,
         PRODUCTID       TEXT,
         PRICEPERUNIT   REAL,
	 CURRENCY 	  TEXT,
	 ORIGIN  	  TEXT,
	 REGION		  TEXT,
	 SCORE		  TEXT,
	 RELIABILITY      TEXT,
	 CONTACT	  TEXT );''')
print "Database creted successfully";
conn.close()


