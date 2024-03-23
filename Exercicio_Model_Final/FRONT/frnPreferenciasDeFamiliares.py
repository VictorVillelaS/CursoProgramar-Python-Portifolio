import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter.simpledialog import askstring
from tkinter import filedialog
from MODELS.preferenciasVO import PreferenciasVO
from MODELS.familiaresVO import FamiliaresVO
from MODELS.preferenciasDeFamiliaresVO import PreferenciasDeFamiliaresVO
from BLL.preferenciasDeFamiliaresBLL import PreferenciasDeFamiliaresBLL
from FRONT.builders import BuilderFamiliaresCombobox, BuilderPreferenciasCombobox
from FRONT.FORMS.formAddPreferenciaDeFamiliar import FormAddPreferenciaDeFamiliar
from FRONT.FORMS.formEditPreferenciaDeFamiliar import FormEditPreferenciaDeFamiliar
from BLL.exportBLL import ExporterBLL


class FrmPreferenciasDeFamiliares(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.btnWidth = 20
        self.btnPadY = 5
        self.btnPadX = 0

        # Esse frame contém todos os elementos da tela, ele só existe pro pack ficar centralizado
        self.frmConteudo = tk.Frame(self)
        self.frmConteudo.pack()

        self.frmBusca = tk.Frame(self.frmConteudo)
        self.frmBusca.grid(row=0, column=0, sticky='sw', pady=5)

        self.familiarCombobox = BuilderFamiliaresCombobox(self.frmBusca, "Familiar:")
        self.familiarCombobox.grid(row=0, column=0, sticky='sew')

        self.preferenciasCombobox = BuilderPreferenciasCombobox(self.frmBusca, 'Preferencias:')
        self.preferenciasCombobox.grid(row=0, column=1, sticky='s', padx=30)

        self.frmBotoes = tk.Frame(self.frmConteudo)
        self.frmBotoes.grid(row=2,column=0, sticky='ew', pady=2)

        self.btnConsultPrefFamiliar = tk.Button(self.frmBotoes, text="Cnslt", command=self.importarPreferenciasFamiliares)
        self.btnConsultPrefFamiliar.pack(side='left', fill='x', expand=True)

        self.btnAddPrefFamiliar = tk.Button(self.frmBotoes, text="Add", command=self.addPreferenciaFamiliar)
        self.btnAddPrefFamiliar.pack(side='left', fill='x', expand=True)

        self.btnUpdatePrefFamiliar = tk.Button(self.frmBotoes, text="Updt", command=self.editarPreferenciaFamiliar)
        self.btnUpdatePrefFamiliar.pack(side='left', fill='x', expand=True)

        self.btnDeletePrefFamiliar = tk.Button(self.frmBotoes, text="Del", command=self.removerPreferenciaFamiliar)
        self.btnDeletePrefFamiliar.pack(side='left', fill='x', expand=True)

        self.btnExportExcel = tk.Button(self.frmBotoes, text='Excel', command=self.exportExcel)
        self.btnExportExcel.pack(side='left', fill='x', expand=True)

        self.btnExportEmail = tk.Button(self.frmBotoes, text='Email', command=self.exportEmail)
        self.btnExportEmail.pack(side='left', fill='x', expand=True)



        # Configurações da tabela para visualizar os dados
        self.cols = ["Nome Familiar", "Nome Preferencia", "Intensidade", "Observacao"]
        self.colsSize = [100, 150, 100, 150]
        self.colsAnchor = [tk.CENTER, tk.CENTER, tk.CENTER, tk.W]

        # Declaração da tabela e atribuição das propriedades de cada coluna
        self.treeview = ttk.Treeview(self.frmConteudo, columns=self.cols, height=6, show='headings')
        self.treeview.grid(row=1, column=0, sticky='nw')

        for i in range(len(self.cols)):
            self.treeview.heading(self.cols[i], text=self.cols[i])
            self.treeview.column(self.cols[i], width=self.colsSize[i], anchor=self.colsAnchor[i])

        self.familiarCombobox.comboboxVar.trace_add('write', self.importarPreferenciasFamiliares)
        self.preferenciasCombobox.comboboxVar.trace_add('write', self.importarPreferenciasFamiliares)
        self.treeview.bind("<Double-1>", self.onDoubleClick)

    def importarPreferenciasFamiliares(self, *e):
        familiar = self.familiarCombobox.get()
        preferencia = self.preferenciasCombobox.get()
        if familiar != "":
            id, nome = familiar.split(": ")
            objFamiliar = FamiliaresVO(id=id, nome=nome)

            lista_familiares = PreferenciasDeFamiliaresBLL().importPreferenciasFamiliares(objFamiliar)
            if preferencia != "":
                id_pref, descricao = preferencia.split(": ")
                id_pref = int(id_pref)
                lista_familiares = [obj for obj in lista_familiares if obj.objPreferencia.id == id_pref]

            self.updateTreeview(lista_familiares)

        else:
            self.clearTreeview()

    def addPreferenciaFamiliar(self):
        FormAddPreferenciaDeFamiliar(self)

    def onDoubleClick(self, event):
        item = self.treeview.selection()[0]
        linha = self.treeview.item(item, "values")

        id_familiar, nome_familiar = linha[0].split(": ")
        objFamiliar = FamiliaresVO(int(id_familiar), nome_familiar)

        id_preferencia, descricao_preferencia = linha[1].split(": ")
        objPreferencia = PreferenciasVO(int(id_preferencia), descricao_preferencia)

        intensidade = float(linha[2])
        descricao = linha[3]

        objPreferenciaDeFamiliarVO = PreferenciasDeFamiliaresVO(objFamiliar, objPreferencia,
                                                                intensidade, descricao)

        self.editarPreferenciaFamiliar(objPreferenciaDeFamiliarVO)

    """Como posso fazer para descobrir o ID da preferencia sem recorrer a obter essa informação em uma string?"""
    def editarPreferenciaFamiliar(self, objPreferenciaDeFamiliarVO=None):
        if objPreferenciaDeFamiliarVO is None:
            item = self.treeview.selection()[0]
            linha = self.treeview.item(item, "values")

            id_familiar, nome_familiar = linha[0].split(": ")
            objFamiliar = FamiliaresVO(int(id_familiar), nome_familiar)

            id_preferencia, descricao_preferencia = linha[1].split(": ")
            objPreferencia = PreferenciasVO(int(id_preferencia), descricao_preferencia)

            intensidade = float(linha[2])
            descricao = linha[3]

            objPreferenciaDeFamiliarVO = PreferenciasDeFamiliaresVO(objFamiliar, objPreferencia,
                                                                    intensidade, descricao)

        FormEditPreferenciaDeFamiliar(objPreferenciaDeFamiliarVO, self)

    def removerPreferenciaFamiliar(self):
        if messagebox.askyesnocancel("Deletar entrada", "Deseja remover essa preferencia de familiar?") is True:
            item = self.treeview.selection()[0]
            linha = self.treeview.item(item, "values")

            id_familiar, nome_familiar = linha[0].split(": ")
            objFamiliar = FamiliaresVO(int(id_familiar), nome_familiar)

            id_preferencia, descricao_preferencia = linha[1].split(": ")
            objPreferencia = PreferenciasVO(int(id_preferencia), descricao_preferencia)

            objPreferenciaDeFamiliarVO = PreferenciasDeFamiliaresVO(objFamiliar, objPreferencia)
            PreferenciasDeFamiliaresBLL().removerPreferenciaFamiliar(objPreferenciaDeFamiliarVO)

    def exportExcel(self):
        file_path = filedialog.asksaveasfile(mode='w', defaultextension='.xlsx', filetypes=[("Arquivo Excel", ".xlsx")],
                                             initialfile=f"pref_familiares")
        if file_path:
            lista_familiares = self.read_valores_combobox()
            ExporterBLL.exportarTabelaExcel(lista_familiares, file_path.name)
            messagebox.showinfo("Sucesso", "Excel exportado com sucesso!")

    def exportEmail(self):
        file_paths = filedialog.askopenfilenames(title="Selecione um arquivo",
                                                 filetypes=[("Arquivos de Excel", "*.xlsx")],
                                                 )
        if file_paths:
            lista_familiares = self.read_valores_combobox()
            ExporterBLL.exportarTabelaEmail(lista_familiares, file_paths)
            messagebox.showinfo("Sucesso", "Email enviado com sucesso!")

    def read_valores_combobox(self):
        familiar = self.familiarCombobox.get()
        preferencia = self.preferenciasCombobox.get()
        if familiar != "":
            id, nome = familiar.split(": ")
            objFamiliar = FamiliaresVO(id=id, nome=nome)

            lista_familiares = PreferenciasDeFamiliaresBLL().importPreferenciasFamiliares(objFamiliar)
            if preferencia != "":
                id_pref, descricao = preferencia.split(": ")
                id_pref = int(id_pref)
                lista_familiares = [obj for obj in lista_familiares if obj.objPreferencia.id == id_pref]
            return lista_familiares
        return None

    def updateTreeview(self, linhas):
        try:
            self.treeview.delete(*self.treeview.get_children())
            for linha in linhas:
                familiar = f"{linha.objFamiliar.id}: {linha.objFamiliar.nome}"
                preferencia = f"{linha.objPreferencia.id}: {linha.objPreferencia.descricao}"

                values = [familiar, preferencia, linha.intensidade, linha.observacao]
                self.treeview.insert('', 'end', values=values)
        except Exception as e:
            raise e

    def clearTreeview(self):
        self.treeview.delete(*self.treeview.get_children())
