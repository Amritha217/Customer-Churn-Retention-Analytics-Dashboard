import pandas as pd
import numpy as np

df = pd.read_csv('dataset_Telco_Customer_Churn.csv')

df.shape
df.info()
df.isnull().sum()
df.describe()


