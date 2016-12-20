def getData():
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
    
    
    csvfile = open("temp.csv",'w')
    csvwriter = csv.writer(csvfile,delimiter=',')
    
    print(timelist)
    
    
    csvwriter.writerow(['year','berkeleyheights','beijing','london','mountainview'])
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

def displayData():
    import csv
    import matplotlib
    #Import matplot library
    matplotlib.use('Agg')
    #Change matlab backend to work with c9
    import matplotlib.pyplot as plt
    #Import python plot for matlab as plt
    import numpy as numpy
    #Import numpy
    from subprocess import call
    #Import subporcess to enable c9 bash commands
    import pandas as pd
    csvfile = open('temp.csv','r')
    reader = csv.reader(csvfile,delimiter=",")
    df = pd.read_csv(csvfile)

    bhtemp = df.berkeleyheights
    bjtemp = df.beijing
    ldtemp = df.london
    mvtemp = df.mountainview

    fig, ax = plt.subplots(1, 1)
    #Initiate fig as a plot with 1 plot
    
    x = numpy.arange(1970, 2016, 1)
    #Generate x variables for the graph
    
    plt.plot(x,bhtemp)
    #Plot the tempmin line
    
    plt.plot(x,bjtemp)
    #Plot the tempmax line
    
    plt.plot(x,ldtemp)
    plt.plot(x,mvtemp)
    plt.legend(['Berkeley Heights','Beijing','London','Mountain View'])
    #Set the plot legend
    
    plt.ylabel('Temperature in Degrees')
    #Set plot y axis label
    
    plt.xlabel('Year on Nov 16')
    #Set plot x axis label
    
    plt.title('Temperature Forecast in on Nov 16')
    #Set plot title
    
    fig.savefig('forecast.png')
    #Save plot as a picture file
    
    print("Opening forecast image...")
    #Just update user on what will be happening 
    
    call('c9 open forecast.png', shell=True)
    #Use c9 shell to open the picture
    csvfile.close()


print("The program will read data from a previous request. If you need new data, please run the getData() function.")
#getdata()
displayData()