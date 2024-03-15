import mysql.connector
import Entity.players
import Entity.decks
import Entity.cards

#connection to database
conectionMtg = mysql.connector.connect(
    host = "localhost",
    user = "javi",
    password = "root",
    database= "mtg",
    auth_plugin = "mysql_native_password"
)

#create the cursor to conect the database
mycursor = conectionMtg.cursor()

def find_card(id):
    sentence = f"SELECT * FROM cards WHERE idApi = '{id}'"
    mycursor.execute(sentence)
    return mycursor.fetchall()


## create query select 
def select_database(database,parametres):

    array = []

    print(parametres)

    stringJson = ""

    sentence = f"SELECT * FROM mtg.{database} WHERE 1=1 "

    for key in parametres:
            if isinstance(parametres[key],(int,float)): 
                if parametres[key] != 0:
                    sentence = sentence + " AND " + key + "= "+str(parametres[key]) 
            else:
                if parametres[key] != "":
                    if key == "idDeck":
                        sentence = sentence + " AND " + key + " LIKE '%,"+parametres[key] +",%'" 
                    elif parametres[key].lower().capitalize()=="Creature" or parametres[key].lower().capitalize() == "Land":
                        sentence = sentence + " AND " + key + " LIKE '%"+parametres[key].lower().capitalize() +"%'"
                    else:
                        sentence = sentence + " AND " + key + "= '"+parametres[key] +"'"
                        

    print(sentence)

    
    mycursor.execute(sentence)
    result = mycursor.fetchall()
        
    if database == "players":

        for x in result:
            player = Entity.players.player(x[0],x[1],x[2])
            stringJson = player.__str__() + "," + stringJson

        return "["+stringJson[:-1]+"]"
        
    
    elif database == "decks":

        for x in result:
            deck = Entity.decks.Deck(x[0],x[1],x[2])
            stringJson = deck.__str__() + "," + stringJson
        return "["+stringJson[:-1]+"]"
    else:

        for x in result:
            print(x)
            card = Entity.cards.Card(x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7])
            stringJson = card.__str__() + "," + stringJson

        return "["+stringJson[:-1]+"]"
        

def insert_database(database,insert_class):

    print(insert_class)

    if database == "players":
        sentence = f"INSERT INTO {database} (name,imagen) VALUE (%s,%s)"
        val = (insert_class.name,insert_class.imagen)
    elif database == "decks":
        sentence = f"INSERT INTO {database} (name,idPlayer) VALUE (%s,%s)"
        val = (insert_class.name,insert_class.id_player)
    else:
        repit_card =find_card(insert_class.idApi)
        if repit_card:
            id_deck_new = repit_card[0][3]+str(insert_class.idDeck)+","
            sentence = f"UPDATE {database} SET idDeck='{id_deck_new}' WHERE idApi='{insert_class.idApi}'"
            print(sentence)
            mycursor.execute(sentence)
            conectionMtg.commit()

            return "right update"

        sentence = f"INSERT INTO {database} (idApi,amount,idDeck,imagen,expansion,cmc,type) VALUE (%s,%s,%s,%s,%s,%s,%s)"
        val = (insert_class.idApi,insert_class.amount,","+str(insert_class.idDeck)+",",insert_class.imagen,insert_class.expansion,insert_class.cmc,insert_class.type)

    mycursor.execute(sentence,val)
    conectionMtg.commit()

    return "Insertado correctamente"

def delete_database(database,id):
    if database =="decks":
        delete_card(id)
    sentence = f"DELETE FROM {database} WHERE id={id}"
        
    mycursor.execute(sentence)
    conectionMtg.commit()

    return "Eliminado correctamente"


def delete_card(id):
    select_sentence = f"SELECT * FROM mtg.cards WHERE idDeck like '%,{str(id)},%'"
    print(select_sentence)
    mycursor.execute(select_sentence)
    result = mycursor.fetchall()
    id_with_coma = ","+str(id)+","
    for x in result:
        if x[3] == id_with_coma:
            sentence = f"DELETE FROM mtg.cards WHERE id={x[0]}"
        else:
            idDeck = x[3].replace(str(id),"")
            idDeck = idDeck.replace(",,,",",")
            idDeck = idDeck.replace(",,",",")
            sentence = f"UPDATE mtg.cards SET idDeck = '{idDeck}' WHERE id = {x[0]}"
        mycursor.execute(sentence)
        conectionMtg.commit()
    


    



    




