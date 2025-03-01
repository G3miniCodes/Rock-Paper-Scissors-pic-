from flask import Flask, render_template, redirect, url_for
import random

app = Flask(__name__)

# Options for Rock, Paper, Scissors
options = ['rock', 'paper', 'scissor']

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/result')
def result():
    # Randomly select an option
    choice = random.choice(options)
    return render_template('game.html', choice=choice)

if __name__ == '__main__':
    app.run(debug=True)
