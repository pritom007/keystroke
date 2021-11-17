import numpy as np
import pandas as pd
data = pd.read_csv('DSL-StrongPasswordData.csv')
print(data.head(5))
data.drop(columns=['rep'],axis=1,inplace=True)
visual_data = data


#One Hot encoding the subject column. seperating the label from the rest of columns

unique_cols = data['subject'].nunique()

data = np.array(data)
X = data[:, unique_cols:]
y = data[:, :unique_cols]
print(data[0])



import seaborn as sn # statistical graphs
import matplotlib.pyplot as plt # data graphs
plt.style.use('seaborn-dark')
visual_data.iloc[:,:-1]

corrMatrix = visual_data[['H.period', 'DD.period.t',
       'UD.period.t', 'H.t', 'DD.t.i', 'UD.t.i', 'H.i', 'DD.i.e', 'UD.i.e',
       'H.e', 'DD.e.five', 'UD.e.five', 'H.five', 'DD.five.Shift.r',
       'UD.five.Shift.r', 'H.Shift.r', 'DD.Shift.r.o', 'UD.Shift.r.o', 'H.o',
       'DD.o.a', 'UD.o.a', 'H.a', 'DD.a.n', 'UD.a.n', 'H.n', 'DD.n.l',
       'UD.n.l', 'H.l', 'DD.l.Return', 'UD.l.Return', 'H.Return']].corr()
fig, ax = plt.subplots(figsize=(10,10))
sn.heatmap(corrMatrix, linewidths=0.1, cmap="BuPu")
plt.show()



visual_data.columns
h_cols=['subject']
ud_cols=['subject']
dd_cols=['subject']

h_cols.append('sessionIndex')
ud_cols.append('sessionIndex')
dd_cols.append('sessionIndex')

for column in visual_data.columns:
    if 'H' in column:
        h_cols.append(str(column))
    if 'UD' in column:
        ud_cols.append(str(column))
    if 'DD' in column:
        dd_cols.append(str(column))
print(dd_cols)
print(h_cols)
print(ud_cols)



key_hold_latency_002 = visual_data[h_cols]
khls_002 = key_hold_latency_002['subject']
key_hold_latency_002 = key_hold_latency_002.where((khls_002 =='s002'))
key_hold_latency_002 = key_hold_latency_002.groupby('sessionIndex').agg('mean')
key_hold_latency_002.T.plot(figsize=(8,5))

# key_hold_latency_008 = visual_data[h_cols]
# khls_008 = key_hold_latency_008['subject']
# key_hold_latency_008 = key_hold_latency_008.where((khls_002 =='s008'))
# key_hold_latency_008 = key_hold_latency_008.groupby('sessionIndex').agg('mean')
# key_hold_latency_008.T.plot(figsize=(8,5))

key_hold_latency = visual_data[h_cols]
key_hold_latency=key_hold_latency.drop(columns=['sessionIndex'])
print(key_hold_latency.columns)
khls = key_hold_latency['subject']
key_hold_latency = key_hold_latency.where((khls =='s002') | (khls =='s003') | (khls=='s004') | (khls== 's005') | (khls=='s007') | (khls=='s008'))
key_hold_latency = key_hold_latency.groupby('subject').agg('mean')
key_hold_latency.T.plot(figsize=(8,5))


visual_data.columns
h_cols=['subject']

h_cols.append('sessionIndex')

for column in visual_data.columns:
    if column in ['H.period', 'H.t', 'H.i', 'H.e']:
        h_cols.append(str(column))
print(h_cols)
h_period = visual_data[h_cols]
khls_h_period = h_period['subject']
h_period = h_period.where((khls_h_period =='s002'))
h_period = h_period.groupby('sessionIndex').mean()
h_period.T.plot(figsize=(8,5), )
