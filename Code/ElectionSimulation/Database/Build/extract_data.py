def generate(fyle, add_lines):
    new_line = ""    
    with open(fyle, "r") as f:
	with open("new_" + fyle, "w") as f1:
	    for line in f:
		new_line = ""
		for stur in line.split(','):
		    fields = stur.split("~")
		    if (len(fields) == 3):
			#",~<substring>~ case"#
			new_line += fields[1] + ","
		    elif (len(fields) == 1):
			#we had a field that wasn't delimited
			new_line += fields[0] + ","
		    else:
			#We had an empty field: no change necessary
			new_line += stur + ","
		if(add_lines):
		    f1.write(new_line[:-1] + "\n") 
		else:
		    f1.write(new_line[:-1])
	f1.close()
    f.close()    
    
if __name__ == '__main__': 
    #Pre-process file and remove delimiter tildes of delimited fields
    #TODO: CHECK IF FILE EXISTS
    generate("erssumry.txt", False)
    
    #Get district, polling ID, and polnumber from erssumry.txt
    pID = "" #stores the polling ID field
    pnum = "" #stores the polling startion number
    dist = "" #stores the district code

    new_line = ""
    with open('new_erssumry.txt', "r") as f:
	with open('new_new_erssumry.txt', "w") as f1:
	    new_line = ""	    
	    for line in f:
		fields = line.split(',')
		if(len(fields) >= 9 and fields[1] != "" \
		   and fields[3] != "" and fields[8] != ""):
		    dist = fields[1]
		    pnum = fields[3]
		    pID = fields[8]
		    if("TOTAL" in pnum or "000000" in fields):
			continue
		    f1.write(dist + "," + pnum + "," + pID + "\n")
	f1.close()
    f.close()
    
    
    generate('ersraw.txt', False)
    #Get district, polling ID, and polnumber from erssumry.txt
    votes = 0 #stores the votes of the according polling station
    pnum = "" #stores the polling startion number
    dist = ""
    first = 0
    
    with open('new_ersraw.txt', "r") as f:
	with open('new_new_ersraw.txt', "w") as f1:	    
	    for line in f:
		fields = line.split(',')
		if(len(fields) >= 6 and not("" in fields)):
		    if("TOTAL" in fields[2] and fields[1][0].isdigit()):			
			continue
		    if(fields[1] == dist and not("" in fields) \
		       and fields[2] == pnum):
			votes += int(fields[5])		   
		    else:
			if(not("" in fields)):
			    if(first == 1):
				f1.write(dist + "," + pnum + "," + str(votes) \
				         + "\n")
			    else:
				first = 1
			    votes = 0
			    pnum = fields[2]
			    dist = fields[1]
	    f1.write(dist + "," + pnum + "," + str(votes)+"\n")
	f1.close()
    f.close()  
    
    generate('pollname.txt', True)
