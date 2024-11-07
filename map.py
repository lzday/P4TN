import geopandas as gpd
import matplotlib.pyplot as plt
from random import choices
import pandas as pd
import numpy as np

# referenced from https://stackoverflow.com/a/65379520
def generate_data():
    
    k = 100
    
    countries_of_interest = ['USA','ARG','BRA','GBR','ESP','RUS']
    countries = choices(countries_of_interest, k=k)
    
    start_yr = 2010
    end_yr = 2021
    
    return pd.DataFrame({'Country':countries, 
                         'Year':np.random.randint(start_yr, end_yr, k)},
                        index=range(len(countries)))
def aggregate_data(df):
    data = df.groupby('Country').agg('count')
    data = data.reset_index().rename(columns={'Year':'count'})
    return data

df = generate_data()

#    Country  Year
# 0      USA  2017
# 1      GBR  2014
# 2      USA  2013
# 3      BRA  2016
# 4      BRA  2018
# ..     ...   ...
# 95     ESP  2014
# 96     USA  2015
# 97     RUS  2019
# 98     RUS  2012
# 99     RUS  2011
# 
# [100 rows x 2 columns]

data = aggregate_data(df)

#   Country  count
# 0     ARG                   20.0
# 1     BRA                   17.0
# 2     ESP                   14.0
# 3     GBR                   14.0
# 4     RUS                   19.0
# 5     USA                   16.0
file = 'countries/ne_110m_admin_0_countries.shp'
countries = gpd.read_file(file)[['ADMIN', 'ADM0_A3', 'geometry']]
countries.columns = ['country', 'country_code', 'geometry']

merged = countries.merge(data, left_on = 'country_code', right_on = 'Country', how='left')
merged['count'] = merged['count'].fillna(0)

fig, ax = plt.subplots(1, 1, figsize=(10, 6))
merged.plot(column='count', cmap='OrRd', legend=True, ax=ax,
           legend_kwds={'label': "Count",
                        'orientation': "horizontal"})
plt.show()