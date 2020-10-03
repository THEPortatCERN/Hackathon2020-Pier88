#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('index.db')


def create(inp0, inp1, inp2, inp3, inp4, inp5, inp6, inp7, inp8, inp9, inp10):
    inp=[inp0, inp1, inp2, inp3, inp4, inp5, inp6, inp7, inp8, inp9, inp10]
    conn.execute('INSERT INTO COMPANY VALUES (?,?,?,?,?,?,?,?,?,?,?)',  inp);
    conn.commit()

def show(inp):
    cur=conn.cursor()
    cur = conn.execute("SELECT ID, COMPANY, CATEGORY, PRODUCTID, PRICE PER UNIT, CURRENCY, ORIGIN, REGION, SCORE, RELIABILITY, CONTACT")
    for row in cur:
        print 'ID= ', row[0]                
	print 'COMPANY= ', row[1]           
	print 'CATEGORY= ', row[2]          
	print 'PRODUCTID= ', row[3]        
	print 'PRICEPERUNIT= ', row[4]    
	print 'CURRENCY= ',  row[5]         
	print 'ORIGIN= ',   row[6]          
	print 'REGION= ',   row[7]          
	print 'SCORE= ',    row[8]          
	print 'RELIABILITY= ',    row[9]    
	print 'CONTACT= ',         row[10]  , "\n"

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

def compare(pid):
	cur=conn.cursor()
	cur2=conn.cursor()
	cur=conn.execute("SELECT ID from COMPANY")
	cur2=conn.execute("SELECT ID, COMPANY, CATEGORY, PRODUCTID, PRICEPERUNIT, CURRENCY, ORIGIN, REGION, SCORE, RELIABILITY, CONTACT from COMPANY") 
	print(cur)
	i=0
	k=0
	for row in cur:
		print("check")
		if pid==row[0]:
			k=1
			for row in cur2[i]:
				print 'ID= ', row[0]
         			print 'COMPANY= ', row[1]
         			print 'CATEGORY= ', row[2]
				print 'PRODUCTID= ', row[3]
                                print 'PRICEPERUNIT= ', row[4]
                                print 'CURRENCY= ',  row[5]
                                print 'ORIGIN= ',   row[6]
                                print 'REGION= ',   row[7]
                                print 'SCORE= ',    row[8]
				print 'RELIABILITY= ',    row[9]
                                print 'CONTACT= ',         row[10] 
			print(i)
			print("k=", k)
			k=0
			break	
		else:
			print("No entry found")
		
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
