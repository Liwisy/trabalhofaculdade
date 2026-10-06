renda_mensal = 0.0
gastos = [] # Lista que vai guardar os gastos

# Laço principal (while) para manter o programa a funcionar até escolher Sair
while True:
    print("\n-----------------------------")
    print("     CONTROLE FINANCEIRO")
    print("-----------------------------")
    print("1 - Informar renda mensal")
    print("2 - Cadastrar gasto")
    print("3 - Consultar gastos")
    print("4 - Consultar situação financeira")
    print("5 - Ver estatísticas")
    print("6 - Sair")
    print("-----------------------------")
    
    opcao = input("Escolha uma opção: ")
    
    # Estruturas condicionais (if/elif/else) para o menu
    if opcao == '1':
        # Uso do tipo float
        renda_mensal = float(input("Informe o valor da sua renda mensal: R$ "))
        print("Renda atualizada com sucesso!")
        
    elif opcao == '2':
        # Coletando os dados conforme o exemplo do slide
        descricao = input("Descrição (ex: Mercado): ")
        valor = float(input("Valor: R$ "))
        
        print("\nCategoria:")
        print("1 - Alimentação")
        print("2 - Transporte")
        print("3 - Lazer")
        print("4 - Saúde")
        print("5 - Outros")
        categoria = input("Escolha uma categoria (1 a 5): ")
        
        # Guardando as 3 informações juntas numa pequena lista dentro da lista principal
        novo_gasto = [descricao, valor, categoria]
        gastos.append(novo_gasto)
        print("Gasto cadastrado com sucesso!")
        
    elif opcao == '3':
        print("\n--- Seus Gastos ---")
        if len(gastos) == 0:
            print("Nenhum gasto cadastrado.")
        else:
            # Laço for para listar os itens
            for item in gastos:
                print(f"Descrição: {item[0]} | Valor: R$ {item[1]} | Categoria: {item[2]}")
                
    elif opcao == '4':
        print("\n--- Situação Financeira ---")
        total_gasto = 0.0
        
        # Laço for para somar os valores
        for item in gastos:
            total_gasto = total_gasto + item[1]
            
        saldo = renda_mensal - total_gasto
        
        print(f"Renda Mensal: R$ {renda_mensal}")
        print(f"Total de Gastos: R$ {total_gasto}")
        print(f"Saldo: R$ {saldo}")
        
        # Condicional (if/else) para o status do orçamento
        if saldo >= 0:
            print("Status: Dentro do orçamento!")
        else:
            print("Status: Atenção! Você gastou mais do que ganha.")
            
    elif opcao == '5':
        print("\n--- Estatísticas ---")
        print("Funcionalidade em desenvolvimento para a versão final.")
        
    elif opcao == '6':
        print("Saindo do programa...")
        break # Encerra o laço while
        
    else:
        print("Opção inválida! Escolha de 1 a 6.")
