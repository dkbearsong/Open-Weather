from datetime import datetime, date
import requests
#import OWSQL as owsql


class openweather:
  wApiKey = 'b9675c37d1e97547e29ffa8b854dca61'
  gApiKey = '8191c92c550f494bba3b69fc55ed8310'
  
  def convert_time(self, time):
    # converts UTC time to GMT time
    return(datetime.utcfromtimestamp(time).strftime('%H:%M:%S'))

  def convert_date(self, time):
    # Converts date from UTC time
    return(datetime.utcfromtimestamp(time).strftime('%m-%d-%Y'))

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
    weblink = 'http://api.openweathermap.org/data/2.5/weather?q=' + coor['city'] + '&units=imperial&appid=' + self.wApiKey
    res = requests.get(weblink)
    data = res.json()
    procData = self.process_today(data, coor)
    return(procData)

  def get_fiveDay(self, coor):
    # Connects to openweather api and retrieves json data for five day forecast
    weblink = 'http://api.openweathermap.org/data/2.5/forecast?q=' + coor['city'] + '&units=imperial&appid=' + self.wApiKey
    res = requests.get(weblink)
    data = res.json()
    procData = self.process_fiveDay(data, coor)
    return(procData)