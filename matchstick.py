import numpy as np
from math import ceil

class Game:
    '''
        Class used to manage the whole game
    '''
    def __init__(self, nb_line, hand_size):
        self.nb_line = nb_line
        self.hand_size = hand_size
        self.nb_stick = self._get_nb_of_stick()
        self.nb_colomn = self._get_nb_colomn()
        self.board = self._draw_board()
    
    _get_nb_of_stick = lambda self : int(self.nb_line + (self.nb_line - 1) * self.nb_line)
    '''
       |             |                                  ref (arithmetic sum)
      |||       ->   |       |          ->
     |||||           |   +   || x 2             3   +   (2 x (2 x (2 + 1) / 2)) 
    '''

    _get_nb_colomn = lambda self : int(1 + 2 * (self.nb_line - 1))

    def _draw_board(self):
        output = []
        for y in range(self.nb_line + 2):
            part = []
            for x in range(self.nb_colomn + 2):
                if x == 0 or y == 0 or y == self.nb_line + 1 or x == self.nb_colomn + 1:
                    part.append('*')
                elif self._is_that_stick(x, y, self.nb_colomn, self.nb_line):
                    part.append('|')
                else:
                    part.append(' ')
            output.append(part)
        return output

    def _is_that_stick(self, x, y, x_max, y_max):
        if x > ceil(x_max / 2) - y and x < ceil(x_max / 2) + y:
            return True
        return False

    def display(self):
        for y in range(len(self.board)):
            for x in range(len(self.board[0])):
                print(self.board[y][x], end="")
            print()
        print()

class P1(Game):
    def __init__(self, nb_lines, hand_size, human=False):
        super().__init__(nb_lines, hand_size)
    
    def turn(self):
        print("Your turn:")
        line = input("Line: ")
        matches = input("Matches: ")
        self.display()

class P2(Game):
    def __init__(self, nb_lines, hand_size, human=False):
        super().__init__(nb_lines, hand_size)
    
    def turn(self):
        print("Your turn:")
        line = input("Line: ")
        matches = input("Matches: ")
        self.display()

nb_lines = int(input("Number of lines ? "))
hand_size = int(input("How much wanna take off sticks per turn ? "))

game = Game(nb_lines, hand_size)
p1 = P1(nb_lines, hand_size, human=True)
p2 = P2(nb_lines, hand_size, human=True)

game.display()
while (game.nb_stick > 0):
    p1.turn()
    p2.turn()
    