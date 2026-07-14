id_venda = int(input("Digite o ID da venda: "))
data = str(input("Digite a data da venda: "))
vendedor = str(input("Digite o nome do vendedor: "))
cliente = input("Digite o nome do cliente: ")
produto = input("Digite o nome do produto: ")
categoria = input("Digite a categoria do produto: ")
quantidade = int(input("Digite a quantidade vendida: "))
if quantidade >= 100:
    print("Quantidade indisponível: ")
else:
    quantidade = quantidade
    preco_unitario = float(input("Digite o preço unitário do produto: "))
    condicao_pagamento = str(input("Digite a forma de pagamento: Pagamento a vista =1, pagemento a prazo = 2: "))
    if condicao_pagamento == "1":
        valor_total = quantidade * preco_unitario *0.95
    elif condicao_pagamento == "2":
        valor_total = quantidade * preco_unitario * 1.05
    else:
        print("Forma de pagamento inválida!")
        exit()
    
    print(f"---------EXTRATO DE VENDA: ---------\n"
        f"ID da venda: {id_venda} \n"
        f"Data de realização: {data} \n"
        f"Vendedor: {vendedor} \n"
        f"Cliente: {cliente} \n"
        f"Produto: {produto} \n"
        f"Categoria: {categoria} \n"
        f"Quantidade: {quantidade} \n"
        f"Preço unitário: R$ {preco_unitario} \n"
        f"Valor total da venda: R$ {valor_total}")