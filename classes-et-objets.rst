*****************
Classes et objets
*****************

La présentation de cette page est inspirée par le livre de Gérard Swinnen `"Apprendre à programmer avec Python 3" <http://inforef.be/swi/python.htm>`_ disponible sous licence `CC BY-NC-SA 2.0 <http://creativecommons.org/licenses/by-nc-sa/2.0/fr/>`_. L'introduction à la programmation orientée objet est également inspirée par le livre de Claude Delannoy "Programmer en Java" (Eyrolles) que vous êtes invités à consulter si vous souhaitez découvrir le langage Java. 

Python est un langage qui permet la **programmation orientée objet** (POO).

Brève introduction à la Programmation Orientée Objet
====================================================

Nous avons vu plusieurs types de base en Python (``int`` pour les entiers, ``float`` pour les flottants, ``str`` pour les chaînes de caractères, etc.). La notion de **classe** va en quelque sorte nous permettre de généraliser la notion de "type" afin de créer de nouvelles structures de données. 

Une classe définit des **attributs** et des **méthodes**. Par exemple, imaginons une classe :class:`Voiture` qui servira à créer des objets qui sont des voitures. Cette classe va pouvoir définir un attribut :attr:`couleur`, un attribut :attr:`vitesse`, etc. Ces attributs correspondent à des propriétés qui peuvent exister pour une voiture. La classe :class:`Voiture` pourra également définir une méthode :meth:`rouler`. Une méthode correspond en quelque sorte à une action, ici l'action de rouler peut être réalisée pour une voiture. Si on imagine une classe :class:`Avion`, elle pourra définir une méthode :meth:`voler`. Elle pourra aussi définir une méthode :meth:`rouler`. Par contre, la classe :class:`Voiture` n'aura pas de méthode :meth:`voler` car une voiture ne peut pas voler. De même, la classe :class:`Avion` pourra avoir un attribut :attr:`altitude` mais ce ne sera pas le cas pour la classe :class:`Voiture`. 


Après avoir présenté la notion de **classe**, nous allons voir la notion d'**objet**. On dit qu'un **objet est une instance de classe**. Si on revient à la classe :class:`Voiture`, nous pourrons avoir plusieurs voitures qui seront chacune des instances bien distinctes. Par exemple, la voiture de Jonathan, qui est de couleur rouge avec une vitesse de 30 km/h, est une instance de la classe :class:`Voiture`, c'est un **objet**. De même, la voiture de Denis, qui est de couleur grise avec une vitesse de 50 km/h, est un autre objet. Nous pouvons donc avoir plusieurs objects pour une même classe, en particulier ici deux objets (autrement dit : deux instances de la même classe). Chacun des objets a des valeurs qui lui sont propres pour les attributs.

La notion de classe
===================

Définition d'une classe :class:`Point`
--------------------------------------

Voici comment définir une classe appelée ici :class:`Point`.

::

    class Point:
        x = 0
        y = 0

Par convention en Python, le nom identifiant une classe (qu'on appelle aussi son identifiant) débute par une majuscule. Ici :class:`Point` débute par un **P** majuscule.
Nous venons de définir une classe :class:`Point`. Nous pouvons dès à présent nous en servir pour créer des objets de ce type, par instanciation. Créons par exemple un nouvel objet et mettons la référence à cet objet dans la variable ``p`` :

>>> p = Point()

.. warning:: 
   
   Comme pour les fonctions, lors de l'appel à une classe dans une instruction pour créer un objet, il faut toujours indiquer des parenthèses (même si aucun argument n'est transmis). Nous verrons un peu plus loin que ces appels peuvent se faire avec des arguments (voir la notion de constructeur).

   Remarquez bien cependant que la définition d'une classe ne nécessite pas de parenthèses (contrairement à ce qui de règle lors de la définition des fonctions), sauf si nous souhaitons que la classe en cours de définition dérive d'une autre classe préexistante (ceci sera expliqué plus loin).

Nous pouvons dès à présent effectuer quelques manipulations élémentaires avec notre nouvel objet dont la référence est dans ``p``. 

**Exemple :**

>>> print(p)
<__main__.Point instance at 0x012CAF30>

