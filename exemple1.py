def affiche(chaine:str):
    return print (f" texte à afficher :{chaine}")
        

class velo:
    vitesse_courante : int = 1
    
    def __init__(self , marque:str, taille:str, pneu:str, couleur:str, nb_vitesse:str):
        self.marque = marque
        self.taille = taille
        self.pneu = pneu
        self.couleur = couleur
        self.nb_vitesse = nb_vitesse
        

    
    def gear_up(self, up:int):
        self.vitesse_courante += up
        if self.vitesse_courante < 1 and self.vitesse_courante >24:
            return print("la vitesse n'est pas correct")
        else:
            return print(self.vitesse_courante)
        
    def gear_down(self, down:int):
        self.vitesse_courante -= down
        if self.vitesse_courante < 1 and self.vitesse_courante >24:
            return print("la vitesse n'est pas correct")
        else:
            return print(self.vitesse_courante)
        
    
def appel():
    str1= "test numero 1"
    affiche(str1)
    v1= velo("Lapierre","155","11''","rouge","24")
    v1.gear_up(12)
    v1.gear_down(5)
    
    
appel()