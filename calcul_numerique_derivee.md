# Calcul Numérique des Dérivées avec Python

## Introduction

La dérivée d'une fonction à une variable révèle le taux de variation de cette fonction. Bien que nous ayons des formules analytiques pour calculer la dérivée de nombreuses fonctions, dans le monde numérique, nous utilisons souvent des approximations discrètes.

## 1. Méthode des Différences Finies

Une approche courante pour approximer des dérivées est d'utiliser la méthode des différences finies.

### 1.1 Dérivée à l'aide de la différence finie avant (Forward Difference)

$f'(x) \approx \frac{f(x + h) - f(x)}{h}$

### 1.2 Dérivée à l'aide de la différence finie arrière (Backward Difference)

$f'(x) \approx \frac{f(x) - f(x - h)}{h}$

### 1.3 Dérivée à l'aide de la différence finie centrale (Central Difference)

$f'(x) \approx \frac{f(x + h) - f(x - h)}{2h}$

où $h$ est un petit intervalle. 

## 2. Implémentation en Python

### 2.1 Exemple de code pour la différence finie avant:

```python
def forward_difference(f, x, h=1e-5):
    return (f(x + h) - f(x)) / h
```

### 2.2 Exemple de code pour la différence finie arrière:

```python
def backward_difference(f, x, h=1e-5):
    return (f(x) - f(x - h)) / h
```

### 2.3 Exemple de code pour la différence finie centrale:

```python
def central_difference(f, x, h=1e-5):
    return (f(x + h) - f(x - h)) / (2 * h)
```

## 3. Exemples:

Supposons que vous vouliez estimer la dérivée de $f(x) = x^2$ au point $x = 1$.

```python
def f(x):
    return x**2

x = 1

print(forward_difference(f, x))
print(backward_difference(f, x))
print(central_difference(f, x))
```

Lorsque vous exécutez le code ci-dessus, vous verrez que les trois méthodes fournissent des approximations de la dérivée vraie (qui est 2 pour $f(x) = x^2$ au point $x = 1$).

## 4. Erreurs et Précision

Il est important de noter que le choix de $h$ peut influencer la précision de votre approximation. Une valeur de $h$ trop grande peut entraîner une sous-estimation de la dérivée, tandis qu'une valeur trop petite peut entraîner des erreurs numériques dues à la précision limitée des ordinateurs.

## Conclusion

Les méthodes de différences finies offrent une approche simple pour estimer numériquement les dérivées. En pratique, il est essentiel d'expérimenter avec différentes valeurs de $h$ pour obtenir un bon équilibre entre précision et stabilité.

## Version complète du programme

```python
def forward_difference(f, x, h=1e-5):
    """Calcule la dérivée à l'aide de la différence finie avant."""
    return (f(x + h) - f(x)) / h

def backward_difference(f, x, h=1e-5):
    """Calcule la dérivée à l'aide de la différence finie arrière."""
    return (f(x) - f(x - h)) / h

def central_difference(f, x, h=1e-5):
    """Calcule la dérivée à l'aide de la différence finie centrale."""
    return (f(x + h) - f(x - h)) / (2 * h)

# Test des fonctions
def f(x):
    return x**2

x = 1

print("Dérivée avec différence finie avant:", forward_difference(f, x))
print("Dérivée avec différence finie arrière:", backward_difference(f, x))
print("Dérivée avec différence finie centrale:", central_difference(f, x))
```
