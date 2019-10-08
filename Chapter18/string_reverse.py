mot = input("Entrez un mot à inverser :")
condition=False

while condition is False: 
    if ' ' in mot :
        print ("merci de n'entrez qu'un seul mot")
        mot = input("Entrez un mot à inverser :")
    else : 
        condition=True
        print(mot[::-1])

