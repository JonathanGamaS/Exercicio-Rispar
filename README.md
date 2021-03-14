#Introdução

* Conforme exercício proposto existem dois arquivos CSV. Um contendo o numero da conta e saldo atual, outro para registrar as transações ocorridas.

##Como Utilizar?

* Executar o arquivo transacoes na pasta code

* Inserir no arquivo transações o que deseja fazer e em qual conta, por default já existem as contas:


* 123,1000000
* 456,2000000
* 789,3000000

Existem algumas operações prontas no arquivo, caso queira realizar uma nova, só adicionar no arquivo. Exemplo:

* Saque na conta 123 de 500:
* run_app.retirada(123, 50000)


* Deposito na conta 123 de 500
* run_app.deposito(123, 50000)


No caso de uma conta que não existe no csv de contas, não será possível realizar deposito e nem retiradas.