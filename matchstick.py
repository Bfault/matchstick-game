import numpy as np


class Game:
    '''
        Class used to manage the whole game
    '''
    def __init__(self, nb_line, hand_size):
        self.nb_line = nb_line
        self.hand_size = hand_size
        self.nb_stick = self.get_nb_of_stick()
        self.nb_colomn = self.get_nb_colomn()
        self.board = self.draw_board()
    
    get_nb_of_stick = lambda self : int(self.nb_line + (self.nb_line - 1) * self.nb_line)
    '''
       |             |                                  ref (arithmetic sum)
      |||       ->   |       |          ->
     |||||           |   +   || x 2             3   +   (2 x (2 x (2 + 1) / 2)) 
    '''

    get_nb_colomn = lambda self : int(1 + 2 * (self.nb_line - 1))

    def draw_board(self):
        output = []
        for y in range(self.nb_colomn):
            part = []
            for x in range(self.nb_line):
                if x == 0 or y == 0 or x == self.nb_line or y == self.nb_colomn:
                    part.append('*')
                else:
                    part.append(' ')
            output.append(part)
        return output

    def display(self):
        for y in range(self.nb_colomn):
            for x in range(self.nb_line):
                print(self.board[y][x], end="")
            print("")

nb_lines = int(input("Number of lines ? "))
hand_size = int(input("How much wanna take off sticks per turn ? "))

game = Game(nb_lines, hand_size)

game.display()
'''
while (game.nb_stick > 0):
    pass
'''