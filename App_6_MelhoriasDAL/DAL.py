import pyodbc
from io import StringIO

class Dados():
    def __init__(self):
        return
    
    def ImportarBDConectado():
        try:
            connectionString = (
                r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
                r'DBQ=C:.\ExercicioAccess_20231012.accdb;'
            )
            objConexao = pyodbc.connect(connectionString)
            objLeitorBD = objConexao.cursor()
            strSQL = StringIO()
            strSQL.write('SELECT')
            strSQL.write(' ID')
            strSQL.write(',Descricao')
            strSQL.write(' FROM ')
            strSQL.write('Preferencias3')
            # strSQL = "SELECT ID, Descricao FROM Preferencias3"
            objLeitorBD.execute(strSQL.getvalue())

            dados = []
            record = objLeitorBD.fetchone()

            while record != None:
                dados.append(record)
                record = objLeitorBD.fetchone()

            objLeitorBD.close()
            return dados

        except Exception as e:
            raise Exception(f'Problemas na consulta da tabela Preferencias: {e.args}')

        finally:
            objConexao.close()

    def ImportarBDDesconectado():
        try:
            connectionString = (
                r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
                r'DBQ=.\ExercicioAccess_20231012.accdb;'
            )
            objConexao = pyodbc.connect(connectionString)
            objLeitorBD = objConexao.cursor()
            strSQL = StringIO()
            strSQL.write('SELECT')
            strSQL.write(' ID')
            strSQL.write(',Descricao')
            strSQL.write(' FROM ')
            strSQL.write('Preferencias3')
            # strSQL = "SELECT ID, Descricao FROM Preferencias3"
            objLeitorBD.execute(strSQL.getvalue())

            record = objLeitorBD.fetchall()
            objConexao.close()

            dados = []
            for dado in record:
                dados.append(dado)

            return dados

        except Exception as e:
            raise Exception(f'Problemas na consulta da tabela Preferencias: {e.args}')

        finally:
            try:
                objLeitorBD.close()
            except:
                pass
            try:
                objConexao.close()
            except:
                pass

    def AdicionarEntradaBD(dadoAdicionar):
        try:
            if dadoAdicionar != None or "":
                connectionString = (
                    r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
                    r'DBQ=.\ExercicioAccess_20231012.accdb;'
                )
                objConexao = pyodbc.connect(connectionString)
                objLeitorBD = objConexao.cursor()

                strSQL = StringIO()
                strSQL.write('INSERT INTO Preferencias3 (')
                strSQL.write(' Descricao')
                strSQL.write(') VALUES (')
                strSQL.write(' ?')
                strSQL.write(')')

                # strSQL = "INSERT INTO Preferencias3 ( Descricao ) VALUES (?)"
                objLeitorBD.execute(strSQL.getvalue(), (dadoAdicionar))
                objLeitorBD.commit()
                objConexao.close()
            else:
                return
        except Exception as e:
            raise Exception(f"Problemas ao adicionar linha em Propriedades: {e}")
        finally:
            try:
                objLeitorBD.close()
            except:
                pass
            try:
                objConexao.close()
            except:
                pass

    def EditarEntradaBD(idEditar, dadoValorNovo):
        try:
            connectionString = (
                r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
                r'DBQ=.\ExercicioAccess_20231012.accdb;'
            )
            objConexao = pyodbc.connect(connectionString)
            objLeitorBD = objConexao.cursor()

            strSQL = StringIO()
            strSQL.write("UPDATE Preferencias3 SET")
            strSQL.write(" Descricao = ?")
            strSQL.write(" WHERE ID = ?")

            # strSQL = "UPDATE Preferencias3 SET Descricao = (?) WHERE ID = (?)"
            objLeitorBD.execute(strSQL.getvalue(), (dadoValorNovo, idEditar))
            objLeitorBD.commit()
            objConexao.close()
        except Exception as e:
            raise Exception(f"Problemas ao editar entrada em propriedades: {e}")
        finally:
            try:
                objLeitorBD.close()
            except:
                pass
            try:
                objConexao.close()
            except:
                pass

    def RemoverEntradaBD(idRemover):
        try:
            connectionString = (
                r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
                r'DBQ=.\ExercicioAccess_20231012.accdb;'
            )
            objConexao = pyodbc.connect(connectionString)
            objLeitorBD = objConexao.cursor()

            strSQL = StringIO()
            strSQL.write("DELETE FROM Preferencias3")
            strSQL.write(" WHERE ID = ?")
            # strSQL = "DELETE FROM Preferencias3 Where ID = (?)"

            objLeitorBD.execute(strSQL.getvalue(), (idRemover))
            objLeitorBD.commit()
            objConexao.close()
        except Exception as e:
            raise Exception(f"Problemas ao adicionar linha em Propriedades: {e}")
        finally:
            try:
                objLeitorBD.close()
            except:
                pass
            try:
                objConexao.close()
            except:
                pass


    #Funcoes da tabela Parentes
    #Nunca usar asterisco, especificar colunas
    def ImportarBDParentesDesconectado():
        try:
            connectionString = (
                r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
                r'DBQ=.\ExercicioAccess_20231012.accdb;'
            )
            objConexao = pyodbc.connect(connectionString)
            objLeitorBD = objConexao.cursor()

            strSQL = StringIO()
            strSQL.write("SELECT")
            strSQL.write(" ID")
            strSQL.write(",Nome")
            strSQL.write(",Sexo")
            strSQL.write(",Idade")
            strSQL.write(",Salario")
            strSQL.write(",Favorito")
            strSQL.write(" FROM PARENTES")

            # strSQL = "SELECT * FROM Parentes"
            objLeitorBD.execute(strSQL.getvalue())

            record = objLeitorBD.fetchall()
            objConexao.close()

            dados = []
            for dado in record:
                dados.append(dado)
            return dados

        except Exception as e:
            raise Exception(f"Erro ao consultar parentes: {e}")
        finally:
            try:
                objLeitorBD.close()
            except:
                pass
            try:
                objConexao.close()
            except:
                pass

    def ConsultarBDParentes(ID=None):
        try:
            connectionString = (
                r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
                r'DBQ=.\ExercicioAccess_20231012.accdb;'
            )
            objConexao = pyodbc.connect(connectionString)
            objLeitorBD = objConexao.cursor()

            strSQL = StringIO()
            strSQL.write("SELECT")
            strSQL.write(" ID")
            strSQL.write(",Nome")
            strSQL.write(",Sexo")
            strSQL.write(",Idade")
            strSQL.write(",Salario")
            strSQL.write(",Favorito")
            strSQL.write(" FROM PARENTES")

            if ID is not None:
                strSQL.write(" WHERE ID = ?")
                objLeitorBD.execute(strSQL.getvalue(), (ID,))
            else:
                objLeitorBD.execute(strSQL.getvalue())

            record = objLeitorBD.fetchall()
            objConexao.close()
        except Exception as e:
            raise Exception(f"Erro aou consultar parentes: {e}")
        else:
            if record:
                return record[0]
            else:
                return None
        finally:
            try:
                objLeitorBD.close()
            except:
                pass
            try:
                objConexao.close()
            except:
                pass

    def AdicionarEntradaBDParentes(dadoAdicionar):
        try:
            if dadoAdicionar != None or "":
                connectionString = (
                    r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
                    r'DBQ=.\ExercicioAccess_20231012.accdb;'
                )
                objConexao = pyodbc.connect(connectionString)
                objLeitorBD = objConexao.cursor()

                strSQL = StringIO()
                strSQL.write("INSERT INTO Parentes (")
                strSQL.write(" Nome")
                strSQL.write(",Sexo")
                strSQL.write(",Idade")
                strSQL.write(",Salario")
                strSQL.write(",Favorito")
                strSQL.write(") VALUES (")
                strSQL.write(" ?")
                strSQL.write(",?")
                strSQL.write(",?")
                strSQL.write(",?")
                strSQL.write(",?")
                strSQL.write(")")
                #strSQL = "INSERT INTO Parentes (Nome, Sexo, Idade, Salario, Favorito) VALUES (?, ?, ?, ?, ?)"

                objLeitorBD.execute(strSQL.getvalue(), tuple(dadoAdicionar))
                objLeitorBD.commit()
            else:
                return
        except Exception as e:
            raise Exception(f"Erro ao adicionar parente: {e}")
        finally:
            try:
                objLeitorBD.close()
            except:
                pass
            try:
                objConexao.close()
            except:
                pass

    def EditarEntradaBDParentes(dadosValorNovo):
        try:
            #Correção de tipo de entrada para a função.
            if type(dadosValorNovo) == list:
                dadosValorNovo = tuple(dadosValorNovo)

            connectionString = (
                r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
                r'DBQ=.\ExercicioAccess_20231012.accdb;'
            )
            objConexao = pyodbc.connect(connectionString)
            objLeitorBD = objConexao.cursor()

            strSQL = StringIO()
            strSQL.write("UPDATE Parentes SET")
            strSQL.write(" Nome = ?")
            strSQL.write(",Sexo = ?")
            strSQL.write(",Idade = ?")
            strSQL.write(",Salario = ?")
            strSQL.write(",Favorito = ?")
            strSQL.write(" WHERE ID = ?")

            # strSQL = "UPDATE Parentes SET Nome = ?, Sexo = ?,Idade = ?,Salario = ?,Favorito = ? WHERE ID = ? "

            objLeitorBD.execute(strSQL.getvalue(), tuple(dadosValorNovo))
            objLeitorBD.commit()
        except Exception as e:
            raise Exception(f"Erro ao editar parentes: {e}")
        finally:
            try:
                objLeitorBD.close()
            except:
                pass
            try:
                objConexao.close()
            except:
                pass

    def RemoverEntradaBDParentes(IdRemover):
        try:
            connectionString = (
                r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
                r'DBQ=.\ExercicioAccess_20231012.accdb;'
            )
            objConexao = pyodbc.connect(connectionString)
            objLeitorBD = objConexao.cursor()

            strSQL = StringIO()
            strSQL.write("DELETE FROM Parentes")
            strSQL.write(" WHERE ID = ?")

            # strSQL = "DELETE FROM Parentes Where ID = (?)"
            objLeitorBD.execute(strSQL.getvalue(), (IdRemover))
            objLeitorBD.commit()
        except Exception as e:
            raise Exception(f"Erro ao deletar parentes: {e}")
        finally:
            try:
                objLeitorBD.close()
            except:
                pass
            try:
                objConexao.close()
            except:
                pass