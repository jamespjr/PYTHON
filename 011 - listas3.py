lista = ['Blumenau', 'São Paulo', 'Paris', 'Madri', 'Londres']

lista[1] = 'Belo horizonte' #Substituir uma posição na lista
print(lista)

lista[1] = 10 #Possivel adicionar um int a lista de strings
print(lista)

print(lista[4])
lista.append('Liverpool')
print(lista[-1])#-1 procura o ultimo item da lista