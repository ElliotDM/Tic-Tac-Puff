import tkinter as tk
import Stack as stack
from tkinter import font

class Window(tk.Tk):
    def __init__(self) -> None:
        super().__init__()

        self.title("Tic-Tac-Puff")
        self.resizable(0,0)

        self._font = font.Font(family="Ubuntu", size="24")

        self._counter = 0
        self._fade = False
        self._stack = stack.Stack()

        self._buttons = {}

        self._create_board()
        self._create_grid()

    def _create_board(self):
        self.master_frame = tk.Frame(self)
        
        self.turn = tk.Label(self.master_frame,
                              text="X's turn",
                              font=self._font)
        
        self.master_frame.pack(fill=tk.X)
        self.turn.pack()
        
    def _create_grid(self):
        self.grid_frame = tk.Frame(self)
        self.grid_frame.pack()

        for row in range(3):
            self.rowconfigure(row, weight=1, minsize=50)
            self.columnconfigure(row, weight=1, minsize=75)

            for col in range(3):
                btn = tk.Button(self.grid_frame,
                                text="",
                                font=self._font,
                                fg="black",
                                width=4,
                                height=2,)
                
                self._buttons[btn] = (row, col)
                btn.bind("<ButtonPress-1>", self._event_listener)

                btn.grid(row=row,
                         column=col,
                         padx=5,
                         pady=5,
                         sticky="nsew")


    # TODO: fix this method            
    def _event_listener(self, event):
        button = event.widget

        self._counter += 1

        if self._counter % 2 == 0:
            button.config(text=" O ")
            button.config(fg="#0052cc")
            button['state'] = tk.DISABLED
        else:
            button.config(text=" X ")
            button.config(fg="#e60000")
            button['state'] = tk.DISABLED


def main():
    app = Window()
    app.mainloop()


if __name__ == '__main__':
    main()
