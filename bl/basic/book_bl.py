import yaml
from common.basic.book import Book
from common.utility.datatypes import MethodResult
from dal.text_file_data_source_manager import TextFileDataSourceManager


class BookBL:

    def __init__(self) -> None:
        self.__save_path = yaml.safe_load(open("App.config"))[
            'appsettings']['filedataPath']
        self.__dal_class = TextFileDataSourceManager(path=self.__save_path)

        result: MethodResult = self.__dal_class.load_data()
        self.__book_list:  list[Book] = []

        for item in result.return_data:
            self.__book_list.append(
                Book.text_to_entity(item)
            )

    # def ____validation(self, book):
    #     pass

    def get_list(self) -> list[Book]:
        return self.__book_list

    def create(self, book: Book) -> MethodResult:

        result: MethodResult = self.__dal_class.save_data(instace=book)

        if not result.success:
            return MethodResult(success=False, error_message="Error !!!")

        self.__book_list.append(book)
        return MethodResult(success=True)

    # def update(self, book):
    #     if not self.__validation(book):
    #         return False

    #     #TODO
    #     return True

    def delete(self, book: Book):

        self.__book_list.remove(book)

        result: MethodResult = self.__dal_class.save_data(
            instace=self.__book_list,
            mode="w",
            write_state="wl"
        )

        if not result.success:
            return MethodResult(success=False, error_message="Error !!!")

        self.__book_list.append(book)
        return MethodResult(success=True)
