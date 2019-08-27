from flask import Flask, request, render_template
import pickle
from sklearn.preprocessing import PolynomialFeatures
import numpy as np

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    #model = pickle.load(open('model.pkl','rb'))
    model = pickle.load(open('Poly_Model.pkl','rb'))
    Poly_reg = PolynomialFeatures(degree=2)
    X = Poly_reg.fit_transform(np.array([float(request.form['Experience'])]).reshape(-1,1))
    #sal = model.predict(float(request.form['Experience']))
    sal = model.predict(X)
    sal_final = str(round(sal[0],2))
    str1 = '<h1>Dear '+ request.form['Name'] +', your expected salary after '+ request.form['Experience'] +'Yrs Experience is '+ sal_final+' LPA</h1>'
    return str1

if __name__=='__main__':
    app.run(debug=True)