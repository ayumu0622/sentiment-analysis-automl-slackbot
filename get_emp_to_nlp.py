def get_users():
    import os
    import logging
    from dotenv import load_dotenv
    import slack
    import aiohttp
    from slack_sdk.errors import SlackApiError
    logging.basicConfig(level=logging.INFO) 
    load_dotenv()
    logger = logging.getLogger()
    SLACK_BOT_TOKEN = os.environ["OAUTH"] 
    SLACK_APP_TOKEN = os.environ["socketoken"]

    client = slack.WebClient(token=SLACK_BOT_TOKEN)

    users_store = {}


    # Put users into the dict
    def save_users(users_array):
        for user in users_array:
            # Key user info on their unique user ID
            user_id = user["id"]
            # Store the entire user object (you may not need all of the info)
            users_store[user_id] = user
    try:
        # Call the users.list method using the WebClient
        # users.list requires the users:read scope
        result = client.users_list()
        save_users(result["members"])

    except SlackApiError as e:
        logger.error("Error creating conversation: {}".format(e))
    #retrieve only name and id
    dict = {}
    for x in users_store:
        if (users_store[x]["is_bot"] != True) and (users_store[x]["name"] != "slackbot"):
            dict[users_store[x]["real_name"]] = users_store[x]["id"]

    return dict

def get_channels():
    import os
    import logging
    from dotenv import load_dotenv
    import slack
    from slack_sdk.errors import SlackApiError
    logging.basicConfig(level=logging.INFO) 
    load_dotenv()
    logger = logging.getLogger()

    SLACK_BOT_TOKEN = os.environ["OAUTH"] 
    SLACK_APP_TOKEN = os.environ["socketoken"]



    client = slack.WebClient(token=SLACK_BOT_TOKEN)
    conversations_store = {}

    def fetch_conversations():
        try:
            # Call the conversations.list method using the WebClient
            result = client.conversations_list()
            save_conversations(result["channels"])

        except SlackApiError as e:
            logger.error("Error fetching conversations: {}".format(e))


    # Put conversations into the JavaScript object
    def save_conversations(conversations):
        conversation_id = ""
        for conversation in conversations:
            # Key conversation info on its unique ID
            conversation_id = conversation["id"]

            # Store the entire conversation object
            # (you may not need all of the info)
            conversations_store[conversation_id] = conversation

    fetch_conversations()
    dict = {}
    list=[]
    for x in conversations_store:
        list.append(conversations_store[x]["id"]) 
    return list 

channel_list = get_channels()
employee_dict = get_users()

def get_conversation(channel_list, employee_dict):
    import os
    import logging
    from dotenv import load_dotenv
    import slack
    import re

    #channel_list = ['C03QQDD1LBY', 'C03QX00A343', 'C03RLPRAERW', 'C03RZ5YRA15']
    #employee_dict = {'Ayumu': 'U03R9LQUVT3', 'Emma': 'U03SCBETEN9', 'Bob': 'U03T5137UQ0', 'Kate': 'U03T52DQQ64'}
    logging.basicConfig(level=logging.INFO) 
    load_dotenv()

    SLACK_BOT_TOKEN = os.environ["OAUTH"] 
    SLACK_APP_TOKEN = os.environ["socketoken"]

    client = slack.WebClient(token=SLACK_BOT_TOKEN)
    # Store conversation history
    conversation_history = []
    dict = {}
    for user_name, user_id in employee_dict.items():
        list = []
        for channel_id in channel_list:
          result = client.conversations_history(channel=channel_id)
          conversation_history = result["messages"]
          for message in conversation_history:
            if message["user"] == user_id:
              if not (("has joined the channel" in message["text"]) or ("@" in message["text"])):
                list.append(message["text"]) 
        dict[user_name] = list

    return dict

input = get_conversation(channel_list, employee_dict)

# Imports the Google Cloud client library
def text_score(input):
    from google.cloud import language_v1
    #import os
    from dotenv import load_dotenv
    load_dotenv()
    #GOOGLE_APPLICATION_CREDENTIALS = os.environ["GOOGLE_APPLICATION_CREDENTIALS"] 

    # Instantiates a client
    client = language_v1.LanguageServiceClient()
    new_dict = {}
    for employee, list in input.items():
        new_list = []
        another_list = []
        for text in list:
          document = language_v1.Document(content=text, type_=language_v1.Document.Type.PLAIN_TEXT)
          sentiment = client.analyze_sentiment(request={"document": document}).document_sentiment
          another_list.append(sentiment.score)
        new_list.append(list)
        new_list.append(another_list)
        new_dict[employee] = new_list

    return new_dict

print(text_score(input))

