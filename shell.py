#!/usr/bin/python

import importlib
from database import *
moduleName = 'database'


print("Every input has to be given in '' , except for the delete ID")

inp="N";
while inp!="X":
    inp=input("Create or Delete?  " )
    while any((inp=='Create', inp=='N')):
        inp = input("New database entry: ['ID', 'BRAND', 'PRODUCT', 'SEGMENT', 'PRICE'] || X for Exit || Press V for showing all entries ");
        while inp=='V':
            show(inp)
            inp = input("New database entry: ['ID', 'BRAND', 'PRODUCT', 'SEGMENT', 'PRICE'] || Press V for showing all entries || X for Exit ");
        if inp=="X":
            break
        print(inp)
        #importlib.import_module(moduleName)
        create(inp[0], inp[1], inp[2], inp[3], inp[4])
        print("Record created successfully")
        inp=input("Another: N || Press V for showing all entries || Delete for deleting an entry || Exit: X ");
        while inp=='V':
            show(inp)
            inp = input("Create another entry: N || Press V for showing all entries || Delete for deleting an entry || X for Exit ");
        if inp=="X":
            break


    while any((inp=='Delete', inp=='N')):
        inp = input("Delete database entry with ID: || Delete all with ALL: || Press V for showing all entries || X for Exit ");
        while inp=='V':
            #importlib.import_module(moduleName)
            show(inp)
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
        #importlib.import_module(moduleName)
        delete(inp)
        print ("Record deleted successfully")
        inp=input("Another: N || Exit: X || Press V for showing all entries ");
        while inp=='V':
            show(inp)
            inp = input("Another: N || Press V for showing all entries || X for Exit ");


inp=input("Show the Database: V || Exit: X ")
while inp=='V':
    importlib.import_module(moduleName)
    show(inp)
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
