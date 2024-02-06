import pandas as pd
import csv
#model,year,price,transmission,mileage,fuelType,tax,mpg,engineSize

# filepath = r"/Users/dannymangle/Documents/GitHub/UsedCarPrices/Used Car Dataset.csv";

# df =pd.read_csv(filepath)

# print(df.head())

with open ('toyota.csv','r') as file:
    read = csv.DictReader(file)


    for line in read:
        if line['model'] == "C-HR":
            print(line['model'],line['price'])