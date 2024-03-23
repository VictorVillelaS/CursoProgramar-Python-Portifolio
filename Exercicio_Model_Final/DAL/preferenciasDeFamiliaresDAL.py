import pyodbc
from io import StringIO
from MODELS.preferenciasDeFamiliaresVO import PreferenciasDeFamiliaresVO
from DAL.DBDAL import DALDAO
from MODELS.familiaresVO import FamiliaresVO
from MODELS.preferenciasVO import PreferenciasVO


class PreferenciasDeFamiliaresDAL(DALDAO):
    def __init__(self):
        super().__init__()

    # Consulta o banco de dados por id de familiar
    def consultarBD(self, objFamiliarVO=None) -> list[PreferenciasDeFamiliaresVO]:
        try:
            objConexao = self.connection
            objLeitorBD = self.connection.cursor()

            strSQL = StringIO()
            strSQL.write("SELECT")
            strSQL.write(" idPreferencia")
            strSQL.write(",idFamiliar")
            strSQL.write(",intensidade")
            strSQL.write(",observacao")
            strSQL.write(" FROM PreferenciasFamiliares")
            strSQL.write(f" WHERE idFamiliar = ?")

            strSQL = strSQL.getvalue()
            objLeitorBD.execute(strSQL, (objFamiliarVO.id,))

            resultados = objLeitorBD.fetchall()
            lista_resultados = []
            if resultados is not None:
                for resultado in resultados:
                    objPreferenciasFamiliares = PreferenciasDeFamiliaresVO(
                        obj_preferencia=PreferenciasVO(id=resultado[0]),
                        obj_familiar=FamiliaresVO(id=resultado[1]),
                        intensidade=resultado[2],
                        observacao=resultado[3]
                    )
                    lista_resultados.append(objPreferenciasFamiliares)

            return lista_resultados
        except Exception as e:
            raise Exception(f"Erro ao consultar preferencias de familiares: {e}")
        finally:
            try:
                objLeitorBD.close()
            except:
                pass

    def incluirBD(self, objPreferenciasDeFamiliaresVO):
        try:
            objConexao = self.connection
            objLeitorBD = self.connection.cursor()

            strSQL = StringIO()
            strSQL.write("INSERT INTO PreferenciasFamiliares (")
            strSQL.write(" idPreferencia")
            strSQL.write(",idFamiliar")
            strSQL.write(",intensidade")
            strSQL.write(",observacao")
            strSQL.write(") VALUES (")
            strSQL.write(" ?, ?, ?, ?")
            strSQL.write(" )")
            strSQL = strSQL.getvalue()

            objLeitorBD.execute(strSQL, (objPreferenciasDeFamiliaresVO.objPreferencia.id,
                                         objPreferenciasDeFamiliaresVO.objFamiliar.id,
                                         objPreferenciasDeFamiliaresVO.intensidade,
                                         objPreferenciasDeFamiliaresVO.observacao))
            objConexao.commit()

        except Exception as e:
            raise Exception(f"Erro ao : {e}")
        finally:
            try:
                objLeitorBD.close()
            except:
                pass

    def editarBD(self, objPreferenciasDeFamiliaresVO):
        try:
            objConexao = self.connection
            objLeitorBD = self.connection.cursor()

            strSQL = StringIO()
            strSQL.write("UPDATE PreferenciasFamiliares SET")
            strSQL.write(" intensidade = ?")
            strSQL.write(",observacao = ?")
            strSQL.write(" WHERE idPreferencia = ?")
            strSQL.write(" AND idFamiliar = ?")
            strSQL = strSQL.getvalue()

            objLeitorBD.execute(strSQL, (objPreferenciasDeFamiliaresVO.intensidade,
                                         objPreferenciasDeFamiliaresVO.observacao,
                                         objPreferenciasDeFamiliaresVO.objPreferencia.id,
                                         objPreferenciasDeFamiliaresVO.objFamiliar.id))
            objConexao.commit()
        except Exception as e:
            raise Exception(f"Erro ao : {e}")
        finally:
            try:
                objLeitorBD.close()
            except:
                pass

    def excluirBD(self, objPreferenciasDeFamiliaresVO):
        try:
            objConexao = self.connection
            objLeitorBD = self.connection.cursor()

            strSQL = StringIO()
            strSQL.write("DELETE FROM PreferenciasFamiliares")
            strSQL.write(" WHERE idPreferencia = ?")
            strSQL.write(" AND idFamiliar = ?")
            strSQL = strSQL.getvalue()

            objLeitorBD.execute(strSQL, (objPreferenciasDeFamiliaresVO.objPreferencia.id,
                                         objPreferenciasDeFamiliaresVO.objFamiliar.id))
            objConexao.commit()

        except Exception as e:
            raise Exception(f"Erro ao : {e}")
        finally:
            try:
                objLeitorBD.close()
            except:
                pass