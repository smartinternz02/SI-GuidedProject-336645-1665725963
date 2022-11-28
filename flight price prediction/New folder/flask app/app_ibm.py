# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 10:48:55 2022

@author: SmartBridge-PC
"""


import requests

import json

# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
API_KEY = "5ZhNtCJu2I_1FFhUtDiYw6TkwjjT8GYtsQcxD6YONuFb"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey":
 API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

# NOTE: manually define and pass the array(s) of values to be scored in the next line
payload_scoring = {"input_data": [{"field": [["Airline",	"Source",	"Destination",	"Date",	"Month",	"Year",	"Dep_Time_Hour",	"Dep_Time_Mins",	"Arrival_date",	"Arrival_Time_Hour",	"Arrival_Time_Mins"]], "values": [[7,	3,	4,	10,	5,	2022,	10,	19,	11,	5,	13	]]}]}

response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/e051981d-2549-473a-8982-2f2d8565373d/predictions?version=2022-06-03', json=payload_scoring,
 headers={'Authorization': 'Bearer ' + mltoken})
print("Scoring response")
print(response_scoring.json())