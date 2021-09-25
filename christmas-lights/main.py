import light_grid


def main():
    grid_height = 1000
    grid_width = 1000

    christmas_light_grid = light_grid(height=grid_height, width=grid_width)

    christmas_light_grid.description()


if __name__ == "__main__":
    main()
