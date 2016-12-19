#Goal: Find the temperature of past 20 years around the world on my Birthday. 
import csv
import requests
darksky = "https://api.darksky.net/forecast/72f40b602f91711ca0f6e35078f38fb1/"
gmaps = "http://maps.google.com/maps/api/geocode/json"

locations = ["berkeley heights","beijing","london","mountain view"]
#List locations to get

lat = [0,0,0,0]
lng = [0,0,0,0]
timelist = [27648000]
tempval = [0,0,0,0]

yrange = 45

for x in range(len(locations)):
    addr = "address=" + locations[x]
    tempans = requests.get(gmaps, params=addr)
    tempansj = tempans.json()

    lat[x] = (tempansj['results'][0]['geometry']['location']['lat'])
    lng[x] = (tempansj['results'][0]['geometry']['location']['lng'])
    
for index in range(yrange):
    timelist.append(timelist[index]+(365*24*3600))
'''
coor = str(lat[0]) + ", " + str(lng[0])
time = timelist[5]
para = "?units=si&exclude=minutely,hourly,alerts,flags,daily"
url = darksky + coor + ", " + str(time) + para
ans = requests.get(url)
anstext = ans.json()
'''
csvfile = open("temp.csv",'w')
csvwriter = csv.writer(csvfile,delimiter=',')

print(timelist)
'''
for index in range(yrange+1):
    file.write(str(index+1970) + " " + str(anstext['currently']['temperature']) +"\n")
'''

csvwriter.writerow(['year','berkeley heights','beijing','london','mountain view'])
for num in range(len(timelist)):
    for y in range(len(locations)):
        coor = str(lat[y]) + ", " + str(lng[y])
        time = timelist[num]
        para = "?units=si&exclude=minutely,hourly,alerts,flags,daily"
        url = darksky + coor + ", " + str(time) + para
        ans = requests.get(url)
        anstext = ans.json()
        try:
            print(anstext['currently']['temperature'])
            tempval[y] = anstext['currently']['temperature']

        except KeyError:
            print("keyerror?")
        
    csvwriter.writerow([str(1970+num),str(tempval[0]),str(tempval[1]),str(tempval[2]),str(tempval[3])])

    

csvfile.close()
