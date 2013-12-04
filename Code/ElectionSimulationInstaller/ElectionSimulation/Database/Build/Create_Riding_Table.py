#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'lichen'
import sqlite3
import codecs

#open database
conn = sqlite3.connect('Riding.db')
c = conn.cursor()
#create riding table
c.execute('''DROP table IF EXISTS Riding;''')
c.execute('''CREATE TABLE Riding
            (Riding_ID CHAR(50) ,
            Riding_Location CHAR(50),
            Candidate CHAR(50),
	    Party CHAR(50),
	    Vote INTEGER  NOT NULL,
	    Expenses  INTERGER  NOT NULL,
	    Polling_Total INTEGER NOT NULL,
	    PRIMARY KEY (Riding_ID, Candidate)
	    )''')
#open file 
f3 = codecs.open('table12.txt',encoding='utf-8',errors='ignore')
f4 = codecs.open('table13.txt',encoding='utf-8',errors='ignore')
f5 = codecs.open('ers.txt',encoding='utf-8',errors='ignore')
Riding_L = {}
Poll_total_D = {}
insert_data = []
for line in f3:
    col = line.split(',')
    Riding_ID = col[1].replace("~","")
    # find english name of riding_location
    Riding_Location = col[2].replace("~","")
    Riding_L[Riding_Location] = Riding_ID
for line in f4:
    col = line.split("\t")
    name = col[1].split("(")[0]
    party = col[1].split("(")[1][:-1]
    volt = col[4]
    #use Riding_Location find riding ID and add to a list
    temp = (col[0].split("/"))[0]
    Riding_ID = Riding_L[temp]
    insert_data.append((Riding_ID, col[0], name, party, volt, 0, Poll_total_D[Riding_ID]))
for line in f5:
    col = line.split(",")
    Riding_ID = col[1].replace("~","")
    Poll_total_D[Riding_ID] = col[11]
#inserts all data into database
c.executemany('INSERT INTO Riding VALUES (?,?,?,?,?,?,?)', insert_data)
for row in c.execute('SELECT * FROM Riding '):
    print (row)
#save to database
conn.commit()
c.close()
