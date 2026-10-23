L = [8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]

maximum = L[0]
minimum = L[0]
for nomber in L:
    if nomber > maximum:
        maximum = nomber
    if nomber < minimum:
        minimum = nomber
print("la valeur max est:", maximum)
print("la valeur min est:", minimum)