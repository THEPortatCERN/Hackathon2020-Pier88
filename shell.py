#!/usr/bin/python


import importlib
from unchained import *
moduleName = 'unchained'



print("Every input has to be given in '' , except for the delete ID")

inp="N";
i=0
while inp!="X":
    inp=input("Create, Delete or Compare?  " )
    while any((inp=='Create', inp=='N')):
	i=1
        inp = input("New database entry: ['ID', 'ORIGIN', 'GOOD', 'CL', 'FL'] || X for Exit || Press V for showing all entries ");
        while inp=='V':
            show()
            inp = input("New database entry: ['ID', 'ORIGIN', 'GOOD', 'CL', 'FL'] || Press V for showing all entries || X for Exit ");
        if inp=="X":
            break
        print(inp)
        create(inp[0], inp[1], inp[2], inp[3], inp[4])
        print("Record created successfully")
        inp=input("Another: N || Press V for showing all entries || Delete for deleting an entry || Exit: X  ");
        while inp=='V':
            show()
            inp = input("Create another entry: N || Press V for showing all entries || Delete for deleting an entry || X for Exit ");
        if inp=="X":
            break


    while any((inp=='Delete', inp=='N')):
	i=1
        inp = input("Delete database entry with ID: || Delete all with ALL: || Press V for showing all entries || X for Exit ");
        while inp=='V':
            show()
            inp = input("Delete database entry with ID: || Press V for showing all entries || X for Exit ");
        if inp=='ALL':
            inp= input("Do you really want to KILL IT ALL?: ")
            if inp=='KILL IT ALL':
                inp=input("Enter security key: ")
                if inp=='88':
                    deleteall()
                    print("You killed all database entries")
                    inp='X'
        if inp=='X':
            break
        print(inp)
        delete(inp)
        print ("Record deleted successfully")
        inp=input("Another: N || Exit: X || Press V for showing all entries ");
        while inp=='V':
            show()
            inp = input("Another: N || Press V for showing all entries || X for Exit ");




    while any((inp=='Compare', inp=='N')):
	i=1
    	inp1 = input("ORIGIN THAT YOU WANT TO COMPARE:  || X or V for skipping ")
	inp2 = input("GOOD THAT YOU WANT TO COMPARE:  || X for Exit || V for showing the database" )
	inp='X'
	while inp2=='V':
        	show()
        	inp1 = input("ORIGIN THAT YOU WANT TO COMPARE:  || X and V for skipping ")
        	inp2 = input("GOOD THAT YOU WANT TO COMPARE:  || X for Exit || V for showing the database ")
	if inp2=='X':
		break
	print(inp1, inp2)
	if inp1!='V' and inp2!='V':
    		compare(inp1, inp2)
    		print("Record compared successfully")
    		inp=input("Another: N || Press V for showing all entries || Delete for deleting an entry || Exit: X ")
    		while inp=='V':
       			show()
       			inp = input("Compare another entry: N || Press V for showing all entries || Delete for deleting ")
    	if inp=="X":
       		break
if i==0:
	inp1='0'
	inp2='0'
	x, y=compare2(inp1, inp2)





inp=input("Show the Database: V || Exit: X ")
while inp=='V':
    importlib.import_module(moduleName)
    show()
    inp = input("Press V for showing all entries || Exit: X ");
close()
print("Closed the database successfully")

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
#['18', 'NIKE', 'AIRMAX', 'SHOES', '180']
#1, 'NIKE', 'AIRMAX', 'SHOES', '180'
