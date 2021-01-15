class Table:
    size = 0

    entry =  [[0 for i in range(101)] for i in range(101)]
    
    def __init__(self, size):
        self.size = size
        for i in range(1, size + 1):
            for j in range(1, size + 1):
                    self.entry[i][j] = 0
    
    def output(self):
        for i in range(1, self.size + 1):
            for j in range(1, self.size + 1):
                    print(str(self.entry[i][j]) + " ", end="")
            print("")
    
    def set(self, x, y, val):
        self.entry[x][y] = val
    
    def __valid(self, x, y):
        if (1 <= x) and (x <= self.size) and (1 <= y) and (y <= self.size):
            return True
        else:
            return False

    def __checkforWinner(self, x, y):
        grid = self.entry[x][y]
        # r
        if (self.__valid(x, y + 3)) and (self.entry[x][y + 3] == self.entry[x][y + 2]) \
            and (self.entry[x][y + 2] == self.entry[x][y + 1]) and (self.entry[x][y + 1] == self.entry[x][y]):
           return (grid, 'r') 
        # ur
        if (self.__valid(x-3, y + 3)) and (self.entry[x-3][y + 3] == self.entry[x-2][y + 2]) \
            and (self.entry[x-2][y + 2] == self.entry[x-1][y + 1]) and (self.entry[x-1][y + 1] == self.entry[x][y]):
           return (grid, 'ur') 
        # dr
        if (self.__valid(x+3, y + 3)) and (self.entry[x+3][y + 3] == self.entry[x+2][y + 2]) \
            and (self.entry[x+2][y + 2] == self.entry[x+1][y + 1]) and (self.entry[x+1][y + 1] == self.entry[x][y]):
           return (grid, 'dr') 
        # d
        if (self.__valid(x+3, y)) and (self.entry[x+3][y] == self.entry[x+2][y]) \
            and (self.entry[x+2][y] == self.entry[x+1][y]) and (self.entry[x+1][y] == self.entry[x][y]):
           return (grid, 'd')
        return (0, 0)

    def check(self):
        for i in range(1, self.size + 1):
            for j in range(1, self.size + 1):
                result = self.__checkforWinner(i, j) #(player, direction)
                if result[0] > 0:
                    return (i, j, result[0], result[1])
        return (0, 0, 0, 0)

class Game():
    status = 0
    tableSize = 0
    table = 0
    turnCount = 0
    log_file = 0
    playerCount = 0
    def __init__(self, tableSize, status, log_file, table, turnCount, playerCount):
        self.tableSize = tableSize
        self.log_file = log_file
        self.status = status
        self.table = Table(tableSize)
        self.table.entry = table
        self.table.size = tableSize
        self.turnCount = turnCount
        self.playerCount = playerCount

    def toDict(self):
        result = {}
        result['status'] = self.status
        result['tableSize'] = self.tableSize
        table = self.table.entry
        result['table'] = table
        result['turnCount'] = self.turnCount
        result['log_file'] = self.log_file
        result['playerCount'] = self.playerCount
        return result


        

if __name__ == "__main__":
    x = Table(10)
    while 1:
        x.turnCount += 1
        print(" ----- TURN " + str(x.turnCount) + " ----- ")
        temp = input()
        a = int(temp.split(sep=" ")[0])
        b = int(temp.split(sep=" ")[1])
        c = int(temp.split(sep=" ")[2])
        x.set(a, b, c)
        x.output()
        result = x.check()
        if (result[2] > 0):
            print(result)
            print(" ----- TURN " + str(x.turnCount) + " ----- ")
            break
        print(" ----- TURN " + str(x.turnCount) + " ----- ")
    
