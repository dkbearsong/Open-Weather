import requests, OpenWeatherfunct as owf
from flask import Flask, render_template, jsonify, redirect, url_for,request, redirect
from flask import make_response
from forms import FindWeatherForm

weather = owf.openweather()

app = Flask(__name__)
app.config['SECRET_KEY'] = '0f403f865aef5523b4cbbe4ba4ba8203'

@app.route("/", methods=['GET', 'POST'])
def home():
  form = FindweatherForm()
  if form.validate_on_submit():
    coord = [request.form.get('city'), request.form.get('state'), request.form.get('country')]      
    flash(f'Weather data retrieved for {form.city.data}', 'success')
    today=weather.get_current(coord)
    fiveDay=weather.get_fiveDay(coord)
    allWeather = [today, fiveDay]
  return render_template('owweb.html', title='Weather', form=form, weather=allWeather)

if __name__ == "__main__":
    app.run(debug = True)