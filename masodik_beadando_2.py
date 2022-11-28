import pandas as pd
from datetime import datetime

adls=pd.read_csv('adls_b.txt', sep=';',header=0)
sensors=pd.read_csv('sensors_b.txt', sep=';',header=0)

adls['Starttime'] = pd.to_datetime(adls['Starttime'])
adls['Endtime'] = pd.to_datetime(adls['Endtime'])

sensors
#a feladat
adls['spent_time']=adls['Endtime']-adls['Starttime']
print(adls.groupby('Activity')['spent_time'].sum().sort_values(ascending=False))


#b feladat
bath=sensors[sensors['Place'].str.contains("Bathroom")]
filtered=bath.loc[(bath['Endtime'] <= '2012-11-15 00:00:00')]
print('Fürdőszobai aktivitások 2012.11.15-ig: \n',filtered)