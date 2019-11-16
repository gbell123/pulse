import geopandas
import matplotlib.pyplot as plt
import pandas as pd
import pdb

YEAR = '2011'

df = pd.read_csv('data.csv', dtype=str)
df = df[df['yearer'] == YEAR]
df.census_county = '0' + df.census_county
df.zscore_smooth_cap = df.zscore_smooth_cap.astype(float)

geo_df = geopandas.read_file('census_blocks/CENSUS2010BLOCKS_POLY.shp')

# pdb.set_trace()

merged_df = pd.merge(geo_df, df, left_on=["BLOCKCE10","TRACTCE10","COUNTYFP10"], right_on=["census_block","census_tract", "census_county"], how="left")
merged_df.plot(
  cmap='Spectral', 
  column='zscore_smooth_cap',
  legend=True
)

# plt.axis('off')
# plt.show()

plt.savefig(f"/tmp/{YEAR}_map.pdf")
