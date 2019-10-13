import json
import requests
import config

TOKEN = config.read_token_from_file()

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

def getparameters():
    # data to be sent to api 
    data = {
            "QuestionText": "What is your favorite book?",
            "DataExportTag": "Q2",
            "QuestionType": "MC",
            "Selector": "SAVR",
            "SubSelector": "TX",
            "Configuration": {
                "QuestionDescriptionOption": "UseText"
            },
            "QuestionDescription": "What is your favorite book?",
            "Choices": {
                "1": {
                    "Display": "Choice created using Survey API!"
                },
                "2": {
                    "Display": "harry potter"
                },
                "3": {
                    "Display": "james bond"
                }
            },
            "ChoiceOrder": [
                "1",
                "2",
                "3"
            ],
            "Validation": {
                "Settings": {
                    "ForceResponse": "OFF",
                    "ForceResponseType": "ON",
                    "Type": "None"
                }
            },
            "Language": []
        }
    
    return data
if __name__ == "__main__":
    params = getparameters()
    headers = {
        "x-api-token": TOKEN,
        "Content-Type": "application/json"
    }
    #"https://terry.qualtrics.com/API/v3/survey-definitions/{TOKEN}/questions"
    baseUrl = "https://{0}.qualtrics.com/API/v3/survey-definitions/{1}/questions".format(config.DATA_CENTER, config.SURVEY_ID)
    response = requests.post(baseUrl, json=params, headers=headers)
    jprint(response.json())