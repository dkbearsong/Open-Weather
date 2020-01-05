import sqlite3, os.path
from datetime import datetime, date
from flask import Flask, render_template, redirect, url_for,request
from flask import make_response

class loadSQL:
  def createSQL(self):
    # Checks to see if a SQL file exists, and if it does not creates the file and loads it with tables and links
    if os.path.exists('OWdata.sqlite'):
      conn = sqlite3.connect('OWdata.sqllite')
      cur = conn.cursor()
    else:
      #create?
      conn = sqlite3.connect('OWdata.sqllite')
      cur = conn.cursor()
      cur.execute('''CREATE TABLE location{
      id INT [pk, increment],
      city VARCHAR(20),
      state VARCHAR(30),
      county VARCHAR(30),
      country VARCHAR(30),
      latitude FLOAT,
      longitude FLOAT,
      timezone VARCHAR(10),
      timezone_offset FLOAT,
      created_at TIMESTAMP,
      };
      CREATE TABLE weather_today{
      id INT [pk, increment],
      location_id INT [ref: > location.id],
      wdate DATE,
      temp FLOAT,
      high FLOAT,
      low FLOAT,
      humidity,  FLOAT,
      wind FLOAT,
      sunrise TIME,
      sunset TIME,
      weather VARCHAR(15),
      created_at TIMESTAMP
      };
      CREATE TABLE weather_forecast{
      id INT [pk, increment],
      location_id INT [ref: > location.id],
      wdate DATE,
      feels_like FLOAT,
      high FLOAT,
      low FLOAT,
      humidity,  FLOAT,
      wind FLOAT,
      sunrise TIME,
      sunset TIME,
      weather VARCHAR(15),
      created_at TIMESTAMP
      };''')
    cur.commit()
    return(cur)

  def loadToday(self, cur, data):
    # loads in today's data pulled in from Openweather into the SQL database
    city_id = self.cityID(cur, data)
    # enters the details of today into the weather table
    cur.execute('INSERT INTO weather_today (location_id, wdate, high, low, humidity, wind, sunsire, sunset, weather) VALUES (' + city_id + ', ' + str(date.today()) + ', ' + data['weather']['temp_high'], ', ' + data['weather']['temp_low'] + ', ' + data['weather']['humidity'] + ', ' + data['weather']['wind'] + ', ' + data['sun']['sunrise'] + ', ' + data['sun']['sunset'] + ', ' + data['weather']['sky'])
    cur.commit
    return()

  def loadForecast(self, cur, data):
    # loads in forecast data pulled from Openweather injto the SQL database
    city_id = self.cityID(cur, data)
    for i in data:
      cur.execute('INSERT INTO weather_forecast (location_id, wdate, feels_like, high, low, humidity, wind, weather) VALUES (' + city_id + ', ' + str(i) + ', ' + data[i]['feels_like'] + ', ' + data[i]['high'] + ', ' + data[i]['low'] + ', ' + data[i]['humidity'] + ', ' + data[i]['wind'] + ', ' + data[i]['weather_desc'] + ');')
      cur.commit()
    return()

class checkSQL:
  
  def checkLocation(self, cur, coor):
    # #8 getLocation checks to see if the location exists in the database. If not it adds the location. In either case it returns the city_id
    cur.execute("IF NOT EXISTS (SELECT 1 FROM location WHERE city = "+coor['city']+")INSERT INTO location (city,state,county,country,latitude,longitude,timezone,timezone_offset) VALUES ('"+coor['city']+"','"+coor['state']+"','"+coor['county']+"','"+coor['country']+"',"+coor['latitude']++","+coor['longitude']+",'"+coor['timezone']+"','"+coor['timezone_offset']+";")
    city_id = cur.execute("SELECT id FROM location WHERE city ='"+coor['city'])
    return city_id

  def checkToday(self, cur, coor):
    result = cur.execute('''SELECT wt.wdate, wt.high, wt.low, wt.feels_like, wt.humidity, wt.wind, wt.sunrise, wt.sunset, wt.weather
	  FROM weather_today wt
	  WHERE wt.location_id = ''' + coor['id'])
    return(result)

  def checkFiveDay(self, cur, coor):
    result = cur.execute('''SELECT wf.wdate, wf.high, wf.low, wf.feels_like, wf.humidity, wf.wind, wf.sunrise, wf.sunset, wf.weather
	  FROM weather_forecast wf
	  WHERE wf.location_id = ''' + coor['id'] + 'AND wf.wdate >= GETDATE()')
    return(result)