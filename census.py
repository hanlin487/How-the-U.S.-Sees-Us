import pandas as pd
import numpy as np

data = pd.read_csv("data/electoral_data.csv")
data.index = data.Label
# data = data.drop('Label', 1)

raceDict = {
'Black': "Black or African American alone", 
"White": "White alone",
"East Asian": "Asian alone",
"Latino_Hispanic": "Hispanic or Latino (of any race)"
}

ageDict = {
 "10-19" : "15 to 19 years",
 "20-29": "20 to 24 years",
 "30-39": "25 to 34 years",
 "30-39": "35 to 44 years",
 "40-49": "45 to 54 years",
 "50-59": "55 to 59 years",
 "60-69": "60 to 64 years",
 "60-69": "65 to 74 years",
"more than 70": "75 to 84 years"
}

genderDict = {
"Masculine": "Male",
"Feminine": "Female"
}

def find_info(info, infoDict):
    key = info["name"]
    print(key)
    if key in list(infoDict.keys()):
        return data.loc[infoDict[key]].Average
    
    print("we couldn't find that in our dictionary")
    return pd.Series(np.zeros(10))

def find_race(info):
    return find_info(info, raceDict)

def find_age(info):
    return find_info(info, ageDict)

def find_gender(info):
    return find_info(info, genderDict)
