from etl import ler_csv, filtrar_produtos_nao_entregues, somar_valores_dos_produtos

path_arquivo = "vendas.csv"

lista_produtos_vendidos = ler_csv(path_arquivo)
produtos_entregues = filtrar_produtos_nao_entregues(lista_produtos_vendidos)
valor_dos_produtos_entregues = somar_valores_dos_produtos(produtos_entregues)

print(valor_dos_produtos_entregues)