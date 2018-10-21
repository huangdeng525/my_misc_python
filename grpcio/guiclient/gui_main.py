#!/usr/bin/python3
# gui_main.py
#
#  grpc gui maint
#
#  Copyright (C) 2018-2018 huangdeng @ chengdu
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License version 3 as
#  published by the Free Software Foundation.
#  2018.10.21 init

import tkinter as tk


class GuiStub(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        self.outMessage = tk.Message(self)
        self.outMessage.grid()
        self.inputText = tk.Text(self)
        self.inputText.grid()


if __name__ == '__main__':
    app = GuiStub()
    app.master.title('andi command')
    app.mainloop()