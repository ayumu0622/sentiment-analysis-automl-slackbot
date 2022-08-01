import logging
import os
from dotenv import load_dotenv
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

logging.basicConfig(level=logging.INFO) 
load_dotenv()

SLACK_BOT_TOKEN = os.environ["OAUTH"] 
SLACK_APP_TOKEN = os.environ["socketoken"]

app = App(token = SLACK_BOT_TOKEN)

@app.event("app_mention")
def mention_handler(body, context, payload, options, say, event):
  say("Hello World!")

@app.event("message")
def message_handler(body, context, payload, options, say, event):
  print("hey")
  pass


if __name__ == "__main__":
    handler = SocketModeHandler(app, SLACK_APP_TOKEN)
    handler.start()



