print('Bem - vindo a sorveteria do Paulo Cesar Baeta Artur')
print('-------------------------------------------Cardápio-----------------------------------------------------')
print('|  Código  |  Descrição            |  Tamanho P (500ml)  |  Tamanho M (1000ml)  |  Tamanho G (2000ml)  |')
print('|    TR    |  Sabores Tradicionais |        R$ 6,00      |        R$ 10,00      |        R$ 18,00      |\n'
      '|    ES    |  Sabores Especiais    |        R$ 7,00      |        R$ 12,00      |        R$ 21,00      |\n'
      '|    PR    |  Sabores Premium      |        R$ 8,00      |        R$ 14,00      |        R$ 24,00      |')
print('--------------------------------------------------------------------------------------------------------')
TR = 'Tradicional'
ES = 'Especial'      # Sabores usados nas impressões
PR = 'Premium'
#----------------
P = 'Pequeno'
M = 'Medio'        # Tamanhos usados nas impressões
G = 'Grande'
acumulador = int(0)
while True:
    tamanho = input('Escolha o tamanho do pote (P/M/G): ') # estrada do usuário para escolher tamanho do pote
    if tamanho != 'P' and tamanho != 'M' and tamanho != 'G':
        print(f"Você digitou '{tamanho}' esse é TAMANHO invalido!!!!\n"
              f">TENTE NOVAMENTE<")
        continue # Faz com que o usuário retorne para digitar corretamente
    cod = input('Escolha o cod do sabor desejado (TR/ES/PR): ') # estrada do usuário para escolher sabor
    if cod != 'TR' and cod != 'ES' and cod != 'PR':
        print(f"Você digitou '{cod}' e esse CÓDIGO é invalido!!!!\n"
              f">TENTE NOVAMENTE<")
        continue # Faz com que o usuário retorne para digitar corretamente


    if cod == 'TR' and tamanho == 'P':
        print(f"-------Seu pedido---------\n"
              f"-sorvete '{TR}'\n"              # Se o Sabor for TR e Tamanho P entra nessa opção
              f"-Tamanho '{P}'\n\n"
              f"-Valor : R$ 6.00 reais!\n"
              f"---------------------------")
        acumulador = acumulador + 6     # os acumuladores de preço para gerar a soma e o valor final
    if cod == 'TR' and tamanho == 'M':
        print(f"-------Seu pedido---------\n"
              f"-sorvete '{TR}'\n"              # Se o Sabor for TR e Tamanho M entra nessa opção
              f"-Tamanho '{M}'\n\n"
              f"-Valor : R$ 10.00 reais!\n"
              f"---------------------------")
        acumulador = acumulador + 10    # os acumuladores de preço para gerar a soma e o valor final
    if cod == 'TR' and tamanho == 'G':
        print(f"-------Seu pedido---------\n"
              f"-sorvete '{TR}'\n"              # Se o Sabor for TR e Tamanho G entra nessa opção
              f"-Tamanho '{G}'\n\n"
              f"-Valor : R$ 18.00 reais!\n"
              f"---------------------------")
        acumulador = acumulador + 18    # os acumuladores de preço para gerar a soma e o valor final
    if cod == 'ES' and tamanho == 'P':
        print(f"-------Seu pedido---------\n"
              f"-sorvete '{ES}'\n"              # Se o Sabor for ES e Tamanho P entra nessa opção
              f"-Tamanho '{P}'\n\n"
              f"-Valor : R$ 7.00 reais!\n"
              f"---------------------------")
        acumulador = acumulador + 7    # os acumuladores de preço para gerar a soma e o valor final
    if cod == 'ES' and tamanho == 'M':
        print(f"-------Seu pedido---------\n"
              f"-sorvete '{ES}'\n"               # Se o Sabor for ES e Tamanho M entra nessa opção
              f"-Tamanho '{M}'\n\n"
              f"-Valor : R$ 12.00 reais!\n"
              f"---------------------------")
        acumulador = acumulador + 12    # os acumuladores de preço para gerar a soma e o valor final
    if cod == 'ES' and tamanho == 'G':
        print(f"-------Seu pedido---------\n"
              f"-sorvete '{ES}'\n"               # Se o Sabor for ES e Tamanho G entra nessa opção
              f"-Tamanho '{G}'\n\n"
              f"-Valor : R$ 21.00 reais!\n"
              f"---------------------------")
        acumulador = acumulador + 21    # os acumuladores de preço para gerar a soma e o valor final
    if cod == 'PR' and tamanho == 'P':
        print(f"-------Seu pedido---------\n"
              f"-sorvete '{PR}'\n"                # Se o Sabor for PR e Tamanho P entra nessa opção
              f"-Tamanho '{P}'\n\n"
              f"-Valor : R$ 8.00 reais!\n"
              f"---------------------------")
        acumulador = acumulador + 8    # os acumuladores de preço para gerar a soma e o valor final
    if cod == 'PR' and tamanho == 'M':
        print(f"-------Seu pedido---------\n"
              f"-sorvete '{PR}'\n"               # Se o Sabor for PR e Tamanho M entra nessa opção
              f"-Tamanho '{M}'\n\n"
              f"-Valor : R$ 14.00 reais!\n"
              f"---------------------------")
        acumulador = acumulador + 14            # os acumuladores de preço para gerar a soma e o valor final
    if cod == 'PR' and tamanho == 'G':
        print(f"-------Seu pedido---------\n"
              f"-sorvete '{PR}'\n"              # Se o Sabor for PR e Tamanho G entra nessa opção
              f"-Tamanho '{M}'\n\n"
              f"-Valor : R$ 24.00 reais!\n"
              f"---------------------------")
        acumulador = acumulador + 24   # os acumuladores de preço para gerar a soma e o valor final

    maisPedidos = input('Gostaria de realizar mais pedidos? (S/N): ') # entrada para o usuário caso queira continuar seu pedido, caso não ele finaliza e ja da o o valor total
    if maisPedidos == 'S':
        continue # Faz com que o usuário continue comprando
    else:
        print(f'----------------------------------------------------\n'
              f'Valor total a ser pago é R${acumulador:.2f} reais.\n' # Mensagem final com o valor a pagar!
              f'----------------------------------------------------')
        break