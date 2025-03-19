
def render(width, height):
    print("#" * width)
    for i in range(height - 2):
        print("#" + " " * (width - 2) + "#")
    print("#" * width)
render(10, 10)
render(4, 3)
render(20, 22)