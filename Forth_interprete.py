class ForthInterpreter:
    def __init__(self):
        self.stack = []
        self.words = {
            '+': self.add,
            '-': self.sub,
            '*': self.mul,
            '/': self.div,
            'dup': self.dup,
            'drop': self.drop,
            'swap': self.swap,
            'over': self.over,
        }

    def add(self):
        b = self.stack.pop()
        a = self.stack.pop()
        self.stack.append(a + b)

    def sub(self):
        b = self.stack.pop()
        a = self.stack.pop()
        self.stack.append(a - b)

    def mul(self):
        b = self.stack.pop()
        a = self.stack.pop()
        self.stack.append(a * b)

    def div(self):
        b = self.stack.pop()
        a = self.stack.pop()
        self.stack.append(a // b)

    def dup(self):
        self.stack.append(self.stack[-1])

    def drop(self):
        self.stack.pop()

    def swap(self):
        a = self.stack.pop()
        b = self.stack.pop()
        self.stack.append(a)
        self.stack.append(b)

    def over(self):
        self.stack.append(self.stack[-2])

    def execute(self, code):
        for word in code.split():
            if word.isdigit():
                self.stack.append(int(word))
            elif word in self.words:
                self.words[word]()
            else:
                raise ValueError(f"Unknown word: {word}")
        return self.stack
