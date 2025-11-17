import pickle
import uvicorn
import requests

from fastapi import FastAPI
from typing import Dict, Any

model_file = 'model.bin'

with open(model_file, 'rb') as f_in:
    pipeline = pickle.load(f_in)

app = FastAPI(title="predict")

def predict_single(person):
    result = pipeline.predict_proba(person) [0,1]
    return float(result)

@app.post("/predict")    
def predict(person: Dict[str, Any]):
    attrition = predict_single(person)
    return {
        "attrition_probability": attrition,
        "attrition": bool(attrition >= 0.5)
        }

if __name__ == "__main__":
        uvicorn.run(app, host="0.0.0.0", port=9696)