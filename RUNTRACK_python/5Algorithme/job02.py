def draw_triangle(height):
    for i in range(height):
        if i == 0:
           print(" " * (height - 1) + "/\\")
        elif i == height - 1:
             print("/" + "_" * (2 * height - 2) + "\\")
        else:
             print(" " * (height - i - 1) + "/" + " " * (2 * i) + "\\") 
height = 10
draw_triangle(height)