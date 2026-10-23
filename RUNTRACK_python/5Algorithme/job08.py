def my_sort(liste):
    coups = 0
    n = len(liste)

# On parcourt la liste plusieurs fois
    for i in range(n):
# On compare les éléments voisins
      for j in range(0, n - i - 1):

# Si les éléments sont dans le mauvais ordre
       if liste[j] > liste[j + 1]:

# On échange les deux éléments
        liste[j], liste[j + 1] = liste[j + 1], liste[j]

# On compte l'échange
    coups += 1

    print("Nombre de coups :", coups)

    return liste


nombres = [5, 2, 8, 1, 3]
print(my_sort(nombres))