Le message renvoyé par Python indique que ``p`` contient une référence à une instance de la classe :class:`Point`, qui est définie elle-même au niveau principal du programme. Elle est située dans un emplacement bien déterminé de la mémoire vive, dont l'adresse apparaît ici en notation hexadécimale.

Définition des attributs
------------------------
::
                                                                                                                                              
    class Point:
        x = 0
        y = 0

La classe :class:`Point` possède deux attributs : les variables :attr:`x` et :attr:`y`.

La syntaxe pour accéder à un attribut est la suivante : on va utiliser la variable qui contient la référence à l'objet et on va mettre un point ``.`` puis le nom de l'attribut.

**Exemple**

::

    class Point:
        x = 0
        y = 0

    a = Point()
    b = Point()
    print("a : x =", a.x, "y =", a.y)
    print("b : x =", b.x, "y =", b.y)
    a.x = 1
    a.y = 2
    b.x = 3
    b.y = 4
    print("a : x =", a.x, "y =", a.y)
    print("b : x =", b.x, "y =", b.y)


Définition des méthodes
-----------------------
                                                                                                                                              
::

    class Point:
        x = 0
        y = 0

        def deplace(self, dx, dy):
            self.x = self.x + dx
            self.y = self.y + dy

Cette classe possède une méthode : :meth:`deplace`.

Pour définir une méthode, il faut :

#. indiquer son nom (ici :meth:`deplace`).
#. indiquer les arguments entre des parenthèses. Le premier argument d'une méthode doit être ``self``.

La notion d'objet
=================

::

    class Point:
        x = 0
        y = 0

        def deplace(self, dx, dy):
            self.x = self.x + dx
            self.y = self.y + dy

    a = Point()
    b = Point()
    print("a : x =", a.x, "y =", a.y)
    print("b : x =", b.x, "y =", b.y)
    a.x = 1
    a.y = 2
    b.x = 3
    b.y = 4
    print("a : x =", a.x, "y =", a.y)
    print("b : x =", b.x, "y =", b.y)
    a.deplace(-1, -1)
    b.deplace(3, 5)
    print("a : x =", a.x, "y =", a.y)
    print("b : x =", b.x, "y =", b.y)

.. raw:: html

    <p><a class="btn btn-primary" href="http://pythontutor.com/visualize.html#code=class+Point%3A%0A++++x+%3D+0%0A++++y+%3D+0%0A%0A++++def+deplace(self,+dx,+dy)%3A%0A++++++++self.x+%3D+self.x+%2B+dx%0A++++++++self.y+%3D+self.y+%2B+dy%0A%0Aa+%3D+Point()%0Ab+%3D+Point()%0Aprint(%22a+%3A+x+%3D%22,+a.x,+%22y+%3D%22,+a.y)%0Aprint(%22b+%3A+x+%3D%22,+b.x,+%22y+%3D%22,+b.y)%0Aa.x+%3D+1%0Aa.y+%3D+2%0Ab.x+%3D+3%0Ab.y+%3D+4%0Aprint(%22a+%3A+x+%3D%22,+a.x,+%22y+%3D%22,+a.y)%0Aprint(%22b+%3A+x+%3D%22,+b.x,+%22y+%3D%22,+b.y)%0Aa.deplace(-1,+-1)%0Ab.deplace(3,+5)%0Aprint(%22a+%3A+x+%3D%22,+a.x,+%22y+%3D%22,+a.y)%0Aprint(%22b+%3A+x+%3D%22,+b.x,+%22y+%3D%22,+b.y)&mode=display&origin=opt-frontend.js&cumulative=false&heapPrimitives=false&drawParentPointers=false&textReferences=false&showOnlyOutputs=false&py=3&rawInputLstJSON=%5B%5D&curInstr=0" target=_blank>Exécuter</a></p>


Création d'un objet de type :class:`Point`
------------------------------------------

::

    Point()

Ceci crée un objet de type :class:`Point`. En POO, on dit que l'on crée une **instance** de la classe :class:`Point`. 

Une phrase emblématique de la POO consiste à dire qu'**un objet est une instance de classe**.

Il faut bien noter que pour créer une instance, on utilise le nom de la classe suivi de parenthèses. Nous verrons par la suite qu'il peut y avoir des arguments entre ces parenthèses.

Affectation à une variable de la référence à un objet
-----------------------------------------------------

