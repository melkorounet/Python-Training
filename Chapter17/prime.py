def is_prime(n) :
    i = 2
    while i < n :
        result = n % i
        i =+ 1
        if result == 0 :
            return False
            break 
        else :
            return True

print(is_prime(4))

print(is_prime(17))