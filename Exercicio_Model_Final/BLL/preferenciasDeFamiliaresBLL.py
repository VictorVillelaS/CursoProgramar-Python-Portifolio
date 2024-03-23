from DAL.preferenciasDeFamiliaresDAL import PreferenciasDeFamiliaresDAL
from MODELS.preferenciasDeFamiliaresVO import PreferenciasDeFamiliaresVO
from BLL.familiaresBLL import FamiliaresBLL
from BLL.preferenciasBLL import PreferenciasBLL


class PreferenciasDeFamiliaresBLL:
    def __init__(self):
        pass

    # Recebe um id de familiar e retorna uma lista das preferencias daquele familiar
    # O retorno contém os objetos referentes às preferências
    def importPreferenciasFamiliares(self, objPreferenciaFamiliar):
        try:
            # Consultar as prefernências do familiar
            dadosPrefFamiliares = PreferenciasDeFamiliaresDAL().consultarBD(objPreferenciaFamiliar)

            # Importar as preferências e familiares para montar os objetos adequadamente
            dadosPreferencias = PreferenciasBLL().importarBDDesconectado()
            dadosPreferencias = {obj.id: obj for obj in dadosPreferencias}

            dadosFamiliares = FamiliaresBLL().importarBDFamiliares()
            dadosFamiliares = {obj.id: obj for obj in dadosFamiliares}

            # Adiciona os objetos de preferencia e familiares na Model do objeto PreferenciasDeFamiliaresVO
            for i in range(len(dadosPrefFamiliares)):

                # Pega o id corresponte ao familiar e a preferência
                id_familiar = dadosPrefFamiliares[i].objFamiliar.id
                id_preferencia = dadosPrefFamiliares[i].objPreferencia.id

                # Adicionar o objeto com o id obtido anteriormente na model
                dadosPrefFamiliares[i].objFamiliar = dadosFamiliares[id_familiar]
                dadosPrefFamiliares[i].objPreferencia = dadosPreferencias[id_preferencia]

            return dadosPrefFamiliares

        except Exception as e:
            raise e

    def adicionarPreferenciaFamiliar(self, objPreferenciaFamiliar):
        try:
            PreferenciasDeFamiliaresDAL().incluirBD(objPreferenciaFamiliar)
        except Exception as e:
            raise e

    def editarPreferenciaFamiliar(self, objPreferenciaFamiliar):
        try:
            dados = PreferenciasDeFamiliaresDAL().editarBD(objPreferenciaFamiliar)
            return dados


        except Exception as e:
            raise e

    def removerPreferenciaFamiliar(self, objPreferenciaFamiliar):
        try:
            PreferenciasDeFamiliaresDAL().excluirBD(objPreferenciaFamiliar)
        except Exception as e:
            raise e
