from time import sleep

def maior(*valores):
    print('-=-' * 30)
    if len(valores) == 0:
        return None
    maior_valor = valores[0]
    for valor in valores:
        if valor > maior_valor:
            maior_valor = valor
    print('Analisando os valores passados...')
    for i in valores:
        print(i, end=' ', flush=True)
        sleep(1)
    print(f'Foram informados {len(valores)} valores ao todo.')
    sleep(1)
    print(f'O maior valor informado foi {maior_valor}.')
    sleep(1)



maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
