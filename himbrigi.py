class Emploey():
    def __init__(self,potato):
        self.potato = self.potato
    def ptprinto(self):
        print(self.potato)
class hamburer( Emploey ):
    def __init__(self, potato,tomato):
        super().__init__(potato)
        self.tomato = tomato
ob = hamburer(1,1)
ob.ptprinto()