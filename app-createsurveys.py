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
      
    #   for item in data["SurveyElements"]:
    #     if (item["PrimaryAttribute"] == "QID16"):
    #         if (item["SecondaryAttribute"]):
    #             t = item["SecondaryAttribute"].split('\xa0')
    #             item["SecondaryAttribute"] = t[0] + " " + "New Title"
                # item["Payload"]["QuestionText"] = "New short_project_description"
                # item["Payload"]["QuestionText_Unsafe"] = "New short_project_description"

      project_title = "project_title"
      
      data = {
            "QuestionText": "Please look at the image below and read the following text. Then answer the questions.<br /> " + project_title,
            "DataExportTag": "Q1",
            "QuestionType": "Matrix",
            "Selector": "Likert",
            "SubSelector": "SingleAnswer",
            "Configuration": {
                "QuestionDescriptionOption": "UseText",
                "TextPosition": "inline",
                "ChoiceColumnWidth": 25,
                "RepeatHeaders": "all",
                "WhiteSpace": "OFF",
                "MobileFirst": True
            },
            "QuestionDescription": "Please look at the image below and read the following text. Then answer the questions.\r\n " + project_title,
            "Choices": {
                "1": {
                "Display": "The person (people) presented in the image is in the need of a donation"
                },
                "2": {
                "Display": "There will be serious consequences if people don't donate to this situation"
                },
                    "3": {
            "Display": "The person (people) presented in the image is responsible for this situation"
          },
          "4": {
            "Display": "The person (people) presented in the image could have controlled or prevented this situation"
          },
          "5": {
            "Display": "The welfare of the person (people) in the image will be improved after receiving a donation"
          },
          "6": {
            "Display": "You feel obligated to make a donation to the person (people) presented in the image"
          },
          "7": {
            "Display": "You support donating to this situation to be fair"
          },
          "8": {
            "Display": "You support donating to this situation to be just"
          },
          "9": {
            "Display": "This situation is presented in a unique way"
          },
          "10": {
            "Display": "This situation is presented in a novel way"
          },
          "11": {
            "Display": "You feel sympathetic with the person (people) presented in the image"
          },
          "12": {
            "Display": "This situation is a rare one"
          },
          "13": {
            "Display": "You feel concerned about the person (people) presented in the image"
          },
          "14": {
            "Display": "You feel compassionate about the person (people) presented in the image"
          },
          "15": {
            "Display": "You feel softhearted by the person (people) presented in the image"
          },
          "17": {
            "Display": "Looking at the person (people) presented in the image made you feel happy"
          },
          "18": {
            "Display": "Looking at the person (people) presented in the image made you feel sad"
          },
          "19": {
            "Display": "Looking at the person (people) presented in the image made you feel angry"
          },
          "20": {
            "Display": "Looking at the person (people) presented in the image made you feel shocked"
          },
          "21": {
            "Display": "Looking at the person (people) presented in the image made you feel guilty"
          },
          "22": {
            "Display": "Looking at the person (people) presented in the image made you feel ashamed"
          },
          "24": {
            "Display": "You feel empathy for the person (people) presented in the image"
          },
          "25": {
            "Display": "You are willing to donate to the person (people) presented in the image if you are hypothetically asked to"
          },
          "28": {
            "Display": "Looking at the person (people) presented in the image made you feel shocked"
          },
          "29": {
            "Display": "Looking at the person (people) presented in the image made you feel surprised"
          },
          "30": {
            "Display": "This situation is presented in a cool way"
          },
          "31": {
            "Display": "The person (people) presented in the image could be you some day"
          },
          "33": {
            "Display": "This situation's need for financial support from donors will be even greater in the future"
          },
          "34": {
            "Display": "The person (people) presented in the image deserves a donation"
          }
            },
         "ChoiceOrder": [
          "1",
          "2",
          "33",
          "34",
          "3",
          "4",
          "5",
          "6",
          "7",
          "8",
          "9",
          "10",
          "12",
          "11",
          "24",
          "13",
          "14",
          "15",
          "17",
          "18",
          "19",
          "20",
          "21",
          "22",
          "28",
          "29",
          "30",
          "31",
          "25"
        ],
        "Validation": {
          "Settings": {
            "ForceResponse": "OFF",
            "ForceResponseType": "ON",
            "Type": "None"
          }
        },
            "GradingData": [],
        "Language": [],
        "NextChoiceId": 36,
        "NextAnswerId": 9,
        "Answers": {
          "1": {
            "Display": "Strongly Disagree"
          },
          "2": {
            "Display": "Disagree"
          },
          "3": {
            "Display": "Somewhat Disagree"
          },
          "4": {
            "Display": "Neither Agree or Disagree"
          },
          "5": {
            "Display": "Somewhat Agree"
          },
          "6": {
            "Display": "Agree"
          },
          "7": {
            "Display": "Strongly Agree"
          }
        },
        "AnswerOrder": [
          "1",
          "2",
          "3",
          "4",
          "5",
          "6",
          "7"
        ],
        "ChoiceDataExportTags": False,
        "QuestionID": "QID16",
        "DataVisibility": {
          "Private": False,
          "Hidden": False
        },
        }
      return data
    
  
    
  
   # return json.dumps(data)

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
    
        
        
        
    
