def getData():
#Function to renew data from darksky and save data in csv file

    #Goal: Find the temperature of past 20 years around the world on my Birthday. 
    import csv
    import requests
    #import necessary modules
    
    darksky = "https://api.darksky.net/forecast/72f40b602f91711ca0f6e35078f38fb1/"
    gmaps = "http://maps.google.com/maps/api/geocode/json"
    #Define url for gmap and darksky api 
    
    locations = ["berkeley heights","beijing","london","mountain view"]
    #List locations to get
    
    lat = [0,0,0,0]
    lng = [0,0,0,0]
    timelist = [27648000]
    #This number is unix time of 1970 November 16th in darksky api
    tempval = [0,0,0,0]
    #Initialize lists for data storage
    
    yrange = 45
    #Control years since 1970 to request via darksky api
    
    for x in range(len(locations)):
    #for loop to get coordinates for locations 
    
        addr = "address=" + locations[x]
        #Set param for gmap api request
        
        tempans = requests.get(gmaps, params=addr)
        #Gmaps api request
        
        tempansj = tempans.json()
        #Parse api response as JSON
        
        lat[x] = (tempansj['results'][0]['geometry']['location']['lat'])
        #Set latitude from gmaps reponse to lat list
        
        lng[x] = (tempansj['results'][0]['geometry']['location']['lng'])
        #Set longitude from gmaps response to lng list
        
    for index in range(yrange):
    #For loop to determine the unix time since 1970 for darksky api request
    
        timelist.append(timelist[index]+(365*24*3600))
        #Add approximately a year in seconds to list (leap years not factored in)
    
    csvfile = open("temp.csv",'w')
    #Open csv file to write
    
    csvwriter = csv.writer(csvfile,delimiter=',')
    #Initiate csvwriter module
    
    csvwriter.writerow(['year','berkeleyheights','beijing','london','mountainview'])
    #Write the first name line to csv file
    
    for num in range(len(timelist)):
    #For loop to cycle through each year for the years listed from 1970
    
        for y in range(len(locations)):
        #For loop to cycle through 4 locations for each year
        
            coor = str(lat[y]) + ", " + str(lng[y])
            #Set coordinate param for api requset
            
            time = timelist[num]
            #Get time value for api request
            
            para = "?units=si&exclude=minutely,hourly,alerts,flags,daily"
            #Set additional parameters for api request
            
            url = darksky + coor + ", " + str(time) + para
            #Concatenate api request url
            
            ans = requests.get(url)
            #API request for darksky
            
            anstext = ans.json()
            #Parse API request as JSON
            
            try:
            #Try to ignore keyerror from darksky api request
            
                print(anstext['currently']['temperature'])
                #print the result temperature to debug
                
                tempval[y] = anstext['currently']['temperature']
                #set the result temperature to a temporary value to be written
    
            except KeyError:
            #predict error
            
                print("keyerror?")
                #Indicate error by printing, but ignore the error
            
        csvwriter.writerow([str(1970+num),str(tempval[0]),str(tempval[1]),str(tempval[2]),str(tempval[3])])
        #Write temporary temperature values into csv file along with year
    
    csvfile.close()
    #Close the csv file

def displayData():
#Function to graph the csv file

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
    #Import pandas data analysis module
    

    df = pd.read_csv('temp.csv')
    #Initialize dataform for pandas module for csv file
    
    bhtemp = df.berkeleyheights
    bjtemp = df.beijing
    ldtemp = df.london
    mvtemp = df.mountainview
    #Set columns in csv file to a pandas list

    fig, ax = plt.subplots(1, 1)
    #Initiate fig as a plot with 1 plot
    
    x = numpy.arange(1970, 2016, 1)
    #Generate x variables for the graph
    
    plt.plot(x,bhtemp)
    plt.plot(x,bjtemp)
    plt.plot(x,ldtemp)
    plt.plot(x,mvtemp)
    #Plot the temperature graphs for each of the four locations
    
    plt.legend(['Berkeley Heights','Beijing','London','Mountain View'])
    #Set the plot legend
    
    plt.ylabel('Temperature in Degrees')
    #Set plot y axis label
    
    plt.xlabel('Year on Nov 16')
    #Set plot x axis label
    
    plt.title('Temperature Forecast on Nov 16')
    #Set plot title
    
    fig.savefig('forecast.png')
    #Save plot as a picture file
    
    print("Opening forecast image...")
    #Just update user on what will be happening 
    
    #call('c9 open forecast.png', shell=True)
    #Use c9 shell to open the picture
    
    
    #Bokeh Test
    from bokeh.plotting import figure, output_file, show
    #Import bokeh
    
    output_file("plot.html")
    #Set output file
    
    p = figure(plot_width=1280, plot_height=720, title="Temperature Forecast on November 16")
    #Set up plot
    
    p.line(x, bhtemp, line_width=2, color="black", legend="Berkeley Heights")
    p.line(x, bjtemp, line_width=2, color="blue", legend="Beijing")
    p.line(x, ldtemp, line_width=2, color="green", legend="London")
    p.line(x, mvtemp, line_width=2, color="red", legend="Mountain View")
    #Plot the temperatures at different locations
    
    show(p)
    #Finalize output file



print("The program will read data from a previous request. If you need new data, please run the getData() function.")
#Notify user that the program will not get new data by default

#getdata()
#Call function to renew data

displayData()
#Call function to graph data