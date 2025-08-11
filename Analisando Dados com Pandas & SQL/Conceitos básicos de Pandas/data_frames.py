#%%
import pandas as pd
import numpy as np
# %%

from numpy.random import randn
# %%
df = pd.DataFrame(randn(5,4), index=["A","B","C","D","E"],columns="W X Y Z".split())
# %%
df
# %%
type(df)
# %%
df[['W',"X"]]
# %%

df["new"] = df["W"] + df["Y"]
# %%
df
# %%

df2 = df.drop('new', axis=1)
# %%
df2
# %%
df.drop('new', axis=1,inplace=True)
# %%
df
# %%

df.loc[['A','B'], ['W']]
# %%

df.iloc[0,2]

# %%

df
# %%
df.iloc[:-1, 1:4]
# %%
df
# %%
df>0
# %%
df[df>0]
# %%
df
# %%
df['Y'] >0
# %%
df[df['Y']> 0]
# %%
df[(df['Y']> 0) & (df['Z']> 0)]
# %%
df
# %%
# OPERACOES COM ÍNDICE

df.index
# %%
df.columns
# %%
df.reset_index()
# %%
df
# %%
df.reset_index(inplace=True)
# %%
df
# %%
df.set_index("index", inplace=True)
# %%
df
# %%
novoind = 'CA NY WY OR CO'.split()
# %%
novoind
# %%
df["novo_index"] = novoind
# %%
df
# %%
df.reset_index().set_index("novo_index")
# %%
df
# %%