::

    a = Point()
    b = Point()

La variable ``a`` va contenir une référence à un objet.

>>> print(a)
<__main__.Point instance at 0x012CADC8>

De même ``b`` va contenir une référence à un autre objet.

>>> print(b)
<__main__.Point instance at 0x012CAF08>

Nous avons ici 2 instances de la classe :class:`Point` (2 objets) :

* la première à laquelle on fait référence au moyen de la variable ``a``,
* la seconde à laquelle on fait référence au moyen de la variable ``b``. 

On fait bien ici la distinction entre classe et objet. Ici nous avons une seule classe :class:`Point`, et deux objets de type :class:`Point`.

L'exemple suivant montre bien la distinction entre variable et objet :

::

    class Point:
        x = 0
        y = 0

        def deplace(self, dx, dy):
            self.x = self.x + dx
            self.y = self.y + dy

    a = Point()
    b = a
    print("a : x =", a.x, "y =", a.y)
    print("b : x =", b.x, "y =", b.y)
    a.x = 3
    a.y = 4
    print("a : x =", a.x, "y =", a.y)
    print("b : x =", b.x, "y =", b.y)
    b.deplace(4, 5)
    print("a : x =", a.x, "y =", a.y)
    print("b : x =", b.x, "y =", b.y)

.. raw:: html

    <p><a class="btn btn-primary" href="http://pythontutor.com/visualize.html#code=class+Point%3A%0A++++x+%3D+0%0A++++y+%3D+0%0A%0A++++def+deplace(self,+dx,+dy)%3A%0A++++++++self.x+%3D+self.x+%2B+dx%0A++++++++self.y+%3D+self.y+%2B+dy%0A%0Aa+%3D+Point()%0Ab+%3D+a%0Aprint(%22a+%3A+x+%3D%22,+a.x,+%22y+%3D%22,+a.y)%0Aprint(%22b+%3A+x+%3D%22,+b.x,+%22y+%3D%22,+b.y)%0Aa.x+%3D+3%0Aa.y+%3D+4%0Aprint(%22a+%3A+x+%3D%22,+a.x,+%22y+%3D%22,+a.y)%0Aprint(%22b+%3A+x+%3D%22,+b.x,+%22y+%3D%22,+b.y)%0Ab.deplace(4,+5)%0Aprint(%22a+%3A+x+%3D%22,+a.x,+%22y+%3D%22,+a.y)%0Aprint(%22b+%3A+x+%3D%22,+b.x,+%22y+%3D%22,+b.y)&mode=display&origin=opt-frontend.js&cumulative=false&heapPrimitives=false&drawParentPointers=false&textReferences=false&showOnlyOutputs=false&py=3&rawInputLstJSON=%5B%5D&curInstr=0" target=_blank>Exécuter</a></p>

Ici les variables ``a`` et ``b`` font référence au même objet puisque lors de l'affectation ``b = a`` on met dans la variable ``b`` la référence contenue dans la variable ``a``. Par conséquent, toute modification des valeurs des attributs de l'objet dont la référence est contenue dans ``a`` entraîne une modification pour ``b``.

.. warning:: par abus de langage on parlera parfois de l'objet ``a`` alors qu'il s'agira en fait de l'objet auquel ``a`` fait référence.

Accès aux attributs et aux méthodes d'un objet
----------------------------------------------

::

    a.x
    b.deplace(3, 5)

Pour accéder aux attributs et aux méthodes d'un objet. On indique :

#. le nom de la variable qui fait référence à cet objet
#. un point
#. le nom de l'attribut ou de la méthode

**Exercice**

Modifier le programme de façon à ajouter deux autres objets de type :class:`Point`. Ils seront référencés par des variables ``c`` et ``d``.

**Exercice**

Définir une classe :class:`Point3D` qui sera analogue à la classe :class:`Point` mais pour des points dans l'espace à 3 dimensions. Créer deux objets de type :class:`Point3D` qui seront référencés par les variables ``a3D`` et ``b3D``. Initialiser ces points et afficher leurs coordonnées *x*, *y*, *z*.

La notion d'encapsulation
=========================

