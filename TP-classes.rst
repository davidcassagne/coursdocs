********************
TP Classes et objets
********************

Exercice 1
==========

Créer une classe Livre qui dispose de trois attributs **privés** :

* titre et auteur
* nb_pages : qui contient le nombre de pages

On définira :

* un constructeur
* une méthode **affiche()** qui affiche l'ensemble des informations sur un livre (auteur, titre, nombre de pages)

Dans le programme principal :

#. Créer 2 livres,
#. Faire afficher les informations sur ces 2 livres.

Modifiez la classe Livre :

* Ajouter un accesseur pour la variable titre et la variable nb_pages.
* Ajouter un mutateur pour les variables auteur et titre.
* Créer un mutateur pour nb_pages : il ne devra changer le nombre de pages que si on lui passe en paramètre un nombre positif, et ne rien faire sinon, en affichant un message d'erreur. On remarquera l'intérêt des variables privées : on peut contrôler leur modification dans les éventuelles méthodes qui permettent de les modifier.
* Dans le programme principal,
      * modifier le nombre de pages de chacun des 2 livres,
      * faire afficher ces nombres de pages,
      * calculer le nombre de pages total de ces 2 livres et affichez-le.

Exercice 2 : Création et utilisation d'une classe simple
========================================================
                                                                                                                                              
Réaliser une classe PointAxe permettant de représenter un point sur un axe. Chaque point sera caractérisé par un nom et une abscisse. On prévoira :

    * un constructeur recevant en arguments le nom et l'abscisse d'un point,
    * une méthode affiche qui affiche le nom du point et son abscisse,
    * une méthode translate effectuant une translation définie par la valeur de son argument.

Dans une fichier nommé test_point_axe.py, écrire un petit programme utilisant cette classe pour créer un point, en afficher les caractéristiques, le déplacer et en afficher à nouveau les caractéristiques.

Exercice 3 : Attributs et méthodes de classe
============================================
Dans un fichier nommé axe_et_origine.py, créer une classe permettant de manipuler un point d'un axe, repéré par une abscisse. On devra pouvoir effectuer des changements d'origine, en conservant en permanence l'abscisse d'une origine courante (initialement 0). On prévoira simplement les méthodes suivantes :

* constructeur, recevant en argument l'abscisse "absolue" du point (c'est-à-dire repérée par rapport au point d'origine 0 et non par rapport à l'origine courante),
* ``affiche()`` qui imprime à la fois l'abscisse absolue de l'origine courante et l'abscisse du point par rapport à cette origine,
* ``set_origine(valeur)`` qui permet de définir une nouvelle abscisse pour l'origine (exprimée de façon absolue et non par rapport à l'origine courante),
* ``get_origine()`` qui permet d'obtenir l'abscisse de l'origine courante.

Ecrire un petit programme de test qui utilise set_origine en tant que méthode de classe et qui fournit les résultats suivants::

    Point A - abscisse = 3
            relative à une origine d'abscisse absolue 0
    Point B - abscisse = 12
            relative à une origine d'abscisse absolue 0
    On place l'origine en 3
    Point A - abscisse = 0
            relative à une origine d'abscisse absolue 3
    Point B - abscisse = 9
            relative à une origine d'abscisse absolue 3
