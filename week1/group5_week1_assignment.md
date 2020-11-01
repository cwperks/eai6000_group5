### Where did the data come from?

Our dataset comes from [Kaggle](https://www.kaggle.com/kartik2112/fraud-detection).

### Why did you choose this data? 

We had an hour long zoom meeting to go through a couple contender datasets. The finalists were:

- [Credit Card Transactions Fraud Detection Dataset
](https://www.kaggle.com/kartik2112/fraud-detection)
- [Synthetic Financial Datasets For Fraud Detection
](https://www.kaggle.com/ntnu-testimon/paysim1)
- [Top Personality Dataset](https://www.kaggle.com/arslanali4343/top-personality-dataset)
- [Suicide Rates Overview 1985 to 2016](https://www.kaggle.com/russellyates88/suicide-rates-overview-1985-to-2016)
- [Credit Card Fraud Detection](https://www.kaggle.com/mlg-ulb/creditcardfraud)
- [Crimes in Boston](https://www.kaggle.com/AnalyzeBoston/crimes-in-boston)
- [National Renewable Energy Laboratory's (NREL) PV Rooftop Database](https://registry.opendata.aws/nrel-oedi-pv-rooftops/)

We ultimately picked the first one on the list because it contains 23 columns and a large number of rows (1,296,675 rows) and we thought we would be able to utilize most or all of the methods presented in the class on the dataset. There is another popular Credit card fraud dataset on Kaggle ([https://www.kaggle.com/mlg-ulb/creditcardfraud](https://www.kaggle.com/mlg-ulb/creditcardfraud)) that we considered, but the columns in the dataset contain only numerical inputs variables which are the result of a PCA transformation due to confidentiality issues. It would be interesting to try the models and thinking we deploy on the first dataset to the other credit card fraud dataset and see if we can port the model to another dataset successfully. 

Our dataset contains:

|column               |dtype         |
|---------------------|--------------|
|`trans_date_trans_time`|object        |
|`cc_num`               |int64         |
|`merchant`             |object        |
|`category`             |object        |
|`amt`                  |float64       |
|`first`                |object        |
|`last`                 |object        |
|`gender`               |object        |
|`street`               |object        |
|`city`                 |object        |
|`state`                |object        |
|`zip`                  |int64         |
|`lat`                  |float64       |
|`long`                 |float64       |
|`city_pop`             |int64         |
|`job`                  |object        |
|`dob`                  |object        |
|`trans_num`            |object        |
|`unix_time`            |int64         |
|`merch_lat`            |float64       |
|`merch_long`           |float64       |
|`is_fraud`             |int64         |
|`txn_datetime`         |datetime64[ns]|
|`txn_date`             |object        |
|`date_of_birth`        |datetime64[ns]|


This is a sample of 1 row with headers explanation:

| column                | value                            |
|:----------------------|:---------------------------------|
| trans\_date\_trans_time | 2019-01-01 00:00:18            |
| cc_num                | 2703186189652095                 |
| merchant              | fraud_Rippin, Kub and Mann       |
| category              | misc_net                         |
| amt                   | 4.97                             |
| first                 | Jennifer                         |
| last                  | Banks                            |
| gender                | F                                |
| street                | 561 Perry Cove                   |
| city                  | Moravian Falls                   |
| state                 | NC                               |
| zip                   | 28654                            |
| lat                   | 36.0788                          |
| long                  | -81.1781                         |
| city_pop              | 3495                             |
| job                   | Psychologist, counselling        |
| dob                   | 1988-03-09                       |
| trans_num             | 0b242abb623afc578575680df30655b9 |
| unix_time             | 1325376018                       |
| merch_lat             | 36.011293                        |
| merch_long            | -82.048315                       |
| is_fraud              | 0                                |
| txn_datetime          | 2019-01-01 00:00:18              |
| date\_of\_birth       | 1988-03-09                       |
| year\_of\_birth       | 1988                             |
| txn_date              | 2019-01-01                       |

Not only can we try to predict fraudulent transactions with this dataset, we may also be able to build models around consumer behavior that could be of interest to advertisers. This dataset also contains categories separated from in person and on the net transactions so we may be able to analyze trends in consumer behavior. Along with consumer behavior, this dataset contains data until July this year so we may be able to gather insights into how the pandemic affects consumer behavior. This is simulated data, so I am not sure if the pandemic was incorporated into the synthesis of the data, but that will certainly be an exercise we perform in our exploratory data analysis.

Ultimately, we think this dataset is rich enough for us to deploy the knowledge we learn in this class and utilize all techniques introduced. Furthermore, financial fraud detection is a great example of how Machine Learning is used in the real world and this dataset could be a good avenue into seeing what challenges financial institutions are presented with in keeping their customers safe.

### What did you do with the data in the context of exploration?

In this explaratory phase we really just wanted to get acclimated with our dataset that we will be using for the next 6 weeks. In the first few analyses performed we analyzed things like:

1) Distribution of the amount of transactions

2) Distribution of the category of transactions

3) Seeing where the transactions took place and plotting on a map using GeoPandas

4) Distribution of the volume of transactions based on gender. It would also be interesting to see total amount spent by gender.

5) Occupation of the highest spenders

6) Volume of transactions by day. Similar to gender it would also be great to see this displayed as dollar amount along with the number of transactions.

7) Age distribution of the spenders in the dataset

8) Number of unique users and merchants in the dataset

9) Merchants with the highest number of transactions and highest dollar amount of transactions

10) Spenders with the highest number of transactions and highest dollar amount of transactions

