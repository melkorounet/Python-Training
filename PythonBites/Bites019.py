from datetime import datetime

NOW = datetime.now()

class Promo:

    def __init__(self, name, expired):
        self.name = name
        self.expired = expired
    
    @property
    def expired(self):
        return self._expired
    
    @expired.setter
    def expired(self, expired):
        if expired < datetime.now():
            self._expired=True
        else : 
            self._expired=False

