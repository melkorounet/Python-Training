paragraph = '''Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut 
labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris 
nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit 
esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, 
sunt in culpa qui officia deserunt mollit anim id est laborum.'''

#on compte le nombre de mots dans paragraph
paragraph=paragraph.split()
count = 0
for word in paragraph :
    count += 1

print(count)

#On compte les itérations d'un même mot dans paragraph
word_iteration = {}
for word in paragraph :
    word=word.lower() #lower des mots pour ignorer les majuscules
    word_iteration.setdefault(word, 0)
    word_iteration[word] += 1
print(word_iteration)



