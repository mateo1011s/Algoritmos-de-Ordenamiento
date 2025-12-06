import tkinter as tk
from gui.welcome import WelcomeScreen

class AppController:
    def __init__(self, master):
        self.master = master
        self.master.withdraw() 
        self.show_welcome_screen()

    def show_welcome_screen(self):

        self.welcome_screen = WelcomeScreen(self.master, next_callback=self.show_input_screen)
        
    def show_input_screen(self):

        self.master.deiconify() 
        self.master.destroy() 
        
if __name__ == "__main__":
    root = tk.Tk()
    app = AppController(root)
    root.mainloop()