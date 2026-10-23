def draw_tapis(n):
    print("+" + "-" * (n + 1) + "+")

    for i in range(n + 1):
       ligne = "#" * (n - i) + " " + "#" * i
       print("|" + ligne + "|")

    print("+" + "-" * (n + 1) + "+")

draw_tapis(30)