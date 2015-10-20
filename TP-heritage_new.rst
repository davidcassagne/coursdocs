TP - L'héritage et le polymorphisme
===================================

Exercice 1 : Définition d'une classe dérivée, droits d'accès
------------------------------------------------------------

On dispose de la classe suivante :

::

    class Point:
        def __init__(self, x, y):
            self.__x = x
            self.__y = y
         
        def deplace(self, dx, dy):
            self.__x = self.__x + dx
            self.__y = self.__y + dy
        
        def get_x(self):
            return self.__x
        
        def get_y(self):
            return self.__y

Réaliser une classe PointA, dérivée de Point disposant d'une méthode affiche() affichant les coordonnées d'un point. Ecrire un petit programme utilisant les deux classes Point et PointA.

Que se passerait-il si la classe Point ne disposait pas des méthodes get_x() et get_y() ?


Exercice 2 : Héritage et appel de constructeurs
-----------------------------------------------

On dispose de la classe suivante (disposant cette fois d'un constructeur) :

::

    class Point:
        def __init__(self, x, y):
            self.__x = x
            self.__y = y
            
        def aff_coord(self):
            print("Coordonnees : ", self.__x, self.__y)

Réaliser une classe PointNom, dérivée de Point permettant de manipuler des points définis par deux coordonnées et un nom. On y prévoira les méthodes suivantes :

    * constructeur pour définir les coordonnées et le nom d'un objet de type PointNom,
    * **aff_coord_nom** pour afficher les coordonnées et le nom d'un objet de type PointNom.

Ecrire un petit programme utilisant la classe PointNom.

Exercice 3 : Redéfinition et polymorphisme
------------------------------------------

On dispose de la classe suivante :

::

    class Point:
        def __init__(self, x, y):
            self.__x = x
            self.__y = y
            
        def affiche(self):
            print("Coordonnees : ", self.__x, self.__y)

Réaliser une classe PointNom, dérivée de Point permettant de manipuler des points définis par deux coordonnées et un nom. On y prévoira les méthodes suivantes :

    * constructeur pour définir les coordonnées et le nom d'un objet de type PointNom,
    * **affiche** pour afficher les coordonnées et le nom d'un objet de type PointNom.

Ecrire un petit programme utilisant les classes Point et PointNom. On créera une liste comprenant des objets de type Point et PointNom, puis une boucle qui utilisera la méthode affiche pour chacun des éléments de la liste.
 
