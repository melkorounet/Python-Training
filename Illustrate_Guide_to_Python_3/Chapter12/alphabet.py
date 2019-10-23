name = input ("Entrez votre nom :")

second_part_alphabet = ("n","o","p","q")

second_half = name.lower().startswith(second_part_alphabet)
print (second_half)