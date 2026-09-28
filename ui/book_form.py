import tkinter as tk
from tkinter.ttk import Treeview, Scrollbar
from tkinter.messagebox import showerror, showinfo, askyesno
from bl.basic.book_bl import BookBL
from common.basic.book import Book
from ui.book_dataentry_form import BookDataEntryForm
from common.utility.datatypes import FormAction, FormResult


class BookForm(tk.Tk):

    def __init__(self) -> None:
        super().__init__()
        self.bind_class('Tk', '<Map>', self.__on_form_shown)
        self.__initializecomponent()
        self.__book_bl = BookBL()

    def __on_form_shown(self, event):  # type: ignore
        self.__refresh_books_data()

    def __refresh_books_data(self):

        for row_book in self.__book_grid.get_children():
            self.__book_grid.delete(row_book)

        book: Book

        for book in self.__book_bl.get_list():
            self.__book_grid.insert("", "end", values=(
                book.guid, book.title, book.isbn, book.printyear, book.pages, book.price, book.genres, book.description))

    def __initializecomponent(self):

        # region config form
        self.title("Book form")
        self.geometry("600x600")
        self.configure(bg="white")
        # endregion

        # region create frame
        self.__header = tk.Frame(
            master=self,
            height=80,
            bg="lightgray",
            highlightbackground="gray",
            highlightthickness=1
        )
        self.__header.pack(side=tk.TOP, fill=tk.X)
        self.__header.propagate(False)

        self.__footer = tk.Frame(
            master=self,
            height=80,
            bg="lightgray",
            highlightbackground="gray",
            highlightthickness=1
        )
        self.__footer.pack(side=tk.BOTTOM, fill=tk.X)
        self.__footer.propagate(False)

        self.__body = tk.LabelFrame(
            text="Book list",
            master=self,
            bg="white"
        )
        self.__body.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        self.__body.propagate(False)

        # endregion

        # region header section
        self.__formtitle = tk.Label(
            master=self.__header,
            text="Book Form",
            font=("tahoma", 11, "bold"),
            fg="black",
            bg="lightgray"
        )
        self.__formtitle.pack(side=tk.LEFT, padx=(10, 0))
        # endregion

        # region footer section
        self.__add_image = tk.PhotoImage(file=r"ui/resources/add_16.png")
        self.__add_btn = tk.Button(
            master=self.__footer,
            text="Add",
            font=("tahoma", 10, "bold"),
            fg="white",
            bg="gray",
            padx=10,
            pady=10,
            image=self.__add_image,
            compound=tk.LEFT,
            command=self.__add_btn_onclick
        )
        self.__add_btn.pack(side=tk.LEFT, padx=(10, 0))

        self.__edit_image = tk.PhotoImage(file=r"ui/resources/edit_16.png")
        self.__edit_btn = tk.Button(
            master=self.__footer,
            text="Edit",
            font=("tahoma", 10, "bold"),
            fg="white",
            bg="gray",
            padx=10,
            pady=10,
            image=self.__edit_image,
            compound=tk.LEFT,
            command=self.__edit_btn_onclick
        )
        self.__edit_btn.pack(side=tk.LEFT, padx=(10, 0))

        self.__remove_image = tk.PhotoImage(file=r"ui/resources/trash_16.png")
        self.__remove_btn = tk.Button(
            master=self.__footer,
            text="Remove",
            font=("tahoma", 10, "bold"),
            fg="white",
            bg="gray",
            padx=10,
            pady=10,
            image=self.__remove_image,
            compound=tk.LEFT,
            command=self.__remove_btn_onclick
        )
        self.__remove_btn.pack(side=tk.LEFT, padx=(10, 0))

        self.__back_image = tk.PhotoImage(file=r"ui\resources\undo_16.png")
        self.__back_btn = tk.Button(
            master=self.__footer,
            text="Back",
            font=("tahoma", 10, "bold"),
            fg="white",
            bg="gray",
            padx=10,
            pady=10,
            image=self.__back_image,
            compound=tk.LEFT,
            command=self.__back_btn_onclick
        )
        self.__back_btn.pack(side=tk.RIGHT, padx=(0, 10))
        # endregion

        # region scrollbar
        self.__verscrlbar = Scrollbar(self.__body, orient="vertical")
        self.__verscrlbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.__horscrlbar = Scrollbar(self.__body, orient="horizontal")
        self.__horscrlbar.pack(side=tk.BOTTOM, fill=tk.X)
        # endregion

        # region treeview

        self.__book_grid = Treeview(
            master=self.__body,
            columns=("id", "title", "isbn", "year", "pages",
                     "price", "genres", "description"),
            displaycolumns=("title", "isbn", "year", "pages",
                            "price", "genres", "description"),
            show="headings",
            selectmode="extended"
        )

        col_width = self.__book_grid.winfo_width()

        self.__book_grid.column(
            column="id", anchor="center", width=col_width)
        self.__book_grid.column(
            column="title", anchor="center", width=col_width)
        self.__book_grid.column(
            column="isbn", anchor="center", width=col_width)
        self.__book_grid.column(
            column="year", anchor="center", width=col_width)
        self.__book_grid.column(
            column="pages", anchor="center", width=col_width)
        self.__book_grid.column(
            column="price", anchor="center", width=col_width)
        self.__book_grid.column(
            column="genres", anchor="center", width=col_width)
        self.__book_grid.column(column="description",
                                anchor="center", width=col_width)

        self.__book_grid.heading(column="id", anchor="center", text="id")
        self.__book_grid.heading(column="title", anchor="center", text="Title")
        self.__book_grid.heading(column="isbn", anchor="center", text="ISBN")
        self.__book_grid.heading(
            column="year", anchor="center", text="Publish year")
        self.__book_grid.heading(column="pages", anchor="center", text="Pages")
        self.__book_grid.heading(column="price", anchor="center", text="Price")
        self.__book_grid.heading(
            column="genres", anchor="center", text="Genres")
        self.__book_grid.heading(column="description",
                                 anchor="center", text="Desc")

        self.__book_grid.pack(fill="both", expand=True)
        # endregion

        # region scroolbar - treeview config
        self.__book_grid.configure(yscrollcommand=self.__verscrlbar.set)
        self.__verscrlbar["command"] = self.__book_grid.yview

        self.__book_grid.configure(xscrollcommand=self.__horscrlbar.set)
        self.__horscrlbar["command"] = self.__book_grid.xview

        # endregion

    def __back_btn_onclick(self):
        pass

    def __add_btn_onclick(self):

        self.withdraw()

        frm = BookDataEntryForm(
            book_bl=self.__book_bl, form_mode=FormAction.CREATE)

        self.wait_window(frm)

        if frm.form_result == FormResult.SAVE:
            self.__refresh_books_data()

        self.deiconify()

    def __edit_btn_onclick(self):
        selected_row: list[Book] = self.__get_selected_rows()

        if not selected_row:
            showerror("Error", "Selected Error")
            return

        if len(selected_row) != 1:
            showerror("Error", message="Selected row Error")
            return

        selected_book: Book = selected_row[0]

        self.withdraw()

        frm = BookDataEntryForm(
            book_bl=self.__book_bl, form_mode=FormAction.UPDATE, instance=selected_book)

        self.wait_window(frm)

        if frm.form_result == FormResult.SAVE:
            self.__refresh_books_data()

        self.deiconify()

    def __remove_btn_onclick(self):
        selected_book: list[Book] = self.__get_selected_rows()

        if not selected_book:
            showerror("Error", "Selected Error")
            return

        for book in selected_book:
            # if askyesno("Message", f"{book}\nAre you sure delete this Book ? "):
            if askyesno("Message", f"Book title : {book.title}\nAre you sure delete this Book ? "):
                result = self.__book_bl.delete(book=book)

                if not result.success:
                    showerror("ERROR", result.error_message)
                else:
                    self.__refresh_books_data()
                    # showinfo("SUCCESS", result.return_data)

        # self.__refresh_books_data()

    def __get_selected_rows(self) -> list[Book]:
        selcted_rows: tuple[str, ...] = self.__book_grid.selection()

        select_book: list[Book] = []

        for row_id in selcted_rows:
            row_data = self.__book_grid.item(row_id, "values")

            selected_book.append(
                Book(
                    guid=row_data[0],
                    title=row_data[1],
                    isbn=row_data[2],
                    pages=row_data[4],
                    printyear=row_data[3],
                    price=row_data[5],
                    genres=row_data[6],
                    description=row_data[7]
                )
            )
        return selected_book
