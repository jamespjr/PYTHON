idade = int(input("Digite sua idade: "))

if(idade < 18):
    print('Idade inferior a permitida')

elif(idade == 18):
    print('Idade correta, pode se alistar')
else:
    print('Idade superior a permitida')