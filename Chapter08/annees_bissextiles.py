annee_test = input("Entrez une année à tester :")
annee_test = int(annee_test)

condition4 = annee_test%4
condition100 = annee_test%100
condition400 = annee_test%400

if condition4 == 0 and condition100 != 0 :
    print (annee_test, " est une année bissextile")
elif condition4 == 0 and condition100 == 0 and condition400 == 0 :
    print (annee_test, " est une année bissextile")
else :
    print (annee_test, " n'est pas une année bissextile")