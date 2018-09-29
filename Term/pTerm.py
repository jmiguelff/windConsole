from tkinter import *
import socket
import threading

PROGRAM_NAME = ' Wind Turbine Remote Console '




class WindConsole:
    def __init__(self, root):
        self.root = root
        root.title(PROGRAM_NAME)
        self.init_gui()

    def initialize_socket(self, address):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.settimeout(5)

        try:
            self.client_socket.connect(address)
        except socket.error as exc:
            self.connect_text.delete("1.0", END)
            self.connect_text.insert(INSERT, "Caught exception socket.error : %s" % exc)

        self.connect_text.delete("1.0", END)
        self.connect_text.insert(INSERT, "Connected to " + address[0] + ":" + str(address[1]))

    def tcp_connect(self):
        connecttext = self.connect_text.get("1.0", END)
        connectlist = connecttext.split(":", 1)
        ip = connectlist[0]
        port = connectlist[1]

        remoteAddress = (ip, int(port))

        # self.console_text_widget.delete("1.0", END)
        # self.console_text_widget.insert(INSERT, "IP: " + ip + "\n")
        # self.console_text_widget.insert(INSERT, "PORT: " + port)

        # Initialize scoket and connect to remote IP
        self.initialize_socket(remoteAddress)

    def create_console_window(self):
        console_frame = Frame(self.root)
        console_frame.grid(row=0, column=0, columnspan=10, padx=5, pady=5)

        Label(console_frame, text='Wind Console').grid(row=0, column=0, sticky=S+W)
        self.console_text_widget = Text(console_frame, wrap=CHAR, height=6, width=80)
        self.console_text_widget.grid(row=1, column=0, columnspan=10)
        self.console_text_widget.insert(INSERT, "Just a test string")

    def ignore_enter(self, event):
        return 'break'

    def create_connect_window(self):
        connect_frame = Frame(self.root)
        connect_frame.grid(row=2, column=0, columnspan=10, padx=5, pady=5)

        self.connect_text = Text(connect_frame, wrap=CHAR, height=1, width=68)
        self.connect_text.bind('<Return>', self.ignore_enter)
        self.connect_text.grid(row=2, column=0, columnspan=9)

        self.connect_button = Button(connect_frame, text="Connect", command=self.tcp_connect)
        self.connect_button.grid(row=2, column=9, sticky=N+W, padx=2, pady=2)



    def create_numpad_window(self):
        numpad_frame = Frame(self.root)
        numpad_frame.configure(background='black')
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

    def create_arrowpad_window(self):
        arrowpad_frame = Frame(self.root)
        arrowpad_frame.configure(background='black')
        arrowpad_frame.grid(row=3, column=4, columnspan=4, padx=5, pady=5, sticky=S)

        self.up_button = Button(arrowpad_frame, text='up', width=3, height=2)
        self.up_button.grid(row=3, column=5, padx=4, pady=4)

        self.down_button = Button(arrowpad_frame, text='down', width=3, height=2)
        self.down_button.grid(row=5, column=5, padx=4, pady=4)

        self.right_button = Button(arrowpad_frame, text='right', width=3, height=2)
        self.right_button.grid(row=4, column=6, padx=4, pady=4)

        self.left_button = Button(arrowpad_frame, text='left', width=3, height=2)
        self.left_button.grid(row=4, column=4, padx=4, pady=4)

        self.enter_button = Button(arrowpad_frame, text="enter", width=3, height=2)
        self.enter_button.grid(row=4, column=5, padx=4, pady=4)

        self.start_button = Button(arrowpad_frame, text='start', width=3, height=2)
        self.start_button.grid(row=6, column=4, padx=4, pady=4)

        self.stop_button = Button(arrowpad_frame, text='stop', width=3, height=2)
        self.stop_button.grid(row=6, column=5, padx=4, pady=4)

        self.help_button = Button(arrowpad_frame, text="help", width=3, height=2)
        self.help_button.grid(row=6, column=6, padx=4, pady=4)



    def init_gui(self):
        self.create_console_window()
        self.create_connect_window()
        self.create_numpad_window()
        self.create_arrowpad_window()

if __name__ == '__main__':
    root = Tk()
    WindConsole(root)
    root.mainloop()