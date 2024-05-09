from string import ascii_letters
from sympy.logic.boolalg import to_cnf
from sympy.abc import symbols

# Define the dictionary of valid operators
OPERATORS = {
    '&': lambda x, y: x and y,
    '|': lambda x, y: x or y,
    '~': lambda x: not x
}

# Define the precedence of operators
PRECEDENCE = {
    '&': 2,
    '|': 1,
    '~': 3
}

# Tokenizer/Lexer
def tokenize(expression):
    tokens = []
    i = 0
    while i < len(expression):
        char = expression[i]
        if char in ascii_letters:
            tokens.append(char)
        elif char in OPERATORS:
            tokens.append(char)
        elif char == '(':
            tokens.append('(')
        elif char == ')':
            tokens.append(')')
        i += 1
    return tokens

# Parser
def parse(tokens):
    def parse_expr(tokens, min_prec=0):
        stack = []
        operator = None
        i = 0
        while i < len(tokens):
            token = tokens[i]
            if token in ascii_letters:
                stack.append(token)
            elif token == '(':
                j = i + 1
                count = 1
                while count > 0:
                    if j >= len(tokens):
                        raise ValueError("Unbalanced parentheses")
                    if tokens[j] == '(':
                        count += 1
                    elif tokens[j] == ')':
                        count -= 1
                    j += 1
                if count != 0:
                    raise ValueError("Unbalanced parentheses")
                sub_expr = parse_expr(tokens[i+1:j-1], 0)
                if sub_expr == []:  # Handle empty subexpression
                    stack.append('False')
                else:
                    stack.append(sub_expr)
                i = j
            elif token == ')':
                break
            elif token == '~':  # Handle the NOT operator
                a = stack.pop()
                if isinstance(a, str):
                    stack.append(OPERATORS[token](a))
                else:
                    stack.append(['~', a])
            elif token in OPERATORS:
                while operator and PRECEDENCE[operator] >= PRECEDENCE[token]:
                    b = stack.pop()
                    a = stack.pop()
                    stack.append([operator, a, b])
            operator = token
        else:
            raise ValueError(f"Invalid token: {token}")
        i += 1
        while operator:
            b = stack.pop()
            a = stack.pop()
            stack.append([operator, a, b])
        return stack[0]

# Simplify the expression
def simplify_boolean_expression(expression):
    symbols_list = list(symbols(expression))
    expr = to_cnf(expression)
    simplified_expr = expr.simplify()
    return simplified_expr

if __name__ == "__main__":
    while True:
        user_input = input("\nEnter a Boolean Expression: ")
        original_expression = user_input
        simplified_expression = simplify_boolean_expression(user_input)
        print("\nOriginal Expression:", original_expression)
        print("\nSimplified Expression:", simplified_expression)
        print("\n- - - - - - - - - - - - - - - - - - - - - - - - ")