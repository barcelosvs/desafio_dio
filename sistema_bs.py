# Sistema bancário simples

def main():
    saldo = 0.0
    extrato = []
    LIMITE_SAQUE = 500.0
    LIMITE_SAQUES_DIARIOS = 3
    saques_realizados = 0

    while True:
        print("\nEscolha uma operação:")
        print("[d] Depositar")
        print("[s] Sacar")
        print("[e] Extrato")
        print("[q] Sair")
        opcao = input("=> ").lower()

        if opcao == 'd':
            valor = float(input("Informe o valor do depósito: "))
            if valor > 0:
                saldo += valor
                extrato.append(f"Depósito: R${valor:.2f}")
                print(f"Depósito de R${valor:.2f} realizado com sucesso.")
            else:
                print("Valor inválido para depósito.")

        elif opcao == 's':
            if saques_realizados >= LIMITE_SAQUES_DIARIOS:
                print("Limite diário de saques atingido.")
                continue
            valor = float(input("Informe o valor do saque: "))
            if valor <= 0:
                print("Valor inválido para saque.")
            elif valor > saldo:
                print("Saldo insuficiente para saque.")
            elif valor > LIMITE_SAQUE:
                print(f"Limite máximo por saque é R${LIMITE_SAQUE:.2f}.")
            else:
                saldo -= valor
                extrato.append(f"Saque:    R${valor:.2f}")
                saques_realizados += 1
                print(f"Saque de R${valor:.2f} realizado com sucesso.")

        elif opcao == 'e':
            print("\n========== EXTRATO ==========")
            if not extrato:
                print("Não foram realizadas movimentações.")
            else:
                for operacao in extrato:
                    print(operacao)
            print(f"\nSaldo atual: R${saldo:.2f}")
            print("=============================")

        elif opcao == 'q':
            print("Saindo do sistema. Obrigado!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
