***********************
Tuples et dictionnaires
***********************

Tuples
======

A partir des types de base (*int*, *float*, etc.), il est possible d'en élaborer de nouveaux. On les appelle des *types construits*. 

Un exemple de *type construit* est le **tuple**. Il permet de créer une **collection ordonnée de plusieurs éléments**. En mathématiques, on parle de **p-uplet**. Par exemple, un quadruplet est constitué de 4 éléments.

Les tuples ressemblent aux listes, mais on ne peut pas les modifier une fois qu'ils ont été créés. 

On dit qu'un tuple n'est pas *mutable*.

On le définit avec des **parenthèses**.

>>> a = (3, 4, 7)
>>> type(a)
<class 'tuple'>
 
Parfois, les tuples ne sont pas entourés de parenthèses, même s'il s'agit quand même de tuples.

Ainsi, on peut utiliser la notation suivante :

>>> b, c = 5, 6
>>> b
5
>>> c
6

En fait, cela revient à :

>>> (b, c) = (5, 6)

Cette syntaxe avec plusieurs variables à gauche du signe ``=`` peut aussi être utilisée avec une variable unique à droite si celle-ci contient un tuple.

>>> a = (3, 4)
>>> u, v = a
>>> u
2
>>> v
3

**Comment écrire une fonction qui renvoie un p-uplet de valeurs ?**

Il est très facile de créer une fonction qui renvoie un tuple. Il suffit d'indiquer ce tuple après ``return``.

::

   def test():
        return 3, 4

>>> a = test()
>>> a
(3, 4)
>>> b, c = test()
>>> b
3
>>> c
4

..note::

   Après ``return``, il aurait aussi été possible d'utiliser une notation avec des parenthèses pour le tuple, par exemple ``return (3, 4)``
   
**Comment itérer sur les éléments d'un tuple ?**   

Comme une liste, il est possible de parcourir un tuple avec une boucle **for**.

::

    for i in a:
        print(i)

*Résultat*

::

    3
    4

La valeur d'un élément du tuple est obtenue en utilisant la même syntaxe que pour une liste.  

>>> a[0]
3
>>> a[1]
4

**Comment créer un tuple qui contient un seul élément ?**

Si on utilise seulement des parenthèses, on n'obtient pas le résultat escompté.

>>> a = (3)
>>> a
3
>>> type(a)
int

En effet, les parenthèses sont alors considérées comme celles d'une expression mathématique, comme par exemple dans ``3*(4+1)``.

Pour créer un tuple contenant un seul élément, il faut donc utiliser une syntaxe spécifique qui contient une virgule.

>>> b = (3,)
>>> b
(3,)
>>> type(b)
<class 'tuple'>

Si on veut récupérer l'unique valeur présente dans le tuple, on va pouvoir utiliser les approches suivantes :

*Première approche*

>>> c = b[0]
>>> c
3

*Deuxième approche*

>>> d, = b
>>> d
3

La deuxième approche avec une virgule ``d, = b`` est plus légère que la syntaxe qui utilise des crochets ``c = b[0]``.

Il est possible d'utiliser la syntaxe ``nom_de_variable, =`` aussi avec une liste à un élément.

>>> u = [5]
>>> v, = u
>>> v
5

Dictionnaires
=============

Nous avons vu qu'il est possible de rassembler des éléments dans un liste ou un tuple.

Les éléments de la liste ou du tuple sont ordonnés et on accéde à un élément grâce à sa position en utilisant un numéro qu'on appelle l'**indice** de l'élément.

Un dictionnaire en Python va également permettre de rassembler des éléments mais ceux-ci seront identifiés par une **clé** de la même façon que dans un dictionnaire de français on accède à une définition à partir d'un mot. 

Contrairement aux listes qui sont délimitées par des crochets, on utilise des accolades pour les dictionnaires. 

**Exemple**

>>> mon_dictionnaire = {"voiture": "véhicule à quatre roues", "vélo": "véhicule à deux roues"}

**Comment construire une entrée dans le dictionnaire ?**

Un élément a été défini ci-dessus dans le dictionnaire en précisant une **clé** au moyen d'une chaîne de caractères suivie de ``:`` puis de la **valeur** associée 

*cle*: *valeur*

On accède à une **valeur** du dictionnaire en utilisant la **clé** entourée par des crochets avec la syntaxe suivante :

>>> mon_dictionnaire["voiture"]
'véhicule à quatre roues'

Il est très facile d'ajouter un élément à un dictionnaire. Il suffit d'affecter une **valeur** pour la nouvelle **clé**. 

>>> mon_dictionnaire["tricycle"] = "véhicule à trois roues"

>>> mon_dictionnaire
{'voiture': 'véhicule à quatre roues',
'vélo': 'véhicule à deux roues',
'tricycle': 'véhicule à trois roues'}


Le *type* d'un dictionnaire est ``dict``.

>>> type(mon_dictionnaire)
<class 'dict'>

Il est aussi possible d'utiliser des valeurs d'autres types.

Voici un exemple où les valeurs sont des entiers.

>>> nombre_de_roues = {"voiture": 4, "vélo": 2}
>>> type(nombre_de_roues)
<class 'dict'>
>>> nombre_de_roues["vélo"]
2

Comment parcourir un dictionnaire ?
-----------------------------------

**Exemple**

::

    nombre_de_roues = {"voiture": 4, "vélo": 2, "tricycle": 3}

    for i in nombre_de_roues.items():
        print(i)

::

    ('voiture', 4)
    ('vélo', 2)
    ('tricycle', 3)

**Autre exemple**

::

    nombre_de_roues = {"voiture": 4, "vélo": 2, "tricycle": 3}

    for cle, valeur in nombre_de_roues.items():
        print("l'élément de clé", cle, "vaut", valeur)

*Résultat*
::

    l'élément de clé voiture vaut 4
    l'élément de clé vélo vaut 2
    l'élément de clé tricycle vaut 3
