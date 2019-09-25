***********************
Tuples et dictionnaires
***********************

Tuples
======

Les tuples ressemblent aux listes, mais contrairement à elles on ne peut pas les modifier une fois qu'ils ont été créés. 

On dit qu'un tuple n'est pas *mutable*.

On le définit avec des parenthèses.

>>> a = (2, 3)
>>> type(a)
<class 'tuple'>
 
Parfois, les tuples ne sont pas entourés de parenthèses, même s'il s'agit en fait de tuples.

Ainsi, on peut utiliser la notation suivante :

>>> b, c = 5, 6
>>> b
5
>>> c
6

En fait, cela revient à :

>>> (b, c) = (5, 6)

>>> u, v = a
>>> u
2
>>> v
3

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

Comme une liste, il est possible de parcourir un tuple avec une boucle **for**.

::

    for i in a:
        print(i)

::

    3
    4

Il est possible de récupérer la valeur d'un élément du tuple en utilisant la même syntaxe que pour une liste.  

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

En effet, les parenthèses sont alors considérées comme celles d'une expression mathématique (par exemple ``3*(4+1)``).

Pour créer un tuple contenant un seul élément, il faut donc utiliser une syntaxe qui contient une virgule.

>>> b = (3,)
>>> b
(3,)
>>> type(b)
<class 'tuple'>

Si on veut récupérer l'unique valeur présente dans le tuple, on va pouvoir utiliser les approches suivantes :

>>> c = b[0]
>>> c
3
>>> d, = b
>>> d
3

Dictionnaires
=============

Nous avons vu qu'il est possible de rassembler des éléments dans un liste ou un tuple.

Les éléments de la liste ou du tuple sont ordonnés et on accéde à un élément grâce à sa position en utilisant un numéro qu'on appelle l'**indice** de l'élément.

Un dictionnaire en Python va également permettre de rassembler des éléments mais ceux-ci seront identifiés par une **clé** de la même façon que dans un dictionnaire de français on accède à une définition à partir d'un mot. 

Contrairement aux listes qui sont délimitées par des crochets, on utilise des accolades pour les dictionnaires. 

**Exemple**

>>> mon_dictionnaire = {"voiture": "véhicule à quatre roues", "vélo": "véhicule à deux roues"}

Un élément est ici défini dans le dictionnaire en précisant une chaîne de caractères comme **clé** suivie de ``:`` puis de la **valeur** associée. 

On accède à la **valeur** en utilisant la **clé** entourée par des crochets avec la syntaxe suivante :

>>> mon_dictionnaire["voiture"]
'véhicule à quatre roues'

Le *type* d'un dictionnaire est ``dict``.

>>> type(mon_dictionnaire)
<class 'dict'>

Il est très facile d'ajouter un élément à une liste. Il suffit d'affecter une valeur pour la nouvelle clé. 

>>> mon_dictionnaire["tricycle"] = "véhicule à trois roues"
>>> mon_dictionnaire
{'voiture': 'véhicule à quatre roues',
'vélo': 'véhicule à deux roues',
'tricycle': 'véhicule à trois roues'}

Il est aussi possible d'utiliser des valeurs d'autres types.

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

::

    l'élément de clé voiture vaut 4
    l'élément de clé vélo vaut 2
    l'élément de clé tricycle vaut 3
