from random import choice, sample

from flask import Flask, render_template, request


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
    'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']


@app.route('/')
def start_here():
    """Homepage."""

    return "Hi! This is the home page."


@app.route('/hello')
def say_hello():
    """Save hello to user."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user."""

    player = request.args.get("person")

    input_compliments = sample(AWESOMENESS,3)

    return render_template("compliment.html",
                           person=player,
                           compliments=input_compliments)

@app.route('/game')
def show_game_form():

     game_choice = request.args.get("play-game")

     if game_choice == "no":
        return "<h2> Goodbye! We'll miss you! </h2>"
     else:
        return render_template("game.html")

@app.route('/madlib')
def mad_lib():
    
    input_person = request.args.get("person")
    input_color = request.args.get("color")
    input_noun = request.args.get("noun")
    input_adjective = request.args.get("adjective")
    input_number = request.args.get("number")
    input_adjective2 = request.args.get("adjective2")
    input_animals = request.args.getlist("animals")
    if len(input_animals)==1:
         input_animals = input_animals[0]
    if len(input_animals)==2:
         input_animals = input_animals[0] + " and " + input_animals[1]
    if len(input_animals)==3:
         input_animals = input_animals[0] + ", " + input_animals[1] + " and " + input_animals[2]

    return render_template("madlib.html",
                            person=input_person,
                            color=input_color,
                            noun=input_noun,
                            adjective=input_adjective,
                            number=input_number,
                            adjective2=input_adjective2,
                            animals=input_animals)
    


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads" our web app
    # if we change the code.
    app.run(debug=True)
