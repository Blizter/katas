class LightGrid:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.grid = [[0 for i in range(self.width)] for j in range(self.height)]

    def __str__(self) -> str:
        return "\n".join([" ".join([str(i) for i in row]) for row in self.grid])
