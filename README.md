<h1 align="center" style="color: #4649FF;">CARPRICE WEB APP</h1>
<p> This repo contains end-end development of car price prediction web app that was created using <b>Python, Machine Learning, Streamlit</b> vist the site at</p>

[CarPrice](https://zethu999-carprice-webapp-car-price-web-app-79545e.streamlitapp.com/) <hr>

### Work Flow
1. Data set collection
2. Data Cleaning and formatting
3. Preparing Final DataFrame
4. Model Building, Testing and Evaluations
5. Creating web app and Hosting

### Libraries used
- Numpy
- Pandas
- sci-kit learn
- pickle
- xgboost
- streamlit
### Environments
- Anaconda 
- Jupyter notebook
- spyder
<hr>

## Data set collection
The data set is taken from kaggle which is test.csv in the repo that has information about the used cars and their prices.Below is a part of data taken. 
![image](https://user-images.githubusercontent.com/103594682/196423884-9296995c-4100-4d62-8add-db5310d274c3.png)
<hr>

## Data Cleaning and formatting

Here,the given dataset contains many categorical values namely **Fuel_Type, Transmission, Owner_Type, Mileage, Engine, Power** which are requried but cannot be given directly to ML model. So, these values should be converted to numeical entites to feed these features to ML model and it has many null values. So, following steps are follwed to clean the data. 
![image](https://user-images.githubusercontent.com/103594682/196425982-1e7ed1b5-c6af-49f7-b554-a873b6976e19.png)
<hr>

## Preparing Final DataFrame
After all the cleaning Process and formatting the final data frame is made that is used for ML model tranning
- Intial DataFrame
![image](https://user-images.githubusercontent.com/103594682/196426909-db3b0155-7293-40e8-b49d-b6790bb3d634.png)
- Final DataFrame
![image](https://user-images.githubusercontent.com/103594682/196426707-e3fbf1aa-70ab-487c-a48e-f630ff4582e6.png)
<hr>

## Model Building, Testing and Evaluations

There are four algorithms used for fitting data and making correct predictions
- Linear Regressor
- Ridge Regression
- Lasso regression
- XGB Regressor

In these XGB Regressor gave the accurate predictions than all
- Linear Regressor

<img src="https://user-images.githubusercontent.com/103594682/196427977-e34a74b4-be8c-457c-aa52-e54fa8a5bd99.png" width="400" height="200">

- Ridge Regression

<img src="https://user-images.githubusercontent.com/103594682/196428103-88f9ff61-8f75-403a-ad58-1b9ebb21dc87.png" width="400" height="200">

- Lasso Regressor

<img src="https://user-images.githubusercontent.com/103594682/196428201-583e9a2a-13c8-493f-bc87-be42260d8fcd.png" width="400" height="200">

- XGB Regressor

<img src="https://user-images.githubusercontent.com/103594682/196428524-32918113-c15f-40ad-8342-e134d6ab376a.png" width="400" height="200">

Evaluation metrices are also performed on each algorithm in which XGB has 99% accuracy.
<hr>

## Creating web app and Hosting

The web app was made using streamlit library. The code avaliable is in car_price_web_app.py file. To run this file use spyder IDE and use command
```
streamlit run filename.py
```
then it runs on your local host. Hosting is done using Streamlit cloud where we need **requirements.txt, CarPricePrediction_Model.sav, car_price_web_app.py.** 

