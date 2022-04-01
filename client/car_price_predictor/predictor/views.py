from cmath import pi
from json import load
from os import O_EXCL
from tkinter.filedialog import Open
from django.shortcuts import render
import pickle
import pandas as pd
import numpy as np
import os
import pprint

data = pd.read_csv('D:\\ML_projects\\car_price_prediction\\model\\cleaned_data.csv')
companies=sorted(data['company'].unique())
car_models=sorted(data['name'].unique())
fuels = sorted(data['fuel_type'].unique())
years = sorted(data['year'].unique(),reverse=True)
# Create your views here.
def Home(request):
    if companies[0]!="Select Company":
        companies.insert(0,"Select Company")
    return render(request, 'home.html', {"companies":companies, "car_models":car_models, "fuels":fuels, "years":years})

def predict(request):
    company = request.POST.get('company','')
    car_model = request.POST.get('car_model','')
    fuel_type = request.POST.get('fuel_type','')
    year = int(request.POST.get('year',''))
    kms_driven = int(request.POST.get('kms_driven',''))

    # fileobj = Open('D:\\ML_projects\\car_price_prediction\\model\\LinearRegressionModel.pkl','rb')
    #model = pd.read_pickle(Open("LinearRegressionModel.pkl",'rb'))

    with open('LinearRegressionModel.pkl', 'rb') as f:
        model = pickle.load(f)  

    prediction = model.predict(pd.DataFrame([[car_model,company,year,kms_driven,fuel_type]],columns=
        ['name','company','year','kms_driven','fuel_type']))


    result=np.round(prediction[0],2)


    return render(request, 'show.html',{ 
        "company":company, "car_model":car_model,"kms_driven":kms_driven, "fuel_type":fuel_type, "year":year, "result":result}) 