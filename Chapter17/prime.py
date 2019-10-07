def is_prime(n) :
    i = 2
    result = False
    while i < n :
        result = n % i
        print(result)
        i =+ 1
        if result == 0 :
            break 
        else :
            return True

print(is_prime(9))

print(is_prime(17))