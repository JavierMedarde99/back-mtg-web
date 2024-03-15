class Deck:

    def __init__(self,id,name,idPlayer):
        self.id = id
        self.idPlayer = idPlayer
        self.name = name

    def __str__(self):
        return '{"id":"'+str(self.id)+'","name":"'+self.name+'","idPlayer":"'+str(self.idPlayer)+'"}'