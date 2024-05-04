from tokenizer import tokenize
from boolean_parser import Parser

# Simplify Boolean expression
def simplify(expression):
    tokens = tokenize(expression)
    parser = Parser(tokens)
    parsed_expression = parser.parse()
    return parsed_expression

# Input from user
expression = input("Enter a Boolean expression: ")
simplified_expression = simplify(expression)
print(f"Simplified expression: {simplified_expression}")
