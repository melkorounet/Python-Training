paragraph = '''Lorem ipsum dolor sit amet , consectetur adipiscing elit, sed do eiusmod tempor incididunt ut 
labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris 
nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit 
esse mate cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, 
sunt in culpa qui officia deserunt mollit anim id set est laborum.'''

paragraph=paragraph.split()
anagram_list=[]
for word1 in paragraph :
    for word2 in paragraph :
        if word1 != word2 and (sorted(word1)==sorted(word2)) :
            anagram_list.append(word1)

print(anagram_list)