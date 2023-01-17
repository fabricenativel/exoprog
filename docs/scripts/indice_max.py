def indice_max(entiers):
    indice = 0
    maxi = entiers[0]
    for i  in range(len(entiers)):
        if entiers[i]>maxi:
            indice = i
            maxi = entiers[i]
    return indice