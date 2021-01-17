import requests
import json

URL=""

data = {
    'name':'ashish',
    'roll':20,
    'city':'Patna',
    'branch':'CSE',
    'college':'Tulas'
}

dump_data=json.dumps(data)
