from random import randint

valores = []

def sorteia():
    print(f'Sorteando {len(valores)} valores da lista: ', end=' ')
    for i in range(0, 5):
        valores.append(randint(1, 10))
        print(valores[i], end=' ', flush=True)
    print('PRONTO!')

def somaPar():
    print(f'Somando os valores pares de {valores}, temos ', end=' ')
    soma = 0
    for i in valores:
        if i % 2 == 0:
            soma += i
    print(soma)


sorteia()
somaPar()
