from utils import file, game
g = file.load()
file.appendLog(g, 123)
file.appendLog(g, 12344)
print(file.getLog(g))