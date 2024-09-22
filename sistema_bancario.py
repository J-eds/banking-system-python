name_bank = "DIO BANK"
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

menu = """ 
 Escolha sua opção abaixo

 [D] Depositar
 [S] Sacar
 [E] Extrato
 [Q] Sair

"""

while True:
    
    print(f"Digite a sua opção:")

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Digite o valor à ser depositado: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f'\nVocê depositou R${valor:.2f}.\n')
           
            menu_1 = """===================================================
            
Digite "1" para continuar ou outro número para sair
            
===================================================
>"""
            opcao_1 = input(menu_1)

            if opcao_1 == "1":
                print("")
            else:
                opcao_1 == ""
                print(f'{name_bank} agradece a sua preferência. Até a próxima!')
                break   
                
        
        else:
            print("Valor depositado é inválido.")

    elif opcao == "s":
        valor = float(input("Digite o valor de saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES
        
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
            menu_1 = """\n===================================================
            
Digite "1" para continuar ou outro número para sair
            
===================================================
>"""
            opcao_1 = input(menu_1)
            
            if opcao_1 == "1":
                print("")   
            else:
                opcao_1 == ""
                print(f'{name_bank} agradece a sua preferência. Até a próxima!')
                break    
        else:
            print("O valor informado é inválido.")

    
    elif opcao == "e":
        print(name_bank.center(50," "))
        print("\n=====================Extrato=======================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"Saldo: R$ {saldo:.2f}")
        menu_1 = """\n===================================================
            
Digite "1" para continuar ou outro número para sair
            
===================================================
>"""
        opcao_1 = input(menu_1)
            
        if opcao_1 == "1":
                print("")   
        else:
            opcao_1 == ""
            print(f'{name_bank} agradece a sua preferência. Até a próxima!')
            break    
    
    elif opcao == "q":
        break

    else: 
        print("Operação Invalida, por favor digite uma das opções do menu")

