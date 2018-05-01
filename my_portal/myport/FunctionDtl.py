import urllib.parse
#from PATH_TO_ROOT_FOLDER.urllib3 import request,response
from PATH_TO_ROOT_FOLDER import requests
from urllib.parse import urlencode
from urllib.request import Request, urlopen
import json

class ProgRoute():
    def FuncBridge(self,funcdtl):
        main_api = 'https://api.jdoodle.com/execute'


        url_ex = {
        "script": funcdtl,
        "language": "python3",
        "versionIndex": "1",
        "clientId": "7b8c971d304ea4f1d25bb993ced8b2e0",
        "clientSecret":  "64be6d0b4bbb98cc9bcd0fae2caf6b0f4f806b72aeb1b07bdb5b59a6bd753f9e"
        }

        url = main_api

        headers = {'Content-type': 'application/json'}


        r = requests.post(url, json=url_ex , headers=headers)
