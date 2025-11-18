# Attrition Prediction Machine Learning project

##  Problem statement
Attrition in the workplace refers to the gradual reduction in the workforce due to employees leaving an organization voluntarily (e.g., resignation, retirement) or involuntarily (e.g., dismissal, layoffs) without being immediately replaced.

Predicting attrition is crucial for organizations as it allows them to proactively address workforce challenges, maintain operational efficiency, and reduce costs associated with employee departures. A high attrition rate can lead to disruptions in productivity, increased recruitment expenses, and loss of institutional knowledge.

## Dataset description
The dataset used is IBM HR Analytics Employee Attrition & Performance dataset from 
https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset

## EDA Summary
Upon exploratory analysis several attributes ('employeecount', 'standardhours', 'department', 'relationshipsatisfaction', 'education', 'gender', 'performancerating','over18') were removed from training the model as they could barely explain the target vatiable as measures by correlation and mutual information. Exploratory analysis revealed no outliers.

## Modeling approach

The following models were used to train the model with the ROC_AUC scores on the test data:


| Model                  | ROC_AUC    |
| -----------------------| -----------|
| LogisticRegression     | 0.71       |
| DecisionTreeClassifier | 0.67       |
| RandomForestClassifier | 0.82       |

The hyperparameters in the models were tuned to achieve the highest ROC_AUC score. As a result Random Forest with max depth of 10 and min samples leaf of 1 is chosen to train the final model.

## How to run the model

To run the model locally, execute the following code in the terminal:

```uv run python predict.py```

You can then test the Webservice either by going to http://localhost:9696/docs or executing the following curl command:

``curl -X 'POST' \
  'http://localhost:9696/predict' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "age": 36,
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
  "maritalstatus": "married",
  "monthlyincome": 3149,
  "monthlyrate": 21821,
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
  "yearswithcurrmanager": 3
}'``

To run the app via Docker, execute:

``docker build -t attrition-prediction .
docker run -it --rm -p 9696:9696 attrition-prediction``

And similarly test the Webservice either by going to http://localhost:9696/docs or executing the following curl command:

```curl -X 'POST' \
  'http://localhost:9696/predict' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{"age": 21,
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
    "yearswithcurrmanager": 3}'```


## Next steps

Next steps for this project would be to obviously deploy it to Cloud.