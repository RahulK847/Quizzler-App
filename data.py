import requests

parameters = dict(amount=10, difficulty="easy", type="boolean")
response = requests.get("https://opentdb.com/api.php", params=parameters)
question_data = response.json()["results"]
