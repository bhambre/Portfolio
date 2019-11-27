from flask import Flask, request, jsonify, render_template
from flask_restful import Resource, Api
from sqlalchemy import create_engine
import numpy as np
import pandas as pd
from sklearn import datasets
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.feature_extraction.text import CountVectorizer,TfidfVectorizer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
import pickle
from flask_cors import CORS, cross_origin


app = Flask(__name__)
api = Api(app)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

pkl_file = open('modeliden.pkl', 'rb')
clf = pickle.load(pkl_file)

pkl_file_stan = open('stan.pkl', 'rb')
stan = pickle.load(pkl_file_stan)

  
def modelidentification(allocperc):
    
    category = str(clf.predict(allocperc)[0])

    prob = str(int((clf.predict_proba(allocperc).max(axis=1)[0]) * 100))

    result = {'Category': category, 'Category Prob':prob}

    out = 'Based on the allocations you entered the category would be ' + result['Category'] + ' with a confidence score of ' + str(result['Category Prob']) + '%'

    return out

@app.route('/')
def home():
   return render_template('home.html')

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if (request.method=='POST'):
      result=request.form
      usstock = result["usstock"]
      usbond = result["usbond"]
      prefstock = result["prefstock"]
      nonusstock = result["nonusstock"]
      nonusbond = result["nonusbond"]
      derevative = result["derevative"]
      depreceipt = result["depreceipt"]
      convertible = result["convertible"]
      cash = result["cash"]
      other = result["other"]
      #['Cash', 'Convertible', 'DepositoryReceipt', 'Derivative','Non-US bonds', 'Non-US stocks', 'Other', 'Preferred stocks','US bonds', 'US stocks']
      list1 = [[cash,convertible,depreceipt,derevative,nonusbond,nonusstock,other,prefstock,usbond,usstock]]
      list1 = stan.transform(list1)
      output1 = modelidentification(list1)
      return str(output1)

@app.route('/api', methods=['get'])
def create_cm():
    cash_api = request.args.get('Cash', 0)
    convertible_api = request.args.get('Convertible', 0)
    depreceipt_api = request.args.get('Depository_Receipt', 0)
    derevative_api = request.args.get('Derevative', 0)
    nonusbond_api = request.args.get('Non_US_Bond', 0)
    nonusstock_api = request.args.get('Non_US_Stock', 0)
    other_api = request.args.get('Other', 0)
    prefstock_api = request.args.get('Preferred_Stock', 0)
    usbond_api = request.args.get('US_Bond', 0)
    usstock_api = request.args.get('US_Stock', 0)


    feat = [[cash_api,convertible_api,depreceipt_api,derevative_api,nonusbond_api,nonusstock_api,other_api,prefstock_api,usbond_api,usstock_api]]
    feat = stan.transform(feat)
    catprob = int((clf.predict_proba(feat).max(axis=1)[0]) * 100)
    cat = str(clf.predict(feat)[0])

    if catprob < 0:
      cat = 'Unable to identify' 

    result = {'category': cat, 'category score':catprob} 


        
    return jsonify(result)
    

            	    
if __name__ == '__main__':
	app.debug = True
	app.run()