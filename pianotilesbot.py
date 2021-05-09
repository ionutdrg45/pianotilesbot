from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con
import tkinter as tk
import tkinter.font as tkFont

# tile 1 pos(313, 525)
# tile 2 pos(406, 525)
# tile 3 pos(466, 525)
# tile 4 pos(550, 532)

bot_running = False

def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

def run_bot(button):
    global bot_running
    while keyboard.is_pressed('q') == False and bot_running == True:
        if pyautogui.pixel(313, 525)[0] == 0: #[0] - R, [1] - G, [2] - B
            click(313, 525)
        if pyautogui.pixel(406, 525)[0] == 0: #[0] - R, [1] - G, [2] - B
            click(406, 525)
        if pyautogui.pixel(466, 525)[0] == 0: #[0] - R, [1] - G, [2] - B
            click(466, 525)
        if pyautogui.pixel(550, 525)[0] == 0: #[0] - R, [1] - G, [2] - B
            click(550, 525)
    button["bg"] = "#90ee90"
    button["text"] = "Start"
    button["fg"] = "#000"
    bot_running = False

class App:
    def __init__(self, root):
        #setting title
        root.title("Piano Tiles BOT")
        #setting window size
        width=295
        height=121
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_764=tk.Label(root)
        ft = tkFont.Font(family='Times',size=13)
        GLabel_764["font"] = ft
        GLabel_764["fg"] = "#000000"
        GLabel_764["justify"] = "center"
        GLabel_764["text"] = "Piano Tiles BOT"
        GLabel_764["relief"] = "ridge"
        GLabel_764["border"] = 0
        GLabel_764.place(x=0,y=0,width=141,height=37)

        GLabel_402=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_402["font"] = ft
        GLabel_402["fg"] = "#333333"
        GLabel_402["justify"] = "center"
        GLabel_402["text"] = "press \"q\" to stop"
        GLabel_402.place(x=70,y=80,width=138,height=30)

        GButton_464=tk.Button(root)
        GButton_464["bg"] = "#90ee90"
        ft = tkFont.Font(family='Times',size=13)
        GButton_464["font"] = ft
        GButton_464["fg"] = "#000"
        GButton_464["justify"] = "center"
        GButton_464["text"] = "Start"
        GButton_464.place(x=70,y=50,width=140,height=30)
        GButton_464["command"] = lambda arg = GButton_464:self.GButton_464_command(arg)

    def GButton_464_command(self, button):
        global bot_running
        if bot_running == False:
            button["bg"] = "#105915"
            button["text"] = "Running ..."
            button["fg"] = "#fff"
            bot_running = True
            root.update()
            run_bot(button)
        
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
