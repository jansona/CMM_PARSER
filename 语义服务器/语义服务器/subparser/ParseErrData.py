LEX_ERR = 'LEX_ERR'
SYN_ERR = 'SYN_ERR'
SEM_ERR = 'SEM_ERR'
RTM_ERR = 'RTM_ERR'

class ParseErrData(Exception):

    def __init__(self, err_type, line=-1, message="", token=None):
        self.err_type = err_type
        self.line = line
        self.message = message
        self.token = token  # 拿来暂存token，很垃圾的写法，用在静态语义检查

    def __str__(self):

        err_str = "line {}: {}\nmessage: {}\n".format(self.line, self.err_type, self.message)

        return err_str

    def __repr__(self):

        err_str = "line {}: {}\nmessage: {}\n".format(self.line, self.err_type, self.message)

        return err_str
