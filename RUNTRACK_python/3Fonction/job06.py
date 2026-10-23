def verifier_nombre(nombre):
      if nombre < 0:
        return "Le nombre est négatif."
      elif nombre == 0:
        return "Le nombre est zéro."
      else:
        return "Le nombre est positif."
print(verifier_nombre(int(input(":entrer un nombre: " "")))) 