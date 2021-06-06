import os


class Config(object):
    TOKEN = os.environ.get("TOKEN", "1860827928:AAHCewh-sPCTBXrQx3BgA55a-yKuWDXdEfg")

    APP_ID = int(os.environ.get("APP_ID", 5489787))

    API_HASH = os.environ.get("API_HASH", "39bb1e66c18e13f1ce8d50bb68c40272")
