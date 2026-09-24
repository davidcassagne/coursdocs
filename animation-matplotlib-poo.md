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

**Exemple : animation du titre**

Le style « Orienté Objet » donne accès à l'objet `ax` à l'intérieur de la fonction `animate()`. On peut ainsi mettre à jour le titre à chaque image, par exemple pour afficher le numéro de l'image.

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

def animate(i):
    t = i * dt
    y = np.cos(k*x - w*t)
    line.set_data(x, y)
    ax.set_title(f"image {i}")
    return line,

# ici blit=False est necessaire pour que le titre soit bien mis a jour
ani = animation.FuncAnimation(fig, animate, frames=100,
                              interval=1, blit=False, repeat=False)
plt.show()
```

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
