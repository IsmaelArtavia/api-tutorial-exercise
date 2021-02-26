import requests

# your code here

import json


response = requests.get("https://assets.breatheco.de/apis/fake/sample/weird_portfolio.php")
casa ={}
casa=response.json()

#print("Current time:",casa["hours"],"hrs",casa["minutes"],"min and",casa["seconds"],"sec")
#print(casa ["posts"][0]["title"] )
print(casa ["posts"][0]["author"] ['name'])
