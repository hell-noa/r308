class Personnage:
    def __init__(self, pseudo: str, niveau: int=1):
        self.__pseudo = pseudo
        self.__niveau = niveau
        self.__pv = niveau
        self.__initiative = niveau


    @property
    def pseudo(self):
        return self.__pseudo
    

    @property
    def niveau(self):
        return self.__niveau
    

    
    @property
    def pv(self):
        return self.__pv
    @pv.setter
    def pv(self, valeur:int):
        self.__pv  = valeur
        
    def soin_pv(self):
        self.__pv = self.niveau
        
    @property
    def initiative(self):
        return self.__initiative
    
    @initiative.setter
    def initiative(self, valeur:int):
        self.__initiative= valeur
    

    
            
    def attaque(self, cible:str):
        if isinstance(cible, Personnage):
            if self.initiative > cible.initiative:
                cible.pv -= self.degats()
                if cible.pv >0:
                    self.pv -= cible.degats()
            elif self.initiative == cible.initiative:
                self.pv -= cible.degats()
                cible.pv -= self.degats()
            else:
                self.pv -= cible.degats()
                if self.pv > 0:
                    cible.pv -= self.degats()
            
                
    def combat(self, cible: str):
        if isinstance(cible, Personnage):
            print (f"~~~~\n{self.pseudo} = {self.pv}\n{cible.pseudo} = {cible.pv}\n~~~~\n")
            while self.pv > 0 and cible.pv > 0:
                self.attaque(cible)
                print (f"~~~~\n{self.pseudo} = {self.pv}\n{cible.pseudo} = {cible.pv}\n~~~~\n")

            if cible.pv <= 0:
                print(f'{cible.pseudo} est mort')
            elif self.pv <= 0:
                print(f'{self.pseudo} est mort')
    
    def degats(self):
        return self.niveau


            
class Guerrier(Personnage):
    def __init__(self, pseudo : str , niveau : int=1):
        super().__init__(pseudo, niveau)
        self.pv = niveau * 8 + 4
        self.initiative = niveau * 4 + 6
        
    def degats(self):
        return self.niveau * 2 
        
        
                        
class Mage(Personnage):
    def __init__(self, pseudo : str , niveau : int=1):
        super().__init__(pseudo, niveau)
        self.pv = niveau * 5 + 10
        self.initiative = niveau * 6 + 4
        self.__mana = niveau * 5
        
        
    @property
    def mana(self):
        return self.__mana
    
    @mana.setter
    def mana(self, valeur:int):
        self.__mana  = valeur
    
        
    def degats(self):
        if self.mana > 0:
            self.mana -= 4
            return self.niveau + 3
        else:
            return self.niveau 
            
            
            
joueur1 = Guerrier('Guerrier')
joueur2 = Mage('Mage')

joueur1.combat(joueur2)
print(joueur2.pv)
joueur2.soin_pv()
print(joueur2.pv)
