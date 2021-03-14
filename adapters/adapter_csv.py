import csv


def carregar_conteudo_csv(nome_arquivo):
    lista_informacoes = []
    with open(f"{nome_arquivo}") as arquivo:
        conteudo = csv.DictReader(arquivo, fieldnames=["Conta", "Saldo"])
        for linha in conteudo:
            lista_informacoes.append(linha)
        return lista_informacoes


def salvar_conteudo_csv(nome_arquivo, valores_atualizados):
    with open(f"{nome_arquivo}", "w", newline="") as arquivo:
        for linha in valores_atualizados:
            conta = linha["Conta"]
            valor_conta = linha["Saldo"]
            escrita = csv.writer(arquivo)
            escrita.writerow([conta, valor_conta])
    return f"Conteudo inserido com sucesso"
