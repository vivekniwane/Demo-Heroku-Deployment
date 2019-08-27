from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    model = pickle.load(open('model.pkl','rb'))
    sal = model.predict(int(request.form['Experience']))
    str1 = '<h1>Dear '+ request.form['Name'] +', your expected salary after '+ request.form['Experience'] +'Yrs Experience is '+ str(sal)+'LPA</h1>'
    return str1

if __name__=='__main__':
    app.run(debug=True)