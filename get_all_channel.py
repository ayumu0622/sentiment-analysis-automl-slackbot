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