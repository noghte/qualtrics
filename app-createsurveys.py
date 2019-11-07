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
    data = None
    with open('Gofundme.qsf') as f:
        data = json.load(f)
    
    for item in data["SurveyElements"]:
        if (item["PrimaryAttribute"] == "QID16"):
            if (item["SecondaryAttribute"]):
                t = item["SecondaryAttribute"].split('\xa0')
                item["SecondaryAttribute"] = t[0] + " " + "New Title"
                # item["Payload"]["QuestionText"] = "New short_project_description"
                # item["Payload"]["QuestionText_Unsafe"] = "New short_project_description"
    
  
    return json.dumps(data)

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
    print(30 * '-')
    print("1. Create Surveys")
    print("2. Update Questions")
    print("3. Exit")
    print(30 * '-')
    #survey_ids = makesurveys(3)
    #logging.info(survey_ids)
    choice = input('Enter your choice [1-3] : ')
    if int(choice) == 1:
        n = int(input("How many survys?"))
        survey_ids = makesurveys(n)
        with open('surveyids.json', 'w') as f:
            json.dump(survey_ids,f)
        print("Done!")
    elif int(choice) == 2:
        print ("Updating questions...")
        survey_ids = []
        with open('surveyids.json') as f:
            survey_ids = json.load(f)
            
        for survey_id in survey_ids:
            updatequestion(survey_id,"QID16")
        print("Done!")
    else:
        print ("Good bye!")
    
        
        
        
    
