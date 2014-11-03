**********
L'héritage
**********

La notion d'héritage
====================

Nous disposons de la classe de base suivante :

.. literalinclude:: heritage/heritage1.py

Nous allons voir que "Un objet d'une classe dérivée peut accéder aux membres de sa classe de base".

.. literalinclude:: heritage/heritage2.py

La notion de redéfinition (ou surcharge)
========================================

La redéfinition désigne la définition dans une classe dérivée d'une méthode de même nom qu'une méthode qui existait déjà dans la classe de base.

Pour pouvoir faire un appel d'un méthode de la classe de base et ne pas risquer de faire un appel récursif de la méthode de la classe dérivée, on utilise le nom de la classe de base suivi d'un point, il faut également remettre self dans les arguments de la méthode de la classe de base à appeler.

.. literalinclude:: heritage/heritage3.py

Exemple avec constructeurs
==========================

.. literalinclude:: heritage/heritage4.py

Le polymorphisme
================

.. literalinclude:: heritage/heritage5.py

.. seealso::

    http://python.developpez.com/cours/TutoSwinnen/?page=Chapitre12#L12 

Exercices - L'héritage et le polymorphisme
==========================================

Exercice 1 : Définition d'une classe dérivée, droits d'accès (1)
----------------------------------------------------------------

On dispose de la classe suivante :

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
        
        def getX(self):
            return self.__x
        
        def getY(self):
            return self.__y

Dans un fichier nommé TestPointA.py, réaliser une classe PointA, dérivée de Point disposant d'une méthode affiche affichant les coordonnées d'un point. Ecrire un petit programme utilisant les deux classes Point et PointA.

Que se passerait-il si la classe Point ne disposait pas des méthodes getX et getY.

Exercice 2 : Définition d'une classe dérivée, droit d'accès (2)
---------------------------------------------------------------

On dispose de la classe suivante :

::

    class Point:
        __x = 0
        __y = 0
        
        def setPoint(self, x, y):
            self.__x = x
            self.__y = y
         
        def deplace(self, dx, dy):
            self.__x = self.__x + dx
            self.__y = self.__y + dy
        
        def affCoord(self):
            print "Coordonnees : ", self.__x, self.__y

Dans un fichier nommé TestPointNom.py, réaliser une classe PointNom, dérivée de Point permettant de manipuler des points définis par deux coordonnées et un nom. On y prévoira les méthodes suivantes :

    * setPointNom pour définir les coordonnées et le nom d'un objet de type PointNom,
    * setNom pour définir seulement le nom d'un tel objet,
    * affCoordNom pour afficher les coordonnées et le nom d'un objet de type PointNom.

Ecrire un petit programme utilisant la classe PointNom. Créer notamment un objet de type PointNom et appliquer lui toutes les méthodes possibles.

Exercice 3 : Héritage et appel de constructeurs
-----------------------------------------------

On dispose de la classe suivante (disposant cette fois d'un constructeur) :

::

    class Point:
        def __init__(self, x, y):
            self.__x = x
            self.__y = y
            
        def affCoord(self):
            print "Coordonnees : ", self.__x, self.__y

Réaliser une classe PointNom, dérivée de Point permettant de manipuler des points définis par deux coordonnées et un nom. On y prévoira les méthodes suivantes :

    * constructeur pour définir les coordonnées et le nom d'un objet de type PointNom,
    * affCoordNom pour afficher les coordonnées et le nom d'un objet de type PointNom.

Ecrire un petit programme utilisant la classe PointNom.

Exercice 4 : Redéfinition et polymorphisme
------------------------------------------

On dispose de la classe suivante :

::

    class Point:
        def __init__(self, x, y):
            self.__x = x
            self.__y = y
            
        def affiche(self):
            print "Coordonnees : ", self.__x, self.__y

Réaliser une classe PointNom, dérivée de Point permettant de manipuler des points définis par deux coordonnées et un nom. On y prévoira les méthodes suivantes :

    * constructeur pour définir les coordonnées et le nom d'un objet de type PointNom,
    * affiche pour afficher les coordonnées et le nom d'un objet de type PointNom.

Ecrire un petit programme utilisant la classe PointNom.
 
