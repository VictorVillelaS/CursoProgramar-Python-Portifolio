# https://www.scaler.com/topics/multiple-constructors-python/
from dataclasses import dataclass, field
from typing import Optional


"""
@dataclass
class PreferenciasVO:
    id: Optional[int] = field(default=None)
    descricao: Optional[str] = field(default=None)"""


class PreferenciasVO:
    def __init__(self, id=None, descricao=None):
        if id is not None:
            if id != int(id):
                raise Exception('ID inválido')

        if descricao is not None:
            if descricao != str(descricao):
                raise Exception('descricao inválida')

        self._id = id
        self._descricao = descricao

    def getId(self):
        return self._id

    def setId(self, id):
        self._id = id

    def getDescricao(self):
        return self._descricao

    def setDescricao(self, descricao):
        self._descricao = descricao

    id = property(getId, setId)
    descricao = property(getDescricao, setDescricao)

