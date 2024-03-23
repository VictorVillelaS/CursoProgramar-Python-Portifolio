import tkinter as tk
from tkinter import messagebox
from BLL.familiaresBLL import FamiliaresBLL
from MODELS.familiaresVO import FamiliaresVO
from FRONT.builders import BuilderEntry, BuilderCombobox


class FormEditFamiliar(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.padx = 10
        self.pady = 5
        self.title = "Editar Cliente"

        self.id = BuilderEntry(self, "ID")
        self.id.pack(side='top', padx=self.padx, pady=self.pady)
        self.id.entry.bind("<KeyRelease>", self.atualizarInformacoes)

        self.entryNome = BuilderEntry(self, "Nome")
        self.entryNome.pack(side='top', padx=self.padx, pady=self.pady)

        self.comboboxSexo = BuilderCombobox(self, "Sexo", ["Homem", "Mulher", "Outro"])
        self.comboboxSexo.pack(side='top', padx=self.padx, pady=self.pady)

        self.entryIdade = BuilderEntry(self, "Idade", varType=int)
        self.entryIdade.pack(side='top', padx=self.padx, pady=self.pady)

        self.entrySalario = BuilderEntry(self, "Salario", varType=int)
        self.entrySalario.pack(side='top', padx=self.padx, pady=self.pady)

        self.entryFavorito = BuilderEntry(self, "Favorito")
        self.entryFavorito.pack(side='top', padx=self.padx, pady=self.pady)

        self.btnSave = tk.Button(self, text="Editar", width=10, command=self.editFamiliar)
        self.btnSave.pack(side='top', padx=self.padx, pady=self.pady)

        self.mainloop()

    def atualizarInformacoes(self, event):
        print("update:")
        id = int(self.id.get())
        print(f"id = {id}")
        infocliente = FamiliaresBLL().consultarBDFamiliares(FamiliaresVO(id=id))

        if infocliente is not None:
            print(f"linha encontrada!:{infocliente}")
            self.entryNome.set(infocliente.nome)
            self.comboboxSexo.set(infocliente.sexo)
            self.entryIdade.set(infocliente.idade)
            self.entrySalario.set(infocliente.salario)
            self.entryFavorito.set(infocliente.favorito)
        else:
            print("nada encontrado.")
            print("")
            self.entryNome.set("")
            self.comboboxSexo.set("")
            self.entryIdade.set("")
            self.entrySalario.set("")
            self.entryFavorito.set("")

    def editFamiliar(self):
        ID = self.id.get()
        nome = self.entryNome.get()
        sexo = self.comboboxSexo.get()
        idade = self.entryIdade.get()
        salario = self.entrySalario.get()
        favorito = self.entryFavorito.get()

        if messagebox.askokcancel("Confirmar edição", "Tem certeza que deseja editar esse familiar") is True:
            try:
                objFamiliaresVO = FamiliaresVO(ID, nome, sexo, idade, salario, favorito)
                FamiliaresBLL().editarFamiliar(objFamiliaresVO)
                self.destroy()
            except Exception as e:
                raise e
