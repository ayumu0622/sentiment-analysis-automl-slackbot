def get_conversation():
    import os
    import logging
    from dotenv import load_dotenv
    import slack
    import re

    channel_list = ['C03QQDD1LBY', 'C03QX00A343', 'C03RLPRAERW', 'C03RZ5YRA15']
    employee_dict = {'Ayumu': 'U03R9LQUVT3', 'Emma': 'U03SCBETEN9', 'Bob': 'U03T5137UQ0', 'Kate': 'U03T52DQQ64'}
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
                print(user_name,message["text"])
                list.append(message["text"]) 
        dict[user_name] = list

    return dict

print(get_conversation())
        # Print results
        #logger.info("{} messages found in {}".format(len(conversation_history), id))

    #except SlackApiError as e:
        #logger.error("Error creating conversation: {}".format(e))
