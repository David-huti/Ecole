def cesar(message, decalage):
    resultat = ""

    for lettre in message:
       if lettre.isalpha() and lettre.isascii():
          base = ord("A") if lettre.isupper() else ord("a")

          nouvelle_lettre = chr(
         (ord(lettre) - base + decalage) % 26 + base)
          resultat += nouvelle_lettre
    else:
     resultat += lettre

    return resultat


print(cesar("abc xyz", 3))
print(cesar("abc", -1))