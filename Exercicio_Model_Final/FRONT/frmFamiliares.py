import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter.simpledialog import askstring
from BLL.familiaresBLL import FamiliaresBLL
from FRONT.FORMS.formAddFamiliar import FormAddFamiliar
from FRONT.FORMS.formEditFamiliar import FormEditFamiliar
from MODELS.familiaresVO import FamiliaresVO


class FrmFamiliares(tk.LabelFrame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.btnWidth = 20
        self.btnPadY = 5
        self.btnPadX = 10

        self.frmBotoes = tk.Frame(self)
        self.frmBotoes.pack(side='left')

        self.btnConsultarFamiliar = tk.Button(self.frmBotoes, width=self.btnWidth, bg='grey', text="Consultar",
                                              command=self.importarFamiliares)
        self.btnConsultarFamiliar.pack(side='top', padx=self.btnPadX, pady=self.btnPadY)

        self.btnAdicionarFamiliar = tk.Button(self.frmBotoes, width=self.btnWidth, bg='grey', text="Adicionar",
                                              command=self.addFamiliar)
        self.btnAdicionarFamiliar.pack(side='top', padx=self.btnPadX, pady=self.btnPadY)

        self.btnEditarFamiliar = tk.Button(self.frmBotoes, width=self.btnWidth, bg='grey', text="Editar",
                                           command=self.editarFamiliar)
        self.btnEditarFamiliar.pack(side='top', padx=self.btnPadX, pady=self.btnPadY)

        self.btnRemoverFamiliar = tk.Button(self.frmBotoes, width=self.btnWidth, bg='grey', text="Remover",
                                            command=self.removerFamiliar)
        self.btnRemoverFamiliar.pack(side='top', padx=self.btnPadX, pady=self.btnPadY)

        # Configurações da tabela para visualizar os dados
        self.cols = ["ID", "Nome", "Sexo", "Idade", "Salário", "Observação"]
        self.colsSize = [20, 100, 55, 40, 50, 100]
        self.colsAnchor = [tk.CENTER, tk.W, tk.CENTER, tk.CENTER, tk.W, tk.W]

        # Declaração da tabela e atribuição das propriedades de cada coluna
        self.treeview = ttk.Treeview(self, columns=self.cols, height=6, show='headings')
        self.treeview.pack(side='left')

        for i in range(len(self.cols)):
            self.treeview.heading(self.cols[i], text=self.cols[i])
            self.treeview.column(self.cols[i], width=self.colsSize[i], anchor=self.colsAnchor[i])

        self.importarFamiliares()

    def importarFamiliares(self):
        try:
            linhas = FamiliaresBLL().importarBDFamiliares()
            self.treeview.delete(*self.treeview.get_children())
            for linha in linhas:
                values = [linha.id, linha.nome, linha.sexo, linha.idade, linha.salario, linha.observacao]
                self.treeview.insert('', 'end', values=values)
        except Exception as e:
            raise e

    def addFamiliar(self):
        try:
            FormAddFamiliar(self)
            self.importarFamiliares()
        except Exception as e:
            messagebox.showinfo("Erro", str(e))

    def editarFamiliar(self):
        try:
            FormEditFamiliar()
            self.importarFamiliares()
        except Exception as e:
            messagebox.showinfo("Erro", str(e))

    def removerFamiliar(self):
        idRemover = askstring("Remover valor", "Escolha um valor para remover:")
        try:
            objFamiliaresVO = FamiliaresVO(id=idRemover)
            FamiliaresBLL().removerFamiliar(objFamiliaresVO)
            self.importarFamiliares()
        except Exception as e:
            messagebox.showinfo("Erro", str(e))