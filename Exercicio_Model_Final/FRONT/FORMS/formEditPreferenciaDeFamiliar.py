import tkinter as tk
from tkinter import messagebox
from MODELS.preferenciasDeFamiliaresVO import PreferenciasDeFamiliaresVO
from FRONT.builders import BuilderFamiliaresCombobox, BuilderPreferenciasCombobox, BuilderEntry
from BLL.preferenciasDeFamiliaresBLL import PreferenciasDeFamiliaresBLL


class FormEditPreferenciaDeFamiliar(tk.Tk):
    def __init__(self, objPreferenciaDeFamiliarVO, controller=None):
        super().__init__()
        self.objPreferenciaDeFamiliarVO = objPreferenciaDeFamiliarVO
        self.controller = controller

        self.comboboxFamiliares = BuilderFamiliaresCombobox(self, labelText="Nome do Familiar:")
        self.comboboxFamiliares.pack()
        self.comboboxFamiliares.set_object(objPreferenciaDeFamiliarVO.objFamiliar)

        self.comboboxPreferencias = BuilderPreferenciasCombobox(self, labelText="Nome da Preferência")
        self.comboboxPreferencias.pack()
        self.comboboxPreferencias.set_object(objPreferenciaDeFamiliarVO.objPreferencia)

        self.intensidade = BuilderEntry(self, labelText="Intensidade:")
        self.intensidade.pack()
        self.intensidade.set(objPreferenciaDeFamiliarVO.intensidade)

        self.observacao = BuilderEntry(self, labelText="Observação:")
        self.observacao.pack()
        self.observacao.set(objPreferenciaDeFamiliarVO.observacao)

        self.btnSave = tk.Button(self, text="Salvar", command=self.salvar)
        self.btnSave.pack()

    def salvar(self):
        familiar = self.comboboxFamiliares.get_object()
        preferencia = self.comboboxPreferencias.get_object()
        intensidade = float(self.intensidade.get())
        observacao = self.observacao.get()

        objPreferenciaDeFamiliarVO = PreferenciasDeFamiliaresVO(familiar, preferencia, intensidade, observacao)
        if messagebox.askyesnocancel("Editar", "Deseja editar a preferência?") is True:
            PreferenciasDeFamiliaresBLL().editarPreferenciaFamiliar(objPreferenciaDeFamiliarVO)
            if self.controller is not None:
                self.controller.importarPreferenciasFamiliares()
            self.destroy()
        else:
            pass
