class Enemy:
    ename =""
    eclass = ""
    ehp=""
    emana=""
    eweapon=""
    edamage=""
    def __init__(self, newename,neweclass,newehp,newedamage,neweweapon=None):
        self.ename =newename 
        self.eclass=neweclass
        self.ehp=newehp
        self.eweapon=neweweapon
        self.edamage=newedamage
        
    def info(self):
        print(f"Имя противника: {self.ename}\nКласс: {self.eclass}\nХп: {self.ehp}\nОружие: {self.eweapon}\nДамаг: {self.edamage}")

# enemy1 = Enemy("Матр4сс","тожегайсфнфмода", 100, 10)
# enemy1.info()