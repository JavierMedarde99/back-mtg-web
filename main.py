from typing import Optional
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import Service.conexionDatabase as conexionDatabase
import Service.mtg_card_service as mtg_service
app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:8000",
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Player_model(BaseModel):
    name : str
    imagen : str

class Deck_model(BaseModel):
    name : str
    id_player : int

class Cards_model(BaseModel):
    text : str


@app.get("/get/players")
def get_players(id: Optional[int]=0 ,name: Optional[str] ="" ,imagen : Optional[str] =""):
    return conexionDatabase.select_database("players",{"id":id,"name":name,"imagen":imagen})

@app.get("/get/desks")
def get_deck(id: Optional[int]=0 ,idPlayer : Optional[int]=0,name: Optional[str] =""):
    return conexionDatabase.select_database("decks",{"id":id,"name":name,"idPlayer":idPlayer})

@app.get("/get/cards")
def get_cards(id : Optional[int]=0, type : Optional[str]="",idDeck : Optional[str]="",cmc : Optional[int]=0):
    return conexionDatabase.select_database("cards",{"id":id,"idDeck":idDeck,"cmc":cmc,"type":type})

@app.post("/insert/player")
def add_player(player : Player_model):
    return conexionDatabase.insert_database("players",player)

@app.post("/insert/deck")
def add_deck(deck : Deck_model):
    return conexionDatabase.insert_database("decks",deck)

@app.post("/insert/cards/{id_decks}")
def add_cards(id_decks : int, text_desck: Cards_model):
    return mtg_service.text_analyzer(text_desck,id_decks)

@app.delete("/delete/player/{id}")
def delete_player(id : int):
    return conexionDatabase.delete_database("players",id)

@app.delete("/delete/deck/{id}")
def delete_deck(id : int):
    return conexionDatabase.delete_database("decks",id)

