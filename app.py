from flask import Flask, request
from get_request import get_json
import database

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "Bem vindo a Home!"

@app.route("/get", methods=["GET"])
def insertDatabase():
    if request.method == "GET":
        return get_json()
    if request.method != "GET":
        return "Erro de request!"
    
@app.route("/droptable", methods=["GET"])
def dropTable():
    if request.method == "GET":
        database.dropTable()
        return "Tabela deletada com sucesso!"
    if request.method != "GET":
        return "Erro de request!"