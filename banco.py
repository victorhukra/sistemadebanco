class SaldoInsuficiente(ValueError):
    pass


class SaqueNegativo(ValueError):
    pass


class ClienteNãoEncontrado(Exception):
    pass



def consultarSaldo(cliente, lista):
    if len(lista) != 0:

        encontrado = False
        for c in lista:
            if cliente == c['nome']:
                encontrado = True
                consultaSaldo = c['saldo']
                consultaCliente = c['nome']
                print(f'\nSaldo de {consultaCliente}: R${consultaSaldo}')
                break
        
        if not encontrado:
            raise ClienteNãoEncontrado('Cliente não encontrado')

    else:
        print('Não há ningúem cadastrado no sistema.')

   
def sacarDinheiro(lista, cliente, saldo):
    saldo = getSaldo(lista, clienteSacar)

    if len(lista) != 0:
        saqueDinheiro = float(input('Quantia a sacar: R$'))


        if saqueDinheiro < 0:
            raise SaqueNegativo('Impossível sacar um valor negativo.')


        if saqueDinheiro > saldo:
            raise SaldoInsuficiente('Saldo insuficiente.')
       
        else:
            encontrado = False
            for c in lista:
                if cliente == c['nome']:
                    encontrado = True
                    c['saldo'] -= saqueDinheiro
                    print(f'Saque realizada com sucesso! Novo Saldo: R${c['saldo']}')
               
            if not encontrado:
                raise ClienteNãoEncontrado('Cliente não encontrado.')
   
           
def depositarDinheiro(lista, cliente):
    if len(lista) != 0: 
        
        try:
            encontrado = False
            for c in lista:
                if cliente == c['nome']:
                    while True:
                        try:
                            depositoDinheiro = float(input('Quantia a depositar: R$'))
                            if depositoDinheiro < 0:
                                raise SaqueNegativo('Impossível depositar um valor negativo.')
                            break
                        except SaqueNegativo as e:
                            print(f'Erro: {e}')
                    encontrado = True
                    c['saldo'] += depositoDinheiro
                    print(f'Novo saldo: R${c['saldo']}')
                    break
            
            if not encontrado:
                raise ClienteNãoEncontrado('Cliente não encontrado.')
        except Exception as e:
            print(f'Erro: {e}')
        
    else:
        print('Não há ningúem cadastrado no sistema.')
   
    
def getSaldo(lista, cliente):
    if len(lista) != 0:

        encontrado = False
        for c in lista:
            if cliente == c['nome']:
                saldo = c['saldo']
                encontrado = True
        
        if not encontrado:
            raise ClienteNãoEncontrado('Cliente não encontrado.')
        
    else:
        print('Não há ningúem cadastrado no sistema.')

    return saldo


def showMenu ():
    print('\n---------BANCO---------')
    print('1 - Consultar saldo')
    print('2 - Realizar saque')
    print('3 - Realizar depósito')
    print('4 - Sair')


def cadastrarCliente():
    listaCliente = []

    while True:
        try:
            qtdClienteCadastrar = int(input('\nInforme a quantidade de clientes a cadastrar: '))
            break
        except ValueError:
            print('Informe um valor válido.')

    for i in range(qtdClienteCadastrar):
        nome = input(f'\nCliente ({i+1}) - Nome: ')
        saldo = float(input(f'{nome} - Saldo: '))
        numeroConta = int(input(f'{nome} - Número da conta: '))


        dictCliente = {'nome': nome, 'saldo': saldo, 'numero': numeroConta}
        listaCliente.append(dictCliente)

    return listaCliente


if __name__ == '__main__':

    listaCliente = cadastrarCliente()

    while True:
        try:
        
            showMenu()
            
            opcao = int(input('\nEscolha uma opção: '))
            match opcao:
                case 1:
                    clienteConsultar = input('\nCliente - Nome: ').lower().title()
                    consultarSaldo(clienteConsultar, listaCliente)

                case 2:
                    try:
                        clienteSacar = input('\nCliente - Nome: ')
                        sacarDinheiro(listaCliente, clienteSacar, getSaldo)
                    except ClienteNãoEncontrado as e:
                        print(f'Erro: {e}')
                    
                    except SaldoInsuficiente as e:
                        print(f'Erro: {e}')

                    except SaqueNegativo as e:
                        print(f'Erro: {e}')

                case 3:
                    try:
                        clienteDepositar = input('\nCliente - Nome: ')
                        depositarDinheiro(listaCliente, clienteDepositar)

                    except ClienteNãoEncontrado as e:
                        print(f'Erro: {e}')
        
                case 4:
                    print('Programa encerrado. Volte sempre!')
                    break

        except Exception as e:
            print(f'{e}')



