numero = int(input('Escreva um número para ver sua tabuada: '))
print(f'Tabuada do {numero}:')
for i in range(1, 11):
    print(f'{numero} x {i} = {numero * i}')