Le concept d'**encapsulation** est un concept très utile de la POO. Il permet en particulier d'éviter une modification par erreur des données d'un objet. En effet, il n'est alors pas possible d'agit directement sur les données d'un objet ; il est nécessaire de passer par ses méthodes qui jouent le rôle d'interface obligatoire.

On réalise l'encapsulation des attributs de notre classe :class:`Point` grâce à l'utilisation de ``__`` (**deux fois** le symbole **underscore** ``_``, qui est le tiret sur la touche ``8``) pour débuter le nom des attributs privés.

::

    class Point:
        __x = 0
        __y = 0

Il n'est alors plus possible de faire appel aux attributs :attr:`__x` et :attr:`__y` depuis l'extérieur de la classe :class:`Point`.

::

    >>> p = Point()
    >>> p.__x

    Traceback (most recent call last):
      File "<pyshell#9>", line 1, in 
        p.__x
    AttributeError: Point instance has no attribute '__x'

Il faut donc définir de nouvelles méthodes qui vont permettre par exemple d'initialiser ou d'afficher les informations associées à ces variables.

::

    class Point:
        __x = 0
        __y = 0

        def initialise(self, x, y):
            self.__x = x
            self.__y = y
            
        def deplace(self, dx, dy):
            self.__x = self.__x + dx
            self.__y = self.__y + dy

        def affiche(self):
            print("Je suis un point de coordonnees ", self.__x, self.__y)
            
    a = Point()
    a.initialise(2, 4)
    a.affiche()
    a.deplace(-1, -1)
    a.affiche()

.. raw:: html

    <p><a class="btn btn-primary" href="http://pythontutor.com/visualize.html#code=class+Point%3A%0A++++__x+%3D+0%0A++++__y+%3D+0%0A%0A++++def+initialise(self,+x,+y)%3A%0A++++++++self.__x+%3D+x%0A++++++++self.__y+%3D+y%0A%0A++++def+deplace(self,+dx,+dy)%3A%0A++++++++self.__x+%3D+self.__x+%2B+dx%0A++++++++self.__y+%3D+self.__y+%2B+dy%0A%0A++++def+affiche(self)%3A%0A++++++++print(%22Je+suis+un+point+de+coordonnees+%22,+self.__x,+self.__y)%0A%0Aa+%3D+Point()%0Aa.initialise(2,+4)%0Aa.affiche()%0Aa.deplace(-1,+-1)%0Aa.affiche()&mode=display&origin=opt-frontend.js&cumulative=false&heapPrimitives=false&drawParentPointers=false&textReferences=false&showOnlyOutputs=false&py=3&rawInputLstJSON=%5B%5D&curInstr=0" target=_blank>Exécuter</a></p>

La notion de constructeur
=========================                                                                                                                                              

Si lors de la création d'un objet nous voulons qu'un certain nombre d'actions soit réalisées (par exemple une initialisation), nous pouvons utiliser un constructeur.

Un constructeur n'est rien d'autre qu'une méthode, sans valeur de retour, qui porte le même nom :meth:`__init__`. Cette méthode sera appelée lors de la création de l'objet. Le constructeur peut disposer d'un nombre quelconque d'arguments, éventuellement aucun.

::

    class Point:
        def __init__(self, x, y):
            self.__x = x
            self.__y = y
            
        def deplace(self, dx, dy):
            self.__x = self.__x + dx
            self.__y = self.__y + dy
            
        def affiche(self):
            print("Je suis un point de coordonnees ", self.__x, self.__y)
            
    a = Point(2, 4)
    a.affiche()
    a.deplace(-1, -1)
    a.affiche()

.. raw:: html

    <p><a class="btn btn-primary" href="http://pythontutor.com/visualize.html#code=class+Point%3A%0A++++def+__init__(self,+x,+y)%3A%0A++++++++self.__x+%3D+x%0A++++++++self.__y+%3D+y%0A%0A++++def+deplace(self,+dx,+dy)%3A%0A++++++++self.__x+%3D+self.__x+%2B+dx%0A++++++++self.__y+%3D+self.__y+%2B+dy%0A%0A++++def+affiche(self)%3A%0A++++++++print(%22Je+suis+un+point+de+coordonnees+%22,+self.__x,+self.__y)%0A%0Aa+%3D+Point(2,+4)%0Aa.affiche()%0Aa.deplace(-1,+-1)%0Aa.affiche()&mode=display&origin=opt-frontend.js&cumulative=false&heapPrimitives=false&drawParentPointers=false&textReferences=false&showOnlyOutputs=false&py=3&rawInputLstJSON=%5B%5D&curInstr=0" target=_blank>Exécuter</a></p>

