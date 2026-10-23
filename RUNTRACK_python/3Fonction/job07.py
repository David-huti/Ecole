def verifier_langage(langage):
    if langage == "Python":
        return "« tu es undéveloppeur IA."
    elif langage == "Java":
        return "tu es undéveloppeur logiciel."
    elif langage == "javascript":
        return "tu es undéveloppeur web."
    elif langage == "reactjs":
            return "tu es undéveloppeur mobile."
    else:
        return "un jour, je serai le meilleur développeur..."
langage = input(":entrer un langage: " "")
print(verifier_langage(langage))