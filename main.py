from fastapi import FastAPI
import requests
import json
from datetime import datetime

app = FastAPI()

# database:
countries = [
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
codes = { c["area_code"]: c["name"] for c in countries }


@app.get("/")
def hello():
    return {"message": "Hello World"}


@app.get("/now")
def datetime_now():
    return {
        "datahora": datetime.now(), 
        "pais": "br"
    }


@app.get("/countries")
def get_countries():
    return countries


@app.get("/country/{area}")
def get_country_area(area: int):
    """/country/55"""
    print(codes)
    if area in codes:
        return {
            "code_area": area, 
            "name": codes[area]
        }


@app.get("/quote")
def get_random_quote():
    """ faz request e retorna o resultado em json """
    url = "https://zenquotes.io/api/random"
    response = requests.get(url)
    quote = response.json()[0]
    return {
        "quote": quote['q'],
        "author": quote['a']
    }


@app.get("/users")
def list_users():
    with open("data/users.json") as f:
        return json.load(f)

