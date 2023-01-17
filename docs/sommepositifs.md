{% set num = 1 %}

# Somme des éléments d'une liste

## Enoncé

### Fonction à écrire

<div class="enonce">
    Ecrire une fonction <code>somme_positifs</code> qui prend en arguments une liste d'entiers <code>entiers</code> et renvoie la somme des éléments positifs de cette liste. Si la liste ne contient aucun entier positif alors la fonction renvoie 0.
</div>

### Exemples

```pycon
>>> somme_positifs([5,2,-11,4])
11
>>> somme_positifs([-15,-9])
0
>>> somme_positifs([1,2,3,4])
10
```



## Prédire des résultats de tests

{{qcm_chapitre(num)}} 

## Proposer une méthode 

<form class="centre">
<textarea rows="5" cols="60">
1) Créer une variable somme valant 0
2) Parcourir la liste, si un élément est positif l'ajouter à la variable somme
3) Renvoyer la variable somme
</textarea>
</form>

## Programmer

{{ IDE('somme_positifs') }}

