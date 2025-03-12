import pandas as pd 

df = pd.read_csv('C:/Users/dstephens/Downloads/mba_decision_dataset.csv')

def map_yes_no(x):
    return {'Yes': 1, 'No': 0}[x]
def map_gender(x):
    return {'Male': 0, 'Female': 1, 'Other': 2}[x]
def mapUndergraduateMajor(x):
    return {'Arts': 0, 'Business': 1, 'Engineering': 2, 'Science': 3, 'Economics': 4}[x]
def map_CurrentJobTitle(x):
    return {'Analyst': 0, 'Manager': 1, 'Other': 2, 'Entrepreneur': 3, 'Consultant': 4, 'Engineer':5}[x]
def map_MBAfunding(x):
    return {'Loan': 0, 'Scholarship': 1, 'Self-funded': 2, 'Employer': 3}[x]
def map_disiredpostmbarole(x):
    return {'Executive': 0, 'Finance Manager': 1, 'Startup Founder': 2, 'Entrepreneur': 3, 'Consultant': 4, 'Marketing Director': 5}[x]
def map_LocationPreference(x):
    return {'International': 0, 'Domestic': 1}[x]
def map_onlineOncampus(x):
    return {'Online': 0, 'On-Campus': 1}[x]
def map_MBA_Reason(x):
    return {'Career Growth': 0, 'Skill Enhancement': 1, 'Networking': 2, 'Entrepreneurship':3}[x]


df['Gender'] = df['Gender'].map(map_gender)
df['UndergraduateMajor'] = df['UndergraduateMajor'].map(mapUndergraduateMajor)
df['CurrentJobTitle'] = df['CurrentJobTitle'].map(map_CurrentJobTitle)
df['HasManagementExperience'] = df['HasManagementExperience'].map(map_yes_no)
df['MBAFundingSource'] = df['MBAFundingSource'].map(map_MBAfunding)
df['LocationPreference'] = df['LocationPreference'].map(map_LocationPreference)
df['ReasonforMBA'] = df['ReasonforMBA'].map(map_MBA_Reason)
df['OnlineorOnCampus'] = df['OnlineorOnCampus'].map(map_onlineOncampus)
df['DesiredPostMBArole'] = df['DesiredPostMBArole'].map(map_disiredpostmbarole)
df['DecidedToPursueMBA'] = df['DecidedToPursueMBA'].map(map_yes_no)

#drop PersonID
df = df.drop('PersonID', axis=1)

print(df)

#save to same location
df.to_csv('C:/Users/dstephens/Downloads/mba_decision_dataset_numerical.csv', index=False)

