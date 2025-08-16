from fastapi import FastAPI
import requests
import json
from datetime import datetime

app = FastAPI()

# fake database:
db_countries = [
    {
        "area_code": 20,
        "iso_code": "eg",
        "name": "Egito",
        "language": "arabic"
    },
    {
        "area_code": 54,
        "tld_code": "ar",
        "name": "Argentina",
        "language": "spanish"
    }, 
    {
        "area_code": 55,
        "tld_code": "br",
        "name": "Brasil",
        "language": "portuguese"
    },
]
codes = { c["area_code"]: c["name"] for c in db_countries }


@app.get("/")
def hello():
    return {"message": "Hello World"}


@app.get("/now")
def datetime_now():
    return {
        "datahora": datetime.now(), 
        "pais": "br"
    }


@app.get("/paises")
def get_db_countries():
    return db_countries


@app.get("/paises/{area}")
def get_db_country_area(area: int):
    """ /paises/55 """
    if area in codes:
        return {
            "code_area": area, 
            "name": codes[area]
        }


@app.get("/quote")
def get_random_zenquote():
    """ faz request e retorna o resultado em json """
    url = "https://zenquotes.io/api/random"
    response = requests.get(url)
    quote = response.json()[0]
    return {
        "quote": quote['q'],
        "author": quote['a']
    }


@app.get("/users")
def list_users_in_file():
    with open("data/users.json") as f:
        return json.load(f)


@app.get("/andorra")
def get_andorra_country():
    """ exemplo usando pydantic """
    from models import Country
    c = Country(
        id=1,
        name="Andorra",
        code="AD",
        code3="AND",
        numeric="020",
        emoji="🇦🇩"
    )
    return c


@app.get("/countries")
def list_countries(results: int = 5):
    """
        http :8000/countries -b
    """
    from services.countries import get_countries
    data = get_countries()
    return data.countries[:results]
