potos = ["alexandre", "julien", "noemie", "valentin", "clement", "nicolas","lucas"]
total_lenght = 0
nb_potos = 0

for name in potos : 
    total_lenght += len(name)
    nb_potos += 1

moy_lenght = total_lenght / nb_potos

print(moy_lenght)
