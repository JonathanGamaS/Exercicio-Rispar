from adapters.adapter_csv import carregar_conteudo_csv, salvar_conteudo_csv

arquivo_conta = "contas.csv"
arquivo_transacoes = "transacoes.csv"


class Orchestrator:

    def __init__(self):
        self.conteudo_conta = carregar_conteudo_csv(arquivo_conta)
        self.conteudo_transacao = carregar_conteudo_csv(arquivo_transacoes)

    def retirada(self, conta, valor):
        conta_inexistente = 1
        try:
            valores_conta = self.conteudo_conta
            valores_transacao = self.conteudo_transacao
            for linha in valores_conta:
                numero_conta = int(linha["Conta"])
                if numero_conta == conta:
                    valor_conta = int(linha["Saldo"])
                    valor_conta = valor_conta - valor
                    if valor_conta < 0:
                        valor_conta = valor_conta - 500
                    linha["Saldo"] = valor_conta
                    valor_log = {"Conta": conta, "Saldo": f"-{valor}"}
                    valores_transacao.append(valor_log)
                    conta_inexistente = 0
            if conta_inexistente == 0:
                salvar_conteudo_csv(arquivo_conta, valores_conta)
                salvar_conteudo_csv(arquivo_transacoes, valores_transacao)
                return f"Retirada de {valor} na conta {conta}. Saldo de {valor_conta}"
            else:
                return "Conta inexistente, faça cadastro primeiro"
        except Exception as e:
            raise e

    def deposito(self, conta, valor):
        conta_inexistente = 1
        try:
            valores_conta = self.conteudo_conta
            valores_transacao = self.conteudo_transacao
            for linha in valores_conta:
                numero_conta = int(linha["Conta"])
                if numero_conta == conta:
                    valor_conta = int(linha["Saldo"])
                    valor_conta = valor_conta + valor
                    linha["Saldo"] = valor_conta
                    valor_log = {"Conta": conta, "Saldo": f"{valor}"}
                    valores_transacao.append(valor_log)
                    conta_inexistente = 0
            if conta_inexistente == 0:
                salvar_conteudo_csv(arquivo_conta, valores_conta)
                salvar_conteudo_csv(arquivo_transacoes, valores_transacao)
                return f"Deposito de {valor} na conta {conta}. Saldo de {valor_conta}"
            else:
                return "Conta inexistente, faça cadastro primeiro"
        except Exception as e:
            raise e


run_app = Orchestrator()