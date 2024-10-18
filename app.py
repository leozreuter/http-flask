from flask import Flask, request, render_template, url_for, redirect
from get_request import get_json
import database
import time

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "Bem vindo a Home!"

@app.route("/get", methods=["GET"])
def insertDatabase():
    if request.method == "GET":
        get_json()
        return "teste"
    if request.method != "GET":
        return "Erro de request!"
    
@app.route("/droptable", methods=["GET", "POST"])
def dropTable():
    if request.method == "GET":
        return render_template('droptable.html')
    
    if request.method == "POST":
        database.dropTable()
        return redirect('/')
    

if __name__ == '__main__':
    app.run(debug=True)