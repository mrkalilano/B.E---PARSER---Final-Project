from tokenizer import tokenize
from boolean_parser import Parser

# Simplify Boolean expression
def simplify(expression):
    tokens = tokenize(expression)
    parser = Parser(tokens)
    parsed_expression = parser.parse()

    # Simplification logic
    simplified_expression = parsed_expression  # Placeholder for actual simplification logic

    return expression, simplified_expression


# Input from user
expression = input("Enter a Boolean expression: ")
original_expression, simplified_expression = simplify(expression)
print(f"Original Expression: {original_expression}")
print(f"Simplified Expression: {simplified_expression}")