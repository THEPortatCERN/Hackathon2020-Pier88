#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('index.db')
print "Opened database successfully";

##########################################################
#Creation of a table using these features
##########################################################

conn.execute('''CREATE TABLE COMPANY
         (ID INT PRIMARY KEY,
         BRAND           TEXT,
         PRODUCT         TEXT,
         SEGMENT        TEXT,
         PRICE          REAL);''')
print "Database creted successfully";
conn.close()

#conn.execute('''CREATE TABLE COMPANY
#         (ID INT PRIMARY KEY     NOT NULL,
#         NAME           TEXT    NOT NULL,
#         AGE            INT     NOT NULL,
#         ADDRESS        CHAR(50),
#         SALARY         REAL);''')
#print "Table created successfully";
