occupation = None
info = {'first':'alex', 'last':'melkor'}
print(info)
#ajout d'une clé
info['age']='31'
info[occupation]='osfc'
print(info)
print(info['age'])

print('age' in info)

#récupérer une value à partir d'une clé
metier = info.get(occupation)
print(metier)
#suppression d'une clé
del info['age']
print(info)

#on compte le nombre d'itérations dans une liste
names = ['Ringo', 'Paul', 'John','Ringo']
count = {}
for name in names:
    count.setdefault(name, 0)
    count[name] += 1
print(count)

#boucle for sur key or value
data = {'Adam': 2, 'Zeek': 5, 'Fred': 3}
#key
for name in data : 
    print(name)
#value
for number in data.values():
    print(number)
#both
for name, number in data.items():
    print(name, number)

data_list = list(data.items())
print (data_list)