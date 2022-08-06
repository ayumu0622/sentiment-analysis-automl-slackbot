# Imports the Google Cloud client library
from google.cloud import language_v1
import os
from dotenv import load_dotenv
load_dotenv()
#GOOGLE_APPLICATION_CREDENTIALS = os.environ["GOOGLE_APPLICATION_CREDENTIALS"] 
dict = {'Ayumu': ['motivation', ':wave:', ':wave:', ':wave:', ':wave:', 'hello', 'I am Ayumu', 'hello-socket-mode', '/ hello-socket-mode', 'hello-socket-mode', '/ hello-socket-mode', 
'/ hello-socket-mode', 'hello', 'motivation', 'ji', 'hello', 'okay sure', 'ok sure', 'that is a good idea', 'this is so boring job', 
'this task is not difficult to do I guess', "I don't like this job."], 'Emma': ['I do not want to go to that meeting because it is always boring', 'I am Emma', 
'yea that was hard'], 'Bob': ['Tomorrow we have a meeting', 'I am Bob', 'It is so difficult to finish', 'I had a meeting from 6pm', 'Hello'], 
'Kate': [':star-struck:', ':smile:', 'Me tooo', 'I am Kate', 'you are fired', 'I hope I can finish this by tomorrow']}
# Instantiates a client
client = language_v1.LanguageServiceClient()
"""
# The text to analyze
text = "fsjofsjofjsofjso"
document = language_v1.Document(
content=text, type_=language_v1.Document.Type.PLAIN_TEXT
)

# Detects the sentiment of the text
sentiment = client.analyze_sentiment(
request={"document": document}
).document_sentiment

print("Text: {}".format(text))
print("Sentiment: {}, {}".format(sentiment.score, sentiment.magnitude))
"""
new_dict = {}
for employee, list in dict.items():
    new_list = []
    another_list = []
    for text in list:
       document = language_v1.Document(
       content=text, type_=language_v1.Document.Type.PLAIN_TEXT)
       sentiment = client.analyze_sentiment(
       request={"document": document}
       ).document_sentiment
       another_list.append(sentiment.score)
    new_list.append(list)
    new_list.append(another_list)
    new_dict[employee] = new_list

print(new_dict)
       




