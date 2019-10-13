import json
import requests
import config
import logging

TOKEN = config.read_token_from_file()
logging.basicConfig(format='%(asctime)s %(levelname)-8s %(message)s', level=logging.INFO, datefmt='%Y-%m-%d %H:%M:%S')

def makesurveys(n):
    survey_ids = []
    headers = { "x-api-token": TOKEN }
    baseUrl = "https://{0}.qualtrics.com/API/v3/surveys".format(config.DATA_CENTER)
    for i in range(n):
        logging.info("Creating survey {0}".format(str(i+1)))
        data = { "name": "Gofundme-{0}".format(str(i+1)) }
        files = {'file': ('Gofundme-{0}.qsf'.format(str(i+1)), open('Gofundme.qsf', 'rb'), 'application/vnd.qualtrics.survey.qsf')}
        response = requests.post(baseUrl, files=files, data=data, headers=headers)
        if (response.status_code == 200):
            survey_ids.append(response.json()["result"]["id"])
        else:
            logging.error("Survey {0} NOT created.".format(str(i+1)))
            

    return survey_ids
def getparameters(survey_id):
    data = {
            "QuestionText": "Specific question for survey {0}?".format(survey_id),
            "DataExportTag": "Q2",
            "QuestionType": "MC",
            "Selector": "SAVR",
            "SubSelector": "TX",
            "Configuration": {
                "QuestionDescriptionOption": "UseText"
            },
            "QuestionDescription": "Who is your favorite character in the {0} survey?".format(survey_id),
            "Choices": {
                "1": {
                "Display": "Thomas Mann"
                },
                "2": {
                "Display": "Albert Camus"
                },
                "3": {
                "Display": "Anton Chekov"
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

def updatequestion(survey_id,question_id):
    headers = { "x-api-token": TOKEN }
    baseUrl = "https://{0}.qualtrics.com/API/v3/survey-definitions/{1}/questions/{2}".format(config.DATA_CENTER,survey_id,question_id)
    params = getparameters(survey_id)
    response = requests.put(baseUrl, json=params, headers=headers)
    
    if (response.status_code == 200):
        logging.info("Survey {0}, question {1} updated.".format(survey_id,question_id))
    else:
        logging.error("Cannot update survey {0}, question {1}.".format(survey_id,question_id))

if __name__ == "__main__":
    #survey_ids = makesurveys(3)
    #logging.info(survey_ids)
    survey_ids = ['SV_aWUIvf1dnGexG1n', 'SV_9GNpWcqsUXjTKkJ', 'SV_5utcO5DoBZLRymh']
    for survey_id in survey_ids:
        updatequestion(survey_id,"QID2")
        
        
        
    
