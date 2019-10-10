import pandas as pd
# Read data
data = pd.read_csv("https://github.com/nickeubank/MIDS_Data/raw/master/World_Development_Indicators/raw_WDI_Data_csv.zip")
# Subset into 2016 data
data_2016 = data[['Country Name','Country Code','Indicator Name','Indicator Code','2016']].copy()
