# Project Purpose
Predicting stock price moving direction with a random forest

# Detailed Description of the Machine Learning Algorithm
In this project, we predict the direction of stock price movement in the future months. So essentially, it is a classification problem.

The random forest is built upon the following 8 features: inflation rate, unemployment rate,
rate of change of Dow Jones Industrial Average and rate of change of S & P 500, three-month 
moving average of stock price, two month moving average of stock price, stock price in current month and current
fundamental value of the company. 

The data we used are all monthly data from Jan. 01 1990 to Sep. 01 2018. We avoided the noisy daily or weekly data.
The data are scraped from the web with Beautiful Soup.

The stocks we used as examples include Apple,ATT.

# Components of the Repository
1. The folder named *data* which contains the data for clustering and svm classification. The raw clustering data are mainly from different government websites. The raw data for classification are from yahoo finance.
2. The python file named *getData.py*. This file contains functions that transforms the raw data into format suitable for training. Since the raw data are taken from different sources, we wrote the ad hoc functions to transform the data. And then save the transformed data into *data* folder as well.
3. The python file *svm.py*. This is the main file. It implements the algorithm. In this file, we created an *StockPrediction* object that can be constructed with the information about the location of the transformed clustering and classification data files. If want to find the final result about the testing error, we can simply call *reportResult()* method embedded in the object. It automatically runs the algorithm and reports tesing error. By default we set have "80-20" split for the training and tesing data.<br />
In addition, for comparison, we implemented a *StockPredNoClassification* object that inherits from the *StockPrediction*. In this derived class, we simply implement a svm with the clustering and classification data combined. Similar to the parent class, we can simply call the *reportResult()* method in this derived class to find out the testing errors.

# Future Work
1. To compare the statistical difference of the performance between the svm with clustering and the svm without clustering, we are planning to perform certain hypothesis testing. 
2. The data amount is still relatively small if we cluster them into three or four clusters. Thus we will perform experiment on the weekly data.
3. Combine the two svm's into one with ensemble methods to see how big improvement we can have.
4. Use the same dataset to implement RNN to compare the results. Perform PCA on the data dimensions
if overfitting occurs.
