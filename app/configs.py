from distutils.debug import DEBUG
from pickle import TRUE
from re import T


class DevConfig(object):
    DEBUG = True
    DEVELOPMENT = TRUE
    PRODUCTION = TRUE
    SECRET_KEY = "lasjdlfjalsdfasfdalasdf"

class ProConfig(object):
    PRODUCTION = True