import os
from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage
import json

model = "mistral-tiny"

client = MistralClient(api_key="0w3q8F4BCcpsHmEpjsBzrZ8NfjVTVeSD")

def retrieveData():
    totaltext = """
    The United Nations agency for Palestinian refugees (UNRWA) said on Friday it had opened an investigation into several employees suspected of involvement in the Oct. 7 attacks in Israel by Hamas-led militants and that it had severed ties with those staff members.

    "The Israeli authorities have provided UNRWA with information about the alleged involvement of several UNRWA employees in the horrific attacks on Israel on Oct. 7," said Philippe Lazzarini, UNRWA commissioner general.

    "To protect the agency's ability to deliver humanitarian assistance, I have taken the decision to immediately terminate the contracts of these staff members and launch an investigation in order to establish the truth without delay."
    """

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

    # Print the JSON string
    print(json_string)

retrieveData()
