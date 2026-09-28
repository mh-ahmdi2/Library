import tkinter as tk
from tkinter.messagebox import showerror, showinfo
from bl.basic.book_bl import BookBL
from common.basic.book import Book
from common.utility.datatypes import FormAction, FormResult
from typing import Any


class BookDataEntryForm(tk.Toplevel):

    def __init__(self, book_bl: BookBL, form_mode: FormAction, instance: Book | None = None) -> None:
        super().__init__()
        self.__initializecomponent()
        self.__book_bl = book_bl
        self.__form_action: FormAction = form_mode

    def __initializecomponent(self):

        # region config form
        self.title("Book data entry form")
        self.geometry("600x600")
        self.configure(bg="white")
        # self.resizable(width=False, height=False)
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
            text="Book info",
            master=self,
            bg="white"
        )
        self.__body.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        self.__body.propagate(False)

        self.__info_frame = tk.Frame(
            master=self.__body, height=150, bg="white")
        self.__info_frame.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)
        self.__info_frame.propagate(False)

        self.__right_frame = tk.Frame(master=self.__info_frame,  bg="white")
        self.__right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        self.__right_frame.propagate(False)

        self.__left_frame = tk.Frame(master=self.__info_frame,  bg="white")
        self.__left_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        self.__left_frame.propagate(False)

        self.__desc_frame = tk.Frame(
            master=self.__body, height=150, bg="yellow")
        self.__desc_frame.pack(fill=tk.BOTH, expand=True,
                               padx=10, pady=(0, 10))
        self.__desc_frame.propagate(False)

        self.__book_title_frame = tk.Frame(
            master=self.__left_frame, height=50, bg="white")
        self.__book_title_frame.pack(side=tk.TOP, fill=tk.X)
        self.__book_title_frame.propagate(False)

        self.__book_pubyear_frame = tk.Frame(
            master=self.__left_frame, height=50, bg="white")
        self.__book_pubyear_frame.pack(side=tk.TOP, fill=tk.X)
        self.__book_pubyear_frame.propagate(False)

        self.__book_price_frame = tk.Frame(
            master=self.__left_frame, height=50, bg="white")
        self.__book_price_frame.pack(side=tk.TOP, fill=tk.X)
        self.__book_price_frame.propagate(False)

        self.__book_isbn_frame = tk.Frame(
            master=self.__right_frame, height=50, bg="white")
        self.__book_isbn_frame.pack(side=tk.TOP, fill=tk.X)
        self.__book_isbn_frame.propagate(False)

        self.__book_pages_frame = tk.Frame(
            master=self.__right_frame, height=50, bg="white")
        self.__book_pages_frame.pack(side=tk.TOP, fill=tk.X)
        self.__book_pages_frame.propagate(False)

        self.__book_genres_frame = tk.Frame(
            master=self.__right_frame, height=50, bg="white")
        self.__book_genres_frame.pack(side=tk.TOP, fill=tk.X)
        self.__book_genres_frame.propagate(False)

        # endregion

        # region header section
        self.__formtitle = tk.Label(
            master=self.__header,
            text="Book data entry",
            font=("tahoma", 11, "bold"),
            fg="black",
            bg="lightgray"
        )
        self.__formtitle.pack(side=tk.LEFT, padx=(10, 0))
        # endregion

        # region footer section
        self.__save_image = tk.PhotoImage(file=r"ui/resources/opts_16.png")
        self.__save_btn = tk.Button(
            master=self.__footer,
            text="Save",
            font=("tahoma", 10, "bold"),
            fg="white",
            bg="gray",
            padx=10,
            pady=10,
            image=self.__save_image,
            compound=tk.LEFT,
            command=self.__save_btn_onclick
        )
        self.__save_btn.pack(side=tk.LEFT, padx=(10, 0))

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

        # region title

        self.__title_label = tk.Label(
            master=self.__book_title_frame,
            text="Title : ",
            fg="black",
            bg="white",
            font=("tahoma", 10, "bold"),
            width=7,
            anchor=tk.W
        )
        self.__title_label.pack(side=tk.LEFT)

        self.__title_val = tk.StringVar()

        self.__title_text_box = tk.Entry(
            textvariable=self.__title_val,
            master=self.__book_title_frame,
            fg="black",
            bg="#f0f3f4",
            font=("tahoma", 11, "normal"),
            bd=1
        )
        self.__title_text_box.pack(
            fill=tk.BOTH, expand=True, padx=(0, 10), pady=5)

        # endregion

        # region publich year

        self.__printyear_label = tk.Label(
            master=self.__book_pubyear_frame,
            text="Year : ",
            fg="black",
            bg="white",
            font=("tahoma", 10, "bold"),
            width=7,
            anchor=tk.W
        )
        self.__printyear_label.pack(side=tk.LEFT)

        self.__print_year_val = tk.StringVar()

        self.__printyear_text_box = tk.Entry(
            textvariable=self.__print_year_val,
            master=self.__book_pubyear_frame,
            fg="black",
            bg="#f0f3f4",
            font=("tahoma", 11, "normal"),
            bd=1
        )
        self.__printyear_text_box.pack(
            fill=tk.BOTH, expand=True, padx=(0, 10), pady=5)

        # endregion

        # region price
        self.__price_label = tk.Label(
            master=self.__book_price_frame,
            text="Price : ",
            fg="black",
            bg="white",
            font=("tahoma", 10, "bold"),
            width=7,
            anchor=tk.W
        )
        self.__price_label.pack(side=tk.LEFT)

        self.__price_val = tk.StringVar()

        self.__price_text_box = tk.Entry(
            textvariable=self.__price_val,
            master=self.__book_price_frame,
            fg="black",
            bg="#f0f3f4",
            font=("tahoma", 11, "normal")
        )
        self.__price_text_box.pack(
            fill=tk.BOTH, expand=True, padx=(0, 10), pady=5)

        # endregion

        # region ISBN
        self.__isbn_label = tk.Label(
            master=self.__book_isbn_frame,
            text="ISBN : ",
            fg="black",
            bg="white",
            font=("tahoma", 10, "bold"),
            width=7,
            anchor=tk.W
        )
        self.__isbn_label.pack(side=tk.LEFT)

        self.__isbn_val = tk.StringVar()

        self.__isbn_text_box = tk.Entry(
            textvariable=self.__isbn_val,
            master=self.__book_isbn_frame,
            fg="black",
            bg="#f0f3f4",
            font=("tahoma", 11, "normal")
        )
        self.__isbn_text_box.pack(
            fill=tk.BOTH, expand=True, padx=(0, 10), pady=5)

        # endregion

        # region pages
        self.__pages_label = tk.Label(
            master=self.__book_pages_frame,
            text="Pages : ",
            fg="black",
            bg="white",
            font=("tahoma", 10, "bold"),
            width=7,
            anchor=tk.W
        )
        self.__pages_label.pack(side=tk.LEFT)

        self.__pages_val = tk.StringVar()

        self.__pages_text_box = tk.Entry(
            textvariable=self.__pages_val,
            master=self.__book_pages_frame,
            fg="black",
            bg="#f0f3f4",
            font=("tahoma", 11, "normal")
        )
        self.__pages_text_box.pack(
            fill=tk.BOTH, expand=True, padx=(0, 10), pady=5)

        # endregion

        # region description

        self.__decription_label = tk.Label(
            master=self.__desc_frame,
            text="Description : ",
            fg="black",
            bg="white",
            font=("tahoma", 10, "bold"),
            anchor=tk.W
        )
        self.__decription_label.pack(side=tk.TOP, fill=tk.X)

        self.__description_text_box = tk.Text(
            master=self.__desc_frame,
            fg="black",
            bg="#f0f3f4",
            font=("tahoma", 11, "normal"),

        )
        self.__description_text_box.pack(fill=tk.BOTH, expand=True)

        # endregion

        # region genres
        self.__genres_label = tk.Label(
            master=self.__book_genres_frame,
            text="Genres : ",
            fg="black",
            bg="white",
            font=("tahoma", 10, "bold"),
            width=7,
            anchor=tk.W
        )
        self.__genres_label.pack(side=tk.LEFT)

        self.__comedy_genres_val = tk.IntVar()
        self.__roman_genres_val = tk.IntVar()

        self.__comedy_genres = tk.Checkbutton(
            master=self.__book_genres_frame, variable=self.__comedy_genres_val, bg="white", text="Comedy", onvalue=1, offvalue=0, height=2, width=10)
        self.__roman_genres = tk.Checkbutton(
            master=self.__book_genres_frame, variable=self.__roman_genres_val, bg="white", text="Romantic", onvalue=1, offvalue=0, height=2, width=10)

        self.__comedy_genres.pack(fill=tk.BOTH, expand=True, side=tk.LEFT)
        self.__roman_genres.pack(fill=tk.BOTH, expand=True, side=tk.LEFT)

        # endregion

    def __validateform(self) -> bool:

        title: str = self.__title_val.get()
        isbn: str = self.__isbn_val.get()
        pages: str = self.__pages_val.get()
        printyear: str = self.__print_year_val.get()
        price: str = self.__price_val.get()

        err_list: list[str] = []

        if not title:
            err_list.append("Name is empty!")

        if not isbn:
            err_list.append("ISBN is empty!")

        if not pages:
            err_list.append("Pages is empty!")
        else:
            try:
                val = int(pages)
            except:
                err_list.append("Page`s Type is not int!")

        if not printyear:
            err_list.append("printyear is empty!")
        else:
            try:
                val = int(printyear)
            except:
                err_list.append("printyear`s Type is not int!")

        if not price:
            err_list.append("Price is empty!")
        else:
            try:
                val = float(price)
            except:
                err_list.append("Price`s Type is not int!")

        if err_list:
            return False, err_list

        return True, None

    def __back_btn_onclick(self):
        self.__form_result = FormResult.BACK
        self.destroy()

    def __save_btn_onclick(self):

        check_validate, err_list = self.__validateform()

        if not check_validate:
            showerror("Error!", "\n".join(err_list))
            return

        # region form data
        title: str = self.__title_val.get()
        isbn: str = self.__isbn_val.get()
        pages: int = int(self.__pages_val.get())
        printyear: int = int(self.__print_year_val.get())
        price: float = float(self.__price_val.get())
        description: str = self.__description_text_box.get("1.0", "end-1c")

        genres_list: list[Any] = []

        if self.__roman_genres_val.get() == 1:
            genres_list.append("roman")

        if self.__comedy_genres_val.get() == 1:
            genres_list.append("comady")

        genres = " , ".join(genres_list)
        # endregion

        book_inst = Book(
            title=title,
            isbn=isbn,
            pages=pages,
            printyear=printyear,
            price=price,
            genres=genres,
            description=description
        )

        match self.__form_action:

            case FormAction.CREATE:
                result: MethodResult = self.__book_bl.create(book_inst)

            case FormAction.UPDATE:
                pass

        if not result.success:
            showerror("ERROR", result.error_message)
            return

        showinfo("SUCCESS", result.return_data)
        self.__form_result = FormResult.SAVE
        self.destroy()

    @property
    def form_result(self):
        return self.__form_result
