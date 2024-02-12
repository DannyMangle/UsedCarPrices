import pandas as pd
import csv
#model,year,price,transmission,mileage,fuelType,tax,mpg,engineSize
file="/Users/dannymangle/Documents/GitHub/UsedCarPrices/mental_health_finaldata_1.csv"

df =pd.read_csv(file)

print(df.head(3))

# with open ('mental_health_finaldata_1.csv','r') as file:
#     read = csv.DictReader(file)


#     for line in read:
#             print(line)

            