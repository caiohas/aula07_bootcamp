import csv 

def ler_csv(nome_arquivo_csv: str) -> list[dict]:
    """
    Funcao que le um arquivo csv e retorna uma 
    lista de dicionarios
    """
    lista = []
    with open(nome_arquivo_csv, mode="r", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            lista.append(linha)

    return lista

def filtrar_produtos_nao_entregues(lista: list[dict]) -> list[dict]:
    """
    Funcao que filtra produtos em que entrega = True
    """
    lista_produtos_filtrados = []
    for produto in lista:
        if produto.get("entregue") == "True":
            lista_produtos_filtrados.append(produto)

    return lista_produtos_filtrados

def somar_valores_dos_produtos(lista: list[dict]) -> list[dict]:
    """
    Funcao que soma os valores de venda
    """
    valor_total = 0
    for produto in lista:
        valor_total += int(produto.get("preco"))
    
    return valor_total

