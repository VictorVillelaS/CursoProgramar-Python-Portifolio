from tkinter import *
from tkinter import messagebox

def FuncaoMensagem():
    messagebox.showinfo(title='Mensagem', message='Parabéms!')


def FuncaoDesvioCondicional():
    resposta = messagebox.askyesno(title='Sim/Não', message='Sim ou não?')
    if resposta:
        messagebox.showinfo(title='Sim', message='Sim!')
    else:
        messagebox.showinfo(title='Não', message='Não...')


def DesvioCondEncadeado():
    resposta = messagebox.askyesnocancel(title='Y/N/C', message='Sim, não ou cancel?')
    if resposta == True:
        messagebox.showinfo(title='Sim', message='Sim!')
    elif resposta == False:
        messagebox.showinfo(title='Não', message='Não...')
    elif resposta == None:
        messagebox.showinfo(title='Cancel', message='Cancelado!')


def MatchCase():
    resposta = messagebox.askyesnocancel(title='Y/N/C', message='Sim, não ou cancel?')
    match resposta:
        case True:
            messagebox.showinfo(title='Sim', message='Sim!')
        case False:
            messagebox.showinfo(title='Não', message='Não...')
        case None:
            messagebox.showinfo(title='Cancel', message='Cancelado!')


def MostrarListbox():
    with open('Preferencias.txt') as arquivo:
        preferencia = arquivo.readline()
        while preferencia != '':
            Lstbox.insert(END, preferencia)
            preferencia = arquivo.readline()
        arquivo.close()


Janela = Tk()

BotaoMensagem = Button(text='Mensagem!', bg='grey', fg='black', command=FuncaoMensagem)
BotaoMensagem.place(width=200, x=30, y=30)

BotaoDesvCond = Button(text='Desvio Condicional', bg='grey', fg='black', command=FuncaoDesvioCondicional)
BotaoDesvCond.place(width=200, x=30, y=70)

BotaoDesvCondEncadeado = Button(text='Desvio Condicional Encadeado', bg='grey', fg='black', command=DesvioCondEncadeado)
BotaoDesvCondEncadeado.place(width=200, x=30, y=110)

BotaoMatchCase = Button(text='Match Case', bg='grey', fg='black', command=MatchCase)
BotaoMatchCase.place(width=200, x=30, y=150)

BotaoListbox = Button(text='Mostrar itens na listbox', bg='grey', fg='black', command=MostrarListbox)
BotaoListbox.place(width=200, x=30, y=190)

Lstbox = Listbox(height=11)
Lstbox.place(x=300, y=30)


Janela.geometry('500x700+10+10')
Janela.mainloop()
