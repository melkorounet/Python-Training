def is_prime(n) :
    i=2
    prime = True
    while i < n :
        result = n % i
        i += 1
        if result == 0 :
            prime=False
            break
        
    print (prime)

is_prime(8)