from math import ceil
from errorexception import *

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
        '''
            remembers how many sticks are available on each line
        '''
        output = {}
        for i in range(self.nb_line):
            output[i + 1] = 1 + 2 * i
        return output
    
    def _draw_board(self):
        '''
            draw map game on tab
        '''
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
        '''
            check if position given is on a stick or not
        '''
        if x > ceil(x_max / 2) - y and x < ceil(x_max / 2) + y:
            return True
        return False

    def display(self):
        '''
            display game board
        '''
        for y in range(len(self.board)):
            for x in range(len(self.board[0])):
                print(self.board[y][x], end="")
            print()
        print()

class P0():
    '''
        Super player cause both players use the same methods
    '''
    def __init__(self, game, player, enemy):
        self.player_name = player
        self.enemy_name = enemy

    def turn(self):
        '''
            Just a turn
        '''
        print("{player} turn:".format(player=self.player_name))
        line, matches = self._get_input()
        self._player_process(line, matches)

        if game.nb_stick == 0:
            print("\n{enemy} Win :) and {player} Loose :(".format(enemy=self.enemy_name, player=self.player_name))
        else:
            game.display()

    def _get_input(self):
        '''
            Get input with errors management
        '''
        line = -1
        matches = -1
        while matches == -1:
            line = self._get_line()
            if line == -1:
                continue
            matches = self._get_matche(line)
        return line, matches

    def _get_line(self):
        '''
            Get line input with errors management
        '''
        try:
            line = int(input("Line: "))
            
            if line <= 0 or line > game.nb_line:
                raise OutRangeException
            elif game.stick_map[line] == 0:
                raise NoStickOnLineException(line)

        except OutRangeException as ore:
            print(ore)

        except NoStickOnLineException as nsole:
            print(nsole)
        
        except Exception:
            print("Error: invalid input (positive number expected)")

        else:
            return line
        return -1

    def _get_matche(self, line):
        '''
            Get matche input with errors management
        '''
        try:
            matche = int(input("Matches: "))

            if matche <= 0:
                raise Exception
            elif matche > game.hand_size:
                raise OverMatcheException(game.hand_size)
            elif game.stick_map[line] < matche:
                raise NotEnoughMatchException(game.stick_map[line], line)
        
        except OverMatcheException as ome:
            print(ome)
        
        except NotEnoughMatchException as neme:
            print(neme)
        
        except Exception:
            print("Error: Invalid input (positive number expected)")
        
        else:
            return matche
        return -1

    def _player_process(self, line, matches):
        '''
            Remove a stick
        '''
        xtrm = 0
        prec = ""
        i = 1
        while xtrm == 0:
            curr = game.board[line][i]
            if (curr == " " or curr == "*") and prec == "|":
                xtrm = i - 1
            prec = curr
            i += 1
        
        for i in range(matches):
            game.board[line][xtrm] = " "
            xtrm -= 1

        game.nb_stick -= matches
        game.stick_map[line] -= matches

class P1(P0):
    '''
        Player 1 (MyFavorite)
    '''
    def __init__(self, game, human=False):
        super().__init__(game, "P1", "P2")
    
class P2(P0):
    '''
        Player 2
    '''
    def __init__(self, game, human=False):
        super().__init__(game, "P2", "P1")

def get_input():
    '''
        Get first input (how many lines i want and how big is my hand) and errors management
    '''
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

game = Game(nb_lines, hand_size)

p1 = P1(game, human=True)
p2 = P2(game, human=True)

player = [p1, p2]

#linear function to swap 0 and 1
f = lambda x : -x + 1
x = 1

game.display()
while (game.nb_stick > 0):
    x = f(x)
    player[x].turn()
    