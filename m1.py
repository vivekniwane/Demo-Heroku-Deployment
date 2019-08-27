import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pickle
sal_data = pd.read_excel('sal_exp.xlsx',sheet_name='Sheet1')
plt.scatter(sal_data['Experience'],sal_data['Salary'])

from sklearn.linear_model import LinearRegression
model1 = LinearRegression()
model1.fit(sal_data.iloc[:,[0]],sal_data.iloc[:,1])

op = model1.predict(np.array([0,1,2,3,4,5,6,7,8,9,10]).reshape(-1,1))
plt.plot(np.array([0,1,2,3,4,5,6,7,8,9,10]),op)
plt.scatter(sal_data['Experience'],sal_data['Salary'])

pickle.dump(model1,open('model.pkl','wb'))

m1 = pickle.load(open('model.pkl','rb'))
m1.predict(100)
model1.score(sal_data.iloc[:,[0]],sal_data.iloc[:,1])