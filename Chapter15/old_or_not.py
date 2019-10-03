potos = [("alex", "melkor", "31"), ("noemie", "joy", "26"), ("valentin", "oupss", None), ("julien", "néluge","33")]
age_total = 0
nb_potos = 0

for member in potos : 
    if member[2] is None :
        continue
    age = int(member[2])
    age_total += age
    nb_potos += 1
    
moy_age = age_total / nb_potos

for member in potos : 
    if member[2] is None : 
        print (member[0], "age unknown")
    elif int(member[2]) >= moy_age : 
        print (member[0], "is old")
    else : 
        print (member[0], "is young")