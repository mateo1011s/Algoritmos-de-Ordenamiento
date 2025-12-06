import tkinter as tk
from tkinter import ttk, messagebox
import random 
from Algoritmos.data_manager import DataManager 
class AlgoritmsInputScreen(tk.Toplevel):
    def __init__(self, master=None, data_manager=None, next_callback=None):
        super().__init__(master)

        self.dm = data_manager if data_manager else DataManager()
        self.next_callback = next_callback

        self.title("Selección de Algoritmos")
        self.WIDTH = 600
        self.HEIGHT = 400
        self.configure(bg="black")
        self.resizable(False, False)
        self._center_window()
        
        if master:
            self.master = master
            self.protocol("WM_DELETE_WINDOW", self.on_closing_master) 
        
        self.create_widgets()
        
    def _center_window(self):
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width // 2) - (self.WIDTH // 2)
        y = (screen_height // 2) - (self.HEIGHT // 2)
        self.geometry(f'{self.WIDTH}x{self.HEIGHT}+{x}+{y}')
        
    def create_widgets(self):
        main_frame = tk.Frame(self, bg="black")
        main_frame.pack(expand=True, fill="both", padx=30, pady=(5,10))
        
        title_label=tk.Label(main_frame, text="SELECCIÓN DE ALGORITMOS", bg="black", fg="white", font=("Helvetica", 20, "bold"))
        title_label.pack(pady=(5,20))
        
        subtitle_label=tk.Label(main_frame, text="Escoja el tipo de algoritmo de ordenamiento que quiera usar", bg="black", fg="white", font=("Helvetica", 10, "bold"))
        subtitle_label.pack(pady=(0, 15))
        
        frame_options = tk.Frame(main_frame, bg="black")
        frame_options.pack(pady=(0,5),anchor="w",fill="x")
        
        algorithms = [
            "Burbuja",
            "Inserción",
            "Selección",
            "Shell Sort",
            "Merge Sort",
            "Quick Sort"
        ]
        style = ttk.Style()
        style.configure(
            "Black.TRadiobutton",
            background="black",
            foreground="white"
        )
        style.map(
            "Black.TRadiobutton",
            background=[("active", "black"), ("selected", "black")],
            foreground=[("active", "white"), ("selected", "white")]
        )
        self.selected_algorithm = tk.StringVar(value=algorithms[0])
        for alg in algorithms:
            rb = tk.Radiobutton(
                frame_options,
                text=alg,
                value=alg,
                font=("Helvetica", 10, "bold"),
                variable=self.selected_algorithm,
                bg="black",
                fg="white",
                selectcolor="black"
            )
            rb.pack(anchor="w", pady=6)
        
        confirm_button = tk.Button(
            frame_options,
            text="Confirmar selección",
            command=self.confirm_selection,
        )
        confirm_button.pack(pady=10)
        
    def confirm_selection(self):
        alg = self.selected_algorithm.get()

        if self.on_select:
            self.on_select(alg)  # Envía el algoritmo a otra pantalla

        tk.messagebox.showinfo("Algoritmo seleccionado", f"Ha elegido: {alg}")
        
    def on_closing_master(self):
        self.master.destroy()
        