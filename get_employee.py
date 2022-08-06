def get_user():
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