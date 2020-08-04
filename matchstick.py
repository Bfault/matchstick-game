import numpy as np
from math import ceil

class Game:
    '''
        Class used to manage the whole game
    '''
    def __init__(self, nb_lines, hand_size):
        self.nb_line = nb_lines
        self.hand_size = hand_size
        self.nb_stick = self._get_nb_of_stick()
        self.stick_map = self._get_stick_map()
        self.nb_colomn = self._get_nb_colomn()
        self.board = self._draw_board()
    
    _get_nb_of_stick = lambda self : int(self.nb_line + (self.nb_line - 1) * self.nb_line)
    '''
       |             |                                  ref (arithmetic sum)
      |||       ->   |       |          ->
     |||||           |   +   || x 2             3   +   (2 x (2 x (2 + 1) / 2)) 
    '''
    _get_nb_colomn = lambda self : int(1 + 2 * (self.nb_line - 1))
    
    def _get_stick_map(self):
        output = {}
        for i in range(self.nb_line):
            output[i + 1] = 1 + 2 * i
        return output
    
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

class P0(Game):
    '''
    '''
    def __init__(self, nb_lines, hand_size):
        super().__init__(nb_lines, hand_size)
    
    def turn(self):
        print("Your turn:")
        line = self._get_line()
        matches = self._get_matche(line)
        self._player_process(line, matches)
        self.display()

    def _get_line(self):
        try:
            line = int(input("Line: "))
            if line <= 0 or line > self.nb_line or self.stick_map[line] == 0:
                raise Exception
        except:
            print("Error: Invalid input (positive number expected)")
            line = self._get_line()
        return line
    
    def _get_matche(self, line):
        try:
            matche = int(input("Matches: "))
            if matche <= 0 or self.stick_map[line] < matche or matche > self.hand_size:
                raise Exception
        except:
            print("Error: Invalid input (positive number expected)")
            matche = self._get_matche(line)
        return matche

    def _player_process(self, line, matches):
        #self.board[i][line]
        self.nb_stick -= matches

class P1(P0):
    '''
    '''
    def __init__(self, nb_lines, hand_size, human=False):
        super().__init__(nb_lines, hand_size)
    
class P2(P0):
    '''
    '''
    def __init__(self, nb_lines, hand_size, human=False):
        super().__init__(nb_lines, hand_size)

def get_input():
    nb_lines = 0
    hand_size = 0

    while nb_lines <= 0:
        try:
            nb_lines = int(input("Number of lines ? "))
            if (nb_lines <= 0):
                raise Exception
        except:
            print("Incorrect (Positive number expected)")

    while hand_size <= 0:
        try:
            hand_size = int(input("How much wanna take off sticks per turn ? "))
            if (hand_size <= 0):
                raise Exception
        except:
            print("Incorrect (Positive number expected)")

    return (nb_lines, hand_size)

nb_lines, hand_size = get_input()

p1 = P1(nb_lines, hand_size, human=True)
p2 = P2(nb_lines, hand_size, human=True)

p1.display()
while (p1.nb_stick > 0):
    p1.turn()
    p2.turn()
    