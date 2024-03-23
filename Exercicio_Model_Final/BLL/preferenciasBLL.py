from DAL.preferenciasDAL import PreferenciasDAL
from FRONT.builders import BuilderPreferenciasCombobox


class PreferenciasBLL:
    def __init__(self):
        pass

    def importarBDDesconectado(self):
        try:
            dados = PreferenciasDAL().consultarBD()
            self.updateComboboxPreferencia(dados)
            return dados
        except Exception as e:
            raise e

    def adicionarEntradaBD(self, parPreferenciasVO):
        try:
            PreferenciasDAL().incluirBD(parPreferenciasVO)
            self.updateComboboxPreferencia()
        except Exception as e:
            raise e

    def editarEntradaBD(self, parPreferenciasVO):
        try:
            PreferenciasDAL().editarBD(parPreferenciasVO)
            self.updateComboboxPreferencia()
        except Exception as e:
            raise e

    def removerEntradaBD(self, parPreferenciasVO):
        try:
            PreferenciasDAL().excluirBD(parPreferenciasVO)
            self.updateComboboxPreferencia()
        except Exception as e:
            raise e

    def updateComboboxPreferencia(self, dados=None):
        if dados is None:
            dados = self.importarBDDesconectado()

        BuilderPreferenciasCombobox.update_all(dados)
