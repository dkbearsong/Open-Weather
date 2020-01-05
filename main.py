import OpenWeatherfunct as owf
from flask import Flask, render_template, request
from forms import FindWeatherForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '0f403f865aef5523b4cbbe4ba4ba8203'

@app.route("/", methods=['GET', 'POST'])
def home():
  form = FindWeatherForm()
  weather = owf.openweather()
  if form.validate_on_submit():
    coord = {'city': request.form.get('city'), 'state': request.form.get('state'), 'country':request.form.get('country')}
    today=weather.get_current(coord)
    fiveDay=weather.get_fiveDay(coord)
    allWeather = [today, fiveDay]
    return render_template('weather.html', title='Weather', form=form, allWeather=allWeather)
  return render_template('owweb.html', title='Weather', form=form)

@app.route("/weather", methods=['GET', 'POST'])
def weather():
  form = FindWeatherForm()
  weather = owf.openweather()
  if form.validate_on_submit():
    coord = {'city': request.form.get('city'), 'state': request.form.get('state'), 'country':request.form.get('country')}
    today=weather.get_current(coord)
    fiveDay=weather.get_fiveDay(coord)
    allWeather = [today, fiveDay]
    return render_template('weather.html', title='Weather', form=form, allWeather=allWeather)
  return render_template('weather.html', title='Weather', form=form, allWeather=allWeather)

if __name__ == "__main__":
    app.run(debug = True)