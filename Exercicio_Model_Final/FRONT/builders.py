import tkinter as tk
from tkinter import ttk


class BuilderEntry(tk.Frame):
    def __init__(self, master, labelText, entryWidth=20, varType=str, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.entryVar = tk.StringVar()
        self.varType = varType

        self.label = tk.Label(self, text=labelText, anchor='w')
        self.label.pack(side='top', fill='x')

        self.entry = tk.Entry(self, textvariable=self.entryVar, width=entryWidth)
        self.entry.pack(side='bottom', anchor='w')

    def get(self):
        value = self.entry.get()
        try:
            return (self.varType(value))
        except(ValueError, TypeError):
            return None

    def set(self, value):
        self.entry.delete(0, tk.END)
        self.entry.insert(0, value)


class BuilderCombobox(tk.Frame):
    def __init__(self, master, labelText, comboboxValues, comboboxWidth=20, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.comboboxVar = tk.StringVar()

        self.label = tk.Label(self, text=labelText, anchor='w')
        self.label.pack(side='top', fill='x')

        self.combobox = ttk.Combobox(self, textvariable=self.comboboxVar, values=comboboxValues, width=comboboxWidth)
        self.combobox.pack(side='bottom')

    def get(self):
        return self.combobox.get()

    def set(self, valor):
        self.combobox.set(valor)


class BuilderFamiliaresCombobox(tk.Frame):
    instancias = []
    dict_valores = {}

    def __init__(self, master, labelText, comboboxWidth=20, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.comboboxVar = tk.StringVar()

        self.label = tk.Label(self, text=labelText, anchor='w')
        self.label.pack(side='top', fill='x')

        self.combobox = ttk.Combobox(self, textvariable=self.comboboxVar, width=comboboxWidth)
        self.combobox.pack(side='bottom')

        BuilderFamiliaresCombobox.instancias.append(self)

        self.update()

    def get(self):
        return self.combobox.get()

    def get_object(self):
        comboboxStr = self.combobox.get()
        id, nome = comboboxStr.split(": ")
        id = int(id)
        return BuilderFamiliaresCombobox.dict_valores[id]

    def set(self, valor):
        self.combobox.set(valor)

    def set_object(self, obj_familiares):
        self.combobox.set(f"{obj_familiares.id}: {obj_familiares.nome}")

    def set_values(self, values):
        self.combobox['values'] = values

    def update(self):
        lista_nomes = [f"{id}: {obj.nome}" for id, obj in BuilderFamiliaresCombobox.dict_valores.items()]
        self.set_values(lista_nomes)

    @staticmethod
    def update_all(novos_valores):
        # Atualiza o dicionario de valores
        BuilderFamiliaresCombobox.dict_valores = {obj.id: obj for obj in novos_valores}

        # Passa esse update para todos os objetos
        for obj in BuilderFamiliaresCombobox.instancias:
            try:
                obj.update()
            except:
                pass


class BuilderPreferenciasCombobox(tk.Frame):
    instancias = []
    dict_valores = {}

    def __init__(self, master, labelText, comboboxWidth=20, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.comboboxVar = tk.StringVar()

        self.label = tk.Label(self, text=labelText, anchor='w')
        self.label.pack(side='top', fill='x')

        self.combobox = ttk.Combobox(self, textvariable=self.comboboxVar, width=comboboxWidth)
        self.combobox.pack(side='bottom')

        BuilderPreferenciasCombobox.instancias.append(self)

        self.update()

    def get(self):
        return self.combobox.get()

    def get_object(self):
        comboboxStr = self.combobox.get()
        id, nome = comboboxStr.split(": ")
        id = int(id)
        return BuilderPreferenciasCombobox.dict_valores[id]

    def set(self, valor):
        self.combobox.set(valor)

    def set_object(self, obj_preferencia):
        self.combobox.set(f"{obj_preferencia.id}: {obj_preferencia.descricao}")

    def set_values(self, values):
        self.combobox['values'] = values

    def update(self):
        lista_nomes = [""] + [f"{id}: {obj.descricao}" for id, obj in BuilderPreferenciasCombobox.dict_valores.items()]
        self.set_values(lista_nomes)

    @staticmethod
    def update_all(novos_valores):
        # Atualiza o dicionario de valores
        BuilderPreferenciasCombobox.dict_valores = {obj.id: obj for obj in novos_valores}

        # Passa esse update para todos os objetos
        for obj in BuilderPreferenciasCombobox.instancias:
            try:
                obj.update()
            except:
                pass