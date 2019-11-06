


LEX_ERR = 'LEX_ERR'
SYN_ERR = 'SYN_ERR'
SEM_ERR = 'SEM_ERR'

class ParseErrData(Exception):

    def __init__(self, err_type, line=-1, message=""):
        self.err_type = err_type
        self.line = line
        self.message = message

    def __str__(self):

        err_str = "line {}: {}\nmessage: {}\n".format(self.line, self.err_type, self.message)

        return err_str

    def __repr__(self):

        err_str = "line {}: {}\nmessage: {}\n".format(self.line, self.err_type, self.message)

        return err_str
