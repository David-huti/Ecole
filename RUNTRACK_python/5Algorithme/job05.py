def distance_semaine(marches, hauteur):
    distance = marches * hauteur * 2 * 5 * 7
    distance = distance / 100

    print(
    f"Pour {marches} marches de {hauteur} cm, "
    f"le gardien parcourt {distance:.2f} m par semaine."
     )


distance_semaine(100, 15)