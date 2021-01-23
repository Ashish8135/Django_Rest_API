import requests
import json

URL="http://127.0.0.1:8000/stuapi/"

# data = {
#     'name':'ashish',
#     'roll':20,
#     'city':'Patna',
#     'branch':'CSE',
#     'college':'Tulas'
# }

# dump_data=json.dumps(data)
# post_data=requests.post(url=URL ,data=dump_data)
#serializer means to convert complex data type into python native data type and then json data.
#complex data type means :in the database data or table data
# Serializer :: Complex data type---------python native data type------json data
# deseriailzer:: json_data(front-end)-----Python native data type-----------Complex data type(database) :Create Data/Insert data
# JSONParser() :::used to parse json data to python native data type.
#JSONRenderer():::used to render serialized data(python data )into JSON understand by front end
# first fetch data from table or model

def get_data(id=None):  
    data={}
    if id is not None:   #if data is present then fetch in dictionary
        data={'id':id}
    json_data=json.dumps(data)  # convert python into json data 
    r=requests.get(url=URL , data=json_data)  #
    data=r.json()
    print(data)

get_data(2)


