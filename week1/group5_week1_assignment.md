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

### What did you find? Why does that matter? 

### What would your proposed next steps be? 

### What business problem are you intending to solve using ML with the data?

