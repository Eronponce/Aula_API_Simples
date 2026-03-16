from server import conectar
import sqlite3


def cadastrar_cliente():
    nome = input("Digite o nome do cliente: ")

    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO clientes (nome) VALUES (?)", (nome,))
    conexao.commit()
    conexao.close()

    print("Cliente cadastrado com sucesso")


def listar_clientes():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM clientes")
    clientes = cursor.fetchall()
    conexao.close()

    if len(clientes) == 0:
        print("Nenhum cliente cadastrado")
    else:
        for cliente in clientes:
            print(f"ID {cliente[0]} | Nome {cliente[1]}")


def cadastrar_pedido():
    descricao = input("Digite a descricao do pedido: ")
    cliente_id = input("Digite o ID do cliente: ")

    conexao = conectar()
    cursor = conexao.cursor()

    try:
        cursor.execute(
            "INSERT INTO pedidos (descricao, cliente_id) VALUES (?, ?)",
            (descricao, cliente_id)
        )
        conexao.commit()
        print("Pedido cadastrado com sucesso")
    except sqlite3.IntegrityError:
        print("Erro, cliente nao encontrado")
    finally:
        conexao.close()


def listar_pedidos():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT pedidos.id, pedidos.descricao, clientes.nome
        FROM pedidos
        JOIN clientes ON pedidos.cliente_id = clientes.id
    """)

    pedidos = cursor.fetchall()
    conexao.close()

    if len(pedidos) == 0:
        print("Nenhum pedido cadastrado")
    else:
        for pedido in pedidos:
            print(f"ID {pedido[0]} | Descricao {pedido[1]} | Cliente {pedido[2]}")
            
def deletar_cliente():
    cliente_id = input("Digite o ID do cliente a ser deletado: ")

    conexao = conectar()
    cursor = conexao.cursor()

    try:
        cursor.execute("DELETE FROM clientes WHERE id = ?", (cliente_id,))
        if cursor.rowcount == 0:
            print("Cliente nao encontrado")
        else:
            conexao.commit()
            print("Cliente deletado com sucesso")
    except sqlite3.IntegrityError:
        print("Erro, cliente possui pedidos associados")
    finally:
        conexao.close()

def deletar_pedido():
    pedido_id = input("Digite o ID do pedido a ser deletado: ")

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("DELETE FROM pedidos WHERE id = ?", (pedido_id,))
    if cursor.rowcount == 0:
        print("Pedido nao encontrado")
    else:
        conexao.commit()
        print("Pedido deletado com sucesso")
    conexao.close()

