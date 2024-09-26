import textwrap

def menu():
    menu = """ 
    Escolha sua opção abaixo

    [d]\tDepositar
    [s]\tSacar
    [e]\tExtratos
    [nc]\tNova conta
    [nu]\tNovo usuário
    [lc]\tListar Conta
    [q]\tSair
    → """
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato,/):
    
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print(f'\n==Você depositou R${valor:.2f}com sucesso! ==')
            
    else:
        print("\nValor depositado é inválido.")
    return saldo,extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques
        
    if excedeu_saldo:
        print("Falha na operação. Saldo insuficiente.")
    
    elif excedeu_limite:
        print("Falha na operação. Valor de saque maior que limite disponivel.")

    elif excedeu_saques:
        print("Falha na operação. Número de saques excedido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print(f"\nVocê sacou R$ {valor:.2f}, retire seu dinheiro no local informado.")
    else:
        print("O valor informado é inválido.")

    return saldo, extrato
    
def exibir_extratos(saldo,/,*,extrato):
    print("\n=====================Extrato=======================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"Saldo: R$ {saldo:.2f}")
  
def criar_usuario(usuarios):

    cpf = input("Informe o seu CPF(somente números: )")
    usuario = filtrar_usuario(cpf,usuarios)
    
    if usuario:
        print("\n Já existe usuario com esse CPF!")
        return
    nome = input("Informe seu nome completo: ")
    data_nascimento = input("Digite sua data de nascimento (dd-mm-aaa): ")
    endereco = input("Digite seu endereço(logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento":data_nascimento, "cpf": cpf, "endereco": endereco})
    
    print("== Usuario cadastrado com sucesso! ==")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informo o CPF do usuário: ")
    usuario = filtrar_usuario (cpf, usuarios)

    if usuario:
        print("\n== Conta criada com SUCESSO! ==")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("\n Usuario não encontrado, fluxo de criação de conta encerrado!")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

def main():

    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas =[]
   
    
    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("Digite o valor à ser depositado: "))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor de saque: "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques= LIMITE_SAQUES,
            )
        elif opcao == "e":
            exibir_extratos(saldo, extrato=extrato)
        
        elif opcao == "nu":
            criar_usuario(usuarios)
        
        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)
        elif opcao == "lc":
            listar_contas(contas)
        
        elif opcao == "q":
            break

main ()

    