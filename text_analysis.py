# Imports the Google Cloud client library
def text_score(dict):
    from google.cloud import language_v1
    #import os
    from dotenv import load_dotenv
    load_dotenv()
    #GOOGLE_APPLICATION_CREDENTIALS = os.environ["GOOGLE_APPLICATION_CREDENTIALS"] 

    # Instantiates a client
    client = language_v1.LanguageServiceClient()
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

    return new_dict
        




