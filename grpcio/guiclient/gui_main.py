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
from grpcio.grpcbase.grpc_base import GrpcStub


class GuiStub(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()
        self._Stub = None
        self._connected = False


    def createWidgets(self):
        self.cwd = tk.StringVar(self)

        self.outMessage = tk.Text(self)
        #self.out_x_Scrollbar = tk.Scrollbar(self, command=self.outMessage.xview)
        #self.out_x_Scrollbar.pack(fill=tk.X, expand=1)
        #self.out_y_Scrollbar = tk.Scrollbar(self, command=self.outMessage.yview)
        #self.out_y_Scrollbar.pack(fill=tk.Y, expand=1)
        #self.outMessage['xscrollcommand'] = self.out_x_Scrollbar.set
        #self.outMessage['yscrollcommand'] = self.out_y_Scrollbar.set
        #self.outMessage.grid(row=0, column=0)
        self.outMessage.grid()


        self.inputText = tk.Text(self)
        #self.inputText.grid(row=2, column=0)
        self.inputText.grid()
        self.inputText.bind('<Return>', func=self.execute_command)
        self.in_y_scroll = tk.Scrollbar(self, command=self.inputText.yview)
        self.inputText.configure(yscrollcommand=self.in_y_scroll.set)
        #self.inputText.tag_configure("current_line", background="gray")
        #self.inputText.tag_configure("current_line")
        self.label = tk.Label(self, text='Grpc Navigator v0.1          powered by huangdeng')
        self.label.grid()
        self.out_help_msg()
        self.load_saved_cmd()

    def load_saved_cmd(self):
        try:
            with open('input.txt', mode='r') as f:
                self.inputText.insert(tk.END, f.read())
        except FileNotFoundError:
            return

    def out_help_msg(self):
        self.outMessage.insert(tk.END, 'for help, input: help\n')
        self.outMessage.insert(tk.END, 'connect, input: conn xxx.xxx.xxx.xxx:xxxx\n')
        self.outMessage.insert(tk.END, 'send command to server, input: :youcommand\n')
        self.outMessage.insert(tk.END, 'save input and output windows, input: save\n')
        self.outMessage.insert(tk.END, '##########################################\n')
        self.outMessage.update()

    def execute_command(self, ev=None):
        #self.inputText.tag_remove("current_line", 1.0, "end")
        #self.inputText.tag_add("current_line", "current linestart", "current lineend+1c")
        input_srt = self.inputText.get(index1='insert linestart', index2='insert lineend')
        if 'help' in input_srt:
            self.out_help_msg()
        if ':' in input_srt[:2]:
            self.call_grpc_and_show(input_srt)
        if input_srt[:4] == 'conn':
            self.connect(input_srt)
        if input_srt[:4] == 'save':
            self.save2file()

    def connect(self, cmd):
        split_cmd = cmd.split()
        if len(split_cmd) == 2:
            self._Stub = GrpcStub(split_cmd[1])
            self._connected = True

    def call_grpc_and_show(self, cmd):
        if not self._connected:
            self.out_help_msg()
            return
        rsp_str, rsp = self._Stub.run(cmd)
        self.outMessage.insert(tk.END, cmd + '\n')
        for line in rsp_str:
            self.outMessage.insert(tk.END, line + '\n')
        self.outMessage.update()

    def save2file(self):
        with open('log.txt', mode='w+') as f:
            f.write(self.outMessage.get(index1='1.0', index2='end'))
        with open('input.txt', 'w') as f:
            f.write(self.inputText.get(index1='1.0', index2='end'))



if __name__ == '__main__':
    app = GuiStub()
    app.master.title('andi command')
    app.mainloop()
