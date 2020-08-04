class OverMatcheException(Exception):
    '''
        if player choose an highter number of stick than game hand size
    '''
    def __init__(self, hand_size):
        self.hand_size = hand_size

    def __str__(self):
        return "Error: you cannot remove more than {0} matches per turn".format(self.hand_size)

class OutRangeException(Exception):
    '''
        if player choose a line out of range
    '''
    def __init__(self):
        pass

    def __str__(self):
        return "Error: this line is out of range"

class NoStickOnLineException(Exception):
    '''
        if player choose a line without stick
    '''
    def __init__(self, line):
        self.line = line
    
    def __str__(self):
        return "Error: line {0} no longer contains a stick".format(self.line)

class NotEnoughMatchException(Exception):
    '''
        if player wanna take more stick than total sticks on the line
    '''
    def __init__(self, stick, line):
        self.stick = stick
        self.line = line
        self.plural = self._get_plural()
    
    def __str__(self):
        return "Error: Not Enough stick on line {0} there's only {1} stick{2} left".format(self.line, self.stick, self.plural)

    def _get_plural(self):
        if self.stick == 1:
            return ""
        else:
            return "s"