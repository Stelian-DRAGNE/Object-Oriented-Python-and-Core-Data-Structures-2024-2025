
string = ""
for i in range(10):
    for j in range(10):
        if i == 0 or i == 9 or j == 0 or j == 9:
            string += "#" 
        else: 
            string += " " 
        # string += f"{i}{j} "
    string += "\n"

print(string)