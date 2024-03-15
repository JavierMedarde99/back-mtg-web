class player:

    def __init__(self,id,name,imagen):
        self.id = id
        self.name = name
        self.imagen = imagen

    def __str__(self):
        return '{"id":"'+str(self.id)+'","name":"'+self.name+'","imagen":"'+self.imagen+'"}'