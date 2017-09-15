import os
import json
import threading

import db
from unbabel.api import UnbabelApi


#to_translate = 'This is a test'
#target_language = 'pt'
#callback_url = 'http://my_awesome_app.com/unbabel_callback/'

#api.post_translations(text=to_translate, target_language=target_language,
#                      callback_url=callback_url)


TRANSLATION_CHECKING_INTERVAL = 20

api = UnbabelApi(
    username='backendchallenge',
    api_key='711b8090e84dcb4981e6381b59757ac5c75ebb26',
    sandbox=True
)