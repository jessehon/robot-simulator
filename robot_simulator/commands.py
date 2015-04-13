from abc import ABCMeta, abstractmethod

class BaseCommand():
    __metaclass__ = ABCMeta
    _identifier = ""
    _args = []

    def __init__(args=None):
        self.args = args

    @property
    def identifier(self):
        return self._identifier

    @property
    def args(self):
        return self._args

    @args.setter
    def args(self, values):
        self._args = values

    @abstractmethod
    def invoke(target):
        pass
