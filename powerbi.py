import pandas as pd

#dataset is for the actual powerbi dashboard, this is a powerbi function
df = dataset

pattern = r'(\b\d{5}\b)' 

df['postalcode'] = df['streetaddress'].str.extract(pattern)

df['streetaddress'] = df['streetaddress'].str.replace(pattern + r',?\s*', '', regex=True)

def extract_state(address):
    parts = address.split(', ')
    try:
        us_index = parts.index('United States')
        if us_index > 0:
            return parts[us_index - 1] 
    except ValueError:
        return None

df['state'] = df['streetaddress'].apply(extract_state)


