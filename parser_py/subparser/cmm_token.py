class Token(object):

    def __init__(self, idt=0, line=0, name="", value=None):
        
        self.idt = idt
        self.name = name
        self.value = value
        self.line = line