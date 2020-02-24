import requests, json
from json2html import *


r = requests.get(' https://sv443.net/jokeapi/v2/joke/Dark')
print(r.status_code)

#Hvis der er forbindelse til API'en skal programmet køre
if(r.status_code == 200):
    f = open("prøveeksame.html","w")
    f.write(json2html.convert(json=r.text))
    f.close()
