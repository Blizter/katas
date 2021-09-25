class LightGrid:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.grid = [[0 for i in range(self.width)] for j in range(self.height)]

    def show_lights(self) -> str:
        return "\n".join(["".join([str(i) for i in row]) for row in self.grid])

    def turn_on(self):
        pass

    def turn_off(self):
        pass

    def toggle(self):
        pass
