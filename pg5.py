class SymbolTable:
    def __init__(self):
        self.symbols = {}

    def add_symbol(self, name, datatype):
        if name in self.symbols:
            raise ValueError(f"Variable {name} already declared")
        self.symbols[name] = datatype

    def check_symbol(self, name):
        if name not in self.symbols:
            raise ValueError(f"Variable {name} not declared")
        return self.symbols[name]

def semantic_analyzer(code):
    symbol_table = SymbolTable()

    for line in code:
        line = line.strip()

        if '=' in line:
            var_name, value = line.split('=')
            var_name = var_name.strip()
            value = value.strip()

            if value.isdigit():
                symbol_table.add_symbol(var_name, 'int')
            else:
                symbol_table.check_symbol(value)  
                symbol_table.add_symbol(var_name, 'unknown')  
        elif 'print' in line:
            var_name = line.split()[1]
            symbol_table.check_symbol(var_name)  

code = [
    "x = 10",
    "y = x",
    "print y"
]

semantic_analyzer(code)
print("Semantic analysis completed successfully!")
