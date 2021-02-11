import requests
import json

URL="http://127.0.0.1:8000/studentapi/"

# dump_data=json.dumps(data)
# post_data=requests.post(url=URL ,data=dump_data)
#serializer means to convert complex data type into python native data type and then json data.
#complex data type means :in the database data or table data
# Serializer :: Complex data type---------python native data type------json data(fetch)
# deseriailzer:: json_data(front-end)-----Python native data type-----------Complex data type(database) :Create Data/Insert data
# JSONParser() :::used to parse json data to python native data type.
#JSONRenderer():::used to render serialized data(python data )into JSON understand by front end
# first fetch data from table or model


# data retrieve function or data fetch function
def get_data(id=None):  
    data={}
    if id is not None:   #if data is present then fetch in dictionary
        data={'id':id}
    json_data=json.dumps(data)  
    headers={'content-Type':'application/json'} # convert python into json data 
    r=requests.get(url=URL ,headers=headers, data=json_data)  #Get data from database by converting complex into python and thenafter json
    data=r.json()
    print(data)


# data Insert or data create function

def post_data():
    data={
     'id': 110,
     'name':'Piyush',
     'roll':120,
     'city':'Fatuha',
    } 
    headers={'content-Type':'application/json'}

# convert python data into json
    json_data=json.dumps(data)
    # send post request to the server
    r=requests.post(url=URL,headers=headers, data=json_data)  #Get data from database by converting complex into python and thenafter json
    data=r.json()
    print(data)





# update data inot database
def update_data():
    data={
     'id': 4,
     'name':'Amit',
     'roll':29,
     'city':'lucknow',
    }
    headers={'content-Type':'application/json'} 
# convert python data into json
    json_data=json.dumps(data)
    # send put request to the server(put means update)
    r=requests.put(url=URL ,headers=headers, data=json_data)  #Get data from database by converting complex into python and thenafter json
    data=r.json()
    print(data)



# delete data from database.
def delete_data():
    data={
     'id': 5
    }
    headers={'content-Type':'application/json'}
# convert python data into json
    json_data=json.dumps(data)
    # send put request to the server(put means update)
    r=requests.delete(url=URL,headers=headers, data=json_data)  #Get data from database by converting complex into python and thenafter json
    data=r.json()
    print(data)


# get_data(2)
# post_data()
# update_data()
delete_data()