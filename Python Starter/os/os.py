# %%
import os


## pega exatamente onde o arquivo está
os.getcwd()
# %%

# lista de todos os arquivos que temos na pasta atual
os.listdir()
# %%

# consigo especificar qual "pasta" eu quero, mostra os arquivos desse destino
os.listdir('c:\\python\\Asimov_Academy')

# %%

#os.chdir()
actual_dir = os.getcwd()
os.chdir('c:\\python\\Asimov_Academy')
print(os.getcwd())
os.chdir(actual_dir)
print(os.getcwd())

# %%

#cria uma pasta
os.mkdir('Pasta2')
# %%

os.rename('teste.txt', 'teste2.txt')

# %%
os.rename('Pasta', 'Pasta3')
# %%

#Posso mover arquivos
os.rename('Pasta2', 'Pasta3/Pasta2')
# %%

os.rename('Pasta3/Pasta2', 'Pasta2')
# %%

os.remove('teste.csv')
# %%

os.rmdir('Pasta2')

# %%
cmd = 'date'
os.system(cmd)
# %%
