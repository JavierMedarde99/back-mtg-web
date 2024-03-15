class Card:
    
    def __init__(self,id,idApi,amount,idDeck,imagen,expansion,cmc,type):
        self.id = id
        self.idApi = idApi
        self.amount = amount
        self.idDeck = idDeck
        self.imagen = imagen
        self.expansion = expansion
        self.cmc = cmc
        self.type = type

    def __str__(self):
        return '{"id":"'+str(self.id)+'","idApi":"'+self.idApi+'","amount":"'+str(self.amount)+'","idDeck":"'+str(self.idDeck)+'","imagen":"'+self.imagen+'","expansion":"'+self.expansion+'","cmc":"'+str(self.cmc)+'","type":"'+self.type+'"}'
