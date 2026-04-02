from time import sleep

def contador():
    print('-=-' * 20)

    print('Contagem de 1 até 10 de 1 em 1')
    for i in range(1, 11):
        print(i, end=' ', flush=True)
        sleep(0.5)
    print('FIM!')
    print('-=-' * 20)
    sleep(1)

    print('Contagem de 10 até 0 de 2 em 2')
    for i in range(10, -1 , -2):
        print(i, end=' ', flush=True)
        sleep(0.5)
    print('FIM!')
    print('-=-' * 20)
    sleep(1)

    print(f'Agora é sua vez de personalizar a contagem!')
    início = int(input('Início: '))
    fim = int(input('Fim: '))
    passo = int(input('Passo: '))
    print('-=-' * 20)

    for i in range(início, fim + 1, passo):
        print(i, end=' ', flush=True)
        sleep(0.5)

contador()
