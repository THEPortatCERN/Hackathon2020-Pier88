#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('index.db')


def create(inp0, inp1, inp2, inp3, inp4):
    inp=[inp0, inp1, inp2, inp3, inp4]
    conn.execute('INSERT INTO COMPANY VALUES (?,?,?,?,?)',  inp);
    conn.commit()
    

def show(inp):
    cur=conn.cursor()
    cur = conn.execute("SELECT ID, BRAND, PRODUCT, SEGMENT, PRICE from COMPANY")
    for row in cur:
       print "ID = ", row[0]
       print "BRAND = ", row[1]
       print "PRODUCT = ", row[2]
       print "SEGMENT = ", row[3] 
       print "PRICE = ", row[4], "\n"

def delete(inp):
    sql='DELETE FROM COMPANY WHERE ID=?'
    cur=conn.cursor()
    conn.execute(sql, (inp,))
    conn.commit()

def deleteall():
    sql='DELETE FROM COMPANY'
    cur=conn.cursor()
    conn.execute(sql)
    conn.commit() 
    

def close():
    conn.close()




####################################
#Try
#############################
##conn.execute("INSERT INTO COMPANY (ID, BRAND, PRODUCT, SEGMENT, PRICE) \
##	VALUES ('inp[0]', 'inp[1]', 'inp[2]', 'inp[3]', 180 )");
#
##conn.execute("INSERT INTO COMPANY (ID, BRAND, PRODUCT, SEGMENT, PRICE) \
##	VALUES ("input("New database entry: [ID, 'BRAND', 'PRODUCT', 'SEGMENT', PRICE] ")")");
#
##conn.execute("INSERT INTO COMPANY (ID, NAME, AGE, ADDRESS, SALARY) \
##	VALUES (1, 'Paul', 32, 'California', 20000.00)");







#["2", "NIKE", "AIRMAX", "SHOES", "180"]
#1, 'NIKE', 'AIRMAX', 'SHOES', '180'
