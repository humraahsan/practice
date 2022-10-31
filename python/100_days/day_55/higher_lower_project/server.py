from flask import Flask
import random

random_num = random.randint(0, 9)

app = Flask(__name__)


@app.route('/')
def home():
    return "<h1>Guess a number between 0 and 9</h1>" \
           "<img src=\"https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif\">"


@app.route('/<int:guess>')
def guess_num(guess):
    if guess < random_num:
        return "<h1 style='color: green'>Guess is too low, try again!</h1>" \
               "<img src=\"https://giphy.com/gifs/gsimedia-bruh-thats-low-bro-TgmiJ4AZ3HSiIqpOj6\">"
    elif guess > random_num:
        return "<h1 style='color: blue'>Guess is too high, try again!</h1>" \
               "<img src=\"https://giphy.com/gifs/SWR3-k-swr3-kemal-VIR3ZuG7qD0JAD7RPt\">"
    elif guess == random_num:
        return "<h1 style='color: orange'>Guess is correct!</h1>" \
               "<img src=\"https://giphy.com/gifs/love-valentines-day-csak-WQaHrd6Z3038DofLRl\">"
    else:
        return "<h1 style='color: orange'>Please make a guess between 0 and 9, try again!</h1>"


if __name__ == '__main__':
    app.run(debug=True)
