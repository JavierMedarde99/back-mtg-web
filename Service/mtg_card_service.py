import requests

from Entity.cards import Card
import Service.conexionDatabase as conexionDatabase

url = "https://api.magicthegathering.io/v1/cards?"

def data_card(array_card):
    amount = array_card[0]
    expansion = array_card[-1]
    name = ""

    del array_card[0]
    del array_card[-1]

    for i in array_card:
        name = name + " " + i
    
    return {"amount" : amount, "name" : name.strip(), "expansion":expansion}

def text_analyzer(text,id):
    array_cards = text.text.split("\n")

    for i in array_cards:
        array_card = i.split(" ")

        print(array_card)

        filter_card = data_card(array_card)

        print(filter_card)

        url_name = url + "name="+ filter_card["name"] + "&set="+filter_card["expansion"]
        print(url_name)
        response = requests.get(url_name)
        data_card_json = response.json()["cards"]
        for cards in data_card_json:
            if cards["name"].lower() == filter_card["name"].lower() :
                card = Card("",cards["id"],filter_card["amount"],id,cards["imageUrl"],cards["set"],cards["cmc"],cards["type"])
                conexionDatabase.insert_database("cards",card)
                break
        
    return "all card insert right"