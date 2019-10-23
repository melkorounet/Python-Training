fout = open("test.md", 'w')
fout.write("Hello")
fout.close()

with open("test.md2", 'w') as fout3:
    fout3.write("coucou")

