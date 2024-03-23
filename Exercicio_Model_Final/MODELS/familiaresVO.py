from dataclasses import dataclass, field
from typing import Optional, Union

"""
@dataclass
class FamiliaresVO:
    id: Optional[int] = None
    nome: Optional[str] = None
    sexo: Optional[str] = None
    idade: Optional[int] = None
    salario: Optional[Union[float, int]] = None
    favorito: Optional[str] = None
"""


class FamiliaresVO:
    def __init__(self, id=None, nome=None, sexo=None, idade=None, salario=None, observacao=None):
        self._id = id
        self._nome = nome
        self._sexo = sexo
        self._idade = idade
        self._salario = salario
        self._observacao = observacao

    def getId(self):
        return self._id

    def setId(self, id):
        self._id = id

    def getNome(self):
        return self._nome

    def setNome(self, nome):
        self._nome = nome

    def getSexo(self):
        return self._sexo

    def setSexo(self, sexo):
        self._sexo = sexo

    def getIdade(self):
        return self._idade

    def setIdade(self, idade):
        self._idade = idade

    def getSalario(self):
        return self._salario

    def setSalario(self, salario):
        self._salario = salario

    def getObservacao(self):
        return self._observacao

    def setObservacao(self, observacao):
        self._observacao = observacao

    id = property(getId, setId)
    nome = property(getNome, setNome)
    sexo = property(getSexo, setSexo)
    idade = property(getIdade, setIdade)
    salario = property(getSalario, setSalario)
    observacao = property(getObservacao, setObservacao)

    def __str__(self):
        return f"Id:{self.id}, Nome:{self.nome}, Sexo:{self.sexo}, Idade:{self.idade}, Salario:{self.salario} ,Observacao:{self.observacao}"
