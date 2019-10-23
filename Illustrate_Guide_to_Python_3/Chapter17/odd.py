def is_odd(num):
    '''
    defini si le nombre est pair
    '''
    num=int(num)
    result = num%2
    if result != 0 : 
        return True
    else : 
        return False

is_odd(3)