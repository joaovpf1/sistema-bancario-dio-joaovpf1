menu = """
    Escolha uma opção:
    [1] Sacar
    [2] Depositar
    [3] Visualizar Extrato
    [4] Sair

    => """

saldo = 0
quantidade_saque = 0
extrato = ""

while True:
    opcao = int(input(menu))

    if opcao == 1:
        if quantidade_saque <= 3:
            valor_saque = float(input("Digite o valor que deseja sacar: R$ "))
            if valor_saque <= 500:
                if valor_saque <= saldo:
                    saldo -= valor_saque
                    extrato += f"Saque: R$ {valor_saque:.2f}\n"
                    quantidade_saque += 1
                    print(
                        "Saque efetuado com sucesso, retire seu dinheiro na boca do caixa."
                    )
                    print(f"O valor atual da sua conta é de R$ {saldo:.2f}")
                else:
                    print("Saldo insuficiente.")
            else:
                print(
                    "Valor máximo que é permitido execido, autorizado: R$500,00 por saque."
                )
        else:
            print("Quantidade de saques diários execidos, tente novamente amanhã.")
    elif opcao == 2:
        valor_deposito = float(input("Digite o valor que deseja depositar: R$ "))
        if valor_deposito > 0:
            saldo += valor_deposito
            print(f"Depósito realizado com sucesso. Agora você tem R$ {saldo:.2f}")
            extrato += f"Depósito: R$ {valor_deposito:.2f}\n"
    elif opcao == 3:
        print("\n========== Extrato ==============")
        print(
            "Não foram realizadas movimentações bancárias." if not extrato else extrato
        )
        print("==================================")
        print(f"\nSeu saldo atual é de R$ {saldo:.2f}")
        print("==================================")
    elif opcao == 4:
        break
    else:
        print("Opção inválida, tente novamente.")
