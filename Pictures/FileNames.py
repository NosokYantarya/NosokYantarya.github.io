import os
import json

File = "Pictures.json"

with open(File, 'r', encoding='utf-8') as file:
    Content = file.read()

Data = json.loads(Content)

for i in range(0,len(Data)):
    Data[i]["Pictures"] = os.listdir("Pictures/" + Data[i]["Dir"] + "/")
Data = json.dumps(Data, ensure_ascii=False)
print(Data)

with open(File, 'w', encoding='utf-8') as file:
    file.write(Data)
