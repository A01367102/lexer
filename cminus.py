import re
import os
from pathlib import Path
import sys

# Define los tokens
tokens = [
    # Keywords
    ('IF', r'if\b'),
    ('ELSE', r'else\b'),
    ('WHILE', r'while\b'),
    ('INT', r'int\b'),
    ('VOID', r'void\b'),
    ('RETURN', r'return\b'),

    # Operators and punctuation
    ('PLUS', r'\+'),                     # Suma
    ('MINUS', r'-'),                     # Resta
    ('TIMES', r'\*'),                    # multiplicacion
    ('DIVIDE', r'/'),                    # division
    ('ASSIGN', r'='),                    # igual
    ('LT', r'<'),                        # menor que
    ('GT', r'>'),                        # mayor que
    ('LTE', r'<='),                      # menor o igual que
    ('GTE', r'>='),                      # mayor o igual que
    ('EQ', r'=='),                       # igualar
    ('NEQ', r'!='),                      # no es igual
    ('LPAREN', r'\('),                   # parentesis izquierdo
    ('RPAREN', r'\)'),                   # parentesis derecho
    ('LBRACE', r'\{'),                   # llave izquierda
    ('RBRACE', r'\}'),                   # llave derecha
    ('SEMI', r';'),                      # punto y coma
    ('COMMA', r','),                     # coma
    ('LBRACKET', r'\['),                 # corchete izquierdo
    ('RBRACKET', r'\]'),                 # corchete derecho
    ('MULTI_COMMENT', r'/\*(.|\n)*?\*/'),# comentario multiples lineas


    # Identifiers and literals
    ('ID', r'[a-zA-Z_][a-zA-Z_]*'),     # identifier
    ('NUM', r'\d+(\.\d*)?'),            # integer or decimal number
    ('char', r'\'[^\']*\''),            # character literal
    ('digit', r'\d+'),                  # integer literal

]

# Define the function to tokenize the input string

patterns = '|'.join('(?P<%s>%s)' % pair for pair in tokens)

def tokenize(code):
    for match in re.finditer(patterns, code):
        token_type = match.lastgroup
        token_value = match.group(token_type)
        if token_type == 'IDENTIFIER':
            yield (token_type, token_value)
        elif token_type == 'NUMBER':
            yield (token_type, float(token_value))
        elif token_type == 'STRING':
            yield (token_type, token_value[1:-1])
        elif token_type == 'CHAR':
            yield (token_type, token_value[1:-1])
        else:
            yield (token_type, token_value)


#import prueba.txt from the same directory

f = open(os.path.join(__location__, 'bundled-resource.jpg'))
f = open('prueba.c-', 'r')


#code = open('prueba.txt').read()
#code = open("prueba.txt", "r")
 


for token in tokenize(code):
    print(token)