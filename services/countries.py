from models import Country, CountryList
import json

def get_countries(filepath="data/country_list.json") -> CountryList:
    with open(filepath) as f:
        data = json.load(f)
    countries = CountryList(**data)
    return countries
