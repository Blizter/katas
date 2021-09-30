import pytest
from app import light_grid


all_one_grid = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

all_zeroes_grid = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]

square_of_one_grid = [
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]

toggled_square_of_one_grid = [
    [0, 0, 0, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]


grid_height = 10
grid_width = 10


class TestLightGrid:

    def test_turn_on_all_lights(self):

        test_light_grid = light_grid.LightGrid(height=grid_height, width=grid_width)

        method_output = test_light_grid.turn_on(x_1=0, y_1=0, x_2=9, y_2=9)
        assert method_output == all_one_grid

    def test_turn_on_all_lights_inverted_coordinates(self):

        test_light_grid = light_grid.LightGrid(height=grid_height, width=grid_width)

        method_output = test_light_grid.turn_on(x_1=9, y_1=9, x_2=0, y_2=0)
        assert method_output == all_one_grid

    def test_turn_on_range(self):

        test_light_grid = light_grid.LightGrid(height=grid_height, width=grid_width)

        method_output = test_light_grid.turn_on(x_1=0, y_1=0, x_2=2, y_2=2)
        assert method_output == square_of_one_grid

    def test_turn_on_range_inverted_coordinates(self):

        test_light_grid = light_grid.LightGrid(height=grid_height, width=grid_width)

        method_output = test_light_grid.turn_on(x_1=2, y_1=2, x_2=0, y_2=0)
        assert method_output == square_of_one_grid

    def test_turn_off_all_lights(self):

        test_light_grid = light_grid.LightGrid(height=grid_height, width=grid_width)
        test_light_grid.turn_on(x_1=0, y_1=0, x_2=9, y_2=9)
        turn_off_all_lights = test_light_grid.turn_off(x_1=0, y_1=0, x_2=9, y_2=9)

        assert turn_off_all_lights == all_zeroes_grid

    def test_turn_off_all_lights_inverted_coordinates(self):

        test_light_grid = light_grid.LightGrid(height=grid_height, width=grid_width)
        test_light_grid.turn_on(x_1=0, y_1=0, x_2=9, y_2=9)
        turn_off_all_lights = test_light_grid.turn_off(x_1=9, y_1=9, x_2=0, y_2=0)

        assert turn_off_all_lights == all_zeroes_grid

    def test_turn_off_range(self):

        test_light_grid = light_grid.LightGrid(height=grid_height, width=grid_width)
        test_light_grid.turn_on(x_1=0, y_1=0, x_2=2, y_2=2)
        turn_off_all_lights = test_light_grid.turn_off(x_1=0, y_1=0, x_2=2, y_2=2)

        assert turn_off_all_lights == all_zeroes_grid

    def test_turn_off_range_inverted_coordinates(self):

        test_light_grid = light_grid.LightGrid(height=grid_height, width=grid_width)
        test_light_grid.turn_on(x_1=0, y_1=0, x_2=2, y_2=2)
        turn_off_all_lights = test_light_grid.turn_off(x_1=2, y_1=2, x_2=0, y_2=0)

        assert turn_off_all_lights == all_zeroes_grid

    def test_toggle_all_lights(self):

        test_light_grid = light_grid.LightGrid(height=grid_height, width=grid_width)
        test_light_grid.turn_on(x_1=0, y_1=0, x_2=9, y_2=9)
        toggle_all_lights = test_light_grid.toggle(x_1=0, y_1=0, x_2=9, y_2=9)

        assert toggle_all_lights == all_zeroes_grid

    def test_toggle_all_lights_inverted_coordinates(self):

        test_light_grid = light_grid.LightGrid(height=grid_height, width=grid_width)
        test_light_grid.turn_on(x_1=0, y_1=0, x_2=9, y_2=9)
        toggle_all_lights = test_light_grid.toggle(x_1=9, y_1=9, x_2=0, y_2=0)

        assert toggle_all_lights == all_zeroes_grid

    def test_toggle_all_lights_alternate_all(self):

        test_light_grid = light_grid.LightGrid(height=grid_height, width=grid_width)
        toggle_all_lights = test_light_grid.toggle(x_1=0, y_1=0, x_2=9, y_2=9)

        assert toggle_all_lights == all_one_grid

    def test_toggle_all_lights_alternate_range(self):

        test_light_grid = light_grid.LightGrid(height=grid_height, width=grid_width)
        toggle_all_lights = test_light_grid.toggle(x_1=0, y_1=0, x_2=2, y_2=2)

        assert toggle_all_lights == square_of_one_grid

    def test_toggle_same_range_lights(self):

        test_light_grid = light_grid.LightGrid(height=grid_height, width=grid_width)
        test_light_grid.turn_on(x_1=0, y_1=0, x_2=2, y_2=2)
        toggle_all_lights = test_light_grid.toggle(x_1=0, y_1=0, x_2=2, y_2=2)

        assert toggle_all_lights == all_zeroes_grid

    def test_toggle_different_range_lights(self):

        test_light_grid = light_grid.LightGrid(height=grid_height, width=grid_width)
        test_light_grid.turn_on(x_1=0, y_1=0, x_2=2, y_2=2)
        toggle_all_lights = test_light_grid.toggle(x_1=0, y_1=0, x_2=9, y_2=9)

        assert toggle_all_lights == toggled_square_of_one_grid
