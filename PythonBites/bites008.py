def rotate(string, n):
    """Rotate characters in a string.
       Expects string and n (int) for number of characters to move.
    """
    print(string[n:]+string[:n])
    pass

rotate("hello", -2)