from server import criar_tabelas
from crud import cadastrar_cliente, deletar_cliente, listar_clientes, cadastrar_pedido, listar_pedidos, deletar_pedido


criar_tabelas()

while True:
    print("\nSISTEMA SIMPLES")
    print("1 - Cadastrar cliente")
    print("2 - Listar clientes")
    print("3 - Cadastrar pedido")
    print("4 - Listar pedidos")
    print("5 - Deletar cliente")
    print("6 - Deletar pedido")
    print("0 - Sair")

    opcao = input("Escolha uma opcao: ")

    if opcao == "1":
        cadastrar_cliente()
    elif opcao == "2":
        listar_clientes()
    elif opcao == "3":
        cadastrar_pedido()
    elif opcao == "4":
        listar_pedidos()
    elif opcao == "5":
        deletar_cliente()
    elif opcao == "6":
        deletar_pedido()
    elif opcao == "0":
        print("Encerrando sistema")
        break
    else:
        print("Opcao invalida")
