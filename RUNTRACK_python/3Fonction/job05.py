def calcule(num1, operator, num2):
    if operator == "+":
     return num1 + num2
    elif operator == "-":
     return num1 - num2
    elif operator == "*":
     return num1 * num2
    elif operator == "/":
     if num2 != 0:
      return num1 / num2
     else:
      return "Erreur : division par zéro"
    elif operator == "%":
     return num1 % num2
    else:
     return "Opérateur invalide"

    
print(calcule(12, "+", 7))
print(calcule(12, "-", 7))
print(calcule(12, "*", 7))
print(calcule(12, "/", 7))
print(calcule(12, "%", 7))