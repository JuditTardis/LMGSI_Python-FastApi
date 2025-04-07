from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import json
import os

app = FastAPI()

# Ruta del fitxer d'alumnes
FITXER = "alumnes.json"

# Classe per validar dades rebudes pel POST
class DataNaixement(BaseModel):
    dia: int
    mes: int
    any: int

class Alumne(BaseModel):
    id: int = None
    nom: str
    cognom: str
    data: DataNaixement
    email: str
    feina: bool
    curs: str

# Carrega els alumnes
def carregar():
    if os.path.exists(FITXER):
        with open(FITXER, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def desar(alumnes):
    with open(FITXER, "w", encoding="utf-8") as f:
        json.dump(alumnes, f, indent=4)

@app.get("/")
def llegenda():
    return "Institut TIC de Barcelona"

@app.get("/alumnes/")
def total_alumnes():
    alumnes = carregar()
    return {"total": len(alumnes)}

@app.get("/id/{numero}")
def obtenir_alumne(numero: int):
    alumnes = carregar()
    for alumne in alumnes:
        if alumne["id"] == numero:
            return alumne
    raise HTTPException(status_code=404, detail="Alumne no trobat")

@app.delete("/del/{numero}")
def eliminar_alumne(numero: int):
    alumnes = carregar()
    alumnes_nou = [a for a in alumnes if a["id"] != numero]
    if len(alumnes_nou) == len(alumnes):
        raise HTTPException(status_code=404, detail="Alumne no trobat")
    desar(alumnes_nou)
    return {"missatge": "Alumne esborrat correctament"}

@app.post("/alumne/")
def afegir_alumne(alumne: Alumne):
    alumnes = carregar()
    nou_id = max([a["id"] for a in alumnes], default=0) + 1
    alumne.id = nou_id
    alumnes.append(alumne.dict())
    desar(alumnes)
    return {"missatge": "Alumne afegit correctament", "id": nou_id}
