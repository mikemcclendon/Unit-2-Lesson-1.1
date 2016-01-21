import pandas as pd
from scipy import stats
import numpy as np

data = '''Region,Alcohol,Tobacco
North,6.47,4.03
Yorkshire,6.13,3.76
Northeast,6.19,3.77
East Midlands,4.89,3.34
West Midlands,5.63,3.47
East Anglia,4.52,2.92
Southeast,5.89,3.20
Southwest,4.79,2.71
Wales,5.27,3.53
Scotland,6.08,4.51
Northern Ireland,4.02,4.56'''

data = data.splitlines()
data = [i.split(',') for i in data]

column_names = data[0] # this is the first row
data_rows = data[1::] # these are all the following rows of data
df = pd.DataFrame(data_rows, columns=column_names)

df['Alcohol'] = df['Alcohol'].astype(float)
df['Tobacco'] = df['Tobacco'].astype(float)

valuelist = []

for index, row in df.iterrows():
	valuelist.append(row['Alcohol'])
	valuelist.append(row['Tobacco'])

mean = np.mean(valuelist)
median = np.median(valuelist)
mode = stats.mode(valuelist)
variance = np.var(valuelist)
range = np.ptp(valuelist)
std = np.std(valuelist)

print('The mean of the Alcohol and Tobacco dataset is ' + str(mean))
print('The median of the Alcohol and Tobacco dataset is ' + str(median))
print('The mode of the Alcohol and Tobacco dataset is ' + str(mode))
print('The variance of the Alcohol and Tobacco dataset is ' + str(variance))
print('The range of the Alcohol and Tobacco dataset is ' + str(range))
print('The standard deviation of the Alcohol and Tobacco dataset is ' + str(std))
	
					



