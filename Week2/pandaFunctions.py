# %%
import pandas as pd
import altair as alt

# %%
df = pd.DataFrame(
{"a" : [5, 4, 6, 2, 3],
"b" : [7, 8, 9, 10, 11],
"c" : [10, 11, 12, 101, 0]})

# %%
df = df.rename(columns = {'a':'ducks'})
df

# %%
df = df[['ducks', 'b']]
df

# %%
df = df[df.b < 9]
df
# %%
