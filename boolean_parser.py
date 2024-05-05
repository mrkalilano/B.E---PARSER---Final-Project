from tokenizer import TokenType, Token, tokenize

# Parser
class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current_token = None
        self.advance()

    def advance(self):
        self.current_token = self.tokens.pop(0) if self.tokens else None

    def factor(self):
        token = self.current_token

        if token.type == TokenType.IDENTIFIER:
            self.advance()
            return token.value
        elif token.type == TokenType.NOT:
            self.advance()
            return f"not {self.factor()}"
        elif token.type == TokenType.LPAREN:
            self.advance()
            expr = self.expr()
            if self.current_token.type != TokenType.RPAREN:
                raise ValueError("Expected ')' after expression")
            self.advance()
            return expr
        else:
            raise ValueError(f"Invalid token {token.type}")

    def term(self):
        left = self.factor()

        while self.current_token.type in (TokenType.AND, TokenType.OR):
            op = self.current_token
            self.advance()
            right = self.factor()

            left = f"{left} {op.type.lower()} {right}"

        return left

    def expr(self):
        result = self.term()

        while self.current_token.type in (TokenType.OR,):
            op = self.current_token
            self.advance()
            right = self.term()
            result = f"{result} {op.type} {right}"

        return result


    def parse(self):
        return self.expr()

# Simplify Boolean expression
def simplify(expression):
    tokens = tokenize(expression)
    parser = Parser(tokens)
    parsed_expression = parser.parse()

    # Simplification logic
    simplified_expression = parsed_expression  # Placeholder for actual simplification logic

    return parsed_expression, simplified_expression
