from common.base.entity import Entity
from typing import Optional, override


class Book(Entity):

    def __init__(self, title: str, isbn: str, printyear: int, pages: int, price: float, genres: str, description: str, guid: Optional[str] = None) -> None:
        super().__init__(description=description, guid=guid)
        self.title = title
        self.isbn = isbn
        self.printyear = printyear
        self.pages = pages
        self.price = price
        self.genres = genres

    # region title
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str) -> None:
        self.__title: str = title
    # endregion

    # region isbn
    @property
    def isbn(self) -> str:
        return self.__isbn

    @isbn.setter
    def isbn(self, isbn: str) -> None:
        self.__isbn: str = isbn
    # endregion

    # region printyear
    @property
    def printyear(self) -> int:
        return self.__printyear

    @printyear.setter
    def printyear(self, printyear: int) -> None:
        self.__printyear: int = printyear
    # endregion

    # region pages
    @property
    def pages(self) -> int:
        return self.__pages

    @pages.setter
    def pages(self, pages: int) -> None:
        self.__pages: int = pages
    # endregion

    # region price
    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, price: float) -> None:
        self.__price: float = price
    # endregion

    # region genres
    @property
    def genres(self) -> str:
        return self.__genres

    @genres.setter
    def genres(self, genres: str) -> None:
        self.__genres: str = genres
    # endregion

    def entity_to_text(self):
        # return f"title:{self.title}, isbn:{self.isbn}, printyear:{self.printyear}, pages:{self.pages}, price:{self.price}, genres:{self.genres}, {super().entity_to_text()}"
        return f"title:{self.title}, isbn:{self.isbn}, printyear:{self.printyear}, pages:{self.pages}, price:{self.price}, genres:{self.genres}"

    @staticmethod
    def text_to_entity(data: str) -> object:

        book_dict: dict = eval(data.strip())  # type: ignore

        return Book(
            guid=book_dict["guid"],
            title=book_dict["title"],
            isbn=book_dict["isbn"],
            pages=book_dict["pages"],
            printyear=book_dict["printyear"],
            price=book_dict["price"],
            genres=book_dict["genres"],
            description=book_dict["description"]
        )
        """This method should implement how to ...."""

    @override
    def __str__(self) -> str:
        # return f"title:{self.title}, isbn:{self.isbn}, printyear:{self.printyear}, pages:{self.pages}, price:{self.price}, genres:{self.genres}, {super().__str__()}"
        return f"title:{self.title}, isbn:{self.isbn}"

    @override
    def __eq__(self, __value: object) -> bool:

        if not isinstance(__value, self.__class__):
            return False

        return str(self) == str(__value)

    @override
    def __hash__(self) -> int:
        return hash(str(self))
