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
emp = ["Bob","Emma","Kate","Ayumu"]
emp.append("Everyone")

@app.message("Hello")
def say_hello(message, say):
  say("Hello PM")

@app.message("I want to know mode")
def say_hello(message, say):
  say("who do you wanna see?")
  say("choose from below option and put name")
  for num,i in enumerate(emp):
    text = f"{num+1}.{i}"
    say(text)


if __name__ == "__main__":
    handler = SocketModeHandler(app, SLACK_APP_TOKEN)
    handler.start()



