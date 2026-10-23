def arrondir_notes(notes):
    resultat = []

    for note in notes:
     if note < 40:
      resultat.append(note)
    else:
        prochain_multiple = ((note // 5) + 1) * 5

    if prochain_multiple - note < 3:
     resultat.append(prochain_multiple)
    else:
      resultat.append(note)

    return resultat

print(arrondir_notes([37, 38, 42, 43, 83, 82]))