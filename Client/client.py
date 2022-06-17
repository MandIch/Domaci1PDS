import requests
import json

url = "http://192.168.0.20:8081/users"

payload = json.dumps({
  "ime": "Stefan",
  "prezime": "Mandic",
  "username": "stevakralj",
  "smer": "RI",
  "predmeti": [
    {
      "ime": "RMVS",
      "espb": "6"
    }
  ]
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
