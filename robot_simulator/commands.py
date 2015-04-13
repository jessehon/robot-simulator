from abc import ABCMeta, abstractmethod

class BaseCommand():
    __metaclass__ = ABCMeta
    _identifier = ""
    _params = []

    def __init__(self, params=None):
        self.params = params

    @property
    def identifier(self):
        return self._identifier

    @property
    def params(self):
        return self._params

    @params.setter
    def params(self, values):
        self._params = values

    @abstractmethod
    def invoke(self, target):
        pass
