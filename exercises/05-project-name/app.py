import requests

# your code here
import json


response = requests.get("https://assets.breatheco.de/apis/fake/sample/project_list.php")
casa ={}
casa=response.json()

#print("Current time:",casa["hours"],"hrs",casa["minutes"],"min and",casa["seconds"],"sec")
print(casa[0])