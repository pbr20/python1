from random import randint


def rgb_color_gen():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)

    return f"rgb({r},{g},{b})"
