class LightGrid:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.grid = [[0 for i in range(self.width)] for j in range(self.height)]

    def show_lights(self) -> str:
        return "\n".join(["".join([str(i) for i in row]) for row in self.grid])

    def __fix_coordinates(self, x_1, y_1, x_2, y_2):

        if x_1 > x_2:
            x_1, x_2 = x_2, x_1
        if y_1 > y_2:
            y_1, y_2 = y_2, y_1

        x_2 += 1
        y_2 += 1

        return x_1, x_2, y_1, y_2

    def turn_on(self, x_1, y_1, x_2, y_2):

        # x_2 += 1
        # y_2 += 1
        local_x_1, local_y_1, local_x_2, local_y_2 = self.__fix_coordinates(x_1=x_1, y_1=y_1, x_2=x_2, y_2=y_2)

        print(str(x_1) + str(y_1) + str(x_2) + str(y_2))

        for i in range(local_x_1, local_x_2):
            print(str(i))
            for j in range(local_y_1, local_y_2):
                print(str(j))
                self.grid[i][j] = 1

        return self.grid

    # def turn_off(self, x_1, y_1, x_2, y_2):

    #     x_1, y_1, x_2, y_2 = self.__fix_coordinates(x_1, y_1, x_2, y_2)

    #     for i in range(x_1, x_2):
    #         for j in range(y_1, y_2):
    #             self.grid[i][j] = 0

    #     return self.grid

    # def toggle(self, x_1, y_1, x_2, y_2):

    #     x_1, y_1, x_2, y_2 = self.__fix_coordinates(x_1, y_1, x_2, y_2)

    #     for i in range(x_1, x_2):
    #         for j in range(y_1, y_2):
    #             if self.grid[i][j] == 0:
    #                 self.grid[i][j] = 1
    #             else:
    #                 self.grid[i][j] = 0

    #     return self.grid
