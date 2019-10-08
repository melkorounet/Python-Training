def csv_file(filename, description):
    with open(filename, 'w') as fout :
        fout.write("name,address,age\n")
        for personne in description: 
            my_string = "{},{},{}\n"
            chain = my_string.format(personne[0],personne[1], personne[2])  
            fout.write(chain)

description=[('George', '4312 Abbey Road', 22),('John', '54 Love Ave', 21)]
filename="test.csv"


csv_file(filename, description)