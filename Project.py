import os
import uvicorn
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.responses import FileResponse
import pandas as pd


app = FastAPI()

@app.get('/')
async def scoring_endpoint():
    try:
        # Read data from Excel file
        df = pd.read_excel("sungenMLmodels.xlsx")
        # Convert float values to string representations
        df = df.astype(str)
        # Convert DataFrame to list of dictionaries
        data = df.to_dict(orient='records')
        return JSONResponse(content=data)
    
    except Exception as e:
        return JSONResponse(content={"error":str(e)})

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)

    