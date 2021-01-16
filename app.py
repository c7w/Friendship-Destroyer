import os
from flask import Flask, render_template, request
from utils import file
from utils import globalVariableManager as gb

gb._init()
file.restart()
app = Flask(__name__)

@app.route("/")
def hw():
    return 'hwd'
    
    
# Game
@app.route("/game")
def game():
    game = gb.get('game')
    table = file.getTable(game)
    control = file.getControl(game)
    log = file.getLog(game)
    return render_template('game.html', table=table, control = control, log = log)


# Control
@app.route("/control", methods=['GET'])
def control():
    game = gb.get('game')
    mode = request.args.get('mode')
    if mode == "getTable":
        return file.getTable(game)
    if mode == "getLog":
        return file.getLog(game)
    if mode == "restart":
        file.restart()
        return 'The game has been restarted!'
    if mode == "set":
        if game.status == "The game has ended!":
            return 'The game has ended!'
        x = request.args.get('x')
        y = request.args.get('y')
        val = request.args.get('val')
        file.set(game, int(x), int(y), int(val))
        return 'Successfully set x_' + x + " and y_" + y + ' to val_' + val + " !"
