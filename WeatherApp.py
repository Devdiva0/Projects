import requests
import json
import os

city=input("Enter the city: \n")
url=f"http://api.weatherapi.com/v1/current.json?key=a7318e629d30410ab90142142252801&q={city}"

r=requests.get(url)
print(r.text)

w_dic=json.loads(r.text)
a=w_dic["current"]["temp_c"]
print(f"The cuurent weather in {city} is {a} degrees ")
os.system(f"say 'The cuurent weather in {city} is {a} degrees '")