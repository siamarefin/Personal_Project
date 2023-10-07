
import pandas as pd 
df = pd.read_csv("Downloads\salaries.csv")

inputs = df.drop("salary_more_then_100k",axis = 'columns') 
target  = df['salary_more_then_100k'] 

from sklearn.preprocessing import LabelEncoder 

le_company = LabelEncoder()
le_job = LabelEncoder()
le_degree   = LabelEncoder() 

inputs['company']  = le_company.fit_transform(inputs['company']) 
inputs['job'] = le_job.fit_transform(inputs['job'])
inputs['degree'] = le_degree.fit_transform(inputs['degree']) 



from sklearn import tree 
model = tree.DecisionTreeClassifier()
model.fit(inputs,target)

ans = model.predict([[2,2,1]])
ans 
