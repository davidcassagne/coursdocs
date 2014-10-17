from  pylab import *

nb_pas = 200
nb_position = nb_pas + 1


position = zeros(nb_position)
# directement position[0] vaut 0

somme = zeros(nb_position)
nb_marcheur = 500

for j in range(nb_marcheur):
    x = 0
    for i in range(1,nb_position):
        if random() < 0.5:
            x = x + 1
        else:
            x = x - 1
        position[i] = x
    somme = somme + position**2
    #print("position",position)
    #print("somme",somme)
    
        
t = arange(nb_position)

plot(t, somme / nb_marcheur)
show()
