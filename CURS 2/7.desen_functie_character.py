def render(width = 10, height = 10):
    string = ""
    for i in range(width):
        for j in range(height):
            if i == 0 or i == (width - 1) or j == 0 or j == (height - 1):
                string += "#" 
            else: 
                string += " " 
            # string += f"{i}{j} "
        string += "\n"
    print(string)


# render(5, 5)
render(5)
# render()        # Eroare