# Sistema bancario modularizado

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if valor > saldo:
        print("Saldo insuficiente.")
    elif valor > limite:
        print("O valor do saque excede o limite por operação.")
    elif numero_saques >= limite_saques:
        print("Número máximo de saques diários atingido.")
    elif valor <= 0:
        print("Valor inválido.")
    else:
        saldo -= valor
        extrato += f"Saque:    R$ {valor:.2f}\n"
        numero_saques += 1
        print("Saque realizado com sucesso.")
    return saldo, extrato, numero_saques

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("Depósito realizado com sucesso.")
    else:
        print("Valor inválido.")
    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("\n===== EXTRATO =====")
    print(extrato if extrato else "Não foram realizadas movimentações.")
    print(f"\nSaldo atual: R$ {saldo:.2f}")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    usuario = [u for u in usuarios if u["cpf"] == cpf]
    
    if usuario:
        print("Já existe um usuário com esse CPF.")
        return
    
    nome = input("Nome completo: ")
    nascimento = input("Data de nascimento (dd-mm-aaaa): ")
    endereco = input("Endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({
        "nome": nome,
        "data_nascimento": nascimento,
        "cpf": cpf,
        "endereco": endereco
    })

    print("Usuário criado com sucesso.")

def criar_conta(agencia, numero_conta, usuarios, contas):
    cpf = input("Informe o CPF do usuário: ")
    usuario = next((u for u in usuarios if u["cpf"] == cpf), None)

    if not usuario:
        print("Usuário não encontrado. Crie o usuário antes.")
        return
    
    conta = {
        "agencia": agencia,
        "numero": numero_conta,
        "usuario": usuario
    }

    contas.append(conta)
    print("Conta criada com sucesso.")

def listar_contas(contas):
    for conta in contas:
        usuario = conta["usuario"]
        print(f"Agência: {conta['agencia']} | Conta: {conta['numero']} | Titular: {usuario['nome']}")

if __name__ == "__main__":
    LIMITE_SAQUES = 3
    LIMITE_SAQUE_VALOR = 50000
    AGENCIA = "0001"
    
    saldo = 0
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []
    numero_conta = 1

    while True:
        print("\n===== MENU =====")
        print("[d] Depositar")
        print("[s] Sacar")
        print("[e] Extrato")
        print("[nu] Novo Usuário")
        print("[nc] Nova Conta")
        print("[lc] Listar Contas")
        print("[q] Sair")
        opcao = input("Escolha uma opção: ").lower()

        if opcao == "d":
            valor = float(input("Valor do depósito: R$ "))
            saldo, extrato = depositar(saldo, valor, extrato)
        elif opcao == "s":
            valor = float(input("Valor do saque: R$ "))
            saldo, extrato, numero_saques = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=LIMITE_SAQUE_VALOR,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES
            )
        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)
        elif opcao == "nu":
            criar_usuario(usuarios)
        elif opcao == "nc":
            criar_conta(AGENCIA, numero_conta, usuarios, contas)
            numero_conta += 1
        elif opcao == "lc":
            listar_contas(contas)
        elif opcao == "q":
            print("Saindo...")
            break
        else:
            print("Opção inválida.")
