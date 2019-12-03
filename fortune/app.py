from flask import Flask, render_template, request
import requests
import os
from dotenv import load_dotenv

app = Flask(__name__)

load_dotenv()
TENOR_API_KEY=os.getenv("TENOR_API_KEY")

@app.route('/')
def index():
    """Renders the home page with links to Fortune and Weather."""
    return render_template('index.html')

@app.route('/fortune')
def fortune():
    """Renders the fortune page"""
    return render_template('fortune_form.html', )

@app.route('/fortune_results')
def results():
    """Displays the user's fortune based on the choices they made."""
    users_bev = request.args.get('beverage_list')
    users_animal = request.args.get('animal')
    users_city = request.args.get('city')


    output = ""
    output2 = ""
    output3 = ""

    if users_bev == 'fortnite_shield':
        output =  "stop playing fortnite you 12 year old"
    elif users_bev == 'sausage':
        output =  "thats nasty bro"
    elif users_bev == 'milk':
        output =  "only the weak drink fresh milk"
    elif users_bev == 'alcohol':
        output =  "you have problems. Tryna drink tn tho?"

    if users_animal == 'fish':
        output2 =  "300 million fish are sold as food everyday."
    elif users_animal == 'dog':
        output2 =  "Your dog is cooler than you"
    elif users_animal == 'crab':
        output2 =  "bro who picks crab lmao"
    elif users_animal == 'snorlax':
        output2 =  "youre gonna be as lazy as snorlax"

    if users_city == 'gotham':
        output3 = "The city you've been to doesn't matter"
    elif users_city == 'metropolis':
        output3 = "The city you've been to doesn't matter"
    elif users_city == 'asgard':
        output3 = "Antman is actually the most powerful avenger because when he becomes smaller than an atom, there is too little volume and too much mass, which in turn would create a black hole and kill everyone. Welcome to my Ted talk."
    elif users_city == 'nashville':
        output3 = "cool"
        
    users_list = {output, output2, output3}
    return render_template('fortune_results.html', users_list=users_list)

@app.route('/weather')
def weather():
    '''Renders the weather page that asks for'''
    return render_template('weather_form.html')

@app.route('/weather_results')
def weather_results_page():
    '''displays the city's weather using the city arg that the user inputs. Runs it through the api. Renders page of that city'''
    weather_url = "https://api.openweathermap.org/data/2.5/weather"
    users_city = request.args.get('city')
    params = {
        'q': users_city,
        'appid': TENOR_API_KEY
    }
    response = requests.get(weather_url, params=params)
    response_json = response.json()
    city = response_json['name']
    temp = response_json['main']['temp']
    
    return render_template('weather_results.html', city=city, temp=temp)

if __name__ == '__main__':
    app.run()



        