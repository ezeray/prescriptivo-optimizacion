class Tablero:
    def __init__(self, size: int) -> None:
        self.board = [['' for _ in range(size)] for _ in range(size)]
        
