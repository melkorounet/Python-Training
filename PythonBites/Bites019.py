from datetime import datetime, timedelta

class Promo:
    '''
    Un constructeur "name" qui prend le nom de la promo
    Un constructeur "expires" qui prend NOW en date
    Une property qui retourne True si promo expired
    '''    
    def __init__(self):
        self._x = 78

    def getx(self):
        return self._x

    def setx(self, value):
        self._x = value

    def delx(self):
        del self._x

    x = property(getx, setx, delx, "I'm the 'x' property.")

c =Promo()
print(c.x)
