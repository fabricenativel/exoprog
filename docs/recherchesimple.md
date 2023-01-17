{% set num = 2 %}

# Recherche simple

## Enoncé

### Fonction à écrire

<div class="enonce">
    Ecrire une fonction <code>est_dans</code> qui prend en arguments un entier <code>n</code> et une liste d'entiers <code>entiers</code> et renvoie <code>True</code> si <code>n</code> est dans la liste <code>entiers</code> et <code>False</code> sinon.
</div>

### Exemples

```pycon
>>> est_dans(4,[5,2,-11,3])
False
>>> est_dans(7,[5,-2,7,-11,3])
True
>>> est_dans(11,[])
False
```

## Prédire des résultats de tests

{{qcm_chapitre(num)}} 

## Proposer une méthode 

<form class="centre">
<textarea rows="5" cols="60">
1) Parcourir la liste si on rencontre l'élément on renvoie True (et on arrête le parcours),
2) A la fin du parcours on renvoie False
</textarea>
</form>

## Programmer

{{ IDE('recherche') }}

