import json
from flask import Flask, render_template, request
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
app = Flask(__name__)
import model

@app.route('/')
def hello():
    df = pd.read_csv('sleepdata.csv')
    chart_data = df.to_dict()
    chart_data = json.dumps(chart_data, indent=2)
    data = {'chart_data': chart_data}
    return render_template("sleep_analysis.html",data=data)
@app.route('/prediction')
def prediction():
    return render_template("sleep_prediction.html")
@app.route('/model')
def model():
    df = model.df
    known_mood = df[pd.notna(df['Wake up'])]
    one_hot = pd.get_dummies(known_mood['Wake up'])
    known_mood = known_mood.drop('Wake up',axis = 1)
    known_mood = known_mood.join(one_hot)
    known_mood['Wake up'] = known_mood[':|'] + known_mood[":)"] * 2
    known_mood = known_mood.drop(':)',axis = 1)
    known_mood = known_mood.drop(':(',axis = 1)
    known_mood = known_mood.drop(':|',axis = 1)
    # Fit the model
    clf = RandomForestClassifier(max_depth=2, random_state=0)
    clf.fit(known_mood.iloc[:,2:-1].drop("Heart rate",axis=1), known_mood['Wake up'])
    # Get data from form
    a, b, c, d, e = 0, 0, 0, 0, 0
    if request.form.get('vehicle1'):
        a = 1
    if request.form.get('vehicle2'):
        b = 1
    if request.form.get('vehicle3'):
        c = 1
    if request.form.get('vehicle4'):
        d = 1
    if request.form.get('vehicle5'):
        e = 1
    return render_template("sleep_prediction.html",result=clf.predict([[request.args['sq'],request.args['tb'],request.args['s'],a,b,c,d,e]]))
