import tkinter as tk
from Usuarios import Usuarios

class Application:
    def __init__(self, master=None):
        self.master = master
        master.title("Gerenciamento de Usuários")

        # Frame principal
        self.frame_principal = tk.Frame(master)
        self.frame_principal.pack(padx=10, pady=10)

        # Mensagem
        self.msg1 = tk.Label(self.frame_principal, text="Informe os dados:", font=("Verdana", "14", "bold"))
        self.msg1.pack()

        # Frame para ID do usuário e botão de busca
        self.frame_id_busca = tk.Frame(self.frame_principal, padx=20)
        self.frame_id_busca.pack()

        self.idusuario_label = tk.Label(self.frame_id_busca, text="Id usuario:")
        self.idusuario_label.pack(side="left")
        self.idusuario = tk.Entry(self.frame_id_busca, width=20)
        self.idusuario.pack(side="left")

        self.busca = tk.Button(self.frame_id_busca, text="Buscar", command=self.buscarUsuario)
        self.busca.pack()

        # Frames para os dados do usuário
        self.frames_dados = {
            'Nome': self._criar_frame_dado("Nome:", 30),
            'Telefone': self._criar_frame_dado("Telefone:", 28),
            'E-mail': self._criar_frame_dado("E-mail:", 30),
            'Usuário': self._criar_frame_dado("Usuário:", 29),
            'Senha': self._criar_frame_dado("Senha:", 30, show="*")
        }

        # Frame para mensagem de autenticidade
        self.frame_autentic = tk.Frame(self.frame_principal, padx=20)
        self.frame_autentic.pack()

        self.autentic = tk.Label(self.frame_autentic, text="", font=("Verdana", "10", "italic", "bold"))
        self.autentic.pack()

        # Frame para botões de ação
        self.frame_botoes = tk.Frame(self.frame_principal, padx=20)
        self.frame_botoes.pack(pady=5)

        self.botao_inserir = tk.Button(self.frame_botoes, width=10, text="Inserir", command=self.inserirUsuario)
        self.botao_inserir.pack(side="left")

        self.botao_alterar = tk.Button(self.frame_botoes, width=10, text="Alterar", command=self.alterarUsuario)
        self.botao_alterar.pack(side="left")

        self.botao_excluir = tk.Button(self.frame_botoes, width=10, text="Excluir", command=self.excluirUsuario)
        self.botao_excluir.pack(side="left")

    def _criar_frame_dado(self, label_text, entry_width, show=None):
        frame = tk.Frame(self.frame_principal, padx=20)
        frame.pack(pady=5)
        label = tk.Label(frame, text=label_text)
        label.pack(side="left")
        entry = tk.Entry(frame, width=entry_width, show=show)
        entry.pack(side="left")
        return entry

    def buscarUsuario(self):
        try:
            user = Usuarios()
            idusuario = self.idusuario.get()
            user.selectUser(idusuario)
            self.autentic["text"] = user.autentic  # Presumindo que `selectUser` define `user.autentic`
            self._preencher_campos(user)
        except Exception as e:
            self.autentic["text"] = f"Erro: {str(e)}"

    def inserirUsuario(self):
        try:
            user = Usuarios()
            self._atualizar_usuario(user)
            self.autentic["text"] = user.insertUser()
            self.limparCampos()
        except Exception as e:
            self.autentic["text"] = f"Erro: {str(e)}"

    def alterarUsuario(self):
        try:
            user = Usuarios()
            user.idusuario = self.idusuario.get()
            self._atualizar_usuario(user)
            self.autentic["text"] = user.updateUser()
            self.limparCampos()
        except Exception as e:
            self.autentic["text"] = f"Erro: {str(e)}"

    def excluirUsuario(self):
        try:
            user = Usuarios()
            user.idusuario = self.idusuario.get()
            self.autentic["text"] = user.deleteUser()
            self.limparCampos()
        except Exception as e:
            self.autentic["text"] = f"Erro: {str(e)}"

    def _atualizar_usuario(self, user):
        user.nome = self.frames_dados['Nome'].get()
        user.telefone = self.frames_dados['Telefone'].get()
        user.email = self.frames_dados['E-mail'].get()
        user.usuario = self.frames_dados['Usuário'].get()
        user.senha = self.frames_dados['Senha'].get()

    def _preencher_campos(self, user):
        self.idusuario.delete(0, tk.END)
        self.idusuario.insert(tk.END, user.idusuario)
        self.frames_dados['Nome'].delete(0, tk.END)
        self.frames_dados['Nome'].insert(tk.END, user.nome)
        self.frames_dados['Telefone'].delete(0, tk.END)
        self.frames_dados['Telefone'].insert(tk.END, user.telefone)
        self.frames_dados['E-mail'].delete(0, tk.END)
        self.frames_dados['E-mail'].insert(tk.END, user.email)
        self.frames_dados['Usuário'].delete(0, tk.END)
        self.frames_dados['Usuário'].insert(tk.END, user.usuario)
        self.frames_dados['Senha'].delete(0, tk.END)
        self.frames_dados['Senha'].insert(tk.END, user.senha)

    def limparCampos(self):
        self.idusuario.delete(0, tk.END)
        for entry in self.frames_dados.values():
            entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = Application(root)
    root.mainloop()
