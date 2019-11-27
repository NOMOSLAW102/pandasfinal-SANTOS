import pandas as pd

carslist = pd.read_csv('cars.csv')
print('**A**')
print(carslist.iloc[0:5:,range(0,11,2)])
print ('**B**')
print(carslist.loc[carslist['Model']=='Mazda RX4'])
print('**C**')
print(carslist.loc[carslist['Model']=='Camaro Z28',['Model','cyl']])
print('**D**')
print(carslist.loc[carslist['Model']=='Mazda RX4 Wag',['Model','cyl','gear']])
print(carslist.loc[carslist['Model']=='Ford Pantera L',['Model','cyl','gear']])
print(carslist.loc[carslist['Model']=='Honda Civic',['Model','cyl','gear']])


