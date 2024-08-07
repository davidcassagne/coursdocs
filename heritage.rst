**********
L'héritage
**********

La notion d'héritage
====================

Nous disposons de la classe de base suivante :

::

    class Point:
        def __init__(self, x, y):
            self.x = x
            self.y = y
    
        def deplace(self, dx, dy):
            self.x = self.x + dx
            self.y = self.y + dy
    
        def affiche(self):
            print("Je suis un point de coordonnees", self.x, self.y)

Nous allons créer une classe ``PointCol`` qui sera dérivée de ``Point`` et qui disposera d'un attribut ``couleur`` et de deux méthodes ``colore()`` et ``affiche_couleur()`` supplémentaires. 

::

    class Point:
        def __init__(self, x, y):
            self.x = x
            self.y = y
    
        def deplace(self, dx, dy):
            self.x = self.x + dx
            self.y = self.y + dy
    
        def affiche(self):
            print("Je suis un point de coordonnees", self.x, self.y)
    
    class PointCol(Point):
        def colore(self, couleur):
            self.couleur = couleur 
            
        def affiche_couleur(self):
            print("ma couleur est :", self.couleur)
    
    pc = PointCol(3, 5)
    pc.affiche()
    pc.colore("rouge")
    pc.deplace(2, -1)
    pc.affiche()
    pc.affiche_couleur()
    
    p = Point(6, 9)
    p.affiche()
    
On constate qu'un objet de type ``PointCol`` dispose du constructeur de la classe ``Point``, ainsi que des attributs ``x`` et ``y`` et des méthodes ``deplace()`` et ``affiche()``.

On dit ainsi qu'**un objet d'une classe dérivée peut accéder aux membres (attributs et méthodes) de sa classe de base**.

La notion de redéfinition (ou surcharge)
========================================

La redéfinition désigne la définition dans une classe dérivée d'une méthode de même nom qu'une méthode qui existait déjà dans la classe de base.

Pour pouvoir faire un appel d'un méthode de la classe de base, on utilise `super()` qui est une fonction intégrée (builtin function) de Python. Elle est utilisée pour appeler une méthode de la classe parente d'une classe dérivée. Cette fonction permet d'accéder à des méthodes des classes parentes sans avoir besoin de nommer explicitement la classe parente.

::

    class Point:
        def __init__(self, x, y):
            self.x = x
            self.y = y
    
        def deplace(self, dx, dy):
            self.x = self.x + dx
            self.y = self.y + dy
    
        def affiche(self):
            print("Je suis un point de coordonnees", self.x, self.y)
    
    class PointCol(Point):
        def __init__(self, x, y, couleur): 
            super().__init__(x, y) # on appelle le constructeur de la classe de base
            self.couleur = couleur
            
        def colore(self, couleur):
            self.couleur = couleur

        def affiche(self):
            super().affiche()
            print("  et ma couleur est :", self.couleur)
    
    pc = PointCol(3, 5, "vert")
    pc.affiche()
    pc.deplace(1, -3)
    pc.affiche()

.. warning:: 

Pour pouvoir faire un appel d'un méthode de la classe de base, il est aussi possible d'utiliser le nom de la classe de base suivi d'un point. Dans ce cas, il faut également remettre ``self`` dans les arguments de la méthode de la classe de base à appeler.

::

    class Point:
        def __init__(self, x, y):
            self.x = x
            self.y = y
    
        def deplace(self, dx, dy):
            self.x = self.x + dx
            self.y = self.y + dy
    
        def affiche(self):
            print("Je suis un point de coordonnees", self.x, self.y)
    
    class PointCol(Point):
        def __init__(self, x, y, couleur): 
            Point.__init__(self, x, y) # on appelle le constructeur de la classe de base
            self.couleur = couleur
            
        def colore(self, couleur):
            self.couleur = couleur

        def affiche(self):
            Point.affiche(self)
            print("  et ma couleur est :", self.couleur)
    
    pc = PointCol(3, 5, "vert")
    pc.affiche()
    pc.deplace(1, -3)
    pc.affiche()

Le polymorphisme
================

::

    class Point:
        def __init__(self, x, y):
            self.x = x
            self.y = y
    
        def deplace(self, dx, dy):
            self.x = self.x + dx
            self.y = self.y + dy
    
        def affiche(self):
            print("Je suis un point de coordonnees", self.x, self.y)
    
    class PointCol(Point):
        def __init__(self, x, y, couleur):
            Point.__init__(self, x, y)
            self.couleur = couleur
    
        def colore(self, couleur):
            self.couleur = couleur

        def affiche(self):
            Point.affiche(self)
            print("  et ma couleur est :", self.couleur)
    
    t = [PointCol(3, 5, "vert"), Point(2, 6), Point(4, 3), PointCol(1, 7, "bleu")]
    
    for i in range(len(t)):
        print("i =", i)
        t[i].affiche()
        t[i].deplace(1, -3)
        t[i].affiche()

.. seealso::

    http://python.developpez.com/cours/TutoSwinnen/?page=Chapitre12#L12 
 
