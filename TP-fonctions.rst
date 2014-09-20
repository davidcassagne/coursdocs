************
TP Fonctions
************

1. Définissez une fonction ligneCar(n, ca) qui renvoie une chaîne de ``n`` caractères ``ca``. ``ca`` fait référence à une chaîne de caractères qui contient un seul caractère.  

2. Définissez une fonction surfCercle(R). Cette fonction doit renvoyer la surface (l'aire) d'un cercle dont on lui a fourni le rayon R en argument. Par exemple, l'exécution de l'instruction :

   >>> a = surfCercle(2.5)
   >>> print("la surface vaut", a)

   doit afficher la surface du cercle.

3. Définissez une fonction volBoite(x1,x2,x3) qui renvoie le volume d'une boîte parallélipipédique dont on fournit les trois dimensions x1, x2, x3 en arguments. Par exemple, l'exécution de l'instruction :

>>> print(volBoite(5.2, 7.7, 3.3)) 

doit donner le résultat :

::

   132.13

4. Définissez une fonction indexMax(liste) qui renvoie l'indice de l'élément ayant la valeur la plus élevée dans la liste transmise en argument. Si le même élément apparaît plusieurs fois, l'indice renvoyé est celui de la dernière occurence.

   **Exemple d'utilisation :**

   ::

       serie = [5, 8, 2, 1, 9, 3, 6, 7]
       i = indexMax(serie) 
       print("Résultat :", i)

   ::

       Résultat : 4
