import tkinter as tk
from cidades import Cidades  # Corrigido para Cidades com inicial maiúscula

class Application:
    def __init__(self, master=None):
        self.master = master
        master.title("Gerenciamento de Cidades")

        # Frame principal
        self.frame_principal = tk.Frame(master)
        self.frame_principal.pack(padx=10, pady=10)

        # Mensagem
        self.msg1 = tk.Label(self.frame_principal, text="Informe os dados da Cidade:", font=("Verdana", "14", "bold"))
        self.msg1.pack()

        # Frame para ID da cidade e botão de busca
        self.frame_id_busca = tk.Frame(self.frame_principal, padx=20)
        self.frame_id_busca.pack()

        self.idcidades_label = tk.Label(self.frame_id_busca, text="Id cidade:")
        self.idcidades_label.pack(side="left")
        self.idcidades = tk.Entry(self.frame_id_busca, width=20)
        self.idcidades.pack(side="left")

        self.busca = tk.Button(self.frame_id_busca, text="Buscar", command=self.buscarCidade)
        self.busca.pack()

        # Frames para os dados da cidade
        self.frame_nome = tk.Frame(self.frame_principal, padx=20)
        self.frame_nome.pack(pady=5)
        self.nome_label = tk.Label(self.frame_nome, text="Cidade:")
        self.nome_label.pack(side="left")
        self.nome = tk.Entry(self.frame_nome, width=30)
        self.nome.pack(side="left")

        self.frame_UF = tk.Frame(self.frame_principal, padx=20)
        self.frame_UF.pack(pady=5)
        self.UF_label = tk.Label(self.frame_UF, text="UF:")
        self.UF_label.pack(side="left")
        self.UF = tk.Entry(self.frame_UF, width=28)
        self.UF.pack(side="left")

        # Frame para mensagem de autenticidade
        self.frame_autentic = tk.Frame(self.frame_principal, padx=20)
        self.frame_autentic.pack()
        self.autentic = tk.Label(self.frame_autentic, text="", font=("Verdana", "10", "italic", "bold"))
        self.autentic.pack()

        # Frame para botões de ação
        self.frame_botoes = tk.Frame(self.frame_principal, padx=20)
        self.frame_botoes.pack(pady=5)

        self.botao_inserir = tk.Button(self.frame_botoes, width=10, text="Inserir", command=self.inserirCidade)
        self.botao_inserir.pack(side="left")

        self.botao_alterar = tk.Button(self.frame_botoes, width=10, text="Alterar", command=self.alterarCidade)
        self.botao_alterar.pack(side="left")

        self.botao_excluir = tk.Button(self.frame_botoes, width=10, text="Excluir", command=self.excluirCidade)
        self.botao_excluir.pack(side="left")

    def buscarCidade(self):
        cidade = Cidades()
        idcidades = self.idcidades.get()
        resultado = cidade.select(idcidades)
        self.autentic["text"] = resultado

        if cidade.idcidades:
            self.idcidades.delete(0, tk.END)
            self.idcidades.insert(tk.END, cidade.idcidades)
            self.nome.delete(0, tk.END)
            self.nome.insert(tk.END, cidade.nome)
            self.UF.delete(0, tk.END)
            self.UF.insert(tk.END, cidade.UF)
        else:
            self.limparCampos()

    def inserirCidade(self):
        cidade = Cidades()
        cidade.nome = self.nome.get()
        cidade.UF = self.UF.get()
        self.autentic["text"] = cidade.insert()
        self.limparCampos()

    def alterarCidade(self):
        cidade = Cidades()
        cidade.idcidades = self.idcidades.get()
        cidade.nome = self.nome.get()
        cidade.UF = self.UF.get()
        self.autentic["text"] = cidade.update()
        self.limparCampos()

    def excluirCidade(self):
        cidade = Cidades()
        cidade.idcidades = self.idcidades.get()
        self.autentic["text"] = cidade.delete()
        self.limparCampos()

    def limparCampos(self):
        self.idcidades.delete(0, tk.END)
        self.nome.delete(0, tk.END)
        self.UF.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = Application(root)
    root.mainloop()
