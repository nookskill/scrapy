from tempfile import NamedTemporaryFile
import shutil
import sys
import re
import csv
import time

count = 0;
temp_data = csv.reader(file('temp.csv'))
chk = False
for temp in temp_data:
	if chk:
		found = False
		current_data = csv.reader(file('data.csv'))
		for curr in current_data:
			#Found
			if str(temp[0]) == str(curr[0]) and str(temp[3]) == str(curr[3]):
				#curr[2] = ''+time.strftime("%x") #update date
				print "Yo1"
				#print str(temp[3]) +'	'+str(curr[3])
				found = True
				break
		#Not Found
		
		if found == False:
			#print 'Not Found'
			#f = open('data1.csv', 'a')
			writer = csv.writer(file('data.csv','a'))
			writer.writerow((temp[0],temp[1],temp[2],temp[3]))
			

	else :
		chk = True
'''
UPDATE DATE
'''
filename = 'data.csv'
tempfile = NamedTemporaryFile(delete=False)
chk = False
with open(filename, 'rb') as csvFile, tempfile:
    reader = csv.reader(csvFile)
    writer = csv.writer(tempfile)

    for row in reader:

    	if chk:
    		temp_data2 = csv.reader(file('temp.csv'))
    	   	for temp in temp_data2:
    	   	
    	   		if str(temp[0]) == str(row[0]) and str(temp[3]) == str(row[3]):
    	   			print 'UPTIME'
    	   			print str(temp[3]) +'	'+str(row[3])
	        		row[2] = ''+time.strftime("%x")
    	   			break
     	else :
    		chk = True
        writer.writerow(row)

shutil.move(tempfile.name, filename)   

