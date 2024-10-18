import requests
import json
import database

def get_json():

    resp = requests.get('http://ghelfer.net/la/weather.json?')

    if resp.status_code != 200:
        return "Erro"

    json_data = resp.content.decode('utf-8-sig')

    data = json.loads(json_data).get("weather")

    for i in data:
        temperatura = i.get("temperature")
        umidade = i.get("humidity")
        dewpoint = i.get("dewpoint")
        pressao = i.get("pressure")
        velocidade = i.get("speed")
        direcao = i.get("direction")
        data_time = i.get("datetime")
        val = (temperatura, umidade, dewpoint, pressao, velocidade, direcao, data_time)

        database.insertDB(val)

    return "Populado com sucesso!"