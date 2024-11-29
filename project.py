from flask import Flask
import random

app = Flask(__name__)

# Generate a random number between 0 and 9
r_number = random.randint(0, 9)

@app.route("/")
def hello_world():
    return """
    <div style="display: flex; justify-content: center; align-items: center; flex-direction: column; height: 100vh;">
        <h1>Welcome to the Number Guessing Game</h1>
        <h3>Choose a number between 0 and 9</h3>
        <img src="https://media.giphy.com/media/glJdAXojfP3wPEg84a/giphy.gif?cid=790b76114tq8xf86gj7admq6ozr9vf1bbesl0ye1wb8pnjc9&ep=v1_gifs_search&rid=giphy.gif&ct=g" width="300px">
    </div>
    """

@app.route("/<int:number>")
def check(number):
    if number > r_number:
        return """
        <div style="text-align: center; margin-top: 50px;">
            <h2>Too high!</h2>
            <img src="https://media.giphy.com/media/3o6wrebnKWmvx4ZBio/giphy.gif?cid=790b761185ypjj3ahf3iyv7m8yy82cntroxqa3ngo2iqgpm2&ep=v1_gifs_search&rid=giphy.gif&ct=g" width="300px">
        </div>
        """
    elif number < r_number:
        return """
        <div style="text-align: center; margin-top: 50px;">
            <h2>Too low!</h2>
            <img src="https://media.giphy.com/media/9Y5BbDSkSTiY8/giphy.gif?cid=790b761185ypjj3ahf3iyv7m8yy82cntroxqa3ngo2iqgpm2&ep=v1_gifs_search&rid=giphy.gif&ct=g" width="300px">
        </div>
        """
    else:
        return """
        <div style="text-align: center; margin-top: 50px;">
            <h2>Great, You got it!</h2>
            <img src="https://media.giphy.com/media/6brH8dM3zeMyA/giphy.gif?cid=790b7611ckfd5z1982bv9w8cvq8ccithao3onmvcambt07tf&ep=v1_gifs_search&rid=giphy.gif&ct=g" width="300px">
        </div>
        """

@app.route("/bye")
def bye():
    return "Bye!"

if __name__ == "__main__":
    app.run(debug=True)
