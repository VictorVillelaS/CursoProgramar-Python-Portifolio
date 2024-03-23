import pyodbc
from io import StringIO
from MODELS.preferenciasVO import PreferenciasVO
from DAL.DBDAL import DALDAO


class PreferenciasDAL(DALDAO):
    def __init__(self):
        super().__init__()

    def consultarBDConectado(self):
        try:
            objConexao = self.connection
            objLeitorBD = objConexao.cursor()
            strSQL = StringIO()
            strSQL.write('SELECT')
            strSQL.write(' ID')
            strSQL.write(',Descricao')
            strSQL.write(' FROM ')
            strSQL.write('Preferencias3')

            objLeitorBD.execute(strSQL.getvalue())

            dados = []
            record = objLeitorBD.fetchone()

            while record is not None:
                dados.append(record)
                record = objLeitorBD.fetchone()

            objLeitorBD.close()
            return dados

        except Exception as e:
            raise Exception(f'Problemas na consulta da tabela Preferencias: {e.args}')

    def consultarBD(self):
        try:
            objConexao = self.connection
            objLeitorBD = objConexao.cursor()
            strSQL = StringIO()
            strSQL.write('SELECT')
            strSQL.write(' ID')
            strSQL.write(',Descricao')
            strSQL.write(' FROM Preferencias3')
            objLeitorBD.execute(strSQL.getvalue())

            record = objLeitorBD.fetchall()

            lstPreferenciasVOCollection = []
            for dado in record:
                objPreferenciasVO = PreferenciasVO(dado[0], dado[1])
                lstPreferenciasVOCollection.append(objPreferenciasVO)

            return lstPreferenciasVOCollection

        except Exception as e:
            raise Exception(f'Problemas na consulta da tabela Preferencias: {e.args}')

        finally:
            try:
                objLeitorBD.close()
            except:
                pass

    def incluirBD(self, parPreferenciasVO):
        try:
            objPreferenciasVO = parPreferenciasVO
            if objPreferenciasVO.descricao is not None or "":
                objConexao = self.connection
                objLeitorBD = objConexao.cursor()

                strSQL = StringIO()
                strSQL.write('INSERT INTO Preferencias3 (')
                strSQL.write(' Descricao')
                strSQL.write(') VALUES (')
                strSQL.write(' ?')
                strSQL.write(')')

                # strSQL = "INSERT INTO Preferencias3 ( Descricao ) VALUES (?)"
                objLeitorBD.execute(strSQL.getvalue(), objPreferenciasVO.descricao)
                objLeitorBD.commit()
            else:
                return
        except Exception as e:
            raise Exception(f"Problemas ao adicionar linha em Propriedades: {e}")
        finally:
            try:
                objLeitorBD.close()
            except:
                pass

    def editarBD(self, parPreferenciasVO):
        try:
            objConexao = self.connection
            objLeitorBD = objConexao.cursor()

            strSQL = StringIO()
            strSQL.write("UPDATE Preferencias3 SET")
            strSQL.write(" Descricao = ?")
            strSQL.write(" WHERE ID = ?")

            # strSQL = "UPDATE Preferencias3 SET Descricao = (?) WHERE ID = (?)"
            objLeitorBD.execute(strSQL.getvalue(), (parPreferenciasVO.descricao, parPreferenciasVO.id))
            objLeitorBD.commit()
        except Exception as e:
            raise Exception(f"Problemas ao editar entrada em propriedades: {e}")
        finally:
            try:
                objLeitorBD.close()
            except:
                pass

    def excluirBD(self, parPreferenciasVO):
        try:
            objConexao = self.connection
            objLeitorBD = objConexao.cursor()

            strSQL = StringIO()
            strSQL.write("DELETE FROM Preferencias3")
            strSQL.write(" WHERE ID = ?")
            # strSQL = "DELETE FROM Preferencias3 Where ID = (?)"

            objLeitorBD.execute(strSQL.getvalue(), parPreferenciasVO.id)
            objLeitorBD.commit()
        except Exception as e:
            raise Exception(f"Problemas ao remover linha em Propriedades: {e}")
        finally:
            try:
                objLeitorBD.close()
            except:
                pass