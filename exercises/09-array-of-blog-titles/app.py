import requests
import json

def get_titles():
    # your code here
 new_array = []
 response = requests.get("https://assets.breatheco.de/apis/fake/sample/weird_portfolio.php")
 casa ={}
 casa=response.json()
 
 for x in range(4):
   #new_array[x] = casa["posts"][x]['title']
   new_array.append(casa["posts"][x]["title"])
     
 return new_array
 
 #print(casa ["posts"][0]['title'])
 #print(casa ["posts"][1]['title'])
 #print(casa ["posts"][2]['title'])
 #print(casa ["posts"][3]['title'])
   


print(get_titles())






