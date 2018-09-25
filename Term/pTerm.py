from tkinter import *

PROGRAM_NAME = ' Wind Turbine Remote Console '




class WindConsole:
    def __init__(self, root):
        self.root = root
        root.title(PROGRAM_NAME)
        self.init_gui()

    def print_console_send(self):
        sendtext = self.send_text.get("1.0", END)
        self.console_text_widget.delete("1.0", END)
        self.console_text_widget.insert(INSERT, sendtext)

    def create_console_window(self):
        console_frame = Frame(self.root)
        console_frame.grid(row=0, column=0, columnspan=10, padx=5, pady=5)

        Label(console_frame, text='Wind Console').grid(row=0, column=0, sticky=S+W)
        self.console_text_widget = Text(console_frame, wrap=CHAR, height=5, width=80)
        self.console_text_widget.grid(row=1, column=0, columnspan=10)
        self.console_text_widget.insert(INSERT, "Just a test string")

    def create_send_window(self):
        send_frame = Frame(self.root)
        send_frame.grid(row=2, column=0, columnspan=10, padx=5, pady=5)

        self.send_text = Text(send_frame, wrap=CHAR, height=1, width=72)
        self.send_text.grid(row=2, column=0, columnspan=9)

        self.send_button = Button(send_frame, text="Send", command=self.print_console_send)
        self.send_button.grid(row=2, column=9, sticky=N+W, padx=2, pady=2)

    def create_numpad_window(self):
        numpad_frame = Frame(self.root)
        numpad_frame.grid(row=3, column=0, columnspan=3, padx=5, pady=5)

        btn_list = ['7', '8', '9', '4', '5', '6', '1', '2', '3', '.', '0', 'Esc']

        # r, c used for row, column grid values
        r = 3
        c = 0
        n = 0

        list(range(0, 12))
        btn = []
        for label in btn_list:
            # partial takes care of function and argument
            cmd = lambda x = label: self.numpad_click(x)
            # create the button
            cur = Button(numpad_frame, text=label, width=3, height=3, command=cmd)
            btn.append(cur)
            # position the button
            btn[-1].grid(row=r, column=c, padx=4, pady=4)
            # increment button index
            n += 1
            # update row/column position
            c += 1
            if c == 3:
                c = 0
                r += 1

    def numpad_click(self, label):
        print(label)

    def init_gui(self):
        self.create_console_window()
        self.create_send_window()
        self.create_numpad_window()

if __name__ == '__main__':
    root = Tk()
    WindConsole(root)
    root.mainloop()