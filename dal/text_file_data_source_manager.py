from typing import Literal, Any
from common.basic.book import Book
from common.utility.datatypes import MethodResult


class TextFileDataSourceManager:

    def __init__(self, path: str) -> None:
        self.__save_path = path

    def save_data(
        self,
        instace: Any | list[Any],
        mode: Literal["w"] | Literal["a"] = "a",
        write_state: Literal["wr"] | Literal["wl"] = "wr"
    ):

        try:
            file_object = open(file=self.__save_path, mode=mode)

            if write_state == "wr":
                file_object.write(f"{str(instace)}\n")

            if write_state == "wl":
                file_object.writelines(
                    map(lambda ins: f"{str(ins)}\n", instace))

        except BaseException as err:
            return MethodResult(success=False, error_message=err)

        else:
            return MethodResult(success=True)

        finally:
            if "file_object" is locals() and (not file_object.closed):
                file_object.close()

    def load_data(self):

        try:
            file_object = open(file=self.__save_path, mode="rt")
            res: list[str] = file_object.readlines()

        except BaseException as err:
            return MethodResult(success=False, error_message=err)

        else:
            return MethodResult(success=True, return_data=res)

        finally:
            if "file_object" is locals() and (not file_object.closed):
                file_object.close()
