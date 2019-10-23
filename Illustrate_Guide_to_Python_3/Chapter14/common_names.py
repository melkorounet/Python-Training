potos = ["alexandre", "julien", "noemie", "valentin", "clement", "nicolas","lucas"]
common_names = ["Gabriel","Raphaël","Léo","Louis","Emma","Lucas","Jade","Adam","Louise","Arthur"]

potos = set([element.lower() for element in potos])
common_names = set([element.lower() for element in common_names])
print(common_names)

result = potos & common_names

print (result)