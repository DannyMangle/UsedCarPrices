import pandas as pd

def create_df():
    file = "/Users/dannymangle/Documents/GitHub/UsedCarPrices/mental_health_finaldata_1.csv"    
    df = pd.read_csv(file)
    return df

df = create_df()

print(df)
