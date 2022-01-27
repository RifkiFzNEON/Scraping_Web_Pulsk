from apps.helper import Log
from apps.schemas import BaseResponse
from apps.models import db as datadb
from apps.schemas.SchemaScrap import RequestKATE, ResponseKATE, ResponseURL
from apps.helper.ConfigHelper import encoder_app
from main import PARAMS
from apps.models.PulskModel import Scrap, Url

SALT = PARAMS.SALT.salt

class ControllerRifki(object):
#---------------------------------------------------------------------------
    @classmethod
    def get_articel_by_judul(cls, input_data=None):
        input_data = RequestKATE(**input_data)
        result = BaseResponse()
        result.status = 400

        try:
            cek_judul = Scrap.where('judul', '=', input_data.judul).get().serialize()
            if cek_judul != []:
                data = Scrap.where('judul', '=', input_data.judul).get().serialize()
                result.status = 200
                result.message = "Success"
                result.data = ResponseKATE(**{"scrap_list": data})
                Log.info(result.message)
            else:
                e = "judul not found!"
                Log.error(e)
                result.status = 404
                result.message = str(e)
        except Exception as e:
            Log.error(e)
            result.status = 400
            result.message = str(e)

        return result

    @classmethod
    def get_trend_kategori_articel(cls, input_data):
        list_kategori = [
            "Everything in Life",
            "Fashion",
            "Musik, Film & Buku",
            "Lucu Lucu",
            "Peristiwa",
            "Misteri",
            "WOW Keren",
            "Beautiful / GIrl"]
        input_data = input_data
        result = BaseResponse()
        result.status = 400
   
        try:
            if input_data in list_kategori:
                data = Scrap.where('kategori', '=', input_data).count()
                result.status = 200
                result.message = "Success"
                result.data = {"count_kategori_articel": data}
                Log.info(result.message)
            else:
                e = "kategori not found! Please check the example input!"
                Log.error(e)
                result.status = 404
                result.message = str(e)
                
        except Exception as e:
            Log.error(e)
            result.status = 404
            result.message = str(e)

        return result

#-----------------------------------------------------------------------------------------------------------------
    @classmethod
    def get_article_url(cls):
        result = BaseResponse()
        result.status = 400

        try:
            data = Url.get().serialize()
            result.status = 200
            result.message = "Success"
            result.data = ResponseURL(**{"url_list": data})
            Log.info(result.message)
                
        except Exception as e:
            Log.error(e)
            result.status = 404
            result.message = str(e)

        return result
    
    def get_detail_article():
        result = BaseResponse()
        result.status = 400

        try:
            data = Scrap.get().serialize()
            result.status = 200
            result.message = "Success"
            result.data = ResponseKATE(**{"scrap_list": data})
            Log.info(result.message)
                
        except Exception as e:
            Log.error(e)
            result.status = 404
            result.message = str(e)

        return result