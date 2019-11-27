import pandas as pd

carslist = pd.read_csv('cars.csv')

print (carslist.iloc[0:5,:],carslist.iloc[27:32,:])

