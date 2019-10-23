class Mario :
    '''on définit mario et ses attributs
    grand ou petit
    combien de vies
    '''
    moustache = True

    def __init__(self,id):
        self.id=id
        self.count=1

    def champi(self):
        if self.count == 1 :
            self.count+=1
    
    def fleur(self):
        if self.count == 2 :
            self.count+=1
        elif self.count == 3 : 
            self.count+=0
        elif self.count == 1 :
            self.count+=2
    
    def touche(self):
        self.count -=1
        if self.count == 0 :
            print ("Oh no Mario est décédé")


mario=Mario(1)
mario.champi()
mario.touche()
mario.touche()
    
