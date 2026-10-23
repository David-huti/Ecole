def pair_ou_impair(nombre):
 if not isinstance(nombre, int) or isinstance(nombre, bool) or nombre < 0:
  print("Erreur : entrez un entier positif.")
 elif nombre % 2 == 0:
  print(nombre, "est pair")
 else:
  print(nombre, "est impair")


nombre = input("Entrez un entier positif : ")
try:
    nombre = int(nombre)
    pair_ou_impair(nombre)
except ValueError:
    print("Erreur : entrez un entier positif.")