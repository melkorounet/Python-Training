class CustomerBank: 
    '''application de banque, on définit ce dont à un besoin un customer
    nom prénom
    identifiant unique
    somme présente sur le compte
    somme après dépôt
    somme après retrait
    '''
    def __init__ (self, id) :
        self.id=id
        self.count=0

    def depot (self, number):
        self.count=+number

    def retrait (self, number):
        self.count=-number

