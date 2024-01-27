import requests

url = "https://api.verbwire.com/v1/nft/store/file"

headers = {
    "accept": "application/json",
    "content-type": "multipart/form-data"
}

response = requests.post(url, headers=headers)

print(response.text)