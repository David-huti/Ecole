L = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]

# Arrondir les nombres sans utiliser round()
for i in range(len(L)):
    entier = int(L[i])
    decimal = L[i] - entier

    if decimal >= 0.5:
       L[i] = entier + 1
    else:
        L[i] = entier

# Trier la liste dans l'ordre croissant
n = 0
for x in L:
    n += 1

for i in range(n):
    for j in range(n - 1):
        if L[j] > L[j + 1]:
         temp = L[j]
         L[j] = L[j + 1]
        L[j + 1] = temp

print(L)