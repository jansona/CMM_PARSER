import sys, getopt
from subparser.lex_parser import LexParser
from subparser.syndax_parser import SyntaxParser


class CmmParser(object):

    def __init__(self, lparser, sparser):
        self.lparser = lparser
        self.sparser = sparser

    def parse(self, ifilename, ofilename=None, show_lex=False, show_syntax=False):
        code_str = None

        with open(ifilename, 'r') as fin:
            code_str = '\n'.join(fin.readlines())

        tokens = self.lparser.parse_sentence(code_str)

        if show_lex:
            self.lparser.check_tokens(tokens)

        

    
def main(argv):
    try:
        opts, args = getopt.getopt(argv, "hlso:", ["output="])

        if len(args) != 1:
            raise Exception

    except getopt.GetoptError:
        print("getopt.GetoptError")
        sys.exit(1)

    infile = args[0]
    outfile = None

    is_show_lex = False
    is_show_syntax = False
    
    for opt, arg in opts:
        if opt in ("-o", "--output"):
            outfile = arg
        elif opt in ("-h"):
            pass
        elif opt in ("-l"):
            is_show_lex = True
        elif opt in ("-s"):
            is_show_syntax = True

    if not outfile:
        outfile = infile.split(".")

    parser = CmmParser(LexParser(), SyntaxParser())

    parser.parse(infile, ofilename=outfile, show_lex=is_show_lex, show_syntax=is_show_syntax)

    


if __name__ == '__main__':
    main(sys.argv[1:])