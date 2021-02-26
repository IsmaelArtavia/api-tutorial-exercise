import requests

def get_post_tags(post_id):
    # your code here
 new_array = []
 response = requests.get("https://assets.breatheco.de/apis/fake/sample/weird_portfolio.php")
 casa = {}
 casa=response.json()
 #print ("casa mide",len(casa))
 for x in range(len(casa)-1):
   #new_array[x] = casa["posts"][x]['title']
  #print(casa["posts"][x]["id"])
  #print(post_id)
  prueba=(casa["posts"][1]["id"])
   
  if post_id == casa["posts"][x]["id"]:
       #print("encontrado")                
       #new_array.append(casa["posts"][x]["author"]["id"])
       #print("tags mide: ",len(casa["posts"][x]["tags"]))
       for y in range(len(casa["posts"][x]["tags"])):
         #print(casa["posts"][x]["tags"][y]["id"])
         #print(casa["posts"][x]["tags"]) 
         
         new_array.append(casa["posts"][x]["tags"][y]["id"])
       #print("el nuevo arreglo mide",len(new_array))  
       print(len(new_array))
       #new_array[x] = casa["posts"][x]["tags"]
 return new_array 

 

print(get_post_tags(146))
#print(get_post_tags(47))