**Exercice**

Définir une classe :class:`Point3D` analogue à la classe :class:`Point` mais pour des points dans l'espace à 3 dimensions.

Attributs et méthodes de classe
===============================

Attributs de classe
-------------------

**Exemple :**

::

    class A:
        nb = 0
        
        def __init__(self, val):
            print("creation objet de type A")
            self.x = val
            A.nb = A.nb + 1

    print("A : nb = ", A.nb)
    print("Partie 1")
    a = A(3)
    print("A : nb = ", A.nb)
    print("a : x = ", a.x, " nb = ", a.nb)
    print("Partie 2")
    b = A(6)
    print("A : nb = ", A.nb)
    print("a : x = ", a.x, " nb = ", a.nb)
    print("b : x = ", b.x, " nb = ", b.nb)
    c = A(8)
    print("Partie 3")
    print("A : nb = ", A.nb)
    print("a : x = ", a.x, " nb = ", a.nb)
    print("b : x = ", b.x, " nb = ", b.nb)
    print("c : x = ", c.x, " nb = ", c.nb)

.. raw:: html

    <p><a class="btn btn-primary" href="http://pythontutor.com/visualize.html#code=class+A%3A%0D%0A++++nb+%3D+0%0D%0A%0D%0A++++def+__init__(self,+val)%3A%0D%0A++++++++print(%22creation+objet+de+type+A%22)%0D%0A++++++++self.x+%3D+val%0D%0A++++++++A.nb+%3D+A.nb+%2B+1%0D%0A%0D%0Aprint(%22A+%3A+nb+%3D+%22,+A.nb)%0D%0Aprint(%22Partie+1%22)%0D%0Aa+%3D+A(3)%0D%0Aprint(%22A+%3A+nb+%3D+%22,+A.nb)%0D%0Aprint(%22a+%3A+x+%3D+%22,+a.x,+%22+nb+%3D+%22,+a.nb)%0D%0Aprint(%22Partie+2%22)%0D%0Ab+%3D+A(6)%0D%0Aprint(%22A+%3A+nb+%3D+%22,+A.nb)%0D%0Aprint(%22a+%3A+x+%3D+%22,+a.x,+%22+nb+%3D+%22,+a.nb)%0D%0Aprint(%22b+%3A+x+%3D+%22,+b.x,+%22+nb+%3D+%22,+b.nb)%0D%0Ac+%3D+A(8)%0D%0Aprint(%22Partie+3%22)%0D%0Aprint(%22A+%3A+nb+%3D+%22,+A.nb)%0D%0Aprint(%22a+%3A+x+%3D+%22,+a.x,+%22+nb+%3D+%22,+a.nb)%0D%0Aprint(%22b+%3A+x+%3D+%22,+b.x,+%22+nb+%3D+%22,+b.nb)%0D%0Aprint(%22c+%3A+x+%3D+%22,+c.x,+%22+nb+%3D+%22,+c.nb)&mode=display&origin=opt-frontend.js&cumulative=false&heapPrimitives=false&drawParentPointers=false&textReferences=false&showOnlyOutputs=false&py=3&rawInputLstJSON=%5B%5D&curInstr=0" target=_blank>Exécuter</a></p>

Méthodes de classe
------------------

**Exemple :**

::

    class A:
        nb = 0
        
        def __init__(self):
            print("creation objet de type A")
            A.nb = A.nb + 1
            print("il y en a maintenant ", A.nb)

        @classmethod
        def get_nb(cls):
            return A.nb

    print("Partie 1 : nb objets = ", A.get_nb()) 
    a = A()
    print("Partie 2 : nb objets = ", A.get_nb()) 
    b = A()
    print("Partie 3 : nb objets = ", A.get_nb())

