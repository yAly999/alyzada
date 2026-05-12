import tkinter as tk

root = tk.Tk()
root.title("simulador de investimentos - Sicredi")
root.geometry("400x420")
root.configure(bg="#005c36")
root.resizable(False, False)

tk.Label(root, text="Simulador de Investimentos", font=("Arial", 14), fg="Black").pack(pady=20)

root.mainloop()