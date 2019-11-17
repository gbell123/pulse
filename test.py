import geopandas
import matplotlib.pyplot as plt
import pandas as pd
import subprocess

import pdb

MIN_YEAR = 1990
MAX_YEAR = 2018

current_year = MIN_YEAR
big_df = pd.read_csv('data.csv', dtype=str)
# big_df = big_df[pd.notnull]
big_df.zscore_smooth_cap = big_df.zscore_smooth_cap.astype(float)
while current_year <= MAX_YEAR:
  filename = f'/tmp/maps/{current_year}_map.png'
  print(f'{filename} started..')

  df = big_df[big_df['yearer'] == f'{current_year}']
  df.census_county = '0' + df.census_county

  geo_df = geopandas.read_file('census_blocks/CENSUS2010BLOCKS_POLY.shp')

  merged_df = pd.merge(
    geo_df, df, 
    left_on=['BLOCKCE10','TRACTCE10','COUNTYFP10'], 
    right_on=['census_block','census_tract', 'census_county'], 
    how='left'
  )
  merged_df.plot(
    cmap='YlOrBr', 
    column='zscore_smooth_cap',
    legend=True,
    vmin=big_df.zscore_smooth_cap.min(),
    vmax=big_df.zscore_smooth_cap.max()
  )
  merged_df = merged_df[pd.notnull(merged_df['zscore_smooth_cap'])]

  plt.axis('off')
  # plt.show()

  plt.title(current_year)
  plt.savefig(filename)
  print(f'{filename} saved!')
  current_year += 1

input_pngs = 'maps/*.png'
output = '/tmp/gifs/output.gif'
subprocess.call(f'convert -delay 100 -loop 0 {input_pngs} {output}', shell=True)
print(f'gif completed!')
