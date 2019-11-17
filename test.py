import geopandas
import matplotlib.pyplot as plt
import pandas as pd
import pdb

MIN_YEAR = 1990
MAX_YEAR = 2018

current_year = MIN_YEAR
while current_year <= MAX_YEAR:
  df = pd.read_csv('data.csv', dtype=str)
  df = df[df['yearer'] == f"{current_year}"]
  df.census_county = '0' + df.census_county
  df.zscore_smooth_cap = df.zscore_smooth_cap.astype(float)

  geo_df = geopandas.read_file('census_blocks/CENSUS2010BLOCKS_POLY.shp')

  merged_df = pd.merge(geo_df, df, left_on=["BLOCKCE10","TRACTCE10","COUNTYFP10"], right_on=["census_block","census_tract", "census_county"], how="left")
  merged_df.plot(
    cmap='Spectral', 
    column='zscore_smooth_cap',
    legend=True
  )

  # plt.axis('off')
  # plt.show()

  plt.savefig(f"/tmp/{current_year}_map.pdf")
