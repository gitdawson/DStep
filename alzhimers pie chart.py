import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("C:/Users/dstephens/Downloads/alzheimers_prediction_dataset.csv")

#map the diagnosis column to 0 for "No" and 1 for "Yes"
data['Alzheimers Diagnosis'] = data['Alzheimers Diagnosis'].map({'No': 0, 'Yes': 1})

#create a pie chart of the diagnosis column
plt.pie(data['Alzheimers Diagnosis'].value_counts(), labels=['No', 'Yes'], autopct='%1.1f%%')
plt.title('Diagnosis of Alzheimer\'s Disease')
plt.show()

