import pandas as pd

#change this url to the url of the AI server then the dataset server
url = 'http://192.168.1.100:8000/api/v1/data/alzheimers_prediction_dataset.csv'



#url = http://192.168.1.100:8000/api/v1/data/alzheimers_prediction_dataset.csv

df = pd.read_csv('C:/Users/dstephens/Downloads/alzheimers_prediction_dataset.csv')


import csv
reader = csv.reader(open('C:/Users/dstephens/Downloads/CountryCodes.csv','r'))
d = {}
for row in reader: 
    k,v = row
    d[k] = v






# Define mapping functions
def map_gender(x):
    return {'Male': 0, 'Female': 1}[x]

def map_activity(x):
    return {'Low': 0, 'Medium': 1, 'High': 2}[x]

def map_smoking(x):
    return {'Never': 0, 'Former': 1, 'Current': 2}[x]

def map_alcohol(x):
    return {'Never': 0, 'Occasionally': 1, 'Regularly': 2}[x]

def map_binary(x):
    return {'No': 0, 'Yes': 1}[x]

def map_levels(x):
    return {'Low': 0, 'Medium': 1, 'High': 2}[x]

def map_dietary(x):
    return {'Healthy': 0, 'Average': 1, 'Unhealthy': 2}[x]

def map_employment(x):
    return {'Unemployed': 0, 'Employed': 1, 'Retired': 2}[x]

def map_marital(x):
    return {'Single': 0, 'Married': 1, 'Widowed': 2}[x]

def map_urban_rural(x):
    return {'Urban': 0, 'Rural': 1}[x]

# Apply the mapping functions
df['Country'] = df['Country'].apply(lambda x: d[x])
df['Gender'] = df['Gender'].apply(map_gender)
df['Physical Activity Level'] = df['Physical Activity Level'].apply(map_activity)
df['Smoking Status'] = df['Smoking Status'].apply(map_smoking)
df['Alcohol Consumption'] = df['Alcohol Consumption'].apply(map_alcohol)
df['Diabetes'] = df['Diabetes'].apply(map_binary)
df['Hypertension'] = df['Hypertension'].apply(map_binary)
df['Cholesterol Level'] = df['Cholesterol Level'].apply(lambda x: 0 if x == 'Normal' else 1)
df['Family History of A'] = df['Family History of A'].apply(map_binary)
df['Depression Level'] = df['Depression Level'].apply(map_levels)
df['Sleep Quality'] = df['Sleep Quality'].apply(map_levels)
df['Dietary Habits'] = df['Dietary Habits'].apply(map_dietary)
df['Air Pollution Exposure'] = df['Air Pollution Exposure'].apply(map_levels)
df['Employment Status'] = df['Employment Status'].apply(map_employment)
df['Marital Status'] = df['Marital Status'].apply(map_marital)
df['Genetic Risk Factor'] = df['Genetic Risk Factor'].apply(map_binary)
df['Social Engagement Level'] = df['Social Engagement Level'].apply(map_levels)
df['Income Level'] = df['Income Level'].apply(map_levels)
df['Stress Level'] = df['Stress Level'].apply(map_levels)
df['Urban vs Rural Living'] = df['Urban vs Rural Living'].apply(map_urban_rural)
df['Alzheimers Diagnosis'] = df['Alzheimers Diagnosis'].apply(map_binary)



"""
#map the country codes to the country names
df['Country'] = df['Country'].map(d)

#map gender to 1 and 0
df['Gender'] = df['Gender'].map({'Male':0,'Female':1})

#map physical activity level to 0 1 and 2
df['Physical Activity Level'] = df['Physical Activity Level'].map({'Low':0,'Medium':2,'High':3})

#map smoking status to 0, 1, and 2
df['Smoking Status'] = df['Smoking Status'].map({'Never':0,'Former':1, 'Current':2})

#map alcohol consumption to 0, 1, and 2
df['Alcohol Consumption'] = df['Alcohol Consumption'].map({'Never':0,'Occasionally':1, 'Regularly':2})

#map diabetes
df['Diabetes'] = df['Diabetes'].map({'No':0,'Yes':1})

#map hypertension
df['Hypertension'] = df['Hypertension'].map({'No':0,'Yes':1})

#map Cholesterol Level
df['Cholesterol Level'] = df['Cholesterol Level'].map({'Normal':0,'High':1})

#map family history of Alzheimers
df['Family History of A'] = df['Family History of A'].map({'No':0,'Yes':1})

#map depression level 1 2 and 3
df['Depression Level'] = df['Depression Level'].map({'Low':0,'Medium':2,'High':3})

#map sleep quality 1 2 and 3
df['Sleep Quality'] = df['Sleep Quality'].map({'Low':0,'Medium':2,'High':3})

#map dietery habits 1 2 and 3
df['Dietary Habits'] = df['Dietary Habits'].map({'Healthy':0,'Average':1, 'Unhealthy':2})

#map air polution exposure 1 3 and 3
df['Air Pollution Exposure'] = df['Air Pollution Exposure'].map({'Low':0,'Medium':2,'High':3})

#map employment status 1 2 and 3
df['Employment Status'] = df['Employment Status'].map({'Unemployed':0,'Employed':1, 'Retired':2})

#map marital status 1 2 and 3
df['Marital Status'] = df['Marital Status'].map({'Single':0,'Married':1, 'Widowed':2})

#map genetic risk factor 1 and 2
df['Genetic Risk Factor'] = df['Genetic Risk Factor'].map({'No':0,'Yes':1})

#map Scoial engagement level 1 2 and 3
df['Social Engagement Level'] = df['Social Engagement Level'].map({'Low':0,'Medium':2,'High':3})

#map Income level 1 2 and 3
df['Income Level'] = df['Income Level'].map({'Low':0,'Medium':2,'High':3})

#map stress level 1 2 and 3
df['Stress Level'] = df['Stress Level'].map({'Low':0,'Medium':2,'High':3})

#map urban vs rural living
df['Urban vs Rural Living'] = df['Urban vs Rural Living'].map({'Urban':0,'Rural':1})

#map alzheimers Diagnosis
df['Alzheimers Diagnosis'] = df['Alzheimers Diagnosis'].map({'No':0,'Yes':1})



print(df.head())
print(df.info())



#save numerical data to a new csv file
df.to_csv('C:/Users/dstephens/Downloads/alzheimers_prediction_dataset_numerical.csv', index=False)

"""