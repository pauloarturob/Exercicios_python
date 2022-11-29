print('Bem-vindo a loja do Paulo Cesar Baeta Artur') # Nome da loja

vlrproduto = float(input('Digite o valor do produto: ')) # declaração de entrar do valor do produto
qtdproduto = int(input('Digite a quantidade desejada: ')) # dedclaração de entra da quantidade de produtos

emb1 = 30 # Valor da embalagem ate 11 unidades
emb2 = 60 # Valor da embalagem ate 101 unidades
emb3 = 120 # Valor da embalagem ate 1001 unidades
emb4 = 240 # Valor da embalagem acima 1001 unidades

# Quando o usuário seleciona a quantidade entre 0 e 11
if 0 <= qtdproduto < 11:
    total = qtdproduto * vlrproduto # Cálculo da entrada do valor X quantidade + embalagem
    print(f'O valor sem frete foi : R$ {total :.2f} reais\n'
          f'O valor com frete foi : R$ {total + emb1:.2f} reais  (frete de R$ {emb1:.2f})')
# Quando o usuário seleciona a quantidade entre 11 e 101
elif 11 <= qtdproduto < 101:
    total = qtdproduto * vlrproduto # Cálculo da entrada do valor X quantidade + embalagem
    print(f'O valor sem frete foi : R$ {total :.2f} reais\n'
          f'O valor com frete foi : R$ {total + emb2:.2f} reais  (frete de R$ {emb2:.2f})')
# Quando o usuário seleciona a quantidade entre 101 e 1001
elif 101 <= qtdproduto < 1001:
    total = qtdproduto * vlrproduto  # Cálculo da entrada do valor X quantidade + embalagem
    print(f'O valor sem frete foi : R$ {total :.2f} reais\n'
          f'O valor com frete foi : R$ {total + emb3:.2f} reais  (frete de R$ {emb3:.2f})')
# E quando a quantidade for maior que 1001
else:
    qtdproduto > 1001
    total = qtdproduto * vlrproduto  # Cálculo da entrada do valor X quantidade + embalagem
    print(f'O valor sem frete foi : R$ {total :.2f} reais\n'
          f'O valor com frete foi : R$ {total + emb4:.2f} reais  (frete de R$ {emb4:.2f})')
print('Muito obrigado por comprar em nossa loja!\n\n'
      '--------------Volte sempre--------------')