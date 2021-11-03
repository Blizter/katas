class LightGrid:
    def __init__(self, height: int, width: int):
        self.height = height
        self.width = width
        self.grid = [[0 for i in range(width)] for j in range(height)]

    def __fix_coordinates(self, x_1, y_1, x_2, y_2):

        if x_1 > x_2:
            x_1, x_2 = x_2, x_1
        if y_1 > y_2:
            y_1, y_2 = y_2, y_1

        x_2 += 1
        y_2 += 1

        return x_1, y_1, x_2, y_2

    def turn_on(self, x_1, y_1, x_2, y_2):

        x_1, y_1, x_2, y_2 = self.__fix_coordinates(x_1, y_1, x_2, y_2)

        for i in range(x_1, x_2):
            for j in range(y_1, y_2):
                self.grid[i][j] = 1

        return self.grid

    def turn_off(self, x_1, y_1, x_2, y_2):

        x_1, y_1, x_2, y_2 = self.__fix_coordinates(x_1, y_1, x_2, y_2)

        for i in range(x_1, x_2):
            for j in range(y_1, y_2):
                self.grid[i][j] = 0

        return self.grid

    def toggle(self, x_1, y_1, x_2, y_2):

        x_1, y_1, x_2, y_2 = self.__fix_coordinates(x_1, y_1, x_2, y_2)

        for i in range(x_1, x_2):
            for j in range(y_1, y_2):
                self.grid[i][j] = 1 if (self.grid[i][j] == 0) else 0

        return self.grid

    def get_lit_lights(self):
        lit_lights = 0
        for i in self.grid:
            for j in i:
                lit_lights += 1 if (j == 1) else 0
        return lit_lights

    def show_lights(self):
        return "\n".join(["".join([str(i) for i in row]) for row in self.grid])

    def write_to_file(self):
        with open("show_light.txt", 'w') as writer:
            writer.write(str(self.grid))
