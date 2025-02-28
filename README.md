## Sistema Bancário 
**Este é um programa simples de sistema bancário escrito em Python. Ele permite que o usuário realize operações básicas como depósito, saque e visualização de extrato. 
O programa é executado em um loop contínuo até que o usuário escolha sair.**

##### Funcionalidades
* *Depositar: 
Permite ao usuário depositar um valor na conta.*

* *Sacar:
Permite ao usuário sacar um valor da conta, respeitando o saldo disponível, o limite de saque e o número máximo de saques permitidos por dia.
Extrato: Exibe o extrato das transações realizadas e o saldo atual.
Sair: Encerra o programa.*

##### Variáveis
* *Saldo: Armazena o saldo atual da conta.*

 * *Limite: Define o limite máximo para cada saque.*

*  *Extrato: Armazena o histórico das transações realizadas.*

* *Numero_Saques: Conta o número de saques realizados.*

*  *LIMITE_SQUES: Define o número máximo de saques permitidos por dia.*

##### Menu

*O menu é exibido continuamente até que o usuário escolha a opção de sair. As opções disponíveis são:*
   
   *[1] Depositar
   [2] Sacar
   [3] Extrato
   [s] Sair*
   

##### Fluxo do Programa
* *Depósito: Solicita ao usuário o valor do depósito.*
  Verifica se o valor é positivo.
  Atualiza o saldo e o extrato com o valor depositado.

* *Saque: Solicita ao usuário o valor do saque.
Verifica se o valor do saque não excede o saldo, o limite de saque e o número máximo de saques permitidos.
Atualiza o saldo, o extrato e o número de saques realizados.*

* *Extrato: Exibe o extrato das transações realizadas e o saldo atual.*

* *Sair: Encerra o programa.
Exemplo de Uso
Ao executar o programa, o usuário verá o menu e poderá escolher uma das opções. Dependendo da escolha, 
o programa solicitará informações adicionais (como o valor do depósito ou saque) e realizará a operação correspondente.*

