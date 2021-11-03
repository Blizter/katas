from src import light_grid


def main():

    christmas_light_grid = light_grid.LightGrid(height=1000, width=1000)

    christmas_light_grid.turn_on(x_1=887, y_1=9, x_2=959, y_2=629)
    print(christmas_light_grid.get_lit_lights())
    christmas_light_grid.turn_on(x_1=454, y_1=398, x_2=844, y_2=448)
    print(christmas_light_grid.get_lit_lights())
    christmas_light_grid.turn_off(x_1=539, y_1=243, x_2=559, y_2=965)
    print(christmas_light_grid.get_lit_lights())
    christmas_light_grid.turn_off(x_1=370, y_1=819, x_2=676, y_2=868)
    print(christmas_light_grid.get_lit_lights())
    christmas_light_grid.turn_off(x_1=145, y_1=40, x_2=370, y_2=997)
    print(christmas_light_grid.get_lit_lights())
    christmas_light_grid.turn_off(x_1=301, y_1=3, x_2=808, y_2=453)
    print(christmas_light_grid.get_lit_lights())
    christmas_light_grid.turn_on(x_1=351, y_1=678, x_2=951, y_2=908)
    print(christmas_light_grid.get_lit_lights())
    christmas_light_grid.toggle(x_1=720, y_1=196, x_2=897, y_2=994)
    print(christmas_light_grid.get_lit_lights())
    christmas_light_grid.toggle(x_1=831, y_1=394, x_2=904, y_2=860)
    print(christmas_light_grid.get_lit_lights())


if __name__ == '__main__':
    main()
