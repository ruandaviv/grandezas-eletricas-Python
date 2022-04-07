print('**********************************************')
print('         CÁLCULO DE GRANDEZAS ELÉTRICAS      ')
print('**********************************************')

print('1. Tensão (em Volt).\n2. Resistência (em Ohm).\n3. Corrente (em Ampére)\n ')
escolha = int(input('Qual grandeza deseja calcular? '))

if escolha == 1:
    R = float(input('Insira o valor da Resistência: '))
    I = float(input('Insira o valor da Corrente: '))
    U = R * I
    print(f'\nU = {U:.2f} V')
elif escolha == 2:
    U = float(input('Insira o valor da Tensão: '))
    i = float(input('Insira o valor da Corrente: '))
    R = U / i
    print(f'\nR= {R:.2f} Ohm')
elif escolha == 3:
    U = float(input('Insira o valor da Tensão: '))
    R = float(input('Insira o valor da Resistência: '))
    i = U / R
    print(f'\ni = {i} A')
elif escolha < 1 or escolha > 3:
    print('O valor escolhido não está disponível.')
