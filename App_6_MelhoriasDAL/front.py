import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter.simpledialog import askstring
from preferenciasBLL import Preferencias
from DAL import Dados
from forms import FormAddParente, FormEditParente

class FrmPreferencias(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        master.title("Exercício 3")

        objFrmLista = FrmLista(self)
        objFrmLista.grid(row=0,column=1, padx=30, pady=20, sticky='NSEW')
        
        objFrmBotoes = FrmBotoes(self, objFrmLista)
        objFrmBotoes.grid(row=0,column=0, padx=30, pady=20, sticky='NSEW')

        objFrmFamiliares = FrmFamiliares(self, text="Parentes")
        objFrmFamiliares.grid(row=1, column=0, columnspan=2, padx=30, pady=20, sticky='nsew', ipadx=5, ipady=5)


class FrmBotoes(tk.Frame):
    def __init__(self, master, objFrmLista, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.objFrmLista = objFrmLista
        self.objPreferencias = Preferencias

        self.btnWidth = 35
        self.btnPadx = 10
        self.btnPady = 5

        btnListboxWhile = tk.Button(self, width=self.btnWidth, bg='grey', text='Listbox While', command=self.listboxWhile)
        btnListboxWhile.grid(row=4, column=0, padx = self.btnPadx, pady=self.btnPady)

        btnListboxForComIndice = tk.Button(self, width=self.btnWidth, bg='grey', text='LstBoxFor c/Indice', command=self.listboxForComIndice)
        btnListboxForComIndice.grid(row=5, column=0, padx = self.btnPadx, pady=self.btnPady)

        btnListboxForSemIndice = tk.Button(self, width=self.btnWidth, bg='grey', text='LstBoxFor s/Indice', command=self.listboxForSemIndice)
        btnListboxForSemIndice.grid(row=6, column=0, padx = self.btnPadx, pady=self.btnPady)

        btnImportabdConectado = tk.Button(self, width=self.btnWidth, bg='blue', text='Importar Listbox do Access (conectado)',command=self.preencheListboxConectado)
        btnImportabdConectado.grid(row=7, column=0, padx = self.btnPadx, pady=self.btnPady)

        btnImportabdDesconectado = tk.Button(self, width=self.btnWidth, bg='blue', text='Importar Listbox do Access (desconectado)',command = self.preencheListboxDesconectado)
        btnImportabdDesconectado.grid(row=8, column=0, padx = self.btnPadx, pady=self.btnPady)

        btnAdicionarEntrada = tk.Button(self, width=self.btnWidth, bg='green', text='Adicionar Item no Listbox', command = self.adicionarEntradaBD)
        btnAdicionarEntrada.grid(row=9, column=0, padx = self.btnPadx, pady=self.btnPady)

        btnEditarEntrada = tk.Button(self, width=self.btnWidth, bg='yellow', text='Editar Item no Listbox', command = self.editarEntradaBD)
        btnEditarEntrada.grid(row=10, column=0, padx = self.btnPadx, pady=self.btnPady)

        btnRemoverEntrada = tk.Button(self, width=self.btnWidth, bg='red', text='Remover Item do Listbox', command = self.removerEntradaBD)
        btnRemoverEntrada.grid(row=11, column=0, padx = self.btnPadx, pady=self.btnPady)

        btnLimpaListbox = tk.Button(self, width=self.btnWidth, bg='grey', text='Limpar ListBox', command = self.limpaListbox)
        btnLimpaListbox.grid(row=12, column=0, padx = self.btnPadx, pady=self.btnPady)
    
    #Funções que importam dados do arquivo de texto. Usam a camada preferenciasBLL
    def listboxWhile(self):
        dados = self.objPreferencias.ListboxWhile()
        self.preencheListbox(dados)

    def listboxForComIndice(self):
        dados = self.objPreferencias.ListboxForComIndice()
        self.preencheListbox(dados)

    def listboxForSemIndice(self):
        dados = self.objPreferencias.ListboxForSemIndice()
        self.preencheListbox(dados)

    #Funções que trabalham com o banco de dados Access. Usam a camada DAL
    def preencheListboxConectado(self):
        try:
            dados = Preferencias.ImportarBDConectado()
            self.preencheListbox(dados)
        except Exception as e:
            messagebox.showinfo("Erro!", e)

    def preencheListboxDesconectado(self):
        try:
            dados = Preferencias.ImportarBDDesconectado()
            self.preencheListbox(dados)
        except Exception as e:
            messagebox.showinfo("Erro!", e)

    def adicionarEntradaBD(self):
        valorAdicionar = askstring("Adicionar Valor", "Adicionar o seguinte dado:")
        try:
            Preferencias.AdicionarEntradaBD(valorAdicionar)
            self.preencheListboxDesconectado()
        except Exception as e:
            messagebox.showinfo("Erro!", e)

    def editarEntradaBD(self):
        idEditar = askstring("Editar valor", "Escolha um ID para editar:")
        valorNovo = askstring("Editar valor", f"Editar linha {idEditar} para:")
        try:
            Preferencias.EditarEntradaBD(idEditar, valorNovo)
        except Exception as e:
            messagebox.showinfo("Erro!", e)
        self.preencheListboxDesconectado()

    def removerEntradaBD(self):
        idRemover = askstring("Remover valor", "Escolha um id para remover:")
        Preferencias.RemoverEntradaBD(idRemover)
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
            self.lstBox.insert("end", f"{linha[0]}: {linha[1]}")


#Criação do frame com as informações da tabela 'Parentes' do banco de dados
class FrmFamiliares(tk.LabelFrame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.btnWidth = 20
        self.btnPadY = 5
        self.btnPadX = 10

        self.frmBotoes = tk.Frame(self)
        self.frmBotoes.pack(side='left')

        self.btnConsultarPaciente = tk.Button(self.frmBotoes, width=self.btnWidth, bg='grey', text="Consultar", command=self.consultarParentes)
        self.btnConsultarPaciente.pack(side='top', padx = self.btnPadX, pady=self.btnPadY)

        self.btnAdicionarLinha = tk.Button(self.frmBotoes, width=self.btnWidth, bg='grey', text="Adicionar", command=self.addParente)
        self.btnAdicionarLinha.pack(side='top', padx = self.btnPadX, pady=self.btnPadY)

        self.btnEditarLinha = tk.Button(self.frmBotoes, width=self.btnWidth, bg='grey', text="Editar", command=self.editarParente)
        self.btnEditarLinha.pack(side='top', padx = self.btnPadX, pady=self.btnPadY)

        self.btnRemoverLinha = tk.Button(self.frmBotoes, width=self.btnWidth, bg='grey', text="Remover", command=self.removerParente)
        self.btnRemoverLinha.pack(side='top', padx = self.btnPadX, pady=self.btnPadY)

        #Configurações da tabela para visualizar os dados
        self.cols = ["ID", "Nome", "Sexo", "Idade", "Salário", "Favorito"]
        self.colsSize = [20, 100, 55, 40, 50, 100]
        self.colsAnchor = [tk.CENTER, tk.W, tk.CENTER, tk.CENTER, tk.W, tk.W]

        #Declaração da tabela e atribuição das propriedades de cada coluna
        self.treeview = ttk.Treeview(self, columns=self.cols, height=6, show='headings')
        self.treeview.pack(side='left')

        for i in range(len(self.cols)):
            self.treeview.heading(self.cols[i], text=self.cols[i])
            self.treeview.column(self.cols[i], width=self.colsSize[i], anchor=self.colsAnchor[i])
 
        self.consultarParentes()

    #DAL Nunca se comunica diretamente com o front
    def consultarParentes(self):
        linhas = Dados.ImportarBDParentesDesconectado()
        self.treeview.delete(*self.treeview.get_children())
        for linha in linhas:
            self.treeview.insert('', 'end', values=list(linha))    

    def addParente(self):
        FormAddParente()
        #Como fazer essa função ser executada somente após a janela FormAddParente ser fechada?
        self.consultarParentes()

    def editarParente(self):
        FormEditParente()
        self.consultarParentes()

    def removerParente(self):
        idRemover = askstring("Remover valor", "Escolha um valor para remover:")
        Dados.RemoverEntradaBDParentes(idRemover)
        self.consultarParentes()