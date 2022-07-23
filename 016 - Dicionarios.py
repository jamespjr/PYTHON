#lista =[] mutavel
#tupla = () imutavel
#dicionario = {} possivel atribuir valor a variaveis dentro da sentença



pessoa = {'nome': 'João', 'sobrenome': 'Pereira', 'idade': 19}
print(pessoa)

print(pessoa['idade']) #MUDA O VALOR DO ITEM SELECIONADO
pessoa['idade'] = 118

print(pessoa)

pessoa['cnh'] = '0000.2222-2222' #ADICIONA ITENS AO DICIONARIO
print(pessoa)

del pessoa['idade'] #DELETE O ITEM SELECIONADO
print(pessoa)
