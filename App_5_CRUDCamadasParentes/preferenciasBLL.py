from DAL import Dados
#BLL = Business Logical Layer

class Preferencias():
    def __init__(self):
        return
    
    def ListboxWhile():
        with open('C:\Curso Programar\python\preferencias.txt') as arquivo:
            lista = []
            preferencia = arquivo.readline()
            while preferencia != '':
                lista.append(preferencia)
                preferencia = arquivo.readline()
            arquivo.close()
        return lista
    
    def ListboxForComIndice():
        with open('C:\Curso Programar\python\preferencias.txt') as arquivo:
            preferencias = arquivo.readlines()
        arquivo.close()
        return preferencias
        
    def ListboxForSemIndice():
        with open('C:\Curso Programar\python\preferencias.txt') as arquivo:
            preferencias = arquivo.readlines()
        arquivo.close()
        return preferencias

    def ImportarBDConectado():
        return Dados.ImportarBDConectado()

    def ImportarBDDesconectado():
        return Dados.ImportarBDDesconectado()

    def AdicionarEntradaBD(dados):
        return Dados.AdicionarEntradaBD(dados)

    def EditarEntradaBD(dadoEditar, dadoValorNovo):
        return Dados.EditarEntradaBD(dadoEditar, dadoValorNovo)

    def RemoverEntradaBD(dadoRemover):
        return Dados.RemoverEntradaBD(dadoRemover)