.. raw:: html

    <p><a class="btn btn-primary" href="http://pythontutor.com/visualize.html#code=class+A%3A%0A++++nb+%3D+0%0A%0A++++def+__init__(self)%3A%0A++++++++print(%22creation+objet+de+type+A%22)%0A++++++++A.nb+%3D+A.nb+%2B+1%0A++++++++print(%22il+y+en+a+maintenant+%22,+A.nb)%0A%0A++++%40classmethod%0A++++def+get_nb(cls)%3A%0A++++++++return+A.nb%0A%0Aprint(%22Partie+1+%3A+nb+objets+%3D+%22,+A.get_nb())%0Aa+%3D+A()%0Aprint(%22Partie+2+%3A+nb+objets+%3D+%22,+A.get_nb())%0Ab+%3D+A()%0Aprint(%22Partie+3+%3A+nb+objets+%3D+%22,+A.get_nb())&mode=display&origin=opt-frontend.js&cumulative=false&heapPrimitives=false&drawParentPointers=false&textReferences=false&showOnlyOutputs=false&py=3&rawInputLstJSON=%5B%5D&curInstr=0" target=_blank>Exécuter</a></p>

Pour créer une méthode de classe, il faut la faire précéder d'un "décorateur" : @classmethod

Le premier argument doit être de la méthode de classe doit être "cls".

Typologie des méthodes
======================

Parmi les différentes méthodes que comporte une classe, on a souvent tendance à distinguer :

* les **constructeurs** ;
* les **accesseurs** (en anglais *accessor*) qui fournissent des informations relatives à l'état d'un objet, c'est-à-dire aux valeurs de certains de ses attributs (généralement privés) sans les modifier ;
* les **mutateurs** (en anglais *mutator*) qui modifient l'état d'un objet, donc les valeurs de certains de ses attributs.

On rencontre souvent l'utilisation de noms de la forme :meth:`get_XXXX` pour les accesseurs et :meth:`set_XXXX` pour les mutateurs, y compris dans des programmes dans lesquels les noms de variable sont francisés. Par exemple, pour la classe :class:`Point` sur laquelle nous avons déjà travaillé on peut définir les méthodes suivantes :

**Exemple :**

::

    class Point:
        def __init__(self, x, y):
            self.__x = x
            self.__y = y
            
        def get_x(self):
            return self.__x

        def get_y(self):
            return self.__y

        def set_x(self, x):
            self.__x = x

        def set_y(self, y):
            self.__y = y    
            
    a = Point(3, 7)
    print("a : abscisse =", a.get_x())
    print("a : ordonnee =", a.get_y())
    a.set_x(6)
    a.set_y(10)
    print("a : abscisse =", a.get_x())
    print("a : ordonnee =", a.get_y())

.. raw:: html

    <p><a class="btn btn-primary" href="http://pythontutor.com/visualize.html#code=class+Point%3A%0A++++def+__init__(self,+x,+y)%3A%0A++++++++self.__x+%3D+x%0A++++++++self.__y+%3D+y%0A%0A++++def+get_x(self)%3A%0A++++++++return+self.__x%0A%0A++++def+get_y(self)%3A%0A++++++++return+self.__y%0A%0A++++def+set_x(self,+x)%3A%0A++++++++self.__x+%3D+x%0A%0A++++def+set_y(self,+y)%3A%0A++++++++self.__y+%3D+y%0A%0Aa+%3D+Point(3,+7)%0Aprint(%22a+%3A+abscisse+%3D%22,+a.get_x())%0Aprint(%22a+%3A+ordonnee+%3D%22,+a.get_y())%0Aa.set_x(6)%0Aa.set_y(10)%0Aprint(%22a+%3A+abscisse+%3D%22,+a.get_x())%0Aprint(%22a+%3A+ordonnee+%3D%22,+a.get_y())&mode=display&origin=opt-frontend.js&cumulative=false&heapPrimitives=false&drawParentPointers=false&textReferences=false&showOnlyOutputs=false&py=3&rawInputLstJSON=%5B%5D&curInstr=0" target=_blank>Exécuter</a></p>

Notez qu'il n'est pas toujours prudent de prévoir une méthode d'accès pour chacun des attributs privés d'un objet. En effet, il ne faut pas oublier qu'il doit toujours être possible de modifier l'implémentation d'une classe de manière transparente pour son utilisateur.

.. seealso::
    http://python.developpez.com/cours/apprendre-python3/?page=page_13#L13
