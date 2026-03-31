def área():
    print('Controle de Terrenos')
    print('-------------------')
    largura = float(input('LARGURA (m): '))
    comprimento = float(input('COMPRIMENTO (m): '))
    área = largura * comprimento
    print(f'A área de um terreno {largura}x{comprimento} é de {área:.1f} m².')


área()
