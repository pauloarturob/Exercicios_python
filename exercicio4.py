
# ------------Inicio Variáveis Globais----------------
lista_funcionario = []
cod_funcionario = 7400
# ------------Fim Variáveis Globais----------------


# ------------Inicio Cadastro de Funcionário-----------
def cadastrar_funcionario(id):
      print('--------------------------------- MENU CADASTRAR FUNCIONÁRIO ---------------------------------')
      # id = input('Digite o ID do funcionário: ')
      nome = input('Digite o NOME do funcionário: ')
      setor = input('Digite o SETOR do funcionário: ')
      salario = input('Digite o SALÁRIO do funcionário: ')
      # print(f'O codigo do funcionário é: {id} ')
      print('----------------------------------')

      dadosFuncionario = {'Id': id, 'Nome': nome, 'Setor': setor, 'Salário': salario} # a variavel 'dadosFuncionarios' cria um dicionario para ser usado depois
      lista_funcionario.append(dadosFuncionario.copy()) # essa linha copia e adiciona os dados a uma lista

# ------------Fim Cadastro de Funcionário-----------


# ------------Inicio Consulta de Funcionário-----------
def consultar_funcionario():
      while True:
            print('--------------------------------- MENU CONSULTAR FUNCIONÁRIO ---------------------------------')
            opcao_consultar = (input('Escolha a opção desejada:\n'
                        '1-Consultar todos os funcionários\n'
                        '2-Consultar funcionários por ID\n'
                        '3-Consultar funcionários por SETOR\n'
                        '4-Retornar\n'
                        '>>> '))
            if opcao_consultar == '1':
                  print('-------------------------Consultar todos funcionários selecionado------------------------')
                  for funcionario in lista_funcionario: # Funcionario vai varrer toda a lista de funcionario (listaFuncionario)
                        print('----------------')
                        for key, value in funcionario.items(): #Varrer todos conjuntos keys(chaves) e value(valor) da biblioteca
                              print(f'{key}: {value}')

            elif opcao_consultar == '2':
                  print('-------------------------Consultar funcionários por ID selecionado------------------------')
                  consulta_id = int(input('Digite o ID do Funcionário: '))
                  for funcionario in lista_funcionario:
                        if funcionario['Id'] == consulta_id: # O valor campo Id desse dicionario(biblioteca) é igual o valor desejado
                              print('----------------')
                              for key, value in funcionario.items():  # Varrer todos conjuntos keys(chaves) e value(valor) da biblioteca
                                    print(f'{key}: {value}')


            elif opcao_consultar == '3':
                  print('-------------------------Consultar funcionário por SETOR selecionado------------------------')
                  consulta_setor = input('Digite o SETOR do Funcionário: ')
                  for funcionario in lista_funcionario:
                        if funcionario['Setor'] == consulta_setor:  # O valor campo Id desse dicionario(biblioteca) é igual o valor desejado
                              print('----------------')
                              for key, value in funcionario.items():  # Varrer todos conjuntos keys(chaves) e value(valor) da biblioteca
                                    print(f'{key}: {value}')

            elif opcao_consultar == '4':
                  return # sai do menu consultar e volta para menu incial

            else:
                  print('Opção Invalida, tente outra vez')
                  continue

# ------------Fim Cadastro de Funcionário-----------


# ------------Inicio Remover Funcionário-----------
def remover_funcionario():
      print('--------------------------------- MENU REMOVER FUNCIONÁRIO ---------------------------------')
      remove_funcionario = int(input('Digite o ID do Funcionário para remover: '))
      for funcionario in lista_funcionario:
            if funcionario['Id'] == remove_funcionario:  # O valor campo Id desse dicionario(biblioteca) é igual o valor desejado
                  print('----------------')
                  lista_funcionario.remove(funcionario)
                  print('Funcionário removido')
                  print('----------------\n')


# ------------Fim Remover Funcionário-----------

# ------------Inicio Main-----------
print('\n---Seja bem-vindo ao controle de funcionários do Paulo Cesar Baeta Artur---')
print('*'* 81)
print('--------------------------------- MENU PRINCIPAL ---------------------------------')
while True:
      opcao_principal = (input('Escolha a opção desejada:\n'
      '1-Cadastrar Funcionario\n'
      '2-Consultar Funcionario(s)\n'
      '3-Remover Funcionario\n'
      '4-Sair\n'
      '>>> '))

      if opcao_principal == '1':
            cod_funcionario = cod_funcionario + 1
            cadastrar_funcionario(cod_funcionario)
      elif opcao_principal == '2':
            consultar_funcionario()
      elif opcao_principal == '3':
            remover_funcionario()
      elif opcao_principal == '4':
            break
      else:
            print('Opção Invalida, tente outra vez')
            continue
# ------------Fim Main-----------