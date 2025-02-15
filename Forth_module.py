from forth_interpreter import ForthInterpreter

class Forth:
    def __init__(self):
        self.interpreter = ForthInterpreter()

    def run(self, code):
        return self.interpreter.execute(code)

# Ejemplo de uso
if __name__ == "__main__":
    forth = Forth()
    print(forth.run("3 4 +"))  # Debería imprimir [7]
    print(forth.run("10 2 /"))  # Debería imprimir [5]
    print(forth.run("5 dup *"))  # Debería imprimir [25]
