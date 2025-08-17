# Credit-Card-Fraud-Detection

Situation:
Financial institutions face millions of transactions daily, and a small fraction may be fraudulent. Detecting these frauds in real-time is critical to prevent financial losses and protect customers.

Task:
The goal of this project was to analyze transaction data and build a predictive model that can identify potentially fraudulent transactions accurately.

Action:

Collected and explored the PaySim / Credit Card transaction dataset, analyzing patterns in transaction types, amounts, and balances.

Performed data preprocessing:

Handled imbalanced data

Scaled numerical features (e.g., transaction amount, account balances)

One-hot encoded categorical features (e.g., transaction type)

Engineered features such as:

Balance differences before and after transactions

Patterns in transfer and cash-out transactions

Built machine learning models using:

Logistic Regression (weighted)

Preprocessing and modeling done via Scikit-learn Pipelines

Evaluated model performance using classification metrics (precision, recall, F1-score, ROC-AUC)

Interpreted feature importance using SHAP values to understand key drivers of fraud.

Result:

The model achieved high recall (~94%) for fraudulent transactions, allowing detection of most fraud cases.

Analysis revealed that TRANSFER and CASH_OUT transactions with zero balances after transfer were highly correlated with fraud.

Enabled data-driven insights to proactively monitor suspicious transactions.

Use Cases

Real-time Fraud Detection: Alert banks or payment processors when a high-risk transaction occurs.

Risk Mitigation: Reduce financial losses by flagging suspicious transfers and cash-outs.

Business Insights: Identify patterns in fraudulent behavior to strengthen internal fraud prevention policies.

Regulatory Compliance: Help financial institutions comply with anti-fraud regulations by monitoring abnormal transactions.

Technologies Used

Python, Pandas, NumPy

Scikit-learn (Logistic Regression, Pipelines, ColumnTransformer)

Seaborn & Matplotlib (Data Visualization)

SHAP (Model Interpretability)
