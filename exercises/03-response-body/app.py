import requests

url =  requests.get("https://assets.breatheco.de/apis/fake/sample/random-status.php")



if url.status_code == 200:
 print(url.text)
else:
    print("Something went wrong")


