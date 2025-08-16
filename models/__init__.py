from pydantic import BaseModel

class Country(BaseModel):
    """ 
        "id": 1,
        "name": "Andorra",
        "code": "AD",
        "emoji": "🇦🇩",
    },
    """
    id: int
    name: str
    code: str
    code3: str
    numeric: str
    emoji: str


class CountryList(BaseModel):
    countries: list[Country]
