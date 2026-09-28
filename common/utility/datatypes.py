from typing import Any
from enum import Enum


class FormAction(Enum):
    CREATE = 0
    UPDATE = 1


class FormResult(Enum):
    SAVE = 1
    BACK = 2
    CANCEL = 3
    EDIT = 4
    CLOSE = 5


class MethodResult:

    def __init__(self, success: bool, error_message: BaseException | str | None = None, return_data: Any = None) -> None:
        self.__success = success
        self.__error_message: BaseException | str | None = error_message
        self.__return_data = return_data

    @property
    def success(self) -> bool:
        return self.__success

    @property
    def error_message(self) -> str:
        return self.__error_message

    @property
    def return_data(self) -> Any:
        return self.__return_data
