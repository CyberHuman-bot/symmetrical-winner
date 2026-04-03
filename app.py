class zubermen(): 
    def __init__(self,age,name,exists):
        self.age = age
        self.name = name
        self.exists = exists
class smolsun():
    def __init__(self,eyeco,age,name,exists):
        self.eyeco = eyeco
        zubermen.__init__(self,age,name,exists)
ob = smolsun("blue",6,"Hamburger"," ")
print(ob.name,ob.eyeco,ob.age,ob.exists)