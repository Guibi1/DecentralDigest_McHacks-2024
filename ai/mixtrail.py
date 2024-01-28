import os
from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage
import json
import requests
import subprocess

model = "mistral-tiny"

client = MistralClient(api_key="0w3q8F4BCcpsHmEpjsBzrZ8NfjVTVeSD")


totaltext = """
    The United Nations agency for Palestinian refugees (UNRWA) said on Friday it had opened an investigation into several employees suspected of involvement in the Oct. 7 attacks in Israel by Hamas-led militants and that it had severed ties with those staff members.

    "The Israeli authorities have provided UNRWA with information about the alleged involvement of several UNRWA employees in the horrific attacks on Israel on Oct. 7," said Philippe Lazzarini, UNRWA commissioner general.

    "To protect the agency's ability to deliver humanitarian assistance, I have taken the decision to immediately terminate the contracts of these staff members and launch an investigation in order to establish the truth without delay."
    """




def sendtoCryptoServer(value):
        # Specify the directory path you want to change to
    target_directory = '/home/zackydout/Downloads/kubo'

    # Specify the file name
    file_name = 'hello.txt'
    file_path = os.path.join(target_directory, file_name)

    try:
        # Create the file if it doesn't exist
        if not os.path.exists(file_path):
            subprocess.run(['touch', file_path], check=True)

        # Change to the target directory
        os.chdir(target_directory)
        print(f"Changed to directory: {os.getcwd()}")

        # Write content to the file
        with open(file_path, 'w') as file:
            file.write(totaltext)

        # Run a command in the console (replace with your actual command)
        command = ['./ipfs', 'add', file_name]
        command_result = subprocess.run(command, capture_output=True, text=True, check=True)
        
        # Print the result or handle it as needed
        print(command_result.stdout)

    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        # Change back to the original directory (optional)
        os.chdir(os.path.expanduser('~'))
        print(f"Changed back to directory: {os.getcwd()}")
  


def retrieveData():
   
    # Create a user message with the original text
    user_message = ChatMessage(role="user", content=totaltext)

    # Use the original text for unbiased and modified for the biased versions
    biased_messages = [ChatMessage(role="user", content=totaltext + " Uniased this entire paragraph and show what you changed in a list")]
    unbiased_messages = [ChatMessage(role="user", content=totaltext + " Unbiased this entire paragraph")]

    
    chat_response_keyword = client.chat(model=model, messages=biased_messages)
    chat_response_unbiased = client.chat(model=model, messages=unbiased_messages)

 
    keyword_content = chat_response_keyword.choices[0].message.content

    

    unbiased_content = chat_response_unbiased.choices[0].message.content

    real_keywords = keyword_content.split('.')
    
    real_keywords = [sentence.replace("\\", '') for sentence in real_keywords]

  
    json_data = {
        "formattedText": unbiased_content,
        "oldText": keyword_content,
        "keywordsText": real_keywords
    }

    # Convert JSON data to a string
    json_string = json.dumps(json_data, indent=len(real_keywords))

    sendtoCryptoServer(json_string)

# Print the response from the IPFS API
retrieveData()


