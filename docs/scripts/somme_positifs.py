def somme_positifs(entiers):
    somme = 0
    for entier in entiers:
        if entier>0:
            somme += entier
    return somme