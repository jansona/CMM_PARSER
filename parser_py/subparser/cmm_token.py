

class Token(object):

    count = 0

    def __init__(self, idt=0, line=0, name="", value=None):
        
        self.idt = idt
        self.name = name
        self.value = value
        self.line = line

        self.count = Token.count
        Token.count += 1