file = open("board.txt", "w+")

class Board:
    def __init__(self):
        self.board = [[None for _ in range(1000)] for _ in range(1000)]
        self.board[500][500] = 0
    
    def __getitem__(self, key):
        return self.board[key]

board = Board()

class Player:
    def __init__(self, moves, num):
        self.m = moves
        self.x = 500
        self.y = 500
        self.rot = 0
        self.num = num
        self.score = 0
    
    def move(self):
        if (self.x + self.y) % 2 == 0:
            self.rot += 1
            self.rot %= 3
            if self.rot == 0:
                if (board[self.y][self.x - 1]) is not None:
                    self.x -= 1
                    self.rot = 2
                    self.move()
            elif self.rot == 1:
                if (board[self.y][self.x + 1]) is not None:
                    self.x += 1
                    self.rot = 0
                    self.move()
            elif self.rot == 2:
                if (board[self.y + 1][self.x]) is not None:
                    self.y += 1
                    self.rot = 1
                    self.move()
        else:
            self.rot += 1
            self.rot %= 3
            if self.rot == 0:
                if (board[self.y][self.x - 1]) is not None:
                    self.x -= 1
                    self.rot = 1
                    self.move()
            elif self.rot == 1:
                if (board[self.y - 1][self.x]) is not None:
                    self.y -= 1
                    self.rot = 2
                    self.move()
            elif self.rot == 2:
                if (board[self.y][self.x + 1]) is not None:
                    self.x += 1
                    self.rot = 0
                    self.move()
    
    def reset(self):
        for i in range(1000):
            for j in range(1000):
                if board[i][j] != None:
                    self.x = j
                    self.y = i
                    self.rot = 0
                    break

    def check(self):
        summ = (self.x + self.y) % 2
        if not summ and self.rot == 0:
            if board[self.y][self.x + 1] == self.num and board[self.y + 1][self.x] == self.num:
                return (True, self.x - 1, self.y)
            else:
                return (False, self.x - 1, self.y)
        elif not summ and self.rot == 1:
            if board[self.y][self.x - 1] == self.num and board[self.y + 1][self.x] == self.num:
                return (True, self.x + 1, self.y)
            else:
                return (False, self.x + 1, self.y)
        elif not summ and self.rot == 2:
            if board[self.y][self.x - 1] == self.num and board[self.y][self.x + 1] == self.num:
                return (True, self.x, self.y + 1)
            else:
                return (False, self.x, self.y + 1)

        elif summ and self.rot == 0:
            if board[self.y][self.x + 1] == self.num and board[self.y - 1][self.x] == self.num:
                return (True, self.x - 1, self.y)
            else:
                return (False, self.x - 1, self.y)
        elif summ and self.rot == 1:
            if board[self.y][self.x - 1] == self.num and board[self.y][self.x + 1] == self.num:
                return (True, self.x, self.y - 1)
            else:
                return (False, self.x, self.y - 1)
        elif summ and self.rot == 2:
            if board[self.y][self.x - 1] == self.num and board[self.y - 1][self.x] == self.num:
                return (True, self.x + 1, self.y)
            else:
                return (False, self.x + 1, self.y)



    def turn(self): 
        summ = (self.x + self.y) % 2

        if not summ and self.rot == 0 and (board[self.y][self.x - 1] != None): self.reset()
        elif not summ and self.rot == 1 and (board[self.y][self.x + 1] != None): self.reset()
        elif not summ and self.rot == 2 and (board[self.y + 1][self.x] != None): self.reset()
        elif summ and self.rot == 0 and (board[self.y][self.x - 1] != None): self.reset()
        elif summ and self.rot == 1 and (board[self.y - 1][self.x] != None): self.reset()
        elif summ and self.rot == 2 and (board[self.y][self.x + 1] != None): self.reset()

        summ = (self.x + self.y) % 2
        check = self.check()
        if check[0]: self.score += 1
        
        for _ in range(self.m):
            self.move()
            if self.check()[0]:
                break

        board[check[2]][check[1]] = self.num

players, turns = input().split(" ")
players, turns = int(players), int(turns)

plays = []

t = input().split(" ")

for i in range(len(t)):
    plays.append(Player(int(t[i]), i + 1))

index = 0
for i in range(turns):
    plays[index].turn()
    index += 1
    index %= players

[print(player.score) for player in plays]
test = Player(1000, 69)
test.reset()
score = 0
coords = (test.x, test.y)
test.move()
score += 1
while not ((test.x, test.y) == coords and test.rot == 0):
    test.move()
    score += 1
print(score)

for i in board.board[495:505]:
    for j in i[495:505]:
        file.write(f"{j} ")
    file.write("\n")