# %%
# Imports
import pandas as pd
import altair as alt

# Get Some Data
cars = pd.read_csv('https://github.com/byuidatascience/data4python4ds/raw/master/data-raw/mpg/mpg.csv')

# Plot some data
alt.Chart(cars).mark_circle().encode(
    x='displ', 
    y='hwy'
)