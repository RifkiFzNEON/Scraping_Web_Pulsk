from ssl import HAS_NEVER_CHECK_COMMON_NAME
from apps.models import Model

class Scrap(Model):
    __table__ = 'data_scrap_pulsk'
    __primary_key__ = 'id_scrap, judul'

class Url(Model):
    __table__ = 'links_pulsk'
    __primary_key__ = 'id_links, judul_head'