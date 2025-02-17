class ForthInterpreter:
    def __init__(self):
        self.stack = []
        self.definitions = {}
        self.variables = {}
        self.current_definition = None
        self.create_mode = False
        self.create_name = None

    def execute(self, code):
        tokens = code.split()
        for token in tokens:
            if self.create_mode:
                self.variables[self.create_name] = int(token)
                self.create_mode = False
            elif self.current_definition is not None:
                if token == ';':
                    self.definitions[self.current_definition] = self.current_definition_body
                    self.current_definition = None
                else:
                    self.current_definition_body.append(token)
            elif token == ':':
                self.current_definition = tokens[tokens.index(token) + 1]
                self.current_definition_body = []
            elif token == 'CREATE':
                self.create_mode = True
                self.create_name = tokens[tokens.index(token) + 1]
            elif token == 'DOES>':
                self.definitions[self.create_name] = self.current_definition_body
                self.current_definition = None
            elif token.isdigit():
                self.stack.append(int(token))
            elif token in self.definitions:
                self.execute(' '.join(self.definitions[token]))
            else:
                self._execute_command(token)
        return self.stack

    def _execute_command(self, command):
        if command == '+':
            b = self.stack.pop()
            a = self.stack.pop()
            self.stack.append(a + b)
        elif command == '-':
            b = self.stack.pop()
            a = self.stack.pop()
            self.stack.append(a - b)
        elif command == '*':
            b = self.stack.pop()
            a = self.stack.pop()
            self.stack.append(a * b)
        elif command == '/':
            b = self.stack.pop()
            a = self.stack.pop()
            self.stack.append(a // b)
        elif command == 'MOD':
            b = self.stack.pop()
            a = self.stack.pop()
            self.stack.append(a % b)
        elif command == 'DUP':
            self.stack.append(self.stack[-1])
        elif command == 'DROP':
            self.stack.pop()
        elif command == 'SWAP':
            self.stack[-1], self.stack[-2] = self.stack[-2], self.stack[-1]
        elif command == 'OVER':
            self.stack.append(self.stack[-2])
        elif command == '.':
            print(self.stack.pop())
        elif command == 'ROT':
            self.stack[-3], self.stack[-2], self.stack[-1] = self.stack[-2], self.stack[-1], self.stack[-3]
        elif command == '@':
            var_name = self.stack.pop()
            self.stack.append(self.variables[var_name])

def main():
    interpreter = ForthInterpreter()
    print("Forth Interpreter. Escribe 'exit' para salir.")
    while True:
        try:
            code = input("> ")
            if code.lower() == 'exit':
                break
            interpreter.execute(code)
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
