import openai
import os
from dotenv import load_dotenv
import json

#CONSTANTS
FILEPATH = "Data/yourcommentsfilename.json"
TEMPERATURE = 1
MODEL = "text-davinci-003"
MAX_TOKENS = 2499

#main control flow of program
def main():
    config()
    data = loadData()
    firstComments = getFirstPrompt(data)
    lastComments = getLastPrompt(data)
    print(f"Based on your first comments, the ai says this about your personality:\n{firstComments}")
    print(f"\n\n\nBased on your last comments, the ai says this about your personality:\n{lastComments}")

#config for program
def config():
    load_dotenv()
    openai.api_key = os.getenv("OPENAI_API_KEY")

#loads in JSON data and returns array of comment objects
def loadData():
    with open(FILEPATH) as json_file:
        json_data = json_file.read()
        data = json.loads(json_data)
        return data["comments_media_comments"]

#gets the first 45 comments you have posted
def getFirstPrompt(data):
    promptuser1 = "what can you say about a person based on their last few social media comments shown bellow:\n"
    for i in range(0,45):
        promptuser1 += f"`{data[i]['string_map_data']['Comment']['value']}`\n"
    response1 = openai.Completion.create(model=MODEL, prompt=promptuser1, temperature=TEMPERATURE, max_tokens=MAX_TOKENS)
    return response1['choices'][0]['text']

#gets the last 45 comments you have posted
def getLastPrompt(data):
    promptuser2 = "what can you say about a person based on their last few social media comments shown bellow:\n"
    for i in range(len(data)-1,len(data)-45,-1):
        promptuser2 += f"`{data[i]['string_map_data']['Comment']['value']}`\n"
    response2 = openai.Completion.create(model=MODEL, prompt=promptuser2, temperature=TEMPERATURE, max_tokens=MAX_TOKENS)
    return response2['choices'][0]['text']

if __name__ == '__main__':
    main()