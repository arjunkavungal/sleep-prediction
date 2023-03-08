import pandas as pd
df = pd.read_csv('sleepdata.csv',sep=";")
df['Sleep quality'] = df['Sleep quality'].str.rstrip('%').astype('float')
# Convert hours and minutes to just minutes.
df['Hours in bed'] = df['Time in bed'].str.split(':').str[0]
df['Minutes in bed'] = df['Time in bed'].str.split(':').str[1]
df['Time in bed'] = df['Hours in bed'].astype(int) * 60 + df['Minutes in bed'].astype(int)
df = df.drop(['Hours in bed','Minutes in bed'],axis = 1)
# Extract data from sleep notes.
df['Sleep Notes'] = df['Sleep Notes'].fillna("None")
df['Stressful day'] = df['Sleep Notes'].str.contains('Stressful day').astype(int)
df['Worked out'] = df['Sleep Notes'].str.contains('Worked out').astype(int)
df['Drank tea'] = df['Sleep Notes'].str.contains('Drank tea').astype(int)
df['Drank coffee'] = df['Sleep Notes'].str.contains('Drank coffee').astype(int)
df['Ate late'] = df['Sleep Notes'].str.contains('Ate late').astype(int)
df = df.drop('Sleep Notes',axis = 1)
