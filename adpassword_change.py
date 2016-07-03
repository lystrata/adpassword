#! /usr/bin/env python
#
# GUI module generated by PAGE version 4.7
# In conjunction with Tcl version 8.6
#    Jun 22, 2016 02:33:28 PM
import sys

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = 0
except ImportError:
    import tkinter.ttk as ttk
    py3 = 1

import adpassword_change_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    top = AD_Password (root)
    adpassword_change_support.init(root, top)
    root.mainloop()

w = None
def create_AD_Password(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = AD_Password (w)
    adpassword_change_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_AD_Password():
    global w
    w.destroy()
    w = None


class AD_Password:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("480x240+323+167")
        top.title("AD Password")



        self.lbl_old_pwd = ttk.Label(top)
        self.lbl_old_pwd.place(relx=0.04, rely=0.08, height=17, width=82)
        self.lbl_old_pwd.configure(background=_bgcolor)
        self.lbl_old_pwd.configure(foreground="#000000")
        self.lbl_old_pwd.configure(relief=FLAT)
        self.lbl_old_pwd.configure(text='''Old Password''')

        self.lbl_new_pwd = ttk.Label(top)
        self.lbl_new_pwd.place(relx=0.04, rely=0.21, height=17, width=88)
        self.lbl_new_pwd.configure(background=_bgcolor)
        self.lbl_new_pwd.configure(foreground="#000000")
        self.lbl_new_pwd.configure(relief=FLAT)
        self.lbl_new_pwd.configure(text='''New Password''')

        self.TEntry1 = ttk.Entry(top)
        self.TEntry1.place(relx=0.35, rely=0.08, relheight=0.08, relwidth=0.34)
        self.TEntry1.configure(takefocus="")
        self.TEntry1.configure(cursor="xterm")

        self.lbl_rep_new_pwd = ttk.Label(top)
        self.lbl_rep_new_pwd.place(relx=0.04, rely=0.33, height=17, width=134)
        self.lbl_rep_new_pwd.configure(background=_bgcolor)
        self.lbl_rep_new_pwd.configure(foreground="#000000")
        self.lbl_rep_new_pwd.configure(relief=FLAT)
        self.lbl_rep_new_pwd.configure(text='''Repeat New Password''')

        self.TEntry2 = ttk.Entry(top)
        self.TEntry2.place(relx=0.35, rely=0.21, relheight=0.08, relwidth=0.34)
        self.TEntry2.configure(takefocus="")
        self.TEntry2.configure(cursor="xterm")

        self.TEntry3 = ttk.Entry(top)
        self.TEntry3.place(relx=0.35, rely=0.33, relheight=0.08, relwidth=0.34)
        self.TEntry3.configure(takefocus="")
        self.TEntry3.configure(cursor="xterm")

        self.bt_ok = ttk.Button(top)
        self.bt_ok.place(relx=0.29, rely=0.79, height=26, width=83)
        self.bt_ok.configure(command=adpassword_change_support.bt_ok_clicked)
        self.bt_ok.configure(takefocus="")
        self.bt_ok.configure(text='''Ok''')

        self.TButton2 = ttk.Button(top)
        self.TButton2.place(relx=0.52, rely=0.79, height=26, width=83)
        self.TButton2.configure(command=adpassword_change_support.bt_cancel_clicked)
        self.TButton2.configure(takefocus="")
        self.TButton2.configure(text='''Cancel''')

        self.TLabel4 = ttk.Label(top)
        self.TLabel4.place(relx=0.46, rely=0.54, height=17, width=37)
        self.TLabel4.configure(background=_bgcolor)
        self.TLabel4.configure(foreground="#f80000")
        self.TLabel4.configure(relief=FLAT)
        self.TLabel4.configure(text='''Tlabel''')






if __name__ == '__main__':
    vp_start_gui()


