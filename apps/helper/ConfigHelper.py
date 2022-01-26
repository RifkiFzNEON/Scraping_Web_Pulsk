import os
import json
import yaml
import binascii
from hashids import Hashids
from yaml.loader import Loader
from apps.helper import Log
from apps.schemas.SchemaConfig import ConfigApps


def decoder_app(code, salt):
    hashids = Hashids(salt=salt)
    text_hex = hashids.decode_hex(code)
    text = binascii.unhexlify(text_hex)
    text_str = str(text, 'utf-8')
    return text_str


def encoder_app(text, salt):
    hashids = Hashids(salt=salt)
    text = binascii.hexlify(text.encode())
    text_str = str(text, 'utf-8')
    text_hex = hashids.encode_hex(text_str)
    return text_hex


class Config:
    __dir_name__ = os.path.dirname(__file__)
    __file_path__ = '../../config/config.yaml'
    __file_config__ = os.path.abspath(os.path.join(__dir_name__, __file_path__))

    __config_yaml__ = None
    PARAMS = ConfigApps

    @classmethod
    def load(cls):
        config = open(cls.__file_config__, "r")
        cls.__config_yaml__ = yaml.load(config, Loader=Loader)
        Log.info("Load config/config.yaml")

        cls.PARAMS = ConfigApps(
            ENVIRONMENT=cls.__config_yaml__['env'],
            APPS_INFORMATION=cls.__config_yaml__["apps"],
            ALLOWED_HOSTS=cls.__config_yaml__["allowed_hosts"],
            ALLOW_METHODS=cls.__config_yaml__["allow_methods"],
            API_TOKEN=cls.__config_yaml__["api_token"][cls.__config_yaml__['env']],
            DATABASE=cls.__config_yaml__["database"][cls.__config_yaml__['env']],
            SALT=cls.__config_yaml__["salt_key"][cls.__config_yaml__['env']]
        )

        Log.info("Environment '{}' has loaded!".format(cls.__config_yaml__['env']))

    responses = {
        200: {
            "description": "Success get data",
            "content": {
                "application/json": {"example": {"status": 200, "message": "Success get data", "data": []}}},
        },
        404: {
            "description": "Not Found",
            "content": {"application/json": {"example": {"status": 404, "message": "Not Found", "data": []}}},
        },
        403: {
            "description": "Not enough privileges",
            "content": {
                "application/json": {"example": {"status": 403, "message": "Not enough privileges", "data": []}}},
        },
    }

    responses_home = {
        200: {"content": {"application/json": {
            "example": {"title": "API using FastAPI", "version": "1.0.0", "description": "API using FastAPI"}}}}
    }


Config.load()