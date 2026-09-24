# Animation avec Matplotlib (incluant style Orienté Objet)

## Contenu

- [Animation avec effacement](#animation-avec-effacement)
  - [Animation avec le module animation de Matplotlib](#animation-avec-le-module-animation-de-matplotlib)
  - [Animation sans le module animation](#animation-sans-le-module-animation)
- [Animation sans effacement](#animation-sans-effacement)

Vous découvrirez ici comment créer une animation avec **Python** et **Matplotlib**.

Comme dans la page [Tracé de courbes](https://courspython.com/introduction-courbes.html), chaque exemple est présenté selon deux styles de programmation :

- le style « pyplot », qui utilise directement des fonctions du module `pyplot` ;
- le style « Orienté Objet (OO) », recommandé dans la documentation de **Matplotlib**, qui agit sur les objets `Figure` et `Axes` créés par `plt.subplots()`.

## Animation avec effacement

### Animation avec le module animation de Matplotlib

Nous allons utiliser la fonction `FuncAnimation()` du module **animation**.

**Exemple**

Dans ce script, nous allons définir une fonction `animate()` qui met à jour la courbe pour chaque image.

> **Avertissement**
> Dans le style « Orienté Objet », il faut utiliser `set_xlim()` et `set_ylim()` à la place de `xlim()` et `ylim()`.

*Style « pyplot »*

```python
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

k = 2*np.pi
w = 2*np.pi
dt = 0.01

xmin = 0
xmax = 3
nbx = 151

x = np.linspace(xmin, xmax, nbx)

fig = plt.figure() # initialise la figure
line, = plt.plot([], [])
plt.xlim(xmin, xmax)
plt.ylim(-1, 1)

def animate(i):
    t = i * dt
    y = np.cos(k*x - w*t)
    line.set_data(x, y)
    return line,

ani = animation.FuncAnimation(fig, animate, frames=100,
                              interval=1, blit=True, repeat=False)
plt.show()
```

*Style « Orienté Objet »*

```python
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

k = 2*np.pi
w = 2*np.pi
dt = 0.01

xmin = 0
xmax = 3
nbx = 151

x = np.linspace(xmin, xmax, nbx)

fig, ax = plt.subplots() # initialise la figure et les axes
line, = ax.plot([], [])
ax.set_xlim(xmin, xmax)
ax.set_ylim(-1, 1)

def animate(i):
    t = i * dt
    y = np.cos(k*x - w*t)
    line.set_data(x, y)
    return line,

ani = animation.FuncAnimation(fig, animate, frames=100,
                              interval=1, blit=True, repeat=False)
plt.show()
```

La fonction `FuncAnimation()` dispose d'un argument avec une étiquette appelée `interval`, qui est le temps en millisecondes entre deux appels de la fonction de mise à jour, ici `animate()`.

> **Note**
> La fonction `animate()` est identique dans les deux styles : elle agit directement sur l'objet `line` renvoyé par `plot()`, grâce à sa méthode `set_data()`.

**À propos des virgules**

Deux virgules apparaissent dans ces scripts à des endroits inhabituels. Dans les deux cas, il s'agit de la virgule qui sert en Python à construire ou à décomposer un tuple, et non d'une faute de frappe.

- `line, = ax.plot([], [])` : la fonction `plot()` renvoie une liste d'objets, car elle peut tracer plusieurs courbes à la fois. La virgule à gauche du signe `=` demande d'extraire l'unique élément de cette liste, de façon à ce que `line` désigne la courbe elle-même et non une liste contenant la courbe. On aurait pu écrire de façon équivalente `line = ax.plot([], [])[0]`.

- `return line,` : la virgule crée un tuple d'un seul élément, `(line,)`. C'est en effet une séquence d'objets graphiques que `FuncAnimation()` attend en retour de la fonction de mise à jour, afin de savoir ce qui doit être redessiné à chaque image. Sans cette virgule, on renverrait la courbe seule et non une séquence. Lorsque plusieurs objets sont mis à jour, ils sont simplement séparés par des virgules, par exemple `return line, point`.

**Exemple : affichage du numéro de l'image**

Le style « Orienté Objet » donne accès à l'objet `ax` à l'intérieur de la fonction `animate()`. On peut ainsi mettre à jour un texte à chaque image, ici pour afficher le numéro de l'image.

Le texte est créé avant l'animation avec `ax.text()`, puis modifié à chaque image avec sa méthode `set_text()`. Comme la courbe, il doit être renvoyé par `animate()` pour être réaffiché.

```python
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

k = 2*np.pi
w = 2*np.pi
dt = 0.01

xmin = 0
xmax = 3
nbx = 151

x = np.linspace(xmin, xmax, nbx)

fig, ax = plt.subplots()
line, = ax.plot([], [])
ax.set_xlim(xmin, xmax)
ax.set_ylim(-1, 1)

texte = ax.text(0.05, 0.9, "", transform=ax.transAxes)

def animate(i):
    t = i * dt
    y = np.cos(k*x - w*t)
    line.set_data(x, y)
    texte.set_text(f"image {i}")
    return line, texte

ani = animation.FuncAnimation(fig, animate, frames=100,
                              interval=1, blit=True, repeat=False)
plt.show()
```

> **Note**
> Les coordonnées données à `ax.text()` sont exprimées ici en coordonnées relatives aux axes grâce à `transform=ax.transAxes` : `(0, 0)` correspond au coin inférieur gauche et `(1, 1)` au coin supérieur droit.

**Ancien exemple**

Nous présentons ici une approche qui se retrouve dans de nombreux anciens exemples disponibles sur internet.

Nous y définissons une fonction `init()` qui est affectée au paramètre `init_func` de `FuncAnimation()`. Ceci entraine un appel de cette fonction avant la première image. Cette approche n'est toutefois pas indispensable pour les usages qui sont réalisés le plus souvent.

*Style « pyplot »*

```python
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

k = 2*np.pi
w = 2*np.pi
dt = 0.01

xmin = 0
xmax = 3
nbx = 151

x = np.linspace(xmin, xmax, nbx)

fig = plt.figure() # initialise la figure
line, = plt.plot([], [])
plt.xlim(xmin, xmax)
plt.ylim(-1, 1)

def init():
    line.set_data([], [])
    return line,

def animate(i):
    t = i * dt
    y = np.cos(k*x - w*t)
    line.set_data(x, y)
    return line,

ani = animation.FuncAnimation(fig, animate, init_func=init, frames=100,
                              interval=1, blit=True, repeat=False)

plt.show()
```

*Style « Orienté Objet »*

```python
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

k = 2*np.pi
w = 2*np.pi
dt = 0.01

xmin = 0
xmax = 3
nbx = 151

x = np.linspace(xmin, xmax, nbx)

fig, ax = plt.subplots() # initialise la figure et les axes
line, = ax.plot([], [])
ax.set_xlim(xmin, xmax)
ax.set_ylim(-1, 1)

def init():
    line.set_data([], [])
    return line,

def animate(i):
    t = i * dt
    y = np.cos(k*x - w*t)
    line.set_data(x, y)
    return line,

ani = animation.FuncAnimation(fig, animate, init_func=init, frames=100,
                              interval=1, blit=True, repeat=False)

plt.show()
```

### Animation sans le module animation

Nous présentons ici une technique d'animation plus basique qui n'utilise pas le module **animation**. Cette technique n'est pas recommandée mais elle peut servir pour des animations simples. Pour des animations plus élaborées, l'utilisation du module **animation** est préférable.

*Style « pyplot »*

```python
import numpy as np
import matplotlib.pyplot as plt

k = 2*np.pi
w = 2*np.pi
dt = 0.01

x = np.linspace(0, 3, 151)

for i in range(50):
    t = i * dt
    y = np.cos(k*x - w*t)
    if i == 0:
        line, = plt.plot(x, y)
    else:
        line.set_data(x, y)
    plt.pause(0.01) # pause avec duree en secondes

plt.show()
```

*Style « Orienté Objet »*

```python
import numpy as np
import matplotlib.pyplot as plt

k = 2*np.pi
w = 2*np.pi
dt = 0.01

x = np.linspace(0, 3, 151)

fig, ax = plt.subplots()

for i in range(50):
    t = i * dt
    y = np.cos(k*x - w*t)
    if i == 0:
        line, = ax.plot(x, y)
    else:
        line.set_data(x, y)
    plt.pause(0.01) # pause avec duree en secondes

plt.show()
```

> **Note**
> Quand il est seulement nécessaire de modifier les valeurs de y, il est possible d'utiliser `set_ydata(y)` au lieu de `set_data(x, y)`.

> **Note**
> La fonction `plt.pause()` n'a pas d'équivalent sous forme de méthode des objets `Figure` ou `Axes` : elle est donc conservée dans le style « Orienté Objet », tout comme `plt.show()`.

## Animation sans effacement

*Style « pyplot »*

```python
import numpy as np
import matplotlib.pyplot as plt

k = 2*np.pi
w = 2*np.pi
dt = 0.01

x = np.linspace(0, 3, 151)

for i in range(50):
    t = i * dt
    y = np.cos(k*x - w*t)
    plt.plot(x, y)
    plt.pause(0.01) # pause avec duree en secondes

plt.show()
```

*Style « Orienté Objet »*

```python
import numpy as np
import matplotlib.pyplot as plt

k = 2*np.pi
w = 2*np.pi
dt = 0.01

x = np.linspace(0, 3, 151)

fig, ax = plt.subplots()

for i in range(50):
    t = i * dt
    y = np.cos(k*x - w*t)
    ax.plot(x, y)
    plt.pause(0.01) # pause avec duree en secondes

plt.show()
```

---

*David Cassagne — Licence [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.fr).*
