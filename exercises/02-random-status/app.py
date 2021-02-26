import requests

response = requests.get("https://assets.breatheco.de/apis/fake/sample/random-status.php")


if response.status_code == 404:
 print(str(response.status_code)+ " The URL you asked is not found")
elif response.status_code == 503:
 print(str(response.status_code)+" Unavailable right now")
elif response.status_code == 200:
 print(str(response.status_code)+" Everything went perfect")
elif response.status_code == 400:
 print(str(response.status_code)+" Something is wrong on the request params")