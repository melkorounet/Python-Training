def is_prime(n, prime=True) :
    i=2
    while i < n :
        result = n % i
        i += 1
        if result == 0 :
            prime=False
            break
        
    print (prime)

is_prime(7)
