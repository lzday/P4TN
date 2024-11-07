import geopandas as gpd
import matplotlib.pyplot as plt
# referenced from https://stackoverflow.com/a/65379520
countries = gpd.read_file('countries/ne_110m_admin_0_countries.dbf')
countries.plot()
plt.show()