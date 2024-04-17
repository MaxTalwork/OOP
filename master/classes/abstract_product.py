from abc import ABC, abstractmethod


class AbstractProduct(ABC):  # pragma: no cover
    @classmethod
    @abstractmethod
    def new_prod(cls, *args, **kwargs):
        return args
