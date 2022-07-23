cabecalho = "="*10
print(cabecalho ,'Sistema de Cadastro de produtos', cabecalho)
nome = input('Digite o nome do produto:')
descricao = input('Digite a descrição do produto:')
valor = input('Digite o valor do produto: ')
valor = float(valor) #float
quantidade = input('Digite a quantidade do produto: ')
perecivel = input('Perecível? Sim ou Não? ')

print('O produto',nome,'\nDo tipo:',descricao,'\nCusta por unidade: R$',valor,'reais','\nPossui',quantidade,'unidades em estoque disponivel','\nÉ perecível?',perecivel,'\n','\nO proutos acima foi cadastrado com sucesso!!')
print('O tipo de classe é ',type(valor))