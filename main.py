from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import json
import os

app = FastAPI()
fitxer = "alumnes.json"

# Models ####################################################

class DataNaixement(BaseModel):
    dia: int
    mes: int
    any: int

class Alumne(BaseModel):
    nom: str
    cognom: str
    data: DataNaixement
    email: str
    feina: bool
    curs: str

# Funcions auxiliars ########################################

def carregar():
    if os.path.exists(fitxer):
        with open(fitxer, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def desar(alumnes):
    with open(fitxer, "w", encoding="utf-8") as f:
        json.dump(alumnes, f, indent=4)

# Endpoints #################################################

@app.get("/")
def llegenda():
    """Torna el nom de l'institut"""
    return {"institut": "Institut TIC de Barcelona"}

@app.get("/alumnes/")
def total_alumnes():
    """Torna el nombre total d'alumnes"""
    alumnes = carregar()
    return {"total": len(alumnes)}

@app.get("/id/{numero}")
def obtenir_alumne(numero: int):
    """Torna l'alumne amb l'ID indicat"""
    alumnes = carregar()
    alumne = next((a for a in alumnes if a["id"] == numero), None)
    if alumne:
        return alumne
    raise HTTPException(status_code=404, detail="Alumne no trobat")

@app.delete("/del/{numero}")
def eliminar_alumne(numero: int):
    """Elimina l'alumne amb l'ID indicat"""
    alumnes = carregar()
    nou_lli = [a for a in alumnes if a["id"] != numero]
    if len(nou_lli) == len(alumnes):
        raise HTTPException(status_code=404, detail="Alumne no trobat")
    desar(nou_lli)
    return {"missatge": "Alumne esborrat correctament"}

@app.post("/alumne/")
def afegir_alumne(alumne: Alumne):
    """Afegeix un alumne nou"""
    alumnes = carregar()
    nou_id = max([a["id"] for a in alumnes], default=0) + 1
    alumne_dict = alumne.dict()
    alumne_dict["id"] = nou_id
    alumnes.append(alumne_dict)
    desar(alumnes)
    return {"missatge": "Alumne afegit correctament", "id": nou_id}