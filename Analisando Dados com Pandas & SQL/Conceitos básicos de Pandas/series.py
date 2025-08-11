#%%
import pandas as pd
import numpy as np
# %%

labels =  ['a','b','c']
minha_lista = [10,20,30]
arr = np.array([10,20,30])

d = {'a':10, 'b':20, 'c':30}
# %%

pd.Series(labels)
# %%

pd.Series(data=labels, index=minha_lista)
# %%
pd.Series(labels, minha_lista)
# %%
d
#%% 
pd.Series(d)
# %%

ser1 = pd.Series([1,2,3,4], index = ['Eua', 'Alemanha', 'URSS', 'Japão'])
# %%
ser1
# %%
ser2 = pd.Series([1,2,5,4], index = ['Eua', 'Alemanha', 'Itália', 'Japão'])

# %%
ser2    
# %%
ser1['Eua']
# %%
ser1[['Alemanha', 'URSS']]
# %%
ser1+ser2
# %%
