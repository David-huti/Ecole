L = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]

nouvelle_liste = []

for x in L:
  if x not in nouvelle_liste:
    nouvelle_liste.append(x)

print(nouvelle_liste)