import tkinter as tk
from client import ClientSocket


class ControlPanel:
    def __init__(self):
        root.geometry("400x400")
        self.client = ClientSocket()
        self.create_widgets()
        

    def create_widgets(self):
        btn = tk.Button(root, text="IP", command=self.get_ip)
        btn.pack()

    def get_ip(self):
        self.client.send_ip()



if __name__ == "__main__":
    root = tk.Tk()
    cp = ControlPanel()
    root.mainloop()