class LightGrid:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.grid = [[0 for i in range(self.width)] for j in range(self.height)]

    def show_lights(self) -> str:
        return "\n".join(["".join([str(i) for i in row]) for row in self.grid])

    def turn_on(self, x_1, y_1, x_2, y_2):

        x_2 += 1
        y_2 += 1

        for i in range(x_1, x_2):
            for j in range(y_1, y_2):
                self.grid[i][j] = 1

        return self.grid

    def turn_off(self):
        pass

    def toggle(self):
        pass
