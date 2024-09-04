from Banco import Banco

class Cidades:
    def __init__(self, idcidades=0, nome="", UF=""):
        self.idcidades = idcidades
        self.nome = nome
        self.UF = UF

    def insert(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("INSERT INTO tbl_cidades (nome, UF) VALUES (?, ?)", (self.nome, self.UF))
            banco.conexao.commit()
            c.close()
            return "Cidade cadastrada com sucesso!"
        except Exception as e:
            return f"Ocorreu um erro na inserção da cidade: {str(e)}"

    def update(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("UPDATE tbl_cidades SET nome = ?, UF = ? WHERE idcidades = ?", (self.nome, self.UF, self.idcidades))
            banco.conexao.commit()
            c.close()
            return "Cidade atualizada com sucesso!"
        except Exception as e:
            return f"Ocorreu um erro na alteração da cidade: {str(e)}"

    def delete(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("DELETE FROM tbl_cidades WHERE idcidades = ?", (self.idcidades,))
            banco.conexao.commit()
            c.close()
            return "Cidade excluída com sucesso!"
        except Exception as e:
            return f"Ocorreu um erro na exclusão da cidade: {str(e)}"

    def select(self, idcidades):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("SELECT * FROM tbl_cidades WHERE idcidades = ?", (idcidades,))
            linha = c.fetchone()
            if linha:
                self.idcidades, self.nome, self.UF = linha
            c.close()
            return "Busca feita com sucesso!" if linha else "Cidade não encontrada."
        except Exception as e:
            return f"Ocorreu um erro na busca da cidade: {str(e)}"

