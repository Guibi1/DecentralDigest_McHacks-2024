import requests

def add_to_ipfs(file_path):
    url = "http://3.143.115.147:5001/api/v0/add"
    
    try:
        with open(file_path, 'rb') as file:
            files = {'file': (file.name, file)}
            response = requests.post(url, files=files)
            
            if response.status_code == 200:
                json_response = response.json()
                cid = json_response['Hash']
                print(f"File added to IPFS. CID: {cid}")
                return cid
            else:
                print(f"Error adding file to IPFS. Status code: {response.status_code}")
                return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Replace 'your_file.txt' with the path to the file you want to add
file_path = 'hello.txt'
add_to_ipfs(file_path)
