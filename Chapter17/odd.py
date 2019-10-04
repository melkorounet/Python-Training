def is_odd():
    num = input("Entrez un nombre :")
    num=int(num)
    result = num %2
    if result != 0 :
        print (num, 'is odd')
    else :
        print (num, 'is pair')

is_odd()