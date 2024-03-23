import tkinter as tk
from tkinter import messagebox
from MODELS.preferenciasDeFamiliaresVO import PreferenciasDeFamiliaresVO
from FRONT.builders import BuilderFamiliaresCombobox, BuilderPreferenciasCombobox, BuilderEntry
from BLL.preferenciasDeFamiliaresBLL import PreferenciasDeFamiliaresBLL


class FormAddPreferenciaDeFamiliar(tk.Tk):
    def __init__(self, controller=None):
        super().__init__()
        self.controller = controller

        self.comboboxFamiliares = BuilderFamiliaresCombobox(self, labelText="Nome do Familiar:")
        self.comboboxFamiliares.pack()

        self.comboboxPreferencias = BuilderPreferenciasCombobox(self, labelText="Nome da Preferência")
        self.comboboxPreferencias.pack()

        self.intensidade = BuilderEntry(self, labelText="Intensidade:")
        self.intensidade.pack()

        self.observacao = BuilderEntry(self, labelText="Observação:")
        self.observacao.pack()

        self.btnSave = tk.Button(self, text="Salvar", command=self.salvar)
        self.btnSave.pack()

    def salvar(self):
        familiar = self.comboboxFamiliares.get_object()
        preferencia = self.comboboxPreferencias.get_object()
        intensidade = self.intensidade.get()
        observacao = self.observacao.get()

        objPreferenciaDeFamiliarVO = PreferenciasDeFamiliaresVO(familiar, preferencia, intensidade, observacao)
        if messagebox.askyesnocancel("Adicionar", "Deseja adicionar a preferência?") is True:
            PreferenciasDeFamiliaresBLL().adicionarPreferenciaFamiliar(objPreferenciaDeFamiliarVO)
            if self.controller is not None:
                self.controller.importarPreferenciasFamiliares()
            self.destroy()
        else:
            pass
