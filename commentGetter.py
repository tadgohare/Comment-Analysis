# Import the necessary libraries
import requests
import json

# Define the Instagram API URL

instagram_api_url = "https://api.instagram.com/{}/?__a=1"

# Define a function to get the comments of a given user
def get_comments(username):
  # Fetch the user data from the Instagram API
  response = requests.get(instagram_api_url.format(username))
  print(response.text)
  # Parse the response as JSON
  if response != None:
    user_data = json.loads(response.text)

    # Get the list of comments from the user's posts
    comments = [comment["text"] for post in user_data["user"]["media"]["nodes"] for comment in post["comments"]["nodes"]]

    # Return the comments as an array
    return comments
  else:
    return "None"


# Prompt the user for a username
username = input("Enter the username: ")

# Get the comments for the user
comments = get_comments(username)

# Print the comments
print(comments)
