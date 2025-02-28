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
LIMITE_SQUES = 3

while True:

          opcao = input(menu)


          if opcao == "1":
                    valor = float(input("Digite o valor do depósito:"))

                    if valor > 0:
                            saldo += valor
                            extrato += f"Depósito: R$ {valor:.2f}\n"
                            print(f"\n######Saldo: R$ {saldo:.2f}######\n")
                            print("Depósito realizado com sucesso!")

                    else:
                            print("Deposito falhou! Valor inválido.")



          elif opcao == "2":
                    valor = float(input("Digite o valor do saque: "))

                    excedeu_saldo = valor > saldo

                    excedeu_limite = valor > limite

                    excedeu_saque = numero_saques >= LIMITE_SQUES

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


          elif opcao == "3":
                    print("\n########EXTRATO########")
                    print("Não foram realizadas movimentações." if not extrato else extrato)
                    print(f"Saldo: R$ {saldo:.2f}")
                    print("########################")


          elif opcao == "s":
                    break

          else:print("Opraçao inválida, seleciona outra opção desejada.")
print("Obrigado! Tenha um excelente dia!")