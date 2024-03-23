from io import StringIO
from MODELS.familiaresVO import FamiliaresVO
from DAL.DBDAL import DALDAO


class FamiliaresDAL(DALDAO):
    def __init__(self):
        super().__init__()

    def importarBD(self):
        try:
            objConexao = self.connection
            objLeitorBD = objConexao.cursor()

            strSQL = StringIO()
            strSQL.write("SELECT")
            strSQL.write(" ID")
            strSQL.write(",Nome")
            strSQL.write(",Sexo")
            strSQL.write(",Idade")
            strSQL.write(",Salario")
            strSQL.write(",Observacao")
            strSQL.write(" FROM Familiares")

            strSQL = strSQL.getvalue()
            objLeitorBD.execute(strSQL)

            record = objLeitorBD.fetchall()

            dados = []
            for dado in record:
                objFamiliaresVO = FamiliaresVO(dado[0], dado[1], dado[2], dado[3], dado[4], dado[5])
                dados.append(objFamiliaresVO)
            return dados

        except Exception as e:
            raise Exception(f"Erro ao consultar Familiares: {e}")
        finally:
            try:
                objLeitorBD.close()
            except:
                pass

    def consultarBD(self, objModel=None):
        try:
            objConexao = self.connection
            objLeitorBD = objConexao.cursor()

            strSQL = StringIO()
            strSQL.write("SELECT")
            strSQL.write(" ID")
            strSQL.write(",Nome")
            strSQL.write(",Sexo")
            strSQL.write(",Idade")
            strSQL.write(",Salario")
            strSQL.write(",Observacao")
            strSQL.write(" FROM Familiares")
            strSQL.write(" WHERE TRUE")

            if objModel.id is not None:
                strSQL.write(" AND ID = ?")
                objLeitorBD.execute(strSQL.getvalue(), (objModel.id,))
            else:
                objLeitorBD.execute(strSQL.getvalue())

            record = objLeitorBD.fetchall()
        except Exception as e:
            raise Exception(f"Erro aou consultar Familiares: {e}")
        else:
            if record:
                record = record[0]
                objFamiliaresVO = FamiliaresVO(record[0], record[1], record[2], int(record[3]), float(record[4]), record[5])
                return objFamiliaresVO
            else:
                return None
        finally:
            try:
                objLeitorBD.close()
            except:
                pass

    def incluirBD(self, parFamiliaresVO):
        try:
            if parFamiliaresVO is not None or "":
                objConexao = self.connection
                objLeitorBD = objConexao.cursor()

                strSQL = StringIO()
                strSQL.write("INSERT INTO Familiares (")
                strSQL.write(" Nome")
                strSQL.write(",Sexo")
                strSQL.write(",Idade")
                strSQL.write(",Salario")
                strSQL.write(",Observacao")
                strSQL.write(") VALUES (")
                strSQL.write(" ?")
                strSQL.write(",?")
                strSQL.write(",?")
                strSQL.write(",?")
                strSQL.write(",?")
                strSQL.write(")")
                # strSQL = "INSERT INTO Familiares (Nome, Sexo, Idade, Salario, Observacao) VALUES (?, ?, ?, ?, ?)"

                objLeitorBD.execute(strSQL.getvalue(), (parFamiliaresVO.nome,
                                                        parFamiliaresVO.sexo,
                                                        parFamiliaresVO.idade,
                                                        parFamiliaresVO.salario,
                                                        parFamiliaresVO.observacao)
                                    )
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

    def editarBD(self, parFamiliaresVO):
        try:
            objConexao = self.connection
            objLeitorBD = objConexao.cursor()

            strSQL = StringIO()
            strSQL.write("UPDATE Familiares SET")
            strSQL.write(" Nome = ?")
            strSQL.write(",Sexo = ?")
            strSQL.write(",Idade = ?")
            strSQL.write(",Salario = ?")
            strSQL.write(",Observacao = ?")
            strSQL.write(" WHERE ID = ?")

            # strSQL = "UPDATE Familiares SET Nome = ?, Sexo = ?,Idade = ?,Salario = ?,Observacao = ? WHERE ID = ? "

            objLeitorBD.execute(strSQL.getvalue(), (parFamiliaresVO.nome,
                                                            parFamiliaresVO.sexo,
                                                            parFamiliaresVO.idade,
                                                            parFamiliaresVO.salario,
                                                            parFamiliaresVO.observacao,
                                                            parFamiliaresVO.id))
            objLeitorBD.commit()
        except Exception as e:
            raise Exception(f"Erro ao editar Familiares: {e}")
        finally:
            try:
                objLeitorBD.close()
            except:
                pass

    def excluirBD(self, parFamiliaresVO):
        try:
            objConexao = self.connection
            objLeitorBD = objConexao.cursor()

            strSQL = StringIO()
            strSQL.write("DELETE FROM Familiares")
            strSQL.write(" WHERE ID = ?")

            # strSQL = "DELETE FROM Familiares Where ID = (?)"
            objLeitorBD.execute(strSQL.getvalue(), (parFamiliaresVO.id))
            objLeitorBD.commit()
        except Exception as e:
            raise Exception(f"Erro ao deletar Familiares: {e}")
        finally:
            try:
                objLeitorBD.close()
            except:
                pass