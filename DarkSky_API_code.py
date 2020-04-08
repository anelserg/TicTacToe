#importing everything from forecastiopy
from forecastiopy import *

#creating a dictionary of the 17 cities, where the key is a string and the value for that is a list of the coordinates.
#the first item in the list is latitude and the second is longitude
citiesLoc = {"Anchorage, Alaska": [61.2181, -149.9003],
             "Buenos Aires, Argentia": [-34.6037, -58.3816],
             "São José dos Campos, Brazil": [-23.2237, -45.9009],
             "San José, Costa Rica": [9.9281, -84.0907],
             "Nanaimo, Canada": [49.1659, -123.9401],
             "Ningbo, China": [29.8683, 121.5440],
             "Giza, Egypt": [30.0131, 31.2089],
             "Mannheim, Germany": [49.4875, 8.4660],
             "Hyderabad, India": [17.3850, 78.4867],
             "Tehran, Iran": [35.6892, 51.3890],
             "Bishkek, Kyrgyzstan": [42.8746, 74.5698],
             "Riga, Latvia": [56.9496, 24.1052],
             "Quetta, Pakistan": [30.1798, 66.9750],
             "Warsaw, Poland": [52.2297, 21.0122],
             "Dhahran, Saudia Arabia": [26.2361, 50.0393],
             "Madrid, Spain": [40.4168, -3.7038],
             "Oldham, United Kingdom": [53.5409, -2.1114]}

#creating a mean function that we will use later in the code
def mean(data):
    return sum(data) / len(data)

#retrieving data from dark sky with the api key
api_key = 'f3e029464eaaaa1fa8eaeb348727a2b3'

#writing to a csv file
file = open('temp.csv', 'w')
file.write('City,Min 1,Max 1,Min 2,Max 2,Min 3,Max 3,Min 4,Max 4,Min 5,Max 5,Min Avg,Max Avg'+'\n')

#starting a loop for the cities above, using city for the key, and loc for the value
for city, loc in citiesLoc.items():

    #inside the loop, we are specifying the lat and long by specifying the index in loc
    weather = ForecastIO.ForecastIO(api_key, latitude=loc[0], longitude=loc[1], units='si')

    daily = FIODaily.FIODaily(weather)
    tempMin = []
    tempMax = []

    #initializing to an empty string to concatenate to it later because we cant concatenate to nothing
    minMaxStr = ''
    for day in range(2, 7):
        dayWeather = daily.get(day)
        keys = dayWeather.keys()

        #storing Mins and Maxs of temperature in a list to average them later
        tempMin.append(dayWeather["temperatureMin"])
        tempMax.append(dayWeather["temperatureMax"])

        #using the empty string we initialized earlier to concatenate to it the weather data points
        #that we converted to a string as well, to be able to display the data in a min max min max order
        #building the string here inside the loop, so we don't have to write it manually for each day
        minMaxStr += str(dayWeather["temperatureMin"]) + ',' +str(dayWeather["temperatureMax"]) + ','

    #averaging the Mins and Maxs
    minAvg = mean(tempMin)
    maxAvg = mean(tempMax)

    #forcing a decimal format to 2 decimal places
    minAvgStr = "{0:.2f}".format(minAvg)
    maxAvgStr = "{0:.2f}".format(maxAvg)

    #instead of actually printing in python, we are writing to a csv file
    file.write('"' + city + '",' + minMaxStr + minAvgStr + ',' + maxAvgStr+'\n')

#closing the csv file
file.close()