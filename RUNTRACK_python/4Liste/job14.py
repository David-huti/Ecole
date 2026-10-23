def my_long_word(n, phrase):
    mots = phrase.split()
    resultat = []

    for mot in mots:
        if len(mot) > n:
            resultat.append(mot)


    return " ".join(resultat)


phrase = "La peur est le chemin vers le côté obscur, la peur mène à la colère, la colère mène à la haine, la haine mène à la souffrance"

print(my_long_word(3, phrase))