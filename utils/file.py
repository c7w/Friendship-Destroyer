import os
import yaml
from datetime import datetime
from utils import game
from utils import globalVariableManager as gb

'''
def load():
    exist = os.path.exists("./data/game.yml")
    # If exist then load it directly:
    if exist:
        f = open("./data/game.yml", encoding='utf-8')
        y = yaml.load(f.read(), Loader=yaml.SafeLoader)
        g = game.Game(y['tableSize'], y['status'], y['log_file'], y['table'], y['turnCount'], y['playerCount']) 
        return g
    # If not exist, create it and load it:
    else:
        f = open("./data/default.yml", encoding='utf-8')
        y = yaml.load(f.read(), Loader=yaml.SafeLoader)
        y['log_file'] = datetime.strftime(datetime.now(), "%Y-%m-%d-%H-%M-%S") + ".log"
        y['table'] = game.Table(y['tableSize']).entry
        g=game.Game(y['tableSize'], y['status'], y['log_file'], y['table'], y['turnCount'], y['playerCount'])
        f1=open("./data/game.yml", encoding='utf-8', mode='a+')
        yaml.dump(y, f1)
        return g
'''
    

def getTable(game):
    status = game.status
    size = game.tableSize
    entry = game.table.entry
    result = '''<p id='currentPlayer' hidden>'''
    result += str((game.turnCount-1) % game.playerCount + 1)
    result +='''</p><table border="8">\n    <thead>\n        <th colspan="'''
    
    # thead
    result += str(size)
    result += '''" id="status">'''
    result += str(status).replace('_', ' ')
    result += '''</th>\n    </thead>\n    <tbody>\n'''
    # tbody
    for i in range(1, size + 1):
        result += "    <tr>\n"
        for j in range(1, size + 1):
            if (entry[i][j] > 0):
                result += '''        <td width=50 height=50 bgcolor="ffff00">''' + \
                    str(entry[i][j]) + '''</td>\n'''
            else:
                result += '''        <td width=50 height=50 onclick="take(''' + str(i) +''', ''' +str(j) + ''')"></td>\n'''
        result += "    </tr>\n"

    result += '''    </tbody>\n</table>'''
    return result

def getControl(game):
    playerCount = game.playerCount
    result= '''<table align="center" border=2>        <thead>
            <th width = 100>玩家</th>
            <th width = 150>颜色</th>
            <th width = 100>选择</th>
        </thead>
        <tbody align="center">'''
    for i in range(1, game.playerCount+1):
        result += '''            <tr>'''
        result += '''                <td>Player ''' + str(i) + '''</td>'''
        result += '''                <td><input></td>'''
        result += '''                <td><button type="" onclick="selPlayer(''' + str(i) + ''')">■ 就你啦 ■</button></td>'''
        result += '''            </tr>'''
    result += '''        </tbody>
    </table>'''
    return result

'''
def getLog(game):
    exist = os.path.exists("./data/log/" + game.log_file)
    if exist:
        f = open("./data/log/" + game.log_file, encoding='utf-8', mode='r+')
    else:
        f = open("./data/log/" + game.log_file, encoding='utf-8', mode='w+')
    return f.read()
'''

def getLog(game):
    return gb.get('log', "")

'''
def restart() :
    path = "./data/game.yml"
    if (os.path.exists(path)) :
        os.remove(path)
'''

def restart():
    f = open("./data/default.yml", encoding='utf-8')
    y = yaml.load(f.read(), Loader=yaml.SafeLoader)
    y['log_file'] = datetime.strftime(datetime.now(), "%Y-%m-%d-%H-%M-%S") + ".log"
    y['table'] = game.Table(y['tableSize']).entry
    g=game.Game(y['tableSize'], y['status'], y['log_file'], y['table'], y['turnCount'], y['playerCount'])
    gb.set('game', g)
    gb.set('log', "")
'''
def save(game):
    y = game.toDict()
    f1 = open("./data/game.yml", encoding='utf-8', mode='w+')
    yaml.dump(y, f1)
'''

def save(game):
    gb.set('game', game)

'''
def appendLog(game, content):
    former = getLog(game)
    current = "[" + datetime.strftime(datetime.now(), "%Y%m%d %H%M%S") + \
        "] " + str(content) + " <br/>\n" + former
    fw = open("./data/log/" + game.log_file, encoding='utf-8', mode='w+')
    fw.write(current)
'''
def appendLog(game, content):
    former = gb.get('log', "")
    current = "[" + datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S") + \
        "] " + str(content) + " <br/>\n" + former
    gb.set('log', current)


def set(game, x, y, val):
    if ((game.turnCount - 1) % game.playerCount + 1 != val):
        return
    game.turnCount += 1
    game.status = "Turn_" + str(game.turnCount) + "_|_Player_" + str((game.turnCount-1) % game.playerCount + 1)
    game.table.entry[x][y] = val
    temp = "Player " + str(val) + ' has taken (' + str(x) + ', ' + str(y) + ')!'
    appendLog(game, temp)
    winner = game.table.check()
    if winner[2] > 0:
        appendLog(game, "Player " + str(winner[2]) + ' has won the game with coordinate (' + str(winner[0]) \
            + ', ' + str(winner[1]) + ') and direction ' + str(winner[3]) + '!')
        game.status = 'The game has ended!'
    save(game)


    
