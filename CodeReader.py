class CodeReader:
    path: str
    last: str
    def __init__(self, path):
        self.path = path

    def setLast(self, char):
        if char == " " or char == "\n":
            return
        self.last = char

    def getLast(self):
        return self.last

    def getchar(self):
        with open(self.path, 'r') as file:
            while True:
                char = file.read(1)  # Lee un solo caracter del archivo
                if not char:
                    break  # Se alcanzó el final del archivo
                yield char
                self.setLast(char)