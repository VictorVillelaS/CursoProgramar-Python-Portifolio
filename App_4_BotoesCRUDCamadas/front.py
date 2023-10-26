import tkinter as tk
from tkinter import messagebox
from tkinter.simpledialog import askstring
from preferenciasBLL import Preferencias


class FrmPreferencias(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        master.title("Exercício 3")

        objFrmLista = FrmLista(self)
        objFrmLista.grid(row=0,column=1, padx=30, pady=30, sticky='NSEW')
        
        objFrameBotoes = FrmBotoes(self, objFrmLista)
        objFrameBotoes.grid(row=0,column=0, padx=30, pady=30, sticky='NSEW')


class FrmBotoes(tk.Frame):
    def __init__(self, master, objFrmLista, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.objFrmLista = objFrmLista
        self.objPreferencias = Preferencias

        self.btnWidth = 35
        self.btnPady = 5

        btnMensagem = tk.Button(self, width=self.btnWidth, bg='grey', text="Mensagem", command=self.mensagem)
        btnMensagem.grid(row=0,column=0, pady=self.btnPady)

        btnDesvCond = tk.Button(self, width=self.btnWidth, bg='grey', text='Desvio Condicional', command=self.desvCond)
        btnDesvCond.grid(row=1, column=0, pady=self.btnPady)

        btnDesvCondEncadeado = tk.Button(self, width=self.btnWidth, bg='grey', text='Desvio Cond Encadeado', command=self.desvCondEncadeado)
        btnDesvCondEncadeado.grid(row=2, column=0, pady=self.btnPady)

        btnMatchCase = tk.Button(self, width=self.btnWidth, bg='grey', text='Match Case', command=self.matchCase)
        btnMatchCase.grid(row=3, column=0, pady=self.btnPady)

        btnListboxWhile = tk.Button(self, width=self.btnWidth, bg='grey', text='Listbox While', command=self.listboxWhile)
        btnListboxWhile.grid(row=4, column=0, pady=self.btnPady)

        btnListboxForComIndice = tk.Button(self, width=self.btnWidth, bg='grey', text='LstBoxFor c/Indice', command=self.listboxForComIndice)
        btnListboxForComIndice.grid(row=5, column=0, pady=self.btnPady)

        btnListboxForSemIndice = tk.Button(self, width=self.btnWidth, bg='grey', text='LstBoxFor s/Indice', command=self.listboxForSemIndice)
        btnListboxForSemIndice.grid(row=6, column=0, pady=self.btnPady)

        btnImportabdConectado = tk.Button(self, width=self.btnWidth, bg='blue', text='Importar Listbox do Access (conectado)',command=self.preencheListboxConectado)
        btnImportabdConectado.grid(row=7, column=0, pady=self.btnPady)

        btnImportabdDesconectado = tk.Button(self, width=self.btnWidth, bg='blue', text='Importar Listbox do Access (desconectado)',command = self.preencheListboxDesconectado)
        btnImportabdDesconectado.grid(row=8, column=0, pady=self.btnPady)

        btnAdicionarEntrada = tk.Button(self, width=self.btnWidth, bg='green', text='Adicionar Item no Listbox', command = self.adicionarEntradaBD)
        btnAdicionarEntrada.grid(row=9, column=0, pady=self.btnPady)

        btnEditarEntrada = tk.Button(self, width=self.btnWidth, bg='yellow', text='Editar Item no Listbox', command = self.editarEntradaBD)
        btnEditarEntrada.grid(row=10, column=0, pady=self.btnPady)

        btnRemoverEntrada = tk.Button(self, width=self.btnWidth, bg='red', text='Remover Item do Listbox', command = self.removerEntradaBD)
        btnRemoverEntrada.grid(row=11, column=0, pady=self.btnPady)

        btnLimpaListbox = tk.Button(self, width=self.btnWidth, bg='grey', text='Limpar ListBox', command = self.limpaListbox)
        btnLimpaListbox.grid(row=12, column=0, pady=self.btnPady)
    
    #Funcoes que não dependem de nenhum arquivo externo
    def mensagem(self):
        messagebox.showinfo(title='Mensagem', message='Isso é uma mensagem!')

    def desvCond(self):
        resposta = messagebox.askyesno(title='y/n', message='Sim ou não?')
        if resposta:
            messagebox.showinfo(title='y', message='Sim')
        else:
            messagebox.showinfo(title='n', message='Nao')

    def desvCondEncadeado(self):
        resposta = messagebox.askyesnocancel(title='y/n/c', message='Sim ou não?')
        if resposta == True:
            messagebox.showinfo(title='y', message='Sim')
        elif resposta == False:
            messagebox.showinfo(title='n', message='Nao')
        else:
            messagebox.showinfo(title='c', message='Cancel')

    def matchCase(self):
        resposta = messagebox.askyesnocancel(title='y/n/c', message='Sim ou não?')
        match resposta:
            case True:
                messagebox.showinfo(title='y', message='Sim')
            case False:
                messagebox.showinfo(title='n', message='Nao')
            case None:
                messagebox.showinfo(title='c', message='Cancel')
    
    #Funções que importam dados do arquivo de texto. Usam a camada preferenciasBLL
    def listboxWhile(self):
        dados = self.objPreferencias.ListboxWhile()
        self.objFrmLista.preencher(dados)

    def listboxForComIndice(self):
        dados = self.objPreferencias.ListboxForComIndice()
        self.objFrmLista.preencher(dados)

    def listboxForSemIndice(self):
        dados = self.objPreferencias.ListboxForSemIndice()
        self.objFrmLista.preencher(dados)

    #Funções que trabalham com o banco de dados Access. Usam a camada DAL
    def preencheListboxConectado(self):
        dados = Preferencias.ImportarBDConectado()
        self.preencheListbox(dados)

    def preencheListboxDesconectado(self):
        dados = Preferencias.ImportarBDDesconectado()
        self.preencheListbox(dados)

    def adicionarEntradaBD(self):
        valorAdicionar = askstring("Adicionar Valor", "Adicionar o seguinte dado:")
        Preferencias.AdicionarEntradaBD(valorAdicionar)
        self.preencheListboxDesconectado()

    def editarEntradaBD(self):
        valorEditar = askstring("Editar valor", "Escolha um valor para editar:")
        valorNovo = askstring("Editar valor", f"Editar '{valorEditar}' para:")
        Preferencias.EditarEntradaBD(valorEditar, valorNovo)
        self.preencheListboxDesconectado()

    def removerEntradaBD(self):
        valorRemover = askstring("Remover valor", "Escolha um valor para remover:")
        Preferencias.RemoverEntradaBD(valorRemover)
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
        for i in linhas:
            self.lstBox.insert("end", i)