import pyodbc
from io import StringIO
from abc import abstractmethod


class DataBank:
    _connection = None
    _pathBD = None

    def __init__(self, pathBD=None):
        if pathBD is not None:
            DataBank._pathBD = pathBD
        else:
            DBstring = StringIO()
            DBstring.write(r"DRIVER={Microsoft Access Driver ( *.mdb, *.accdb)};")
            DBstring.write(r"DBQ = C:\Curso Programar\python\Exercicio_Model_Refatorado_20240110\DAL\ExercicioAccess_20231012.accdb;;")

            DataBank._pathBD = DBstring.getvalue()

        DataBank.getConexao()

    @staticmethod
    def getConexao():
        if DataBank._connection is None:
            DataBank.setConexao()

        return DataBank._connection

    @staticmethod
    def setConexao():
        """connectionString = (
            r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
            r'DBQ=C:.\ExercicioAccess_20231012.accdb;'
        )"""
        with (open(".\config.ini", "r") as arquivo):
            connectionString = StringIO()
            connectionString.write(arquivo.readline())
            connectionString.write(arquivo.readline())

            connectionString = connectionString.getvalue()

        objConexao = pyodbc.connect(connectionString)
        DataBank._connection = objConexao

    @property
    def connection(self):
        return DataBank.getConexao()


# Data Access Layer Data Access Object
class DALDAO(DataBank):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def consultarBD(self):
        pass

    @abstractmethod
    def incluirBD(self, objModel):
        pass

    @abstractmethod
    def editarBD(self, objModel):
        pass

    @abstractmethod
    def excluirBD(self, objModel):
        pass


# Data Access Layer Data Access Object
class DALDAO(DataBank):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def consultarBD(self):
        pass

    @abstractmethod
    def incluirBD(self, objModel):
        pass

    @abstractmethod
    def editarBD(self, objModel):
        pass

    @abstractmethod
    def excluirBD(self, objModel):
        pass
