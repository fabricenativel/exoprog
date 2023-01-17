{% set num = 3 %}

# Indice du maximum

## Enoncé

### Fonction à écrire

<div class="enonce">
    Ecrire une fonction <code>indice_max</code> qui prend en arguments  une liste d'entiers <code>entiers</code> non vide et renvoie l'indice de la première occurrence du maximum des éléments de cette liste.
</div>

### Exemples

```pycon
>>> indice_max([3,5,2,-11,3])
1
>>> indice_max([9,9,9,9])
0
>>> indice_max([-9,-12,-3,-1,-8])
3
```

## Prédire des résultats de tests


{{qcm_chapitre(num)}} 

## Proposer une méthode 

<form class="centre">
<textarea rows="5" cols="60">
1) Comme la liste est supposée non vide, on initialise la position du maximum à 0 et sa valeur au premier élément de la liste
2) On parcours la liste par indice, si on rencontre un élément plus grand que le maximum, on met le maximum et sa position à jour.
3) On renvoie l'indice du maximum
</textarea>
</form>

## Programmer

{{ IDE('indice_max') }}

