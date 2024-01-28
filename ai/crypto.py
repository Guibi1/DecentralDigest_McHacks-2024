import requests

def get_ipfs_data(cid):
    # Replace "http://localhost:5001" with the appropriate IPFS API endpoint
    api_url = "http://localhost:5001/api/v0/cat?arg=" + cid

    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            return response.content
        else:
            print(f"Error: {response.status_code} - {response.text}")
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Replace 'your-cid' with the actual CID you want to retrieve
your_cid = 'QmZULkCELmmk5XNfCgTnCyFgAVxBRBXyDHGGMVoLFLiXEN'

data = get_ipfs_data(your_cid)

if data:
    print("Data retrieved successfully:")
    print(data.decode('utf-8'))  # Decode binary data to UTF-8 for text content
else:
    print("Failed to retrieve data.")
