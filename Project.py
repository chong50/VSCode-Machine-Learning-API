import os

import uvicorn

from fastapi import FastAPI

from fastapi.responses import JSONResponse

from fastapi.responses import FileResponse

import pandas as pd

 

app = FastAPI()

 

@app.get('/predicted')

async def get_predicted():

    try:

        # Read data from Excel file

        df2 = pd.read_excel("GenerationForecasts.xlsx", usecols='D, E, F')

        # Convert float values to string representations

        df2 = df2.astype(str)

        # Convert DataFrame to list of dictionaries

        data = df2.to_dict(orient='records')

        return JSONResponse(content=data)

 

    except Exception as e:

        return JSONResponse(content={"error": str(e)})

 

@app.get('/{start_date}/{end_date}')

async def scoring_endpoint(start_date: str, end_date: str):

    try:

        # Read data from Excel file

        df1 = pd.read_excel("GenerationForecasts.xlsx", usecols='A, B, C')

        # Convert float values to string representations

        df1 = df1.astype(str)

 

        # start date and end date in datetime format

        start_date = pd.to_datetime(

            start_date, format="%Y-%m-%d-%H:%M")

        end_date = pd.to_datetime(

            end_date, format="%Y-%m-%d-%H:%M")

 

        df1['Time'] = pd.to_datetime(df1['Time'])

 

        # filter by start and end date

        df = df1[df1['Time'] >= start_date]

        df = df[df['Time'] <= end_date]

 

        df["Time"] = df["Time"].dt.strftime("%Y-%m-%d %H:%M")

 

        # Read data from Excel file

        df2 = pd.read_excel("GenerationForecasts.xlsx", usecols='D, E, F')

        # Convert float values to string representations

        df2 = df2.astype(str)

        # Convert DataFrame to list of dictionaries

        data = df.to_dict(orient='records')

        return JSONResponse(content=data)

 

    except Exception as e:

        return JSONResponse(content={"error": str(e)})

 

if __name__ == '__main__':

    uvicorn.run(app, host='127.0.0.1', port=8000)
