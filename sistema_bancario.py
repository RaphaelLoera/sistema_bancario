menu = """ 
   [1] Depositar
   [2] Sacar
   [3] Extrato
   [s] Sair
   
   ==>    """
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

def depositar(saldo, extrato):
    valor = float(input("Digite o valor do depósito:"))
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print(f"\n###### Saldo: R$ {saldo:.2f} ######\n")
        print("Depósito realizado com sucesso!")
    else:
        print("Depósito falhou! Valor inválido.")
    return saldo, extrato

def sacar(saldo, extrato, numero_saques, limite, LIMITE_SAQUES):
    valor = float(input("Digite o valor do saque: "))
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saque = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print("Saque falhou! Saldo insuficiente.")
    elif excedeu_limite:
        print("Saque falhou! Limite excedido.")
    elif excedeu_saque:
        print("Saque falhou! Limite de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
    else:
        print("Saque falhou! Valor inválido.")
    return saldo, extrato, numero_saques

def exibir_extrato(saldo, extrato):
    print("\n######## EXTRATO ########")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"Saldo: R$ {saldo:.2f}")
    print("########################")

while True:
    opcao = input(menu)

    if opcao == "1":
        saldo, extrato = depositar(saldo, extrato)
    elif opcao == "2":
        saldo, extrato, numero_saques = sacar(saldo, extrato, numero_saques, limite, LIMITE_SAQUES)
    elif opcao == "3":
        exibir_extrato(saldo, extrato)
    elif opcao == "s":
        break
    else:
        print("Operação inválida, selecione outra opção desejada.")

print("Obrigado! Tenha um excelente dia!")