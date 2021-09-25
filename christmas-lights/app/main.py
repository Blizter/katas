import light_grid


def main():
    grid_height = 1000
    grid_width = 1000

    christmas_light_grid = light_grid.LightGrid(height=grid_height, width=grid_width)

    print(christmas_light_grid.show_lights())


if __name__ == "__main__":
    main()
