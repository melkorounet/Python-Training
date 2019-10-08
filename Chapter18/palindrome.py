def is_palindrome(word) :
    word=word.lower()
    reverse = word[::-1]
    if reverse == word :
        return True
    else : 
        return False

word = input ("ecrivez un mot : ")
result = is_palindrome(word)
print(result)
