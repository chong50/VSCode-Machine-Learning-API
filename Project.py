import os
import uvicorn
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],  # Replace with the appropriate origins for your use case
    allow_methods=['*'],  # Replace with the appropriate HTTP methods for your use case
    allow_headers=['*'],  # Replace with the appropriate headers for your use case
)

@app.get('/predicted/{start_date}/{end_date}')

async def get_predicted(start_date: str, end_date: str):

    try:

        # Read data from Excel file
        df2 = pd.read_excel("GenerationForecasts.xlsx", usecols='D, E, F')
        # Convert float values to string representations
        df2 = df2.astype(str)

        # start date and end date in datetime format
        start_date = pd.to_datetime(
            start_date, format="%Y-%m-%d-%H:%M")

        end_date = pd.to_datetime(
            end_date, format="%Y-%m-%d-%H:%M")
        
        df2['Future Time'] = pd.to_datetime(df2['Future Time'])

        # filter by start and end date
        df = df2[df2['Future Time'] >= start_date]
        df = df[df['Future Time'] <= end_date]

        df["Future Time"] = df["Future Time"].dt.strftime("%Y-%m-%d %H:%M")
        
        # Convert DataFrame to list of dictionaries
        data = df.to_dict(orient='records')
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

        # Convert DataFrame to list of dictionaries
        data = df.to_dict(orient='records')
        return JSONResponse(content=data)

    except Exception as e:

        return JSONResponse(content={"error": str(e)})
    

@app.get('/predicted/consumption/{start_date}/{end_date}')

async def get_predicted(start_date: str, end_date: str):

    try:

        # Read data from Excel file
        df2 = pd.read_excel("TimeSeriesForecasting.xlsx", usecols='C, D')
        # Convert float values to string representations
        df2 = df2.astype(str)

        # start date and end date in datetime format
        start_date = pd.to_datetime(
            start_date, format="%Y-%m-%d-%H:%M")

        end_date = pd.to_datetime(
            end_date, format="%Y-%m-%d-%H:%M")
        
        df2['Time'] = pd.to_datetime(df2['Time'])

        # filter by start and end date
        df = df2[df2['Time'] >= start_date]
        df = df[df['Time'] <= end_date]

        df["Time"] = df["Time"].dt.strftime("%Y-%m-%d %H:%M")
        
        # Convert DataFrame to list of dictionaries
        data = df.to_dict(orient='records')
        return JSONResponse(content=data)

    except Exception as e:

        return JSONResponse(content={"error": str(e)})


@app.get('/consumption/{start_date}/{end_date}')

async def scoring_endpoint(start_date: str, end_date: str):

    try:

        # Read data from Excel file
        df1 = pd.read_excel("TimeSeriesForecasting.xlsx", usecols='A, B')
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

        # Convert DataFrame to list of dictionaries
        data = df.to_dict(orient='records')
        return JSONResponse(content=data)

    except Exception as e:

        return JSONResponse(content={"error": str(e)})
    

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
