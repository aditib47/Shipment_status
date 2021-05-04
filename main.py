from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import numpy as np
import pandas as pd
import uvicorn
import os 
from sklearn.ensemble import GradientBoostingClassifier

#creating app
app = FastAPI()

@app.get('/')
def home():
    return"SHIPMENT DELAY PREDICTION"

class request_body(BaseModel):
    Customer_care_calls: int
    Customer_rating    : int  
    Cost_of_the_Product: int 
    Prior_purchases    : int
    Discount_offered   : int
    Weight_in_gms      : int
           
@app.post('/predict')
async def predict_shipment(data: request_body):
    loaded_model=pickle.load(open('shipment_ecom.pkl','rb'))
    test_data = [[
            data.Customer_care_calls,
            data.Customer_rating,
            data.Cost_of_the_Product,
            data.Prior_purchases,
            data.Discount_offered, 
            data.Weight_in_gms
            ]]
    prediction = int(loaded_model.predict(test_data))
    if(prediction==0):
        return { 'The shipment is likely to be on time  as the predicted value is':prediction}
        
    elif(prediction==1):
        return{'The shipment is likely to be delayed as the predicted value is':prediction}
    
    
if __name__=="__main__":
    uvicorn.run(app)