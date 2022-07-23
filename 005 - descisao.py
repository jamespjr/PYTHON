#Estrutura de decisão

idade = input("Qual a sua idade?")
idade = int(idade)

if(idade == 18):
    print('A idade é igual a 18 anos!')
#print("")Se o print estiver aqui estará fora da sentença
if(idade < 18):
    print('Você é menor de idade')
if(idade > 18):
    print('Você tem mais de 18 anos...')