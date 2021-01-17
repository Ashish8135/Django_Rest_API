import requests
import json

URL ="http://127.0.0.1:8000/stucreate/"

data  = {
    'id':1,
    'name':'ashish',
    'roll':1,
    'city':'lkr',
    'Class':'10',
    'id':3,
    'name':'anand',
    'roll':2,
    'city':'lkr',
    'Class':'11'
    }
json_data=json.dumps(data)
r = requests.post(url = URL, data=json_data)
data1=r.json()
print(data1)
