import model
import json
import requests

import os
from dotenv import load_dotenv

load_dotenv()
CODE = os.getenv('CODE')
GAME = os.getenv('GAME')


params = {'api_version':'0.1','game_number':GAME,'code':CODE}
response = requests.post("https://np.ironhelmet.com/api",data=params)


print(response.status_code)
a = json.loads(response.text)
r = model.Root()
r.json_parse(a)
print(r)

