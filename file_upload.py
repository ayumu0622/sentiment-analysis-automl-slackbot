def upload():
  
  import os
  from dotenv import load_dotenv
  import slack
  import logging
  logging.basicConfig(level=logging.INFO) 
  load_dotenv()

  SLACK_BOT_TOKEN = os.environ["OAUTH"] 
  SLACK_APP_TOKEN = os.environ["socketoken"]

  client = slack.WebClient(token=SLACK_BOT_TOKEN)
  # The name of the file you're going to upload
  file_name = r"./output.png"
 
  # Create and configure logger

 
  # Creating an object
  logger = logging.getLogger()
  # ID of channel that you want to upload file to
  channel_id = "D03QH31K8CX"
  result = client.files_upload(
        channels=channel_id,
        initial_comment="Here it is :smile:",
        file=file_name,
    )
