import sqlite3


class Banco:
    def __init__(self):
        self.conexao = sqlite3.connect('banco.db')
        self.createTables()

    def createTables(self):
        c = self.conexao.cursor()

        # Criação da tabela de usuários
        c.execute("""
            CREATE TABLE IF NOT EXISTS tbl_usuarios (
                idusuario INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT,
                telefone TEXT,
                email TEXT,
                usuario TEXT,
                senha TEXT
            )
        """)

        # Criação da tabela de cidades
        c.execute("""
            CREATE TABLE IF NOT EXISTS tbl_cidades (
                idcidades INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT,
                UF TEXT
            )
        """)

        self.conexao.commit()
        c.close()

    def __del__(self):
        if self.conexao:
            self.conexao.close()
