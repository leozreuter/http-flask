import sqlite3

def conectDB():
    db = sqlite3.connect("banco.db")
    curs = db.cursor()

    curs.execute("""CREATE TABLE IF NOT EXISTS sensores (
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                temp FLOAT,
                umidade FLOAT,
                dewpoint FLOAT,
                pressao FLOAT,
                velocidade FLOAT,
                direcao TEXT,
                data DATE)""")
    
    return db

def insertDB(val):
    db = conectDB() 
    curs = db.cursor()

    sql = ("INSERT INTO sensores (temp, umidade, dewpoint, pressao, velocidade, direcao, data) VALUES (?,?,?,?,?,?,?)")
    curs.execute(sql, val) 

    db.commit()
    db.close()

def dropTable():
    db = conectDB()
    curs = db.cursor()

    sql = ("DROP TABLE IF EXISTS sensores")
    curs.execute(sql)

    db.commit()
    db.close()