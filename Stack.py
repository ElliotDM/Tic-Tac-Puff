class Stack():
    def __init__(self) -> None:
        self.items = []

    def append(self, x):
        self.items.append(x)

    def pop(self):
        try:
            return self.items.pop()
        except IndexError:
            raise ValueError("Stack is empty")
        
    def print(self):
        for _ in self.items:
            print(_)
