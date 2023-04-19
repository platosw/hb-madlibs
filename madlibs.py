"""A madlib game that compliments its users."""

from random import sample

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    "awesome",
    "terrific",
    "fantastic",
    "neato",
    "fantabulous",
    "wowza",
    "oh-so-not-meh",
    "brilliant",
    "ducky",
    "coolio",
    "incredible",
    "wonderful",
    "smashing",
    "lovely",
]


@app.route("/")
def start_here():
    """Display homepage."""

    return "Hi! This is the home page."


@app.route("/hello")
def say_hello():
    """Say hello to user."""
    compliments = AWESOMENESS

    return render_template("hello.html", compliments=compliments)


@app.route("/greet")
def greet_person():
    """Greet user with compliment."""
    player = request.args.get("person")
    compliments = request.args.getlist("compliments")

    return render_template("compliment.html", name=player, compliments=compliments)


@app.route('/game')
def show_madlib_form():
    choice = request.args.get('choice')

    if choice == 'yes':
        return render_template('game.html', adjective=AWESOMENESS)
    else:
        return render_template('goodbye.html')


@app.route('/madlib', methods=["POST"])
def show_madlib():
    person = request.form.get('person')
    color = request.form.get('color')
    noun = request.form.get('noun')
    adjective = request.form.get('adjective')

    return render_template('madlib.html', person=person, color=color, noun=noun, adjective=adjective)


if __name__ == "__main__":
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True, host="0.0.0.0")
