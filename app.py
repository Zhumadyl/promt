from flask import Flask, render_template
import random

app = Flask(__name__)

endangered_animals_north_america1 = [
    "California Condor",
    "North Atlantic Right Whale",
    "Mexican Wolf",
    "Green Sea Turtle",
    "Loggerhead Turtle",
    "Florida Panther",
    "Gray Wolf",
]

endangered_animals_north_america2 = [
    "San Joaquin Kit Fox",
    "Red Wolf",
]

endangered_animals_north_america3 = [
    "Steller Sea Lion",
    "Whooping Crane",
]

notendangeredanimals = [
    "Gila Monster", "Florida Manatee", "Black-footed Ferret",
    "American Crocodile", "Northern Spotted Owl", "Sonoran Pronghorn",
    "Vaquita", "Houston Toad", "Schaus' Swallowtail Butterfly"
]

# Function definitions
def get_choices():
    computer_choice = random.choice(endangered_animals_north_america1)
    return computer_choice

def get_choices2():
    computer_choice2 = random.choice(notendangeredanimals)
    return computer_choice2

def get_choices3():
    computer_choice3 = random.choice(endangered_animals_north_america2)
    return computer_choice3

@app.route('/')
def index():
    message = "Hello from Python!"
    choice1 = get_choices()
    choice2 = get_choices2()
    return render_template('index.html', message=message, choice1=choice1, choice2=choice2)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)