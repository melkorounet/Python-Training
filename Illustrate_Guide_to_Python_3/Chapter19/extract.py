def cvs_read(filename):
    dico = {}
    with open(filename) as fin :
        for line in fin:
            print(line)


filename="test.csv"

cvs_read(filename)