from datetime import datetime, date
import requests
#import OWSQL as owsql


class openweather:
#  check = owsql.checkSQL()
#  load = owsql.loadSQL()
  wApiKey = 'b9675c37d1e97547e29ffa8b854dca61'
  gApiKey = '8191c92c550f494bba3b69fc55ed8310'
#  cur = load.createSQL()

  def convert_time(self, time):
    # converts UTC time to GMT time
    return(datetime.utcfromtimestamp(time).strftime('%H:%M:%S'))

  def convert_date(self, time):
    # Converts date from UTC time
    return(datetime.utcfromtimestamp(time).strftime('%m-%d-%Y'))

#  def get_location(self, loc):
    #need a way to know what I am looking for with the provided location information
#    if len(loc) > 1: 
#      search = '&latitude=' + str(loc['latitude']) + '&longitude=' + str(loc['longitude'])
#    else:
#      search = '&' + loc + '=' + str(loc.get())
#    geo_link = 'https://api.ipgeolocation.io/timezone?apiKey=' + self.gApiKey + search
#    res = requests.get(geo_link)
#    geo_api = res.json()
#    coordinates = {
#     'longitude': geo_api['geo']['longitude'],
#     'latitude': geo_api['geo']['latitude'],
#     'city': geo_api['geo']['city'],
#     'state_provence': geo_api['geo']['state_prov'],
#     'county' : geo_api['geo']['district'],
#     'country': geo_api['geo']['country_name'],
#     'timezone' : geo_api['timezone'],
#     'timezone_offset': geo_api['timezone_offset']
#    }
#    coordinates['id'] = self.check.checkLocation(coordinates)
#    return(coordinates)

  def process_today(self, data, coord):
    #takes JSON form API and seperates it into different dictionaries, converts time, and loads into another dictionary to return
    weather = {
      'sky': data['weather'][0]['description'],
      'current_Temp': data['main']['temp'],
      'temp_low': data['main']['temp_min'],
      'temp_high': data['main']['temp_max'],
      'humidity': data['main']['humidity'],
      'wind': data['wind']['speed']
    }
    sun = {
      'sunrise': self.convert_time(data['sys']['sunrise']),
      'sunset': self.convert_time(data['sys']['sunset'])
    }
    processed_data = {'weather': weather, 'sun_info': sun, 'measurement': 'imperial'}
    return(processed_data)

  def process_fiveDay(self, data, coord):
    #takes JSON form API and seeprates it into different dictionaries, converts time and loads into another dictionary to return
    #returns weather{'date': {'temp': int, 'feels_like': int, 'low', int, 'high': int, 'humidity': int, 'wind': int, 'weather_main': string, 'weather_desc': string, 'measurement':, 'imperial'}}
    for i in data['list']:
      date = self.convert_date(i['dt'])
      weather = [date, {
        'temp': i['main']['temp'],
        'feels_like': i['main']['feels_like'],
        'low': i['main']['temp_min'],
        'high': i['main']['temp_max'],
        'humidity': i['main']['humidity'],
        'wind': i['wind']['speed'],
        'weather_main': i['weather'][0]['main'],
        'weather_desc': i['weather'][0]['description'],
        'measurement': 'imperial'
      }]
    return (weather)

  def get_current(self, coor):
    # Connects to openweather api and retrieves json data for today's forecast
    # returns prodata
#    result = self.check.checkToday(self.cur, coor)
#    if result != null:
#      return(result)
#    else:
#      weblink = 'http://api.openweathermap.org/data/2.5/weather?q=' + coor['city'] + '&units=imperial&appid=' + self.wApiKey
#      res = requests.get(weblink)
#      data = res.json()
#      procData = self.process_today(data, coor)
    weblink = 'http://api.openweathermap.org/data/2.5/weather?q=' + coor['city'] + '&units=imperial&appid=' + self.wApiKey
    res = requests.get(weblink)
    data = res.json()
    procData = self.process_today(data, coor)
#      self.load.loadToday(self.cur, procData) 
#      return(procData)
    return(procData)

  def get_fiveDay(self, coor):
    # Connects to openweather api and retrieves json data for five day forecast
    # #12 get_fiveDay checks to see if five day forecast is already in the SQL database and returns it if it is. If not, it queries the webapi to retreive the information and then loads it to the SQL database, then returns it
#    result = self.check.checkForecast(self.cur, coor)
#    if result != null:
#      return(result)
#    else:
#      weblink = 'http://api.openweathermap.org/data/2.5/forecast?q=' + coor['city'] + '&units=imperial&appid=' + self.wApiKey
#      res = requests.get(weblink)
#      data = res.json()
#      procData = self.process_fiveDay(data, coor)
    weblink = 'http://api.openweathermap.org/data/2.5/forecast?q=' + coor['city'] + '&units=imperial&appid=' + self.wApiKey
    res = requests.get(weblink)
    data = res.json()
    procData = self.process_fiveDay(data, coor)
#      self.load.loadForecast(self.cur, procData)
#      return(procData)
    return(procData)