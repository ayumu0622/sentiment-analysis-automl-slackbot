import logging
import os
from dotenv import load_dotenv
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from test import get_value
from get_negative import get_min
from get_positive import get_max
from get_everything import calc_mean
from viz import create_viz
from file_upload import upload
import re

logging.basicConfig(level=logging.INFO) 
load_dotenv()

SLACK_BOT_TOKEN = os.environ["OAUTH"] 
SLACK_APP_TOKEN = os.environ["socketoken"]

app = App(token = SLACK_BOT_TOKEN)

#main_data = get_value()
main_data = {'Ayumu': [['motivation', ':wave:', ':wave:', ':wave:', ':wave:', 'hello', 'I am Ayumu', 'hello-socket-mode', 
'/ hello-socket-mode', 'hello-socket-mode', '/ hello-socket-mode', '/ hello-socket-mode', 'hello', 'motivation', 'ji', 'hello', 'okay sure', 'ok sure', 
'that is a good idea', 'this is so boring job', 'this task is not difficult to do I guess', "I don't like this job."], [0.699999988079071, 0.20000000298023224, 
0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.10000000149011612, 0.0, 0.0, 0.0, 0.0, 0.0, 0.20000000298023224, 0.699999988079071, 
0.10000000149011612, 0.20000000298023224, 0.30000001192092896, 0.5, 0.8999999761581421, -0.8999999761581421, 0.10000000149011612, -0.8999999761581421]], 
'Emma': [['I do not want to go to that meeting because it is always boring', 'I am Emma', 'yea that was hard'], [-0.800000011920929, 0.10000000149011612, -0.30000001192092896]], 
'Bob': [['Tomorrow we have a meeting', 'I am Bob', 'It is so difficult to finish', 'I had a meeting from 6pm', 'Hello'],
 [0.0, 0.10000000149011612, -0.800000011920929, 0.0, 0.20000000298023224]], 
 'Kate': [[':star-struck:', ':smile:', 'Me tooo', 'I am Kate', 'you are fired', 'I hope I can finish this by tomorrow'], [0.0, 0.6000000238418579,
  0.699999988079071, 0.10000000149011612, -0.699999988079071, 0.20000000298023224]]}


@app.message(re.compile("(hi|hello|hey)",re.IGNORECASE))
def say_hello(message,say):
  say("Hello CEO :smile:")

@app.message(re.compile("(motivation|atmosphere)",re.IGNORECASE))
def say_hello(message, say):
  say("Okay sure!")
  say("choose from below option :smile:")
  say("1.everyone")
  say("2.the most positive sentence")
  say("3.the most negative sentence")
  for num, name in enumerate(main_data.keys()):
    say(f"{num+4}.{name}")

#notcasesensitive + number
@app.message(re.compile("(positive)",re.IGNORECASE))
def answer1(message,say):
  say(get_max(main_data))


@app.message(re.compile("(negative)",re.IGNORECASE))
def answer2(message,say):
  say(get_min(main_data))

@app.message(re.compile("(everyone)",re.IGNORECASE))
def answer3(message,say):
  data = calc_mean(main_data)
  create_viz(data)
  upload()


@app.message("")
def answer4(message,say):
  if message["text"] in list(main_data.keys()):
    lista = main_data[message["text"]]
    for sentence, score in zip(lista[0],lista[1]):
      say(f"{sentence}:{score}")
  else:
    say("Try again")



if __name__ == "__main__":
    handler = SocketModeHandler(app, SLACK_APP_TOKEN)
    handler.start()