11) In the training set we identified how many transactions were flagged as fraudulent and it would be good to analyze these cases more in depth for patterns


### What did you find? Why does that matter? 
To find meaningful information from the data we wanted to explore the data in a manner that could possibly guide us into where to focus our predictive models later in the course. Initially we wanted to see how fraudulent credit card charges related to the features that we have available. The three areas that we looked at were how age was correlated with fraud, how merchant categories were corelated with fraud, and if there was an age range and merchant category combination where fraud was more prevalent. These insights could help us understand where to focus our efforts and how these features are related to each other. Due to the large data set, a sample size of 10% of the data was taken to complete this analysis. 

First, we plotted two frequency distribution histograms to see how the age distribution differed between fraudulent and non-fraudulent credit card transactions. 
(insert chart)
Here we can see that for the most part the age distribution of fraudulent charges vs not is similar. However, there is a key spike in fraudulent charges that starts in the 70-79 age range and then in the 80-89 age range.

Next, we looked at the percentage of fraudulent charges across the various merchant categories.
(insert chart)
Interestingly there are some categories that had a relatively higher percentage than the others. It is not surprising that online shopping was the most susceptible to fraudulent charges, however it was surprising to see that grocery stores were also high in that chart.

Lastly, we also reviewed the combination of age ranges and merchant categories. In this part we new broke the ages by both ten-year buckets and then into deciles. The 10-year buckets allow us to easily read where age and merchant categories may overlap, however creating deciles, allows for a more focused and even distribution of the data. 
(Insert charts)
Reviewing the charts, it is interesting to see how the fraudulent charge percentage changes depending on how the ages are broken out and where the hot spots are. 


### What would your proposed next steps be? 
Exploratory Data Analysis (EDA) has led us to understand the structure and some of the content within the dataset. The next steps that we will take will be to clean up and pre-process the data. We will be looking for Missing Values, Anomalies, Duplicates, and a Class Imbalance. Our EDA has shown that we have no missing values or duplicates (Figure 1.0).

Figure 1.0  

duplicate_rows_df = df[df.duplicated()]
print("number of duplicate rows:",duplicate_rows_df.shape)

print(df.isnull().sum())

A Class Imbalance is where an item I am looking for, such as fraud, has an uneven distribution within the dataset. This can cause machine learning algorithms to have a low predictive accuracy. We are at risk of having a Class Imbalance in this dataset, due to the low percentage of identified fraud when compared to the total length of the dataset (shown in Figure 2.0).

Figure 2.0 

isFraudTotal=df['is_fraud'].sum()
print("Count of Fraud:",isFraudTotal)
total_rows = df['merchant'].count()
print("Total Rows:",total_rows)

Our next steps to solve this will be to evaluate the following techniques to correct this imbalance: Over Sampling, Under Sampling, and SMOTE.
We have also identified some outliers within our dataset, which will need to be removed to ensure the accuracy of our eventual algorithm. Outliers are anything that does not fall within the minimum and maximum range as defined by the following equation.

Equation 1.0
minimum: ‘Quartile 1’ – 1.5 * (‘Quartile 3’ – ‘Quartile 1’)
maximum: ‘Quartile 3’ – 1.5 * (‘Quartile 3’ – ‘Quartile 1’)

To understand our outliers, we must calculate them by column. In this case, I am going to evaluate outliers for both the ‘amt’ column, which shows the transaction amount and the ‘unix_time’ column which shows our date range. Using a boxplot, I can visualize my interquartile range and with a df.describe() function, I can see some of the relevant numbers to calculate my outliers.

Figure 3.0: Transaction Amount 

stats = df['amt'].describe()
print("Transaction Amount:")
print(stats)
df.boxplot(column='amt', figsize=(6, 6))

Figure 4.0: Unix Timeframe  

statstime = df['unix_time'].describe()
print("Unix Timeframe:")
print(statstime)
df.boxplot(column='unix_time', figsize=(6, 6))


In the case of transaction amount, I am viewing a significant number of outliers. In the case of my Unix Timeframe, I am not viewing outliers. My next steps here would be to use this information to remove outliers from the amount column. 

After my dataset is suitably clean, I would start laying out my framework for how I am going to develop my algorithm. We are interested in setting up an algorithm for Pattern Recognition, which would detect classes, clusters, and patterns of suspicious behavior. This could help us identify characteristics most often found in fraudulent transactions and patterns in consumer spending. 

We could plot out a consumers path to see patterns in a single users spending habits. Based on a single user's spending habits it would be interesting to see if we could predict a big life change such as new occupation, birth of a child, etc.

### What business problem are you intending to solve using ML with the data?
1. Which features are highly correlated to credit card fraud? 
Correlation matrix and regression models will be used to find out which features, such as gender, age and state, have strong correlations with the target variable is_fraud, which can provide banks more details about which group of people might be the target in credit card fraud.

2. To predict whether the user's credit card will be frauded or not. 
Tree-based models, such as random forest, decision tree and gradient boosting models, and neural networks will be applied to predict the accuracy of target variable is_fraud. We will also compare and seek the best performance among these predictive models by using different Machine Learning Algorithms. 

