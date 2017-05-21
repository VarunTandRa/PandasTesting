import numpy as np
import pandas as pd

path = "C:/Users/Varun TandRa/Desktop/dirty_data.csv"

df = pd.read_csv(path, encoding ="ISO-8859-1")

# Drop Html Column
df = df.drop(['Strange HTML'], axis = 1)

# Removing Special Characters
df["Street"] = df["Street"].str.replace("Ì´",' ')
df["Street"] = df["Street"].str.replace(".",'')
df["Street"] = df["Street"].str.replace("@",'')
#df["Street"] = df["Street"].map(str.strip)
df["Street 2"] = df["Street 2"].str.replace(".",'')
df["Street"] = df["Street"].str.replace(" ,",',')
df["Street 2"] = df["Street 2"].str.replace(" ,",',')

# Capitalize First Word
df["Street 2"] = df["Street 2"].str.title()
df["Street"] = df["Street"].str.title()

# Checking if Street 2 is the same as Street 1 and Removing Street 2 value based on it
df["Street 2"] = np.where((df["Street"] == df["Street 2"]), '', df["Street 2"])

# Creating a Map to clean Street to Str, Avenue to Ave, etc.

CleanMap = {'Street': 'Str', "Avenue": "Ave", "Road": "Rd", 'Station': 'Stn', 'Lane': 'Ln',
            'Street,': 'Str,', "Avenue,": "Ave,", "Road,": "Rd,", 'Station,': 'Stn,', 'Lane,': 'Ln,'}
keyMap = CleanMap.keys()
keyValues = CleanMap.values()

# function to look up map and clean the data
def cleanup(str):
    strlists = str.split()
    for (i,strlist) in enumerate(strlists):
        if strlist in keyMap:
            strlists[i] = CleanMap[strlist]
    return ' '.join(strlists)

# Applying the function
df["Street"] = df['Street'].apply(cleanup)


# Creating Area List to populate the Area
Area = ['Birmingham', 'Coldfield','Quinton','Alum','Harborne','Bristol','Belchers','Bordesley', 'Coventry', 'Dudley', 'Sandwell', 'Solihull', 'Walsall', 'Wolverhampton', 'Moseley', "W'Ton",'Wednesfield','Victoria']

def check_area(str):
    strLists = str.split()
    for location in Area:
        if location in strLists:
            return location

df["Area"] = df['Street'].apply(check_area)
df.to_csv('Clean_data', sep='\t', encoding='utf-8')
#data.to_csv('ch06/out.csv')
print(df)