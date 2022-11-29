
# Inicio da função metragem
def metragem():
    print('---------------------------------Menu 1 de 3 Metragem da Limpeza------------------------------')
    while True: # para que fique em loop caso digite errado/perguntas novas opções
        try:
            metros = int(input('Entre com a metragem da casa (m²): '))
            if metros >= 30 and metros < 300:
                print('Será necessário um(a) funcionário(a) para a limpeza\n'
                      '*********************************************************************')
                return 60 + 0.3 * metros
            elif metros >= 300 and metros < 700:
                print('Será necessário dois(duas) funcionários(as) para a limpeza\n'
                      '*********************************************************************')
                return 120 + 0.5 * metros
            else:
                print('!! Não aceitamos casas com metragem menor que 30m² ou maior que 700m² !!')
        except ValueError: # Caso o usuário não digite números inteiros, como se pede no programa!
            print('>>ATENÇÃO Error<<<\n ---Você tem que digitar somente números inteiros---')
# Fim da função metragem


# Inicio da função tipo
def tipo():
    print('---------------------------------Menu 2 de 3 Tipo de Limpeza----------------------------------')
    print('Entre com o tipo de limpeza:\n'
          'B - Básica -  Indicada para sujeiras semanais ou quinzenais.\n'
          'C - Completa (30% a mais) - Indicada para sujeiras antigas e/ou não rotineiras.')

    while True: # para que fique em loop caso digite errado/perguntas novas opções
        tipo = input('>> ')

        tipo = tipo.upper() # caso usuário digite letras minúsculas, será retornado letras maiúscula
        tipo = tipo.strip() # caso o usuário coloque espaço na hora de digitar na da erro!
        if tipo == 'B':
            print("Você selecionou a limpeza 'BÁSICA'")
            return 1.00
        elif tipo == 'C':
            print("Você selecionou a limpeza 'COMPLETA'")
            return 1.30
        else:
            print(f">>'{tipo}'--!!!!Opção invalida!!!!!--")
            continue
# Fim da função tipo

# Inicio da função adicional
def adicional():
    print('---------------------------------Menu 3 de 3 Adicional de Limpeza-----------------------------')

    acumulador = 0 # e para ir acumulando valores para soma
    while True: # para que fique em loop caso digite errado/perguntas novas opções
        adicional = input('Entre com o tipo de Limpeza\n'
                          '0- Não desejo mais nada (encerrar)\n'
                          '1- Passar 10 peças de roupas - R$ 10,00\n'
                          '2- Limpeza de 1 forno/micro-ondas - R$ 12,00\n'
                          '3- Limpeza de 1 geladeira/freezer - R$ 20,00\n'
                          '>>')
        if adicional == '0':
            return acumulador
        elif adicional == '1':
            acumulador += 10
        elif adicional == '2':
            acumulador += 12
        elif adicional == '3':
            acumulador += 20
        else:
            print(f"'{adicional}' Número incorreto! Digite somente 1, 2, 3, e 0 para finalizar...")
# Fim da função adicional

# Inicio
print('------------Bem-vindo ao Programa de Serviços de Limpeza do Paulo Cesar Baeta Artur-----------')
metragens = metragem()
tipos = tipo()
adicionais = adicional()
res = metragens * tipos + adicionais
print(f'=======================================================================================\n'
      f'O total do serviços R${res:.2f}  (Metragem R${metragens:.2f} * Tipo R${tipos:.2f} + Adicional R${adicionais:.2f})')


