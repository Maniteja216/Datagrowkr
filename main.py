import pandas as pd
import os
os.chdir('C:\\Users\\karna\\Downloads')
data=pd.read_csv('survey_results_public.csv')

#find the null values
data.isnull().sum()

#describe the data
data.describe()

#Separate devloper data
devloper=data[data.MainBranch == 'I am a developer by profession'	]
#fill null values
devloper['Age'].fillna(method='ffill',inplace=True)
#find the avarage age of developer
devloper['Age'].mean()

#Whos's know python in each country and Calculate the percentage
data_py=devloper[devloper.LanguageWorkedWith == 'Python'	]
x=data_py['Country'].value_counts(normalize=True)*100
y=devloper['Country'].value_counts(normalize=True)*100
total=(x/y)
total.head()

#Developer Salary
#Find Monthly Average
Salary_month=devloper[devloper.CompFreq=='Monthly']
Salary_month['CompTotal']*12
x=Salary_month['CompTotal'].mean()
#Find Yearly Average
Salary_anum=devloper[devloper.CompFreq=='Yearly']
y=Salary_anum['CompTotal'].mean()
#Devlopers Avarahe Salary
dev_avg=(x+y)/2
dev_avg

#Most desired programming Language for 2020
data['LanguageDesireNextYear'].value_counts()

#Who code as hobby.
hobby_list=data[data.Hobbyist == 'Yes'	]
Male_data=hobby_list[hobby_list.Gender == 'Man'	]
x=Male_data['Gender'].value_counts()
Female_data=hobby_list[hobby_list.Gender == 'Woman'	]
y=Female_data['Gender'].value_counts()
print(x,y)

#Job and Career satisfaction
Male_data=data[data.Gender == 'Man'	]
Female_data=data[data.Gender=='Woman']
career_sat=Male_data['CareerSat']
x=career_sat.value_counts()
career_sat=Female_data['CareerSat']
x1=career_sat.value_counts()
job_sat=Male_data['JobSat']
y=job_sat.value_counts()
job_sat=Female_data['JobSat']
y1=job_sat.value_counts()
print(x,x1,y,y1)

#Gender is others
Other_data=data[data.Trans=='Yes']
Other_data.value_counts().sum()
