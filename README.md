# VSCode-Machine-Learning-API

This is the subsystem of Data Analysis. Basic operations such as Time-Series Analysis and Visualization are featured primarily in the MATLAB platform. At research, this subsystem extends its ability to performing data analysis into Optimization and Machine Learning. Since the core of our work works with data of consumption and generation of power in time series format, the hardware also enables the ability to collect sensor data in terms of irradiation from sunlight. In supervised learning definition, this can be represented as a feature input in Machine Learning context with generation and consumption of power as observation variables y, while exploring methods such as Linear Regression, Polynomial Regression, Artificial Neural Network, Time-Series Forecasting to forecast future events denoting the predicted consumption and generation of power in the system. The most effective method is Time-Series Forecasting that leveraged ARIMA technology application that integrates autocorrelation and feature of moving average to study the dependency between each timestep of observation variable and predict the next observation value of output based on time. This is the smart and efficient way to apply ARIMA application in the context of forecasting time-series consumption and generation data of solar panel system to maximize productivity. In our GITHUB, the repository is built and storing the effort and work of ARIMA application file that is built using available resources in MATLAB, and also the work of Linear, Polynomial Regression and Artificial Neural Network in MATLAB that uses LiveScript file to feature step-by-step work. At the byproduct of our work, all data of predictions and the corresponding feature input in values will be recorded on an Excel .xlsx file that is ready for the next stage.

### Established 4/13/2023

# Development 

- Creation of Generation Forecast
- Creation of Consumption Forecast
- API Endpoint Development for User Interface and Data Retrieval 

## ConsumptionForecast.mlx
### Time-Series Forecasting

This code is for performance of time series forecasting of energy consumption data using ARIMA model in MATLAB. The dataset contains energy consumption data for 1097 days with 24-hour readings. The code imports the dataset and configures it for analysis by computing the average load per hour. Then, the code splits the data into training and testing sets using cvpartition. For each hour of the day, the code fits an ARIMA model to the training data, generates forecasts for the test set, and adds the average load per hour back to calculate the forecasted consumption. The code visualizes the 24-hour forecasted consumption compared with the actual data. Finally, the code exports the forecast data onto a server in an Excel format.

### Pseudocode

1. Import the consumption data and time data

2. Configure the data for the load and time before entering into the model
 
3. Compute the average load per hour for the given days

4. Split the data into training and testing sets using cvpartition
 
5. Fit an ARIMA model to the training data for each hour of the day

6. Generate forecasts for the test set for each hour of the day

7. Add the average load per hour back to the equation to calculate the forecasted l(t)

8. Visualize the 24-hour forecasted consumption compared with actual data
 
9. Configure the output data format compatible for export
 
10. Export the forecast onto the server in the format .xlsx.

## GenerationForecast.mlx
### Machine Learning & Deep Learning

This code is for solar forecasting for power generation, and it aims to predict the solar power generation based on environmental parameters such as irradiation and temperature. The code first imports the metadata from a CSV file and visualizes the data using plots. Then it performs correlation and trend analysis, followed by linear and polynomial regression modeling with different degrees of freedom. The effect of advancing to a higher order of polynomial and feature normalization are also explored. Finally, the dataset is split into training and validation sets, and the quadratic model is retrained on this split dataset. The code also iterates on different training and test splits to evaluate the model's performance.

### Pseudocode

1. Import metadata (sensor data) from a CSV file

2. Extract time, generation, irradiation, and temperature data from the metadata and store them in separate variables

3. Visualize the data by plotting irradiation, temperature, and solar generation against time using different figures

4. Calculate correlation coefficients between irradiation and generation, and between temperature and generation

5. Fit a linear regression model to predict solar generation based on irradiation and calculate the root mean square error (RMSE) and relative RMSE (RRMSE)

6. Fit a polynomial regression model of degree 2 to predict solar generation based on irradiation and calculate the RMSE and RRMSE

7. Normalize the irradiation data using feature normalization

8. Fit a polynomial regression model of degree 2 to the normalized data and calculate the RMSE and RRMSE

9. Evaluate the effect of advancing to higher orders of polynomial by fitting polynomial regression models of degree 1 to 20 to the normalized data and plotting the error against degree

10. Split the data into training and validation sets using a random permutation

11. Fit a quadratic model to the training data and evaluate its performance on the validation data by calculating the RMSE

12. Evaluate the effect of advancing to higher orders of polynomial on the training and validation data by fitting polynomial regression models of degree 1 to 10 and plotting the RMSE against degree for both sets

13. Repeat steps 10-12 for 100 iterations with different training and validation splits and store the average RMSE values for each degree in two arrays, one for the training data and one for the validation data

14. Plot the average RMSE values for the training and validation data against degree of polynomial and compare them to identify the optimal degree for the model.


## Fast API Endpoint for Data Retrieval
### Project.py (API Endpoint File)
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

## Heroku 

### URL

Base URL: https://mlmodelingforecast.herokuapp.com/

Measured Generation: (Available dates between 2020-5-15 00:00 and 2020-5-26 00:00)

https://mlmodelingforecast.herokuapp.com/generation/2020-5-15-00:00/2020-5-16-00:00

Predicted Generation: (Available dates between 2020-5-26 00:15 and 2020-5-31 04:00)

https://mlmodelingforecast.herokuapp.com/genpred/2020-5-26-00:15/2020-5-31-04:00

Measured Consumption: (Available dates between 2018-01-11-00:00 and 2021-03-27-23:00)

https://mlmodelingforecast.herokuapp.com/consumption/2018-01-11-00:00/2021-03-27-23:00

Predicted Consumption: (Available dates between 2021-03-28-00:00 and 2021-11-01-23:00)

https://mlmodelingforecast.herokuapp.com/conpred/2021-03-28-00:00/2021-11-01-23:00

### Description

Heroku is a cloud platform that allows users to deploy and run their applications, including web applications, on the cloud. The fastapi endpoint for data retrieval is a web application built using the FastAPI framework, which is a modern, fast, web framework for building APIs leveraging Python language. This endpoint is hosted on Heroku, meaning that it is deployed on Heroku's cloud platform, and it can be accessed by users over the internet through a specific URL. Users can send requests to the FastAPI endpoint to retrieve data, and the endpoint will return the requested data in a JSON format.

## Activity Log

#### 4/17/2023

1. Pushed the Completed Progress about work and effort on development of URL parameters and establishment of function to take in inputs e.g. start data and end date; to output datas and available resources between those indicated dates. 
2. The URL is available below. The instruction page will be featured below on instructions on how to use the URL and access the functions.
3. The URL completion is ready. 

#### 4/18/2023

1. Researched on module that handles CORS-related functionality to disable CORS on API URL environment.
2. Added CORS headers to the URL response. Disabled cross-origin request function to welcome Application Development subsystem owner into local development environment for the URL and allow persons to access the resources for his/her own development. 
3. Implementing ARIMA Autocorrelation, Integration, Moving Average application involving resources and built-in functions on MATLAB for Time-Series Forecasting Purposes. 
