
import pandas as pd
import wget
import pickle

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import DictVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import make_pipeline

#Loading the file

url =  'https://raw.githubusercontent.com/Veranika23/attrition-prediction/refs/heads/main/WA_Fn-UseC_-HR-Employee-Attrition.csv'
downloaded_file = wget.download(url)
df = pd.read_csv(downloaded_file)

#Data preparation

df.columns = df.columns.str.lower().str.replace(' ', '_')
education_values = {
    1: 'Below College',
    2: 'College',
    3: 'Bachelor',
    4: 'Master',
    5: 'Doctor'
}
df.education = df.education.map(education_values)

environment_values = {
    1: 'Low',
    2: 'Medium',
    3: 'High',
    4: 'Very High'
}
df.environmentsatisfaction = df.environmentsatisfaction.map(environment_values)

involvement_values = {
    1: 'Low',
    2: 'Medium',
    3: 'High',
    4: 'Very High'
}
df.jobinvolvement = df.jobinvolvement.map(involvement_values)

job_level_values = {
    1: 'Junior',
    2: 'Middle',
    3: 'Senior',
    4: 'Lead',
    4: 'Manager'
}
df.joblevel = df.joblevel.map(job_level_values)

jobsatisfaction_values = {
    1: 'Low',
    2: 'Medium',
    3: 'High',
    4: 'Very High'
}
df.jobsatisfaction = df.jobsatisfaction.map(jobsatisfaction_values) 

performance_values = {
    1: 'Low',
    2: 'Good',
    3: 'Excellent',
    4: 'Outstanding'
}
df.performancerating = df.performancerating.map(performance_values)

relationshipsatisfaction_values = {
    1: 'Low',
    2: 'Medium',
    3: 'High',
    4: 'Very High'
}
df.relationshipsatisfaction = df.relationshipsatisfaction.map(relationshipsatisfaction_values)

stockoption_values = {
    0: 'Not Eligible',
    1: 'Eligible L1',
    2: 'Eligible L2',
    3: 'Eligible L3'
}
df.stockoptionlevel = df.stockoptionlevel.map(stockoption_values)

worklifebalance_values = {
    1: 'Bad',
    2: 'Good',
    3: 'Better',
    4: 'Best'
}
df.worklifebalance = df.worklifebalance.map(worklifebalance_values)

attrition_values = {
    'Yes': 1,
    'No': 0
}
df.attrition = df.attrition.map(attrition_values)

categorical_columns = list(df.dtypes[df.dtypes == 'object'].index)
for c in categorical_columns:
    df[c] = df[c].replace("_", " ").str.lower()

numerical_columns = list(df.dtypes[df.dtypes == 'int64'].index)
df[categorical_columns] = df[categorical_columns].fillna('NA')

del df['employeecount']
del df['standardhours']
numerical_columns = list(df.dtypes[df.dtypes == 'int64'].index)

del df['department']
del df['relationshipsatisfaction']
del df['education']
del df['gender']
del df['performancerating']
del df['over18']
categorical_columns = list(df.dtypes[df.dtypes == 'object'].index)

#Random Forest model

df_full_train, df_test = train_test_split(df, test_size=0.2, random_state=1)

df_full_train = df_full_train.reset_index(drop=True)

y_full_train = df_full_train.attrition.values

del df_full_train['attrition']

full_train_dicts = df_full_train.to_dict(orient='records')

pipeline = make_pipeline(DictVectorizer(), RandomForestClassifier(n_estimators=60,
                            max_depth=10,
                            min_samples_leaf=1,
                            random_state=1))



pipeline.fit(full_train_dicts, y_full_train)

with open('model.bin', 'wb') as f_out: 
    pickle.dump(pipeline, f_out)

