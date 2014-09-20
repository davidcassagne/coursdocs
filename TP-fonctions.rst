************
TP Fonctions
************

1. Définissez une fonction ``ligne_car(n, ca)`` qui renvoie une chaîne de ``n`` caractères ``ca``. ``ca`` fait référence à une chaîne de caractères qui contient un seul caractère.  

2. Définissez une fonction ``surf_cercle(R)``. Cette fonction doit renvoyer la surface (l'aire) d'un cercle dont on lui a fourni le rayon R en argument. Par exemple, l'exécution de l'instruction :

   >>> a = surf_cercle(2.5)
   >>> print("la surface vaut", a)

   doit afficher la surface du cercle.

3. Définissez une fonction ``vol_boite(x1, x2, x3)`` qui renvoie le volume d'une boîte parallélipipédique dont on fournit les trois dimensions x1, x2, x3 en arguments. Par exemple, l'exécution de l'instruction :

   >>> print(vol_boite(5.2, 7.7, 3.3)) 

   doit donner le résultat :

   ::

      132.13

4. Définissez une fonction ``index_max(liste)`` qui renvoie l'indice de l'élément ayant la valeur la plus élevée dans la liste transmise en argument. Si le même élément apparaît plusieurs fois, l'indice renvoyé est celui de la dernière occurence.

   **Exemple d'utilisation :**

   ::

       serie = [5, 8, 2, 1, 9, 3, 6, 7]
       i = index_max(serie) 
       print("Résultat :", i)

   ::

       Résultat : 4

Ces exercices sont en partie extraits du livre **Apprendre à programmer avec Python** de *Gérard Swinnen* disponible en licence `Creative Commons BY-NC-SA 2.0 FR <http://creativecommons.org/licenses/by-nc-sa/2.0/fr/>`_ 
Paternité - Pas d'utilisation commerciale - Partage des conditions initiales à l'identique.

Vous pourrez trouver d'autres exercices dans son édition en ligne à l'adresse suivante :

http://python.developpez.com/cours/apprendre-python3/?page=page_9
