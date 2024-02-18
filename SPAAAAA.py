import tkinter as tk
import pickle

filename = 'betalinger.pk'

# Prøv at indlæse tidligere data fra pickle-fil, eller opret en tom dictionary
try:
    with open(filename, 'rb') as f:
        betalinger = pickle.load(f)
    print("Data indlæst fra fil.")
except (FileNotFoundError, EOFError):
    betalinger = {}
    print("Ingen tidligere data fundet. Opret ny opsparingsordning.")

class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        label = tk.Label(self, text="Home Page")
        label.pack(pady=100, padx=14)

        button1 = tk.Button(self, text="Register Payment", command=lambda: controller.show_frame("RegisterPayment"))
        button1.pack()

        button2 = tk.Button(self, text="View Payments", command=lambda: controller.show_frame("ListPayments"))
        button2.pack()

        button3 = tk.Button(self, text="View Worst Payers", command=lambda: controller.show_frame("WorstPayers"))
        button3.pack()

class RegisterPayment(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        label = tk.Label(self, text="Register Payment Page")
        label.pack(pady=10, padx=10)

        #TODO Vise visuelt inputfelter og en submit knap"""

        button = tk.Button(self, text="Back to Home", command=lambda: controller.show_frame("HomePage"))
        button.pack()

    def Betal (self):
        #TODO Implementere betalings kode så en fodboldnørd kan indbetale til deres rejse

class ListPayments(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        label = tk.Label(self, text="View Payments Page")
        label.pack(pady=10, padx=10)
        #TODO Visuelt repræsenter tabel over fodboldnørdernes indbetalte penge
        button = tk.Button(self, text="Back to Home", command=lambda: controller.show_frame("HomePage"))
        button.pack()

    def Liste_over_betalinger (self):
        #TODO Implentere kode som henter og fremviser betalinger for dict (Pickl)
class WorstPayers(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        label = tk.Label(self, text="View Worst Payers Page")
        label.pack(pady=10, padx=10)

        #TODO Visuelt repræsenter tabel over hvem af fodboldnørderne der har indbetaltet mindst penge"""

        button = tk.Button(self, text="Back to Home", command=lambda: controller.show_frame("HomePage"))
        button.pack()
    def Liste_over_mindst_betalinger (self):
        #TODO Implentere kode som henter og sortere for at fremvise hvilke fodboldnørder der har indbetalt mindst. Fra dict (Pickl)"""
class SinglePageApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("FodboldTur")

        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)

        self.frames = {}
        self.create_frames()

        self.show_frame("HomePage")

    def create_frames(self):
        # Define all frames/pages here
        pages = [HomePage, RegisterPayment, ListPayments, WorstPayers]

        for F in pages:
            frame = F(self.container, self)
            self.frames[F.__name__] = frame
            frame.grid(row=0, column=0, sticky="nsew")

    def show_frame(self, page_name):
        # Show a frame for the given page name
        frame = self.frames[page_name]
        frame.tkraise()

if __name__ == "__main__":
    app = SinglePageApp()
    app.mainloop()