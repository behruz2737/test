import json
import os; os.system("cls")

odam = {
    "ism" : "javohir",
    "yosh" : 10,
    'adress': 'xorazm,yangiariq'
}

o = json.dumps(odam, indent= 4)  

f = open("odam.json", "w+")
f.write(o)

f.close()