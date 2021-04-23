import os
import dialogflow
from google.api_core.exceptions import InvalidArgument

# if __name__ == "__main__":
#     import env.env as env
# else:
#     import src.speaker.env.env as env
import os
os.chdir(os.path.dirname(os.path.abspath( __file__ )))

from .env import *

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = CREDENTIALS

DIALOGFLOW_PROJECT_ID = DIALOGFLOW_PROJECT_ID
DIALOGFLOW_LANGUAGE_CODE = 'ko'
SESSION_ID = 'me'

session_client = dialogflow.SessionsClient()
session = session_client.session_path(DIALOGFLOW_PROJECT_ID, SESSION_ID)

def meal(text_to_be_analyzed):
    text_input = dialogflow.types.TextInput(text=text_to_be_analyzed, language_code=DIALOGFLOW_LANGUAGE_CODE)
    query_input = dialogflow.types.QueryInput(text=text_input)
    try:
        response = session_client.detect_intent(session=session, query_input=query_input)
    except InvalidArgument:
        raise

    res=response.query_result.parameters.fields

    meal_time=res['meal-time'].string_value

    date=res['date'].string_value
    date=date[:date.find('T')].replace('-','')

    return date, meal_time

def schedule(text_to_be_analyzed):
    text_input = dialogflow.types.TextInput(text=text_to_be_analyzed, language_code=DIALOGFLOW_LANGUAGE_CODE)
    query_input = dialogflow.types.QueryInput(text=text_input)
    try:
        response = session_client.detect_intent(session=session, query_input=query_input)
    except InvalidArgument:
        raise

    res=response.query_result.parameters.fields

    date=res['date'].string_value
    date=date[:date.find('T')].replace('-','')

    grade=res['grade'].string_value

    number=str(int(res['number'].number_value))
    
    return date, grade, number

if __name__ == '__main__':
    date, meal_time=meal('저번주 월요일 점심 급식')
    print(date, meal_time)
    date, grade, number=schedule('저번수 수요일 2학년 4반 시간표')
    print(date, grade, number)