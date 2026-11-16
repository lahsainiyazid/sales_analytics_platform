import pandas as pd 

df=pd.read_csv("/home/yazid/sales/data/sales.csv")

#Our dataframe looks like this:
print(df.head())
#Our columns are like this :
print(df.columns.to_list())
#Useful info about our df:
print(df.info())
