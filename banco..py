import tkinter as tk
from tkinter import

class Usuario:

    def __init__(self):
        self.idusuario = ""
        self.nome = ""
        self.telefone = ""
        self.email = ""
        self.usuario = ""
        self.senha = ""

    def selectUser(self, idusuario):

        self.idusuario = idusuario
        self.nome = "Nome Exemplo"
        self.telefone = "123456789"
        self.email = "exemplo@email.com"
        self.usuario = "usuario"
        self.senha = "senha"
        return "Usuário encontrado"

    def insertUser(self):

        return "Usuário inserido com sucesso"

    def updateUser(self):

        return "Usuário atualizado com sucesso"

    def deleteUser(self):

        return "Usuário excluído com sucesso"

class Aplicacao:
    def __init__(self, root):
        self.root = root
        self.root.title("Gerenciamento de Usuários")


        self.txtidusuario = tk.Entry(root)
        self.txtnome = tk.Entry(root)
        self.txttelefone = tk.Entry(root)
        self.txtemail = tk.Entry(root)
        self.txtusuario = tk.Entry(root)
        self.txtsenha = tk.Entry(root, show="*")


        self.btnBuscar = tk.Button(root, text="Buscar", command=self.buscarUsuario)
        self.bntInsert = tk.Button(root, text="Inserir", command=self.inserirUsuario)
        self.bntAlterar = tk.Button(root, text="Alterar", command=self.alterarUsuario)
        self.bntExcluir = tk.Button(root, text="Excluir", command=self.excluirUsuario)


        self.lblmsg = tk.Label(root, text="")


        self.txtidusuario.pack()
        self.txtnome.pack()
        self.txttelefone.pack()
        self.txtemail.pack()
        self.txtusuario.pack()
        self.txtsenha.pack()

        self.btnBuscar.pack()
        self.bntInsert.pack()
        self.bntAlterar.pack()
        self.bntExcluir.pack()

        self.lblmsg.pack()

    def buscarUsuario(self):
        user = Usuario()
        idusuario = self.txtidusuario.get()
        msg = user.selectUser(idusuario)
        self.lblmsg["text"] = msg
        self.txtidusuario.delete(0, END)
        self.txtidusuario.insert(INSERT, user.idusuario)
        self.txtnome.delete(0, END)
        self.txtnome.insert(INSERT, user.nome)
        self.txttelefone.delete(0, END)
        self.txttelefone.insert(INSERT, user.telefone)
        self.txtemail.delete(0, END)
        self.txtemail.insert(INSERT, user.email)
        self.txtusuario.delete(0, END)
        self.txtusuario.insert(INSERT, user.usuario)
        self.txtsenha.delete(0, END)
        self.txtsenha.insert(INSERT, user.senha)

    def inserirUsuario(self):
        user = Usuario()
        user.nome = self.txtnome.get()
        user.telefone = self.txttelefone.get()
        user.email = self.txtemail.get()
        user.usuario = self.txtusuario.get()
        user.senha = self.txtsenha.get()
        self.lblmsg["text"] = user.insertUser()
        self.limparCampos()

    def alterarUsuario(self):
        user = Usuario()
        user.idusuario = self.txtidusuario.get()
        user.nome = self.txtnome.get()
        user.telefone = self.txttelefone.get()
        user.email = self.txtemail.get()
        user.usuario = self.txtusuario.get()
        user.senha = self.txtsenha.get()
        self.lblmsg["text"] = user.updateUser()
        self.limparCampos()

    def excluirUsuario(self):
        user = Usuario()
        user.idusuario = self.txtidusuario.get()
        self.lblmsg["text"] = user.deleteUser()
        self.limparCampos()                     

    def limparCampos(self):
        self.txtidusuario.delete(0, END)
        self.txtnome.delete(0, END)
        self.txttelefone.delete(0, END)
        self.txtemail.delete(0, END)
        self.txtusuario.delete(0, END)
        self.txtsenha.delete(0, END)

if __name__ == "__main__":
    root = tk.Tk()
    app = Aplicacao(root)
    root.mainloop()
