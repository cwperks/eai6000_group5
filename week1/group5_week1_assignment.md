### Where did the data come from?

Our dataset comes from [Kaggle](https://www.kaggle.com/ntnu-testimon/paysim1).

### Why did you choose this data? 

We had an hour long zoom meeting to go through a couple contender datasets. The finalists were:

- [Synthetic Financial Datasets For Fraud Detection
](https://www.kaggle.com/ntnu-testimon/paysim1)
- [Top Personality Dataset](https://www.kaggle.com/arslanali4343/top-personality-dataset)
- [Suicide Rates Overview 1985 to 2016](https://www.kaggle.com/russellyates88/suicide-rates-overview-1985-to-2016)
- [Credit Card Fraud Detection](https://www.kaggle.com/mlg-ulb/creditcardfraud)
- [Crimes in Boston](https://www.kaggle.com/AnalyzeBoston/crimes-in-boston)
- [National Renewable Energy Laboratory's (NREL) PV Rooftop Database](https://registry.opendata.aws/nrel-oedi-pv-rooftops/)

We ultimately picked the first one on the list because it contains a large number of rows (6,362,620 rows) and we thought we would be able to utilize most or all of the methods presented in the class on the dataset. There is another popular Credit card fraud dataset on Kaggle ([https://www.kaggle.com/mlg-ulb/creditcardfraud](https://www.kaggle.com/mlg-ulb/creditcardfraud)) that we considered, but the columns in the dataset contain only numerical inputs variables which are the result of a PCA transformation due to confidentiality issues. It would be interesting to try the models and thinking we deploy on the first dataset to the other credit card fraud dataset and see if we can port the model to another dataset successfully. 

Our dataset contains:

`step` - maps a unit of time in the real world. In this case 1 step is 1 hour of time. Total steps 744 (30 days simulation).

`type` - CASH-IN, CASH-OUT, DEBIT, PAYMENT and TRANSFER.

`amount` -
amount of the transaction in local currency.

`nameOrig` - customer who started the transaction

`oldbalanceOrg` - initial balance before the transaction

`newbalanceOrig` - new balance after the transaction

`nameDest` - customer who is the recipient of the transaction

`oldbalanceDest` - initial balance recipient before the transaction. Note that there is not information for customers that start with M (Merchants).

`newbalanceDest` - new balance recipient after the transaction. Note that there is not information for customers that start with M (Merchants).

`isFraud` - This is the transactions made by the fraudulent agents inside the simulation. In this specific dataset the fraudulent behavior of the agents aims to profit by taking control or customers accounts and try to empty the funds by transferring to another account and then cashing out of the system.

`isFlaggedFraud` - The business model aims to control massive transfers from one account to another and flags illegal attempts. An illegal attempt in this dataset is an attempt to transfer more than 200.000 in a single transaction.

This is a sample of 1 row with headers explanation:

| step| type    | amount  | nameOrig   | oldbalanceOrig | newbalanceOrig | nameDest    | oldbalanceDest | newbalanceDest | isFraud | isFlaggedFraud |
| --- | ------- | ------- | ---------- | -------------- | -------------- | ----------- | -------------- | -------------- | ------- | -------------- |
| 1   | PAYMENT | 1060.31 | C429214117 | 1089.0         | 28.69          | M1591654462 | 0.0            | 0.0            | 0       | 0              |

### What did you do with the data in the context of exploration?
#Craig

### What did you find? Why does that matter? 
#Cosimo

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

After my dataset is suitably clean, I would start laying out my framework for how I am going to develop my algorithm. We are interested in setting up an algorithm for Pattern Recognition, which would detect classes, clusters, and patterns of suspicious behavior. This could help us identify characteristics most often found in fraudulent transactions. 

### What business problem are you intending to solve using ML with the data?
1. Which features are highly correlated to credit card fraud? 
Correlation matrix and regression models will be used to find out which features, such as gender, age and state, have strong correlations with the target variable is_fraud, which can provide banks more details about which group of people might be the target in credit card fraud.

2. To predict whether the user's credit card will be frauded or not. 
Tree-based models, such as random forest, decision tree and gradient boosting models, and neural networks will be applied to predict the accuracy of target variable is_fraud. We will also compare and seek the best performance among these predictive models by using different Machine Learning Algorithms. 

