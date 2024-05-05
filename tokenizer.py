import re

# Token types
class TokenType:
    AND = "AND"
    OR = "OR"
    NOT = "NOT"
    LPAREN = "LPAREN"
    RPAREN = "RPAREN"
    IDENTIFIER = "IDENTIFIER"
    EOF = "EOF"

# Token class
class Token:
    def __init__(self, type, value=None):
        self.type = type
        self.value = value

    def __str__(self):
        return f"Token({self.type}, {self.value})"

# Tokenizer/lexer
def tokenize(expression):
    tokens = []
    current_pos = 0

    while current_pos < len(expression):
        char = expression[current_pos]

        if char == ' ':
            current_pos += 1
            continue
        elif char in ['(', ')', 'AND', 'OR', 'NOT']:
            tokens.append(Token(char))
            current_pos += len(char)
        elif char == '&':
            tokens.append(Token(TokenType.AND))
            current_pos += 1
        elif char == '|':
            tokens.append(Token(TokenType.OR))
            current_pos += 1
        else:
            # Identifier
            identifier = re.match(r'[a-zA-Z]+', expression[current_pos:])
            if identifier:
                tokens.append(Token(TokenType.IDENTIFIER, identifier.group()))
                current_pos += len(identifier.group())
            else:
                raise ValueError(f"Invalid character '{char}' at position {current_pos}")

    tokens.append(Token(TokenType.EOF))
    return tokens


