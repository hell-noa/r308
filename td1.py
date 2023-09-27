def plus_grand_des_deux(a,b):
    if a > b:
        return a
    else:
        return b
    
def seuil(a , seuil=10):
    if a >seuil :
        return True
    else:
        return False
    
def max_liste():
    liste=[2,65,9,8]
    return max(liste)



def list_inf(seuil=3):
    L = [22,65,98,0,1,4]
    c = 0
    for i in range (len(L)):
        if L[i] < seuil :
            c+=1
    print(c)

def dico(dictio):
    dictio['a':2, 'b':3]
    
class Tasse:
    matiere :str = "céramique"
    
    def __init__(self,couleur:str , contenance:float , marque:str):
        self.couleur = couleur
        self.contenance=contenance
        self.marque = marque
        
    def __str__(self)-> str:
        return f"la tasse de matiere {self.matiere}, de couleur {self.couleur}, et de marque {self.marque} à une constance de {self.contenance}"

    def cont(self, contenu) ->str:
        self.contenu = contenu
        
a= Tasse('bleur', 'duralex', '50')

    
#print(plus_grand_des_deux(0,1))
#print (seuil(2, 1))
#print(max_liste())
#list_inf()
print(a)