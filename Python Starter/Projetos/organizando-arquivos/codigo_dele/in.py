import os
 
cwd = os.getcwd()
full_list = os.listdir(cwd)

#aqui vai retirar tudo que não é arquivo e o executavel python
files_list = [i.lower() for i in full_list if os.path.isfile(i) and '.py' not in i]

# Aqui a logica foi primeiro fazer o split e pegar o que esta no final, ou seja o que vem depois do . teste.mp3, vai pegar mp3.
# Apos isso, precisa retirar da lista o que esta duplicado, por isso transforma em set, depois fazemos lista novamente para manipular

types = list(set([i.split('.')[-1] for i in files_list]))

# aqui vai fazer as pastas conforme os tipos de arquivos
for file_type in types:
    os.mkdir(file_type)


for file in files_list:
    path_from = cwd + '/' + file
    path_to = cwd + '/' + file.split('.')[-1] + '/' + file
    os.replace(path_from, path_to)