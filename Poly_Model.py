import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from matplotlib import pyplot as plt
import numpy as np
import pickle

sal_data = pd.read_excel('sal_exp.xlsx',sheet_name='Sheet1')
X = sal_data.iloc[:,[0]]
Y = sal_data.iloc[:,1]

Model = LinearRegression()
Poly_reg = PolynomialFeatures(degree=2)
X_poly = Poly_reg.fit_transform(X)
Model.fit(X_poly,Y)
Model.score(X_poly,Y)

plt.scatter(X,Y)
plt.plot(X,Model.predict(X_poly))

Model.predict(Poly_reg.fit_transform(np.array([8]).reshape(-1,1)))
pickle.dump(Model,open('Poly_Model.pkl','wb'))