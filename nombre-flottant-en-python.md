# Représentation des nombres flottants en mémoire pour Python

## 1. Qu’est-ce qu'un nombre flottant ?

En informatique, les nombres de type `float` représentent les nombres à virgule flottante, c'est-à-dire des nombres qui peuvent avoir une partie décimale (par exemple, 3.14, -0.001). Contrairement aux entiers (de type `int`), qui ne stockent que des valeurs entières, les nombres flottants permettent de représenter une plus grande gamme de valeurs, incluant des fractions et des valeurs très petites ou très grandes.

## 2. La norme IEEE 754

Les valeurs flottantes en Python sont stockées en suivant la norme IEEE 754, qui définit une méthode de représentation en mémoire pour les nombres en virgule flottante. Python utilise des "doubles" de précision pour les nombres flottants, ce qui signifie que chaque nombre de type `float` est représenté par **64 bits** en mémoire (c'est-à-dire 8 octets).

### Répartition des bits en IEEE 754

La norme IEEE 754 divise ces 64 bits en trois parties :

1. **Signe (1 bit)** : Ce bit indique si le nombre est positif ou négatif. Il vaut 0 pour les nombres positifs et 1 pour les nombres négatifs.
   
2. **Exposant (11 bits)** : Il permet de "déplacer" la virgule pour représenter des valeurs très grandes ou très petites. L'exposant est stocké sous forme de "bias", ce qui signifie qu'on lui ajoute une valeur constante (dans le cas des doubles, cette constante est 1023). Par exemple, un exposant binaire de 00000000000 représente -1023.

3. **Mantisse (52 bits)** : C’est la partie fractionnaire du nombre. La mantisse, également appelée "partie significative", contient les chiffres qui constituent le nombre, et elle est normalisée. Cela signifie que le premier bit de la mantisse est implicite et considéré comme 1 pour les nombres normaux.

### Exemple de structure

Imaginons que nous ayons un nombre flottant de type double, comme 5.75. En mémoire, il serait stocké de la manière suivante :

- **Signe** : 0 (positif)
- **Exposant** : 10000000001 (correspond à l'exposant de 1024 - 1023 = 1)
- **Mantisse** : 1011100000000000000000000000000000000000000000000000 (représentation en binaire de la partie décimale)

## 3. Précision et limites des nombres flottants

Les nombres flottants peuvent représenter une très grande plage de valeurs, mais avec une précision limitée. Cette limitation provient du nombre de bits disponibles pour la mantisse. Dans le cas des doubles en IEEE 754, les 52 bits de la mantisse permettent de stocker environ 15 à 17 chiffres significatifs.

Toutefois, la limite de cette précision peut parfois engendrer des erreurs de calcul dues à des "artéfacts de précision". Par exemple, certaines opérations comme `0.1 + 0.2` ne donnent pas exactement `0.3` en raison des limitations de la représentation binaire en mémoire.

# Exemples de conversion en représentation binaire

Voici un programme Python qui convertit une valeur `float` en sa représentation binaire, en respectant la norme IEEE 754 pour les nombres flottants en double précision (64 bits). Ce programme décompose le nombre flottant en ses trois composantes : le signe, l'exposant et la mantisse.

```python
import struct
import numpy as np

def float_to_binary(num):
    # On utilise la bibliothèque struct pour obtenir l'équivalent binaire d'un float en IEEE 754
    # ">d" signifie un double (64 bits) avec un big-endian (ordre des octets)
    packed_num = struct.pack('>d', num)
    # Convertir les octets en un nombre binaire de 64 bits
    binary_num = ''.join(f'{byte:08b}' for byte in packed_num)

    # Récupérer les composants
    sign = binary_num[0]  # Premier bit pour le signe
    exponent = binary_num[1:12]  # 11 bits suivants pour l'exposant
    mantissa = binary_num[12:]  # 52 bits restants pour la mantisse

    # Affichage des résultats
    print(f"Nombre flottant: {num}")
    print(f"Signe: {sign}")
    print(f"Exposant: {exponent} (en binaire)")
    print(f"Mantisse: {mantissa} (en binaire)")
    
    return sign, exponent, mantissa

# Exemple d'utilisation
float_number = 5.75
float_to_binary(float_number)

one = 1.0
float_to_binary(one)

epsilon = np.finfo(float).eps
print(f"epsilon vaut {epsilon}")
float_to_binary(one+epsilon)
```

Ce programme affiche :

```
Nombre flottant: 5.75
Signe: 0
Exposant: 10000000001 (en binaire)
Mantisse: 0111000000000000000000000000000000000000000000000000 (en binaire)
Nombre flottant: 1.0
Signe: 0
Exposant: 01111111111 (en binaire)
Mantisse: 0000000000000000000000000000000000000000000000000000 (en binaire)
epsilon vaut 2.220446049250313e-16
Nombre flottant: 1.0000000000000002
Signe: 0
Exposant: 01111111111 (en binaire)
Mantisse: 0000000000000000000000000000000000000000000000000001 (en binaire)
```

## Explications du code

1. **struct.pack('>d', num)** : On utilise le format `'>d'` pour convertir le nombre flottant `num` en une séquence de 8 octets (64 bits), correspondant à sa représentation IEEE 754.
2. **binary_num** : On convertit chaque octet en une chaîne binaire de 8 bits et on les joint pour obtenir une représentation binaire de 64 bits.
3. **Signe, exposant et mantisse** : Une fois la chaîne de 64 bits obtenue, on sépare les bits :
   - **Signe** : Le premier bit
   - **Exposant** : Les 11 bits suivants
   - **Mantisse** : Les 52 bits restants

Lorsque vous exécutez ce code avec une valeur comme `5.75`, le programme affichera les valeurs en binaire pour le signe, l'exposant et la mantisse, permettant de visualiser la structure du nombre en mémoire.

Pour comprendre comment la valeur flottante `1.0` est représentée en mémoire selon la norme IEEE 754, nous devons examiner la manière dont Python et d'autres langages stockent les nombres flottants en utilisant cette norme.

Rappelons que dans la norme IEEE 754 pour les flottants en double précision (64 bits), les 64 bits sont répartis comme suit :

1. **Signe** : 1 bit
2. **Exposant** : 11 bits
3. **Mantisse** : 52 bits

## Explication de la représentation de la valeur `1.0`.

### Étape 1 : Calcul du signe

Puisque `1.0` est un nombre positif, le bit de signe sera `0`.

### Étape 2 : Calcul de l'exposant

L’exposant, qui utilise 11 bits, est stocké en "exposant biaisé". En double précision, l'exposant est biaisé avec une valeur de **1023**. 

Le calcul de l’exposant pour la valeur `1.0` est donc le suivant :

1. On écrit `1.0` en notation scientifique binaire : $1.0 = 1 \times 2^0$.
2. L'exposant est donc $0$.
3. Pour obtenir l'exposant biaisé, on ajoute 1023 :  
   $$0 + 1023 = 1023$$

En binaire, 1023 est représenté par `01111111111` sur 11 bits.

### Étape 3 : Calcul de la mantisse

La mantisse (ou fraction significative) est la partie binaire qui suit la virgule. Dans la norme IEEE 754, la mantisse est toujours normalisée, ce qui signifie qu’elle est stockée sous la forme $1.0xxx\ldots$ avec le bit implicite `1` qui n'est pas enregistré. 

Pour `1.0`, on n'a pas de décimale autre que le `1` de départ, donc tous les bits de la mantisse seront `0`.

### Résumé de la représentation binaire de 1.0

En rassemblant les trois composants, la représentation IEEE 754 pour `1.0` est donc :

- **Signe** : `0`
- **Exposant** : `01111111111` (soit 1023 en décimal)
- **Mantisse** : `0000000000000000000000000000000000000000000000000000`

Ainsi, la valeur `1.0` est représentée en binaire par cette séquence de 64 bits :
```
0 01111111111 0000000000000000000000000000000000000000000000000000
```

Ce format permet de stocker `1.0` en respectant la norme IEEE 754 pour les flottants en double précision.

`np.finfo(float).eps` correspond à la différence entre 1.0 et le plus proche flottant représentable plus grand que 1.0. Par exemple, pour des flottants de 64 bits dans le standard IEEE-754, eps = 2**-52, approximativement 2.22e-16.

