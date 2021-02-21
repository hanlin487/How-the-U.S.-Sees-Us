import requests
import json
import base64

import census as cen

clarafai = 'https://api.clarifai.com/v2/workflows/Demographics/results'

headers = {
    "authorization": "Key 27dbcb9920e24e7f974dff675a25ddee",
    "content-type": "application/json"
}

def get_base64_encoded_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode('utf-8')

def predict_path(image_path):
    # this here
    base64 = get_base64_encoded_image(image_path)
    myobj = {
        "inputs": [
            {
              "data": {
                "image": {
                  "base64": base64
              }
            }
          }
        ]
    }
    
    x = requests.post(clarafai, data = json.dumps(myobj), headers = headers)
    v = json.loads(x.text)
    
    race = v["results"][0]["outputs"][2]["data"]["regions"][0]["data"]["concepts"]
    gender = v["results"][0]["outputs"][3]["data"]["regions"][0]["data"]["concepts"]
    age = v["results"][0]["outputs"][4]["data"]["regions"][0]["data"]["concepts"]

    return get_information(v) 

def predict_url(image_url):
    # this here
    myobj = {
        "inputs": [
            {
              "data": {
                "image": {
                  "url": image_url
              }
            }
          }
        ]
    }
    
    x = requests.post(clarafai, data = json.dumps(myobj), headers = headers)
    v = json.loads(x.text)

    return get_information(v) 
    
def get_information(v):
    race = v["results"][0]["outputs"][2]["data"]["regions"][0]["data"]["concepts"][0]
    gender = v["results"][0]["outputs"][3]["data"]["regions"][0]["data"]["concepts"][0]
    age = v["results"][0]["outputs"][4]["data"]["regions"][0]["data"]["concepts"][0]

    race = cen.find_race(race)
    age = cen.find_age(age)
    gender = cen.find_gender(gender)

    return race, gender, age


print(predict_path("server/uploaded_images/bobby.jpeg"))
