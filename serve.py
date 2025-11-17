import requests

url = 'http://localhost:9696/predict'

person = {"age": 31,
    "businesstravel": "travel_rarely",
    "dailyrate": 1325,
    "distancefromhome": 11,
    "educationfield": "life sciences",
    "employeenumber": 813,
    "environmentsatisfaction": "very high",
    "hourlyrate": 82,
    "jobinvolvement": "high",
    "joblevel": "middle",
    "jobrole": "laboratory technician",
    "jobsatisfaction": "high",
    "maritalstatus": "single",
    "monthlyincome": 3149,
    "monthlyrate": 15003,
    "numcompaniesworked": 8,
    "overtime": "no",
    "percentsalaryhike": 20,
    "stockoptionlevel": "eligible l1",
    "totalworkingyears": 11,
    "trainingtimeslastyear": 2,
    "worklifebalance": "better",
    "yearsatcompany": 5,
    "yearsincurrentrole": 2,
    "yearssincelastpromotion": 5,
    "yearswithcurrmanager": 3}

response = requests.post(url, json = person)
attrition = response.json() 

print('Response', attrition)

if attrition['attrition'] >= 0.5:
    print('Reach out to an employee')
else:
    print('Chill')