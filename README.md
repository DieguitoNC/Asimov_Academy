# Coluna (SERIES)
- Se chama "series"

## Pd.series
- A
```
pd.Series(data=labels, index=minha_lista)
```
- Os dados são o que consideramos primeiro e em segundo o índice para acessar esses dados.
- Obs - O indice nao precisa ser numerico


## Data frame
- Tabelas / composições de Series

## Métodos
### Dados ausentes
- Posso usar 
```
df.dropna 

df.fillna
```
#### Dropna
- Vai retirar as linhas com número zero, caso eu queira tirar as colunas, coloco 'dropna(axis=1)'
#### fillna
- Vai colocar um valor para dados ausentes

## Hierarquia de índices múltiplos
- Baiscamente vamos criar uma tabela composta
```
# Níveis de Índice

outside = ['G1','G1','G1','G2','G2','G2']

inside = [1,2,3,1,2,3]

hier_index = list(zip(outside,inside))

hier_index = pd.MultiIndex.from_tuples(hier_index)



df = pd.DataFrame(np.random.randn(6,2),index=hier_index,columns=['A','B'])
```

## Group by -> Igual no SQL
- Vai pegar os dados e fazer um "agrupamento" dos valores conforme o parâmetro definido
```
 por_companhia = df.groupby("Empresa")

por_companhia.describe()
```
- Esse último vai pegar todas as estátisticas "basicas" para fazer a conta

## Mesclar, Juntar, e concatenar
### Concatenação 
- As dimensões devem ser correspondentes, vai juntar os diferentes DataFrames em um só
- Caso não sejam iguais, vai ficar com "NaN" nas partes que são vazias
```
pd.concat([df1,df2,df3])
```

### Mesclar
- Vai mesclar os dados
- Basicamente vai pegar os dados em comum, e adicionar as colunas nas tabelas
```
pd.merge(esquerda,direita,how='inner',on='key')
```
- Caso as colunas tiverem algum dado que não coexiste em alguma tabela, ela por padrão vai pegar aquelas que tem em comum e excluir os outros
- Para juntar todas as opções, podemos usar o merge com "how" para incluir todos os casos e o que não tiver dados fica como nulo
```
pd.merge(esquerda, direita, how='right', on=['key1', 'key2'])
```
### Juntar
- combinar colunas diferentes de dataframes conectados
- adiciona "NaN" naquele que tem dado vazio
```
esquerda.join(direita)
```


