# VSCode-Machine-Learning-API

This is the subsystem of Data Analysis. Basic operations such as Time-Series Analysis and Visualization are featured primarily in the MATLAB platform. At research, this subsystem extends its ability to performing data analysis into Optimization and Machine Learning. Since the core of our work works with data of consumption and generation of power in time series format, the hardware also enables the ability to collect sensor data in terms of irradiation from sunlight. In supervised learning definition, this can be represented as a feature input in Machine Learning context with generation and consumption of power as observation variables y, while exploring methods such as Linear Regression, Polynomial Regression, Artificial Neural Network, Time-Series Forecasting to forecast future events denoting the predicted consumption and generation of power in the system. The most effective method is Time-Series Forecasting that leveraged ARIMA technology application that integrates autocorrelation and feature of moving average to study the dependency between each timestep of observation variable and predict the next observation value of output based on time. This is the smart and efficient way to apply ARIMA application in the context of forecasting time-series consumption and generation data of solar panel system to maximize productivity. In our GITHUB, the repository is built and storing the effort and work of ARIMA application file that is built using available resources in MATLAB, and also the work of Linear, Polynomial Regression and Artificial Neural Network in MATLAB that uses LiveScript file to feature step-by-step work. At the byproduct of our work, all data of predictions and the corresponding feature input in values will be recorded on an Excel .xlsx file that is ready for the next stage.

### Established 4/13/2023

# Development 

## ConsumptionForecast.mlx | Time-Series Forecasting
### Decision Making

## GenerationForecast.mlx | Machine Learning | Deep Learning
### Decision Making



## Fast API Endpoint for Data Retrieval
### Project.py (API Endpoint Creation)
### Pseudocode
1. Import required modules and packages:
    - os
    - uvicorn
    - FastAPI
    - JSONResponse
    - FileResponse
    - CORSMiddleware
    - pandas

2. Create an instance of the FastAPI application.

3. Use the app object to add CORS middleware to allow cross-origin resource sharing.

4. Define two endpoints using the app object:
    - An endpoint with the path `/predicted/{start_date}/{end_date}` that accepts two parameters, `start_date` and `end_date`.
    - An endpoint with the path `/{start_date}/{end_date}` that accepts two parameters, `start_date` and `end_date`.

5. Inside the `get_predicted` function:
    - Read data from an Excel file using the pandas `read_excel` method.
    - Convert float values to string representations.
    - Convert the `start_date` and `end_date` parameters to datetime format using the pandas `to_datetime` method.
    - Filter the DataFrame to include only rows that have a `Future Time` value between the `start_date` and `end_date`.
    - Convert the `Future Time` column to a string representation.
    - Convert the DataFrame to a list of dictionaries.
    - Return a JSON response with the data.

6. Inside the `scoring_endpoint` function:
    - Read data from an Excel file using the pandas `read_excel` method.
    - Convert float values to string representations.
    - Convert the `start_date` and `end_date` parameters to datetime format using the pandas `to_datetime` method.
    - Filter the DataFrame to include only rows that have a `Time` value between the `start_date` and `end_date`.
    - Convert the `Time` column to a string representation.
    - Convert the DataFrame to a list of dictionaries.
    - Return a JSON response with the data.

7. Start the application using the `uvicorn.run` method with the following parameters:
    - The app object
    - The host IP address as a string (`'127.0.0.1'`)
    - The port number as an integer (`8000`)


## Activity Log

#### 4/17/2023

1. Pushed the Completed Progress about work and effort on development of URL parameters and establishment of function to take in inputs e.g. start data and end date; to output datas and available resources between those indicated dates. 
2. The URL is available below. The instruction page will be featured below on instructions on how to use the URL and access the functions.
3. The URL completion is ready. 

#### 4/18/2023

1. Researched on module that handles CORS-related functionality to disable CORS on API URL environment.
2. Added CORS headers to the URL response. Disabled cross-origin request function to welcome Application Development subsystem owner into local development environment for the URL and allow persons to access the resources for his/her own development. 
3. Implementing ARIMA Autocorrelation, Integration, Moving Average application involving resources and built-in functions on MATLAB for Time-Series Forecasting Purposes. 
