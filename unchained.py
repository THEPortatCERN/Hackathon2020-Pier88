#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('unchained.db')


def create(inp0, inp1, inp2, inp3, inp4):
    inp=[inp0, inp1, inp2, inp3, inp4]
    conn.execute('INSERT INTO UNCHAINED VALUES (?,?,?,?,?)',  inp);
    conn.commit()

def show():
    cur=conn.cursor()
    cur = conn.execute("SELECT ID, ORIGIN, GOOD, CL, FL from UNCHAINED ")
    for row in cur:
        print ('ID= ', row[0])
        print ('ORIGIN= ', row[1])
        print ('GOOD= ', row[2])
        print ('CL= ', row[3])
        print ('FL= ', row[4]), "\n"

def delete(inp):
    sql='DELETE FROM UNCHAINED WHERE ID=?'
    cur=conn.cursor()
    conn.execute(sql, (inp,))
    conn.commit()

def deleteall():
    sql='DELETE FROM UNCHAINED'
    cur=conn.cursor()
    conn.execute(sql)
    conn.commit() 

def compare(origin, good):
	cur=conn.cursor()
	cur=conn.execute("SELECT ID, ORIGIN, GOOD, CL, FL from UNCHAINED")
	k=0
	for row in cur:
		if origin==row[1] and good==row[2]:
                        print ('ID= ', row[0])
                        print ('ORIGIN= ', row[1])
                        print ('GOOD= ', row[2])
                        print ('CL= ', row[3])
                        print ('FL= ', row[4]), "\n"
                        k=1
	if k==0:
		print("No entry found")

def compare2(origin,good)
	cur=conn.cursor()
	cur=conn.execute("SELECT ID, ORIGIN, GOOD, CL, FL from UNCHAINED")
	k=0
	for row in cur:
        	if origin==row[1] and good==row[2]:
                        return(row[3], row[4])
			k=1
	if k==0:
        	return('NaN', 'NaN')


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
