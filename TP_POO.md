### Exercice : Création d'une classe "Voiture"

1. Créez une classe appelée `Voiture`.
2. La classe doit avoir les attributs suivants :
   - `marque` (chaîne de caractères)
   - `modele` (chaîne de caractères)
   - `annee` (entier)
   - `kilometrage` (entier)
3. Ajoutez un constructeur (`__init__`) qui initialise ces attributs lors de la création d'une instance de la classe.
4. Ajoutez une méthode appelée `afficher_info` qui affiche toutes les informations sur la voiture.
5. Ajoutez une méthode appelée `ajouter_kilometres` qui prend un nombre entier en paramètre et ajoute cette valeur au kilométrage de la voiture.

### Exemple d'utilisation attendu :

```python
# Création d'une instance de Voiture
ma_voiture = Voiture("Toyota", "Corolla", 2020, 10000)

# Affichage des informations sur la voiture
ma_voiture.afficher_info()
# Sortie attendue :
# Marque : Toyota, Modèle : Corolla, Année : 2020, Kilométrage : 10000 km

# Ajout de kilométrage
ma_voiture.ajouter_kilometres(500)

# Affichage des informations mises à jour
ma_voiture.afficher_info()
# Sortie attendue :
# Marque : Toyota, Modèle : Corolla, Année : 2020, Kilométrage : 10500 km
```
