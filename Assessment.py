import pandas as pd
orderfile=pd.read_csv('./order.csv')
execfile=pd.read_csv('./exec.csv')

#Converting price into float so that arithmatic opertaions can be performed
for i in range(len(execfile.PRICE)):
    execfile.PRICE[i]=float(execfile.PRICE[i][1:-1])

#Converting quantity to int so that arithmatic opertaions can be performed
for i in range(len(execfile.QUANTITY)):
    execfile.QUANTITY[i]=int(execfile.QUANTITY[i][1:-1])

execfile=execfile.groupby(['USER','PRICE']).sum().reset_index()

execfile.rename(columns={'PRICE':'Price'}, inplace=True)

df2=pd.merge(orderfile, execfile, on=['USER', 'Price'])

df2['Qty_Unexecuted']=df2['Qty']-df2['QUANTITY']

#Selecting only relevant columns for output file
final=df2[['USER', 'Price', 'ORDER REF', 'Qty_Unexecuted']]

#Saving the final df to csv
final.to_csv('./output.csv', sep=',', encoding='utf-8', index=False)
