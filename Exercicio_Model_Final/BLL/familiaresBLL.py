from DAL.familiaresDAL import FamiliaresDAL
from FRONT.builders import BuilderFamiliaresCombobox


class FamiliaresBLL:
    def __init__(self):
        pass

    def importarBDFamiliares(self):
        try:
            dados = FamiliaresDAL().importarBD()
            self.updateComboboxFamiliar(dados)
            return dados
        except Exception as e:
            raise e

    def consultarBDFamiliares(self, parFamiliaresVO):
        try:
            return FamiliaresDAL().consultarBD(parFamiliaresVO)
        except Exception as e:
            raise e

    def adicionarFamiliar(self, parFamiliaresVO):
        try:
            FamiliaresDAL().incluirBD(parFamiliaresVO)
            self.updateComboboxFamiliar()
        except Exception as e:
            raise e

    def editarFamiliar(self, parFamiliaresVO):
        try:
            FamiliaresDAL().editarBD(parFamiliaresVO)
            self.updateComboboxFamiliar()
        except Exception as e:
            raise e

    def removerFamiliar(self, parFamiliaresVO):
        try:
            FamiliaresDAL().excluirBD(parFamiliaresVO)
            self.updateComboboxFamiliar()
        except Exception as e:
            raise e

    def updateComboboxFamiliar(self, dados=None):
        if dados is None:
            dados = self.importarBDFamiliares()

        BuilderFamiliaresCombobox.update_all(dados)

