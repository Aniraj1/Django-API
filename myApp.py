import requests
import json



URL="http://127.0.0.1:8000/studentapi/"

#Function based Get Request

def get_data(id=None):
  data = {}
  if id is not None:
    data = {'id': id}
    json_data = json.dumps(data)
    r = requests.get(url=URL, data=json_data)
    datas = r.json()
    print("single data \n",datas)
  # for gettin whole data
  json_data = json.dumps(data)    
  r = requests.get(url=URL, data=json_data)    
  data = r.json()
  print("datas are",data)
  
get_data(2)