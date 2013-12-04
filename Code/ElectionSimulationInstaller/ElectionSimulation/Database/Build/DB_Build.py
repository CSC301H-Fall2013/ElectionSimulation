import sqlite3


if __name__ == '__main__':
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    c.execute("Drop table IF EXISTS Polling_Station")
    c.execute('''CREATE TABLE Polling_Station(
    PS_ID CHAR(50) NOT NULL,
    Poll_name CHAR(50),
    Riding_ID CHAR(50) NOT NULL,
    Vote INTEGER NOT NULL,
    PRIMARY KEY (PS_ID)
    )''')
    
    Values = {}
    with open('new_pollname.txt', "r") as f:
	for line in f:
	    fields = line.split(',')
	    if(len(fields) > 1):
		Values[fields[0]] = fields[1]
    f.close()
    
    sumry = {}
    with open('new_new_erssumry.txt', "r") as f:
	for line in f: 
	    fields = line.split(',')
	    sumry[(fields[0], fields[1])] = fields[2]
    f.close()
    
    row = []
    PS_ID = ""
    Poll_name = ""
    Riding_ID = ""
    Vote = 0  
    
    
    with open('new_new_ersraw.txt', "r") as f:
	for line in f: 
	    fields = line.split(',')
	    
	    Riding_ID = fields[0]
	    Poll_name = Values[fields[0]]
	    PS_ID = sumry[(fields[0], fields[1])]
	    Vote = fields[2]
	    
	    row = (PS_ID, Poll_name, Riding_ID, Vote)   
	    c.execute("INSERT INTO Polling_Station VALUES (?,?,?,?)", row)
    f.close()
    
		
    #Insert a row of data
    #c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")
    
    #Commit the changes
    #conn.commit()
    
    # We can also close the connection if we are done with it.
    # Just be sure any changes have been committed or they will be lost.
    #conn.close()   
