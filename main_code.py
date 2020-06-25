import pandas as pd
import numpy as np
import os
from datetime import datetime
import re

	
def summation():
	#Working with Employee repository
	xcel=pd.ExcelFile('Employee Repository.xlsx')
	LIST=xcel.sheet_names
	df=xcel.parse(LIST[-2],header=None)

	df.columns = df.iloc[1] #Setting columns names

	#Removing not Nan Rows
	df=df.drop(df.index[0])
	df=df.drop(df.index[0])

	#Creating desired series
	emp=df['Rate/ Hour'].astype(str).astype(float)
	emp.index=df['Emp Code'].astype(str).astype(np.int64)


	#Working with starline data
	arr=os.listdir('Upload')

	xcel=pd.ExcelFile('Upload/'+arr[-1])
	LIST=xcel.sheet_names
	df=xcel.parse(LIST[-1],header=None)

	start_date=df[2][1]
	start_date = datetime.strptime(re.findall(r'\d\d-(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)-\d{4}', start_date)[0], '%d-%b-%Y').date()

	df=df.drop(df.index[0])
	df=df.drop(df.index[0])
	df=df.drop(df.index[0])

	t_df=df.T #Transposing the dataframe for better data wrangling

	t_df.columns = t_df.iloc[0]
	t_df=t_df.drop(t_df.index[0])

	#Getting column names and replacing with emp code
	LIST=t_df.columns
	reg=[]
	for i in range(3,len(LIST),11):
		LIST.values[i+6]=int(t_df.iloc[0][i])
		reg.append(int(t_df.iloc[0][i]))

	t_df.columns=LIST #Changing 


	reg=t_df.columns.tolist()
	reg_two=emp.index.tolist()

	final_columns=[value for value in reg_two if value in reg]

	t_df=t_df[final_columns] #only keeping columns with   correspondind emp code in employee repository

	#Dropping two more rows
	t_df=t_df.drop(t_df.index[0])
	t_df=t_df.drop(t_df.index[0])

	#setting index as data type
	t_df.index = pd.date_range(start=start_date, periods=len(t_df), freq='D')

	#taking only common columns
	emp=emp.loc[final_columns]


	#chaning every column to int
	t_df=t_df.apply(pd.to_numeric)

	month_sum = t_df.sum(axis=1)

	d=pd.DataFrame()
	for column_name in final_columns:
		d[column_name]=emp.get(key=column_name)*t_df[column_name]

	month_sum = d.sum(axis=1)

	return month_sum.tolist(),month_sum.index.tolist()