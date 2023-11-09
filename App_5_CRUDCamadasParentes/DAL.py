import pyodbc

class Dados():
    def __init__(self):
        return
    
    def ImportarBDConectado():
        connectionString = (
            r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
            r'DBQ=C:\Curso Programar\python\ExercicioAccess_20231012.accdb;'
        )
        objConexao = pyodbc.connect(connectionString)
        objLeitorBD = objConexao.cursor()
        strSQL = "SELECT Descricao FROM Preferencias3"
        objLeitorBD.execute(strSQL)

        dados = []
        record = objLeitorBD.fetchone()

        while record != None:
            dados.append(record[0])
            record = objLeitorBD.fetchone()

        objLeitorBD.close()
        objConexao.close()
        return dados

    def ImportarBDDesconectado():
        connectionString = (
            r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
            r'DBQ=.\ExercicioAccess_20231012.accdb;'
        )
        objConexao = pyodbc.connect(connectionString)
        objLeitorBD = objConexao.cursor()
        strSQL = "SELECT Descricao FROM Preferencias3"
        objLeitorBD.execute(strSQL)

        record = objLeitorBD.fetchall()
        objConexao.close()

        dados = []
        for dado in record:
            dados.append(dado[0])

        return dados

    def AdicionarEntradaBD(dadoAdicionar):
        if dadoAdicionar != None or "":
            connectionString = (
                r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
                r'DBQ=.\ExercicioAccess_20231012.accdb;'
            )
            objConexao = pyodbc.connect(connectionString)
            objLeitorBD = objConexao.cursor()
        
            strSQL = "INSERT INTO Preferencias3 ( Descricao ) VALUES (?)"
            objLeitorBD.execute(strSQL, (dadoAdicionar))
            objLeitorBD.commit()
            objConexao.close()
        else:
            return

    def EditarEntradaBD(dadoEditar, dadoValorNovo):
        connectionString = (
            r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
            r'DBQ=.\ExercicioAccess_20231012.accdb;'
        )
        objConexao = pyodbc.connect(connectionString)
        objLeitorBD = objConexao.cursor()

        strSQL = "UPDATE Preferencias3 SET Descricao = (?) WHERE Descricao = (?)"
        objLeitorBD.execute(strSQL, (dadoValorNovo, dadoEditar))
        objLeitorBD.commit()
        objConexao.close()

    def RemoverEntradaBD(dadoRemover):
        connectionString = (
            r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
            r'DBQ=.\ExercicioAccess_20231012.accdb;'
        )
        objConexao = pyodbc.connect(connectionString)
        objLeitorBD = objConexao.cursor()
    
        strSQL = "DELETE FROM Preferencias3 Where Descricao = (?)"
        objLeitorBD.execute(strSQL, (dadoRemover))
        objLeitorBD.commit()
        objConexao.close()
    
    #Funcoes da tabela Parentes
    #Nunca usar asterisco, especificar colunas
    def ImportarBDParentesDesconectado():
        connectionString = (
            r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
            r'DBQ=.\ExercicioAccess_20231012.accdb;'
        )
        objConexao = pyodbc.connect(connectionString)
        objLeitorBD = objConexao.cursor()
        strSQL = "SELECT * FROM Parentes"
        objLeitorBD.execute(strSQL)

        record = objLeitorBD.fetchall()
        objConexao.close()

        dados = []
        for dado in record:
            dados.append(dado)

        return dados
    
    def ImportarLinhaBDParentesDesconectado(ID):
        connectionString = (
            r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
            r'DBQ=.\ExercicioAccess_20231012.accdb;'
        )
        objConexao = pyodbc.connect(connectionString)
        objLeitorBD = objConexao.cursor()
        strSQL = "SELECT * FROM Parentes WHERE ID = ?"
        objLeitorBD.execute(strSQL, (ID,))

        record = objLeitorBD.fetchall()
        objConexao.close()

        if record:
            return record[0]
        else:
            return None

    def AdicionarEntradaBDParentes(dadoAdicionar):
        if dadoAdicionar != None or "":
            connectionString = (
                r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
                r'DBQ=.\ExercicioAccess_20231012.accdb;'
            )
            objConexao = pyodbc.connect(connectionString)
            objLeitorBD = objConexao.cursor()
        
            strSQL = "INSERT INTO Parentes (Nome, Sexo, Idade, Salario, Favorito) VALUES (?, ?, ?, ?, ?)"
            objLeitorBD.execute(strSQL, tuple(dadoAdicionar))
            objLeitorBD.commit()
            objConexao.close()
        else:
            return

    def EditarEntradaBDParentes(dadosValorNovo):
        #Correção de tipo de entrada para a função. 
        if type(dadosValorNovo) == list:
            dadosValorNovo = tuple(dadosValorNovo)

        #Conexão do banco de dados
        connectionString = (
            r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
            r'DBQ=.\ExercicioAccess_20231012.accdb;'
        )
        objConexao = pyodbc.connect(connectionString)
        objLeitorBD = objConexao.cursor()

        #Execução do comando em SQL
        strSQL = "UPDATE Parentes SET Nome = ?, Sexo = ?,Idade = ?,Salario = ?,Favorito = ? WHERE ID = ? "

        objLeitorBD.execute(strSQL, tuple(dadosValorNovo))
        objLeitorBD.commit()
        objConexao.close()

    def RemoverEntradaBDParentes(IdRemover):
        connectionString = (
            r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
            r'DBQ=.\ExercicioAccess_20231012.accdb;'
        )
        objConexao = pyodbc.connect(connectionString)
        objLeitorBD = objConexao.cursor()
    
        strSQL = "DELETE FROM Parentes Where ID = (?)"
        objLeitorBD.execute(strSQL, (IdRemover))
        objLeitorBD.commit()
        objConexao.close()