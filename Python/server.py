import sqlite3


def conectar():
    conexao = sqlite3.connect("sistema.db")
    conexao.execute("PRAGMA foreign_keys = ON")
    return conexao


def criar_tabelas():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS pedidos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        descricao TEXT NOT NULL,
        cliente_id INTEGER NOT NULL,
        FOREIGN KEY (cliente_id) REFERENCES clientes(id)
    )
    """)

    conexao.commit()
    conexao.close()
