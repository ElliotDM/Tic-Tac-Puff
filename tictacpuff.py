import tkinter as tk
import Stack as stack

class Window(tk.Tk):
    def __init__(self) -> None:
        super().__init__()

        self.title("Tic-Tac-Puff")
        self.geometry("300x300")
        self.resizable(0,0)
        self.option_add("*Font", "Helvetica 36 bold")

        self._counter = 0
        self._fade = False
        self._stack = stack.Stack()
        self._create_board()

    def _create_board(self):
        self.btn_list = []

        self.frame1 = tk.Frame(self, bg="#FFFFFF")      
        self.frame2 = tk.Frame(self, bg="#FFFFFF")
        self.frame3 = tk.Frame(self, bg="#FFFFFF")

        self.btn0 = tk.Button(self.frame1, text="   ", borderwidth=0)
        self.btn1 = tk.Button(self.frame1, text="   ", borderwidth=0)
        self.btn2 = tk.Button(self.frame1, text="   ", borderwidth=0)
        self.btn3 = tk.Button(self.frame2, text="   ", borderwidth=0)
        self.btn4 = tk.Button(self.frame2, text="   ", borderwidth=0)
        self.btn5 = tk.Button(self.frame2, text="   ", borderwidth=0)
        self.btn6 = tk.Button(self.frame3, text="   ", borderwidth=0)
        self.btn7 = tk.Button(self.frame3, text="   ", borderwidth=0)
        self.btn8 = tk.Button(self.frame3, text="   ", borderwidth=0)

        self.btn_list.append(self.btn0)
        self.btn_list.append(self.btn1)
        self.btn_list.append(self.btn2)
        self.btn_list.append(self.btn3)
        self.btn_list.append(self.btn4)
        self.btn_list.append(self.btn5)
        self.btn_list.append(self.btn6)
        self.btn_list.append(self.btn7)
        self.btn_list.append(self.btn8)

        self.btn0.config(command=lambda: self._game_mechanics(self.btn_list[0]))
        self.btn1.config(command=lambda: self._game_mechanics(self.btn_list[1]))
        self.btn2.config(command=lambda: self._game_mechanics(self.btn_list[2]))
        self.btn3.config(command=lambda: self._game_mechanics(self.btn_list[3]))
        self.btn4.config(command=lambda: self._game_mechanics(self.btn_list[4]))
        self.btn5.config(command=lambda: self._game_mechanics(self.btn_list[5]))
        self.btn6.config(command=lambda: self._game_mechanics(self.btn_list[6]))
        self.btn7.config(command=lambda: self._game_mechanics(self.btn_list[7]))
        self.btn8.config(command=lambda: self._game_mechanics(self.btn_list[8]))

        self.frame1.pack(expand=True, fill=tk.BOTH)
        self.frame2.pack(expand=True, fill=tk.BOTH)
        self.frame3.pack(expand=True, fill=tk.BOTH)

        self.btn0.pack(side=tk.LEFT, expand=True, fill=tk.BOTH, padx=2, pady=2)
        self.btn1.pack(side=tk.LEFT, expand=True, fill=tk.BOTH, padx=2, pady=2)
        self.btn2.pack(side=tk.LEFT, expand=True, fill=tk.BOTH, padx=2, pady=2)
        self.btn3.pack(side=tk.LEFT, expand=True, fill=tk.BOTH, padx=2, pady=2)
        self.btn4.pack(side=tk.LEFT, expand=True, fill=tk.BOTH, padx=2, pady=2)
        self.btn5.pack(side=tk.LEFT, expand=True, fill=tk.BOTH, padx=2, pady=2)
        self.btn6.pack(side=tk.LEFT, expand=True, fill=tk.BOTH, padx=2, pady=2)
        self.btn7.pack(side=tk.LEFT, expand=True, fill=tk.BOTH, padx=2, pady=2)
        self.btn8.pack(side=tk.LEFT, expand=True, fill=tk.BOTH, padx=2, pady=2)

    def _game_mechanics(self, button):
        self._counter += 1

        if self._counter % 2 == 0:
            button.config(text=" O ")
            button['state'] = tk.DISABLED
        else:
            button.config(text=" X ")
            button['state'] = tk.DISABLED

        self._stack.append({button:button.cget('text')})
        print()
        self._stack.print()


if __name__ == '__main__':
    app = Window()
    app.mainloop()