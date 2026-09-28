import uuid
from typing import Optional
from abc import ABCMeta, ABC, abstractmethod


# class Entity(metaclass=ABCMeta):
# class Entity(metaclass=ABCMeta):

class Entity(ABC):

    def __init__(self, description: str, guid: Optional[str] = None) -> None:
        self.description = description
        if not guid:
            self.guid = uuid.uuid4()
        else:
            self.guid = guid

    # region description
    @property
    def description(self) -> str:
        return self._description

    @description.setter
    def description(self, description: str) -> None:
        self._description: str = description
    # endregion

    # region guid
    @property
    def guid(self) -> uuid.UUID:
        return self._guid

    @guid.setter
    def guid(self, guid: uuid.UUID) -> None:
        self._guid: uuid.UUID = guid
    # endregion
    
    @abstractmethod
    def entity_to_text(self):
        return f"description:{self.description}, guid:{self.guid},"
        # """This method should implement how to ...."""

    @abstractmethod
    @staticmethod
    def text_to_entity(data: str) -> object:
        """This method should implement how to ...."""

    def __str__(self) -> str:
        return f"description:{self.description}, guid:{self.guid},"

    # @staticmethod
    # @abstractmethod
    # def say_hi():
    #     pass
