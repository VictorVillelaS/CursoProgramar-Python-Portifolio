class PreferenciasDeFamiliaresVO:
    def __init__(self, obj_familiar=None, obj_preferencia=None, intensidade=None, observacao=None):
        self._obj_familiar = obj_familiar
        self._obj_preferencia = obj_preferencia
        self._intensidade = intensidade
        self._observacao = observacao

    def get_obj_familiar(self):
        return self._obj_familiar

    def set_obj_familiar(self, value):
        self._obj_familiar = value

    def get_obj_preferencia(self):
        return self._obj_preferencia

    def set_obj_preferencia(self, value):
        self._obj_preferencia = value

    def get_intensidade(self):
        return self._intensidade

    def set_intensidade(self, value):
        self._intensidade = value

    def get_observacao(self):
        return self._observacao

    def set_observacao(self, value):
        self._observacao = value

    objFamiliar = property(get_obj_familiar, set_obj_familiar)
    objPreferencia = property(get_obj_preferencia, set_obj_preferencia)
    intensidade = property(get_intensidade, set_intensidade)
    observacao = property(get_observacao, set_observacao)
