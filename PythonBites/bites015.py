names = 'Julian Bob PyBites Dante Martin Rodolfo'.split()
countries = 'Australia Spain Global Argentina USA Mexico'.split()


def enumerate_names_countries(names, country):
    iteration = len(names)
    i = 0
    while i < iteration : 
        print('{i}.'.format(i=i+1), '{:<10}'.format(names[i]),countries[i])
        i+=1

enumerate_names_countries(names, countries)