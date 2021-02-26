import requests
import json


response = requests.get("https://assets.breatheco.de/apis/fake/sample/time.php")
casa ={}
casa=response.json()

print("Current time:",casa["hours"],"hrs",casa["minutes"],"min and",casa["seconds"],"sec")
#print("Current time: 19 hrs 45 min and 06 sec ")
       
    
#"Current time: 19 hrs 45 min and 06 sec\n"