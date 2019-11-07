from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    """Renders the home page with links to Fortune and Weather."""
    return render_template('index.html')

@app.route('/fortune')
def fortune():
    """Renders the home page with links to Fortune and Weather."""
    return render_template('fortune_form.html', )

@app.route('/fortune_results')
def results():
    """Displays the user's fortune."""
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
        

    users_list = {'beverage' : output,'animal': output2, 'city': output3}
    return render_template('fortune_results.html', users_list=users_list)

        