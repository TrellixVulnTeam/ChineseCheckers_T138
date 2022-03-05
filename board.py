from re import X
import numpy as np
class GameBoard:
    _board = np.zeros((24, 16))
    _goalpos = []
    # Taken from https://github.com/AndreaVidali/ChineseChekersAI/blob/master/engine_2.py which is why x and y is flipped
    player1 = [[0, 12], [1, 11], [1, 13], [2, 10], [2, 12], [2, 14], [3, 9], [3, 11], [3, 13], [3, 15]]
    player2 = [[4, 18], [4, 20], [4, 22], [4, 24], [5, 19], [5, 21], [5, 23], [6, 20], [6, 22], [7, 21]]
    player3 = [[9, 21], [10, 20], [10, 22], [11, 19], [11, 21], [11, 23], [12, 18], [12, 20], [12, 22], [12, 24]]
    player4 = [[13, 9], [13, 11], [13, 13], [13, 15], [14, 10], [14, 12], [14, 14], [15, 11], [15, 13], [16, 12]]
    player5 = [[9, 3], [10, 2], [10, 4], [11, 1], [11, 3], [11, 5], [12, 0], [12, 2], [12, 4], [12, 6]]
    player6 = [[4, 0], [4, 2], [4, 4], [4, 6], [5, 1], [5, 3], [5, 5], [6, 2], [6, 4], [7, 3]]
    playerlist = [player1, player2, player3, player4, player5, player6]
    #Takes a tuple of 6, indicating players
    def __init__(self, players):
        #Invalid positions to move to
        border =    [[10,0], [9,1], [8,2], [7,3], [5,3], [3,3], [1,3],
                     [0,6], [1,7], [2,8], [2,9], [0,10],
                     [1,13], [3,13], [5,13], [7,13], [8,14], [9,15], [10,16],
                     [14,16], [15,15], [16,14], [17,13], [19,13], [21,13], [23,13],
                     [24,10], [23,9], [22,8], [23,7], [24,6],
                     [23,3], [21,3], [19,3], [17,3], [16,2], [15,1], [14,0]]
        #Place border on board
        for x, y in border:
            self._board[x,y] = -1

        #Put players on the board
        for i in range(1, players + 1):
            for y,x in self.playerlist[i]:
                self._board[x,y] = i
        
        #playerhomes = self.player1 + self.player2 + self.player3 + self.player4 + self.player5 + self.player6
        #for y, x in playerhomes:
        #    self._board[x,y] = 'x'

    #def init_players(self):
    #    self.players += 1
    #    for y, x in self.player1:
    #        self._board[x,y] = '1'

    # Find all possible moves for a single piece
    def get_possible_moves(self, piece, recCall=False):
        possible_moves = []
        jump_pos = []

        # Left up
        x = piece[0] - 1
        y = piece[1] - 1
        if(x >= 0 & y >= 0 & self._board[x,y] == 0 & recCall== False):
            possible_moves.append([x,y])
        #Position was occupied. Check if we can jump it instead
        elif(x >= 0 & y >= 0 & self._board[x,y] > 0):
            x = piece[0] - 2
            y = piece[1] - 2
            if(x >= 0 & y >= 0 & self._board[x,y] == 0):
                jump_pos.append([x,y])
                possible_moves.append([x,y])

        # Left down
        x = piece[0] - 1
        y = piece[1] + 1
        if(x >= 0 & y <= 16 & self._board[x,y] == 0 & recCall== False):
            possible_moves.append([x,y])
        #Position was occupied. Check if we can jump it instead
        elif(x >= 0 & y <= 16 & self._board[x,y] > 0):
            x = piece[0] - 2
            y = piece[1] + 2
            if(x >= 0 & y <= 16 & self._board[x,y] == 0):
                jump_pos.append([x,y])
                possible_moves.append([x,y])

        # Left
        x = piece[0] - 2
        y = piece[1]
        if(x >= 0 & self._board[x,y] == 0 & recCall== False):
            possible_moves.append([x,y])
        #Position was occupied. Check if we can jump it instead
        elif(x >= 0 & self._board[x,y] > 0):
            x = piece[0] - 4
            if(x >= 0 & self._board[x,y] == 0):
                jump_pos.append([x,y])
                possible_moves.append([x,y])

        # Right up
        x = piece[0] + 1
        y = piece[1] - 1
        if(x <= 24 & y >= 0 & self._board[x,y] == 0 & recCall== False):
            possible_moves.append([x,y])
        #Position was occupied. Check if we can jump it instead
        elif(x <= 24 & y >= 0 & self._board[x,y] > 0):
            x = piece[0] + 2
            y = piece[1] - 2
            if(x <= 24 & y >= 0 & self._board[x,y] == 0):
                jump_pos.append([x,y])
                possible_moves.append([x,y])

        # Right down
        x = piece[0] + 1
        y = piece[1] + 1
        if(x <= 24 & y <= 16 & self._board[x,y] == 0 & recCall== False):
            possible_moves.append([x,y])
        #Position was occupied. Check if we can jump it instead
        elif(x <= 24 & y <= 16 & self._board[x,y] > 0):
            x = piece[0] + 2
            y = piece[1] + 2
            if(x <= 24 & y <= 16 & self._board[x,y] == 0):
                jump_pos.append([x,y])
                possible_moves.append([x,y])

        # Right
        x = piece[0] + 2
        y = piece[1]
        if(x <= 24 & self._board[x,y] == 0 & recCall== False):
            possible_moves.append([x,y])
        #Position was occupied. Check if we can jump it instead
        elif(x <= 24 & self._board[x,y] > 0):
            x = piece[0] + 4
            if(x <= 24 & self._board[x,y] == 0):
                jump_pos.append([x,y])
                possible_moves.append([x,y])


        #Recursive call to find all positions we can jump to
        if(len(jump_pos) > 0):
            for i in range(len(jump_pos)):
                possible_moves = possible_moves + self.get_possible_moves(jump_pos[i], recCall=True)
        
        return possible_moves