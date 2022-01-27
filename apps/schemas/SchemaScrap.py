from typing import  List
from datetime import date
from pydantic import BaseModel

#---------------------------------------------
class RequestKATE(BaseModel):
    id_scrap: int = None
    judul: str = None
    penulis: str = None
    foto_profil: str = None
    kategori: str = None
    thumbnail: str = None
    jumlah_views: int = None
    deskripsi: str  = None
    konten: str = None
    konten_gambar: str = None
    tanggal: date = None
    
class CountArticel_by_Kategori(BaseModel):
    id_scrap: int = None
    judul: str = None
    penulis: str = None
    foto_profil: str = None
    kategori: str = None
    thumbnail: str = None
    jumlah_views: int = None
    deskripsi: str  = None
    konten: str = None
    konten_gambar: str = None
    tanggal: date = None
    
class ResponseKATE(BaseModel):
    scrap_list: List[CountArticel_by_Kategori]

#---------------------------------------------------------------

class RequestURL(BaseModel):
    id_links: int = None
    judul_head: str = None 
    kategori: str = None
    url: str = None
    time: date = None 

class Get_URL_ArticelPulsk(BaseModel):
    id_links: int = None
    judul_head: str = None 
    kategori: str = None
    url: str = None
    time: date = None

class ResponseURL(BaseModel):
    url_list: List[Get_URL_ArticelPulsk]
