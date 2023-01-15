import tkinter as tk

from tool.controller.ControllerInterface import ControllerInterface
from tool.view.ViewInterface import ViewInterface


class BasicView(ViewInterface):
    def __init__(self, controller: ControllerInterface,
                 title: str = "Vocabulary Trainer - a student project by Benjamin",
                 width: int = 600,
                 height: int = 400):
        self.__title = title
        self.__width = width
        self.__height = height
        self.__root = None
        self.__controller = controller
        self.__vocabulary_label = None
        self.__answer_block = None
        self.__first_button = None
        self.__previous_button = None
        self.__reversal_button = None
        self.__next_button = None
        self.__last_button = None
        self.__index_label = None
        self.initialize()

    def run(self) -> None:
        self.__root.mainloop()

    def initialize(self) -> None:
        self.__controller.register_observer(self)
        self.__root = tk.Tk()
        self.__root.title(self.__title)
        self.__root.geometry(f"{self.__width}x{self.__height}")
        self.create_index_label()
        self.create_vocabulary_label()
        self.create_user_input()
        self.create_menu()

    def create_vocabulary_label(self) -> None:
        self.__vocabulary_label = tk.Label(self.__root, text=self.__controller.get_card())
        self.__vocabulary_label.config(font=("Courier", int((self.__width + self.__height) ** 0.55)))
        self.__vocabulary_label.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    def create_index_label(self) -> None:
        self.__index_label = tk.Label(self.__root,
                                      text=f"{self.__controller.get_index() + 1} / {self.__controller.get_size()}")
        self.__index_label.pack(side=tk.TOP, fill=tk.BOTH, expand=False)

    def create_user_input(self) -> None:
        self.__answer_block = tk.Entry(self.__root)
        self.__answer_block.config(font=("Courier", int((self.__width + self.__height) ** 0.5)),justify='center')
        self.__answer_block.bind("<Return>", self.check_answer)  # bind the enter key to the check_answer method
        self.__answer_block.pack(side=tk.TOP, fill=tk.BOTH, expand=False)

    def create_menu(self) -> None:
        self.__first_button = tk.Button(self.__root, text="First", command=self.__controller.first)
        self.__first_button.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.__previous_button = tk.Button(self.__root, text="Previous", command=self.__controller.previous)
        self.__previous_button.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.__reversal_button = tk.Button(self.__root, text="Reversal", command=self.__controller.reversal)
        self.__reversal_button.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.__next_button = tk.Button(self.__root, text="Next", command=self.__controller.next)
        self.__next_button.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.__last_button = tk.Button(self.__root, text="Last", command=self.__controller.last)
        self.__last_button.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    def update(self) -> None:
        self.__answer_block.delete(0, tk.END)
        self.__answer_block.config({"background": "White"})
        self.__vocabulary_label.config(text=self.__controller.get_card())
        self.__index_label.config(text=f"{self.__controller.get_index() + 1} / {self.__controller.get_size()}")

    def check_answer(self, *args) -> None:
        user_answer = self.__answer_block.get()
        if self.__controller.check_answer(user_answer):
            self.__answer_block.config({"background": "Green"})
        else:
            self.__answer_block.config({"background": "Red"})
