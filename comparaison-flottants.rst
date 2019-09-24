*****************************************************
Comment vérifier une "égalité" entre deux flottants ?
*****************************************************

Les nombres flottants sont stockés avec un nombre fini de décimales.

On peut donc se retrouver avec des valeurs qui ne sont pas strictement égales alors qu'on calcule des expressions qui devraient donner le même résultat.

Par exemple :

>>> a = 2/3
>>> b = 1-1/3
>>> a == b
False

Mathématiquement, les expressions affectées à ``a`` et ``b`` devraient donner le même résultat. 

Pourtant quand on affiche ``a`` et ``b``,  on constate que les valeurs numériques ne sont pas strictement égales.

>>> a
0.6666666666666666
>>> b
0.6666666666666667

Comment définir une expression booléenne afin de vérifier que ``a`` et ``b`` sont suffisamment proches ?
--------------------------------------------------------------------------------------------------------

La démarche va être de vérifier que la différence entre ``a`` et ``b`` est suffisamment petite. 

On définit une certaine tolérance (par exemple ici 1e-8) et si la différence entre ``a`` et ``b`` est inférieure ou égale, nous considérerons que la proximité est vérifiée. 

>>> abs(a-b) <= 1e-8
True

**Toutefois que se passe-t-il si on prend des nombres plus grands ?**

On étudie le cas suivant :

>>> a = 2/3 * 1e20
>>> b = (1-1/3 )* 1e20
>>> abs(a-b) <= 1e-8
False

On constate donc que le critère défini précédemment ne marche plus. 

Au lieu de considérer une différence absolue entre ``a`` et ``b``, nous allons donc plutôt calculer un écart relatif ``(a-b)/b`` et vérifier que cet écart est suffisamment petit (par exemple ici inférieur ou égal à 1e-5)

>>> abs(a-b)/abs(b) <= 1e-5
True

Au final, nous pouvons écrire un critère qui sera :

>>> abs(a-b) <= (1e-8 + 1e-5 * abs(b))
True

Il se trouve que c'est ce critère qui est appliqué dans la fonction ``numpy.isclose(a, b)``.

Voir :  https://docs.scipy.org/doc/numpy/reference/generated/numpy.isclose.html

Dans le cas où on souhaite comparer toutes les valeurs entre deux tableaux, on utilisera la fonction ``numpy.allclose(a, b)``.

Voir :  https://docs.scipy.org/doc/numpy/reference/generated/numpy.allclose.html
