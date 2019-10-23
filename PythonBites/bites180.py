from collections import defaultdict

data = """last_name,first_name,country_code
Watsham,Husain,ID
Harrold,Alphonso,BR
Apdell,Margo,CN
Tomblings,Deerdre,RU
Wasielewski,Sula,ID
Jeffry,Rudolph,TD
Brenston,Luke,SE
Parrett,Ines,CN
Braunle,Kermit,PL
Halbard,Davie,CN"""

def group_names_by_country(data: str = data) -> defaultdict:
    countries = defaultdict(list)
    data_list = []
    formatted_data = data.split('\n')
    for entry in formatted_data :
        data_list.append(entry.split(','))

    for name, surname, country in data_list:
        #print(data_list)
        if len(country) == 2:
            #print(type(countries))
            countries[country].append(surname + " " + name)
    return countries        

group_names_by_country(data)