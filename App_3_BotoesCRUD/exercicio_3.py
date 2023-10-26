# 5 botoes: 1 com mensagem, 1 desvio condicional, 1 desv cond encadeado, 1 match case, 1 importar texto c/ while e
# mostrar na listbox while, mostrar na listbox for c/ indice, mostrar na listbox for s/ indice, limpar listbox
# tempo limite: 35 min

"""
main: iniciar programa


class FrmPrincipal
definir nela a construção da tela principal

#data access layer
class dal - banco de dados
class preferenciasDao
"""

from tkinter import *
from tkinter import messagebox
from tkinter.simpledialog import askstring
from preferencias import Preferencias_BLL

def Mensagem():
    messagebox.showinfo(title='Mensagem', message='Isso é uma mensagem!')


def DesvCond():
    resposta = messagebox.askyesno(title='y/n', message='Sim ou não?')
    if resposta:
        messagebox.showinfo(title='y', message='Sim')
    else:
        messagebox.showinfo(title='n', message='Nao')


def DesvCondEncadeado():
    resposta = messagebox.askyesnocancel(title='y/n/c', message='Sim ou não?')
    if resposta == True:
        messagebox.showinfo(title='y', message='Sim')
    elif resposta == False:
        messagebox.showinfo(title='n', message='Nao')
    else:
        messagebox.showinfo(title='c', message='Cancel')


def MatchCase():
    resposta = messagebox.askyesnocancel(title='y/n/c', message='Sim ou não?')
    match resposta:
        case True:
            messagebox.showinfo(title='y', message='Sim')
        case False:
            messagebox.showinfo(title='n', message='Nao')
        case None:
            messagebox.showinfo(title='c', message='Cancel')


def ListboxWhile(listbox):
    objPreferencia = Preferencias_BLL
    PreencheListbox(objPreferencia.ListboxWhile(), listbox)


def ListboxForComIndice(listbox):
    objPreferencia = Preferencias_BLL
    PreencheListbox(objPreferencia.ListboxForComIndice(), listbox)


def ListboxForSemIndice(listbox):
    objPreferencia = Preferencias_BLL
    PreencheListbox(objPreferencia.ListboxForSemIndice(), listbox)


def getInfoAdicionar():
    def funcao_adicionar():
        Preferencias_BLL.AdicionarEntradaBD(entryAdicionar.get())
        janelaAdicionar.destroy()

    janelaAdicionar = Tk()
    janelaAdicionar.title("Adicionar dados")

    labelAdicionar = Label(janelaAdicionar, text="Adicionar dado:")
    labelAdicionar.grid(row=0,column=0, padx=10, pady=10)
    entryAdicionar = Entry(janelaAdicionar)
    entryAdicionar.grid(row=1, column=0, padx=10, pady=10)
    btnAdicionar = Button(janelaAdicionar, text="Salvar", command=funcao_adicionar)
    btnAdicionar.grid(row=2, column=0, padx=10, pady=10)


def getInfoEditar():
    dadoEditar = askstring("Editar dado", "Valor que deve ser editado:")
    dadoEditado = askstring(f"Editar dado", f"Mudar '{dadoEditar}' para:")
    return (dadoEditar, dadoEditado)


def getInfoRemover():
    dadoRemover = askstring("Remover dado", "Dado a ser removido:")
    return dadoRemover


def PreencheListbox(linhas, listbox):
    LimpaListbox(listbox)
    for i in linhas:
        listbox.insert(END, i)

def LimpaListbox(listbox):
    listbox.delete(0, END)


Janela = Tk()

LstBox = Listbox(Janela, height=21,  width=30)
LstBox.place(x=300, y=30)

BtnMensagem = Button(Janela, fg='black', width=30, bg='grey', text='Mensagem', command=lambda:messagebox.showinfo(title='Mensagem', message='Isso é uma mensagem!'))
BtnMensagem.place(x=30, y=30)

BtnDesvCond = Button(Janela, fg='black', width=30, bg='grey', text='Desvio Condicional', command=DesvCond)
BtnDesvCond.place(x=30, y=70)

BtnDesvCondEncadeado = Button(Janela, fg='black', width=30, bg='grey', text='Desvio Cond Encadeado', command=DesvCondEncadeado)
BtnDesvCondEncadeado.place(x=30, y=110)

BtnMatchCase = Button(Janela, fg='black', width=30, bg='grey', text='Match Case', command=MatchCase)
BtnMatchCase.place(x=30, y=150)

BtnListboxWhile = Button(Janela, fg='black', width=30, bg='grey', text='Listbox While', command=lambda:ListboxWhile(LstBox))
BtnListboxWhile.place(x=30, y=190)

BtnListboxForComIndice = Button(Janela, fg='black', width=30, bg='grey', text='LstBoxFor c/Indice', command=lambda:ListboxForComIndice(LstBox))
BtnListboxForComIndice.place(x=30, y=230)

BtnListboxForSemIndice = Button(Janela, fg='black', width=30, bg='grey', text='LstBoxFor s/Indice', command=lambda:ListboxForSemIndice(LstBox))
BtnListboxForSemIndice.place(x=30, y=270)

BtnImportabdConectado = Button(Janela, fg='black', width=30, bg='blue', text='Importar Listbox do Access (conectado)',
                               command = lambda:PreencheListbox(Preferencias_BLL.ImportarBDConectado(), LstBox))
BtnImportabdConectado.place(x=30, y=310)

BtnImportabdDesconectado = Button(Janela, fg='black', width=30, bg='blue', text='Importar Listbox do Access (desconectado)',
                               command = lambda:PreencheListbox(Preferencias_BLL.ImportarBDDesconectado(), LstBox))
BtnImportabdDesconectado.place(x=30, y=350)

BtnAdicionarEntrada = Button(Janela, fg='black', width=30, bg='green', text='Adicionar Item no Listbox', 
                             command = lambda:Preferencias_BLL.AdicionarEntradaBD(getInfoAdicionar()))
BtnAdicionarEntrada.place(x=30, y=390)

BtnEditarEntrada = Button(Janela, fg='black', width=30, bg='yellow', text='Editar Item no Listbox', 
                          command=lambda:Preferencias_BLL.EditarEntradaBD(*getInfoEditar()))
BtnEditarEntrada.place(x=30, y=430)

BtnRemoverEntrada = Button(Janela, fg='black', width=30, bg='red', text='Remover Item do Listbox', 
                           command = lambda:Preferencias_BLL.RemoverEntradaBD(getInfoRemover()))
BtnRemoverEntrada.place(x=30, y=470)


BtnLimpaListbox = Button(Janela, fg='black', width=30, bg='grey', text='Limpar ListBox', command=lambda:LimpaListbox(LstBox))
BtnLimpaListbox.place(x=30, y=510)


Janela.geometry('600x600+30+30')
Janela.mainloop()