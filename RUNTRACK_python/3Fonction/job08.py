def verifier_saison(type, saison):
    if type == "fruits" and saison == "hiver":
     print("orange, mandarine et kiwi")
    elif type == "fruits" and saison == "été":
     print("Poire, fraise, cassis")
    elif type == "légume" and saison == "hiver":
     print("carotte, topinambour, endive")
    elif type == "légume" and saison == "été":
     print("artichaut, aubergine, navet")

type = input("entrer un type (fruits ou légume): ")
saison = input("entrer une saison (hiver ou été): ")
verifier_saison(type, saison)