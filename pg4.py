import re

def lexical_analyzer(text):
    token_specification = [
        ('NUMBER', r'\d+'),
        ('ASSIGN', r'='),
        ('END', r';'),
        ('ID', r'[A-Za-z]+'),
        ('OP', r'[+\-*/]'),
        ('SKIP', r'[ \t\n]+'),
        ('MISMATCH', r'.')
    ]
    
    tok_regex = '|'.join(f'(?P<{pair[0]}>{pair[1]})' for pair in token_specification)
    line_num = 1
    line_start = 0

    for mo in re.finditer(tok_regex, text):
        kind = mo.lastgroup
        value = mo.group()
        
        if kind == 'SKIP':
            continue
        elif kind == 'MISMATCH':
            raise RuntimeError(f'{value!r} unexpected on line {line_num}')
        
        yield kind, value

text = "x = 10 + 20;"
tokens = list(lexical_analyzer(text))
print(tokens)
