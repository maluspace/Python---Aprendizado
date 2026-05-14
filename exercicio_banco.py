saldo_inicial = 0

while True:
    print('''=== Caixa Eletrônico ===
1 - Consultar saldo
2 - Depositar
3 - Sacar
4 - Sair''')
    
    try:
        opcao = input("Escolha uma opção: ").strip()
        opcao = int(opcao)
    
        if opcao < 1 or opcao > 4:
            print("A opção deve ser entre 1 e 4. Tente novamente.")
        
    except ValueError:
        print("Por favor, digite uma opção válida.")
        continue

    if opcao == 1:

        print(f"Seu saldo é R$ {saldo_inicial}")

        continue
                
    if opcao == 2:
        try:

            valor_depositado = input ("Insira um valor que deseja depositar: ").strip()
            valor_depositado = float(valor_depositado)

            if valor_depositado > 0:
                valor_apos_deposito = saldo_inicial + valor_depositado
                saldo_inicial = valor_apos_deposito
                print(f"Você depositou {valor_depositado} \nApós o depósito, seu saldo é: {valor_apos_deposito}")
            else:
                print("Por favor, digite um valor positivo.")

        except ValueError:
            print("Por favor, digite uma opção válida.")
        continue
        
    if opcao == 3:

        try:

            valor_sacado = input ("Insira um valor que deseja sacar: ").strip()
            valor_sacado = float(valor_sacado)

            if valor_sacado > 0 and valor_sacado <= saldo_inicial:
                valor_apos_saque = saldo_inicial - valor_sacado
                saldo_inicial = valor_apos_saque
                print(f"Você sacou {valor_sacado} \nApós o saque, seu saldo é: {valor_apos_saque}")
            
            elif saldo_inicial == 0:

                print(f'Você não possui nenhum saldo para sacar')
            else:
                print(f"Por favor, digite um valor menor ou igual ao saldo atual. Seu saldo atual é {saldo_inicial}.")
        except ValueError:
            print("Por favor, digite uma opção válida.")

        continue
        
    if opcao == 4:
        break  
    

