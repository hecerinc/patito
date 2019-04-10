import sys
import fileinput
from antlr4 import *
from PostfixLexer import PostfixLexer
from PostfixParser import PostfixParser

def main(argv):
	input_stream = FileStream(argv[1])
	lexer = PostfixLexer(input_stream)
	stream = CommonTokenStream(lexer)
	parser = PostfixParser(stream)
	tree = parser.prog()
	print(tree)

if __name__ == '__main__':
	main(sys.argv)