import json
from typing import Optional
from fastapi import APIRouter, Body, Query, Response
from apps.controllers.RifkiController import ControllerRifki as Rifki

router = APIRouter()

example_input_idscrap = json.dumps({
    "id_scrap": "11"
}, indent=2)

example_kategori_articel = ["Everything in Life",
                            "Fashion",
                            "Musik, Film & Buku",
                            "Lucu Lucu",
                            "Peristiwa",
                            "Misteri",
                            "WOW Keren",
                            "Beautiful / GIrl"]

#--------------------------------------------------------------------------------------------------

@router.get("/get_trend_kategori_articel")
async def get_trend_kategori_articel(response: Response, 
            kategori: Optional[str]=Query(None, example=example_kategori_articel)):
    result = Rifki.get_trend_kategori_articel(kategori)
    response.status_code = result.status
    return result

@router.post("/get_articel_by_idscrap")
async def get_articel_by_idscrap(response: Response, input_data=Body(..., example=example_input_idscrap)):
    result = Rifki.get_articel_by_idscrap(input_data=input_data)
    response.status_code = result.status
    return result

#--------------------------------------------------------------------------------------------------

@router.get("/get_article_url")
async def get_article_url(response: Response):
    result = Rifki.get_article_url()
    response.status_code = result.status
    return result

