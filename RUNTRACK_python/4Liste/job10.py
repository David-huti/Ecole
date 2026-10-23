L = [8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]

produit = 1
for nomber in L:
    if nomber <= 25 and nomber <= 90:
        produit = produit * nomber
print(produit)