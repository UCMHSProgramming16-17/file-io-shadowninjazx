import csv
import math
#Import 
csvfile = open('csvfile.csv','w')
#Open file
csvwriter = csv.writer(csvfile,delimiter=',')
#Initiate writer
csvwriter.writerow(['a','b','hypotenuse'])
#initialize first row
for x in range(100):
    for y in range(x,100):
        if (math.sqrt((x+1)**2+(y+1)**2).is_integer()):
            csvwriter.writerow([x+1,y+1,math.sqrt((x+1)**2+(y+1)**2)])
    
csvfile.close()