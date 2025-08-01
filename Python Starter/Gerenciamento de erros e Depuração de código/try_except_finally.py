# %%
x = [1,2,3]
y = 1
x+y
# %%
x = [1,2,3]
y = 1
try:
    
    x+y
    x=1
    y=1
except Exception as e:
    print("Erro: {}".format(e))
finally:
    print("Olá")
# %%
