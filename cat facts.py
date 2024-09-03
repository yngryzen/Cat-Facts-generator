import requests

# req = requests.get("https://www.example.com")
# print(req.text)

req = requests.get("https://catfact.ninja/fact", params={"max_length": 58})
fact = req.json()

file = open("cat jokes.txt", "a")
file.write(f"[{fact["length"]}] {fact["fact"]} \n")