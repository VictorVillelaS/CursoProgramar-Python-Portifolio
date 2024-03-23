import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter.simpledialog import askstring
from BLL.preferenciasBLL import PreferenciasBLL
from MODELS.preferenciasVO import PreferenciasVO


class FrmPreferencias(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        objFrmLista = FrmLista(self)
        objFrmLista.grid(row=0, column=1, padx=30, pady=20, sticky='NSEW')

        objFrmBotoes = FrmBotoes(self, objFrmLista, clsFrmMestre=FrmPreferencias)
        objFrmBotoes.grid(row=0, column=0, padx=30, pady=20, sticky='NSEW')

        objFrmTreeCRUD = FrmTreeCRUD(self, clsFrmMestre=FrmPreferencias)
        objFrmTreeCRUD.grid(row=1, column=0, padx=30, pady=20, sticky='NSEW', columnspan=2)

        objFrmBotoes.preencheListboxDesconectado()
    @staticmethod
    def importarPreferencias():
        return PreferenciasBLL().importarBDDesconectado()

    @staticmethod
    def adicionarEntradaBD():
        valorAdicionar = askstring("Adicionar Valor", "Adicionar o seguinte dado:")
        try:
            objPreferenciasVO = PreferenciasVO(descricao=valorAdicionar)
            PreferenciasBLL().adicionarEntradaBD(objPreferenciasVO)
        except Exception as e:
            messagebox.showinfo("Erro!", e)

    @staticmethod
    def editarEntradaBD():
        idEditar = int(askstring("Editar valor", "Escolha um ID para editar:"))
        valorNovo = askstring("Editar valor", f"Editar linha {idEditar} para:")
        try:
            objPreferenciasVO = PreferenciasVO(idEditar, valorNovo)
            PreferenciasBLL().editarEntradaBD(objPreferenciasVO)
        except Exception as e:
            messagebox.showinfo("Erro!", e)

    @staticmethod
    def removerEntradaBD():
        idRemover = askstring("Remover valor", "Escolha um id para remover:")
        idRemover = int(idRemover)
        objPreferenciasVO = PreferenciasVO(id=idRemover)
        PreferenciasBLL().removerEntradaBD(objPreferenciasVO)


class FrmBotoes(tk.Frame):
    def __init__(self, master, objFrmLista, clsFrmMestre, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.objFrmLista = objFrmLista
        self.objPreferencias = PreferenciasBLL
        self.clsFrmMestre = clsFrmMestre

        self.btnWidth = 35
        self.btnPadx = 10
        self.btnPady = 5

        btnImportabdDesconectado = tk.Button(self, width=self.btnWidth, bg='blue',
                                             text='Importar Listbox do Access (desconectado)',
                                             command=self.preencheListboxDesconectado)
        btnImportabdDesconectado.grid(row=8, column=0, padx=self.btnPadx, pady=self.btnPady)

        btnAdicionarEntrada = tk.Button(self, width=self.btnWidth, bg='green',
                                        text='Adicionar Item no Listbox', command=self.adicionarEntradaBD)
        btnAdicionarEntrada.grid(row=9, column=0, padx=self.btnPadx, pady=self.btnPady)

        btnEditarEntrada = tk.Button(self, width=self.btnWidth, bg='yellow', text='Editar Item no Listbox',
                                     command=self.editarEntradaBD)
        btnEditarEntrada.grid(row=10, column=0, padx=self.btnPadx, pady=self.btnPady)

        btnRemoverEntrada = tk.Button(self, width=self.btnWidth, bg='red', text='Remover Item do Listbox',
                                      command=self.removerEntradaBD)
        btnRemoverEntrada.grid(row=11, column=0, padx=self.btnPadx, pady=self.btnPady)

        btnLimpaListbox = tk.Button(self, width=self.btnWidth, bg='grey', text='Limpar ListBox',
                                    command=self.limpaListbox)
        btnLimpaListbox.grid(row=12, column=0, padx=self.btnPadx, pady=self.btnPady)

    def preencheListboxDesconectado(self):
        try:
            dados = self.clsFrmMestre.importarPreferencias()
            self.preencheListbox(dados)  # [[id, descricao], [id, descricao]]
        except Exception as e:
            messagebox.showinfo("Erro!", e)

    def adicionarEntradaBD(self):
        self.clsFrmMestre.adicionarEntradaBD()
        self.preencheListboxDesconectado()

    def editarEntradaBD(self):
        self.clsFrmMestre.editarEntradaBD()
        self.preencheListboxDesconectado()

    def removerEntradaBD(self):
        self.clsFrmMestre.removerEntradaBD()
        self.preencheListboxDesconectado()

    # Funções referentes à edição da listbox
    def limpaListbox(self):
        self.objFrmLista.limpar()

    def preencheListbox(self, dados):
        self.objFrmLista.preencher(dados)


class FrmLista(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.lstBox = tk.Listbox(self, width=30)
        self.lstBox.pack(fill='both', expand=True)

    def limpar(self):
        self.lstBox.delete(0, "end")

    def preencher(self, linhas):
        self.limpar()
        print(linhas)
        for linha in linhas:
            if isinstance(linha, PreferenciasVO):
                self.lstBox.insert("end", f"{linha.id}: {linha.descricao}")
            else:
                self.lstBox.insert("end", f"{linha[0]}: {linha[1]}")


class FrmTreeCRUD(tk.Frame):
    def __init__(self, master, clsFrmMestre, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.clsFrmMestre = clsFrmMestre

        self.btnWidth = 20
        self.btnPadY = 5
        self.btnPadX = 10

        self.subframe = tk.Frame(self)
        self.subframe.pack()

        self.frmBotoes = tk.Frame(self.subframe)
        self.frmBotoes.pack(side='left')

        self.btnConsultarPreferencia = tk.Button(self.frmBotoes, width=self.btnWidth, bg='grey', text="Consultar",
                                                 command=self.importarPreferencias)
        self.btnConsultarPreferencia.pack(side='top', padx=self.btnPadX, pady=self.btnPadY)

        self.btnAdicionarPreferencia = tk.Button(self.frmBotoes, width=self.btnWidth, bg='grey', text="Adicionar",
                                                 command=self.addPreferencia)
        self.btnAdicionarPreferencia.pack(side='top', padx=self.btnPadX, pady=self.btnPadY)

        self.btnEditarPreferencia = tk.Button(self.frmBotoes, width=self.btnWidth, bg='grey', text="Editar",
                                              command=self.editarPreferencia)
        self.btnEditarPreferencia.pack(side='top', padx=self.btnPadX, pady=self.btnPadY)

        self.btnRemoverPreferencia = tk.Button(self.frmBotoes, width=self.btnWidth, bg='grey', text="Remover",
                                               command=self.removerPreferencia)
        self.btnRemoverPreferencia.pack(side='top', padx=self.btnPadX, pady=self.btnPadY)

        # Configurações da tabela para visualizar os dados
        self.cols = ["ID", "Preferencia"]
        self.colsSize = [30, 150]
        self.colsAnchor = [tk.CENTER, tk.W]

        # Declaração da tabela e atribuição das propriedades de cada coluna
        self.treeview = ttk.Treeview(self.subframe, columns=self.cols, height=6, show='headings')
        self.treeview.pack(side='left')

        for i in range(len(self.cols)):
            self.treeview.heading(self.cols[i], text=self.cols[i])
            self.treeview.column(self.cols[i], width=self.colsSize[i], anchor=self.colsAnchor[i])

    def importarPreferencias(self):
        try:
            linhas = self.clsFrmMestre.importarPreferencias()
            self.treeview.delete(*self.treeview.get_children())
            for linha in linhas:
                values = [linha.id, linha.descricao]
                self.treeview.insert('', 'end', values=values)
        except Exception as e:
            raise e

    def addPreferencia(self):
        try:
            self.clsFrmMestre.adicionarEntradaBD()
            self.importarPreferencias()
        except Exception as e:
            messagebox.showinfo("Erro!", e)

    def editarPreferencia(self):
        try:
            self.clsFrmMestre.editarEntradaBD()
            self.importarPreferencias()
        except Exception as e:
            messagebox.showinfo("Erro!", e)

    def removerPreferencia(self):
        try:
            self.clsFrmMestre.removerEntradaBD()
            self.importarPreferencias()
        except Exception as e:
            messagebox.showinfo("Erro!", e)