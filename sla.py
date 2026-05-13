import tkinter as tk

root = tk.Tk()
root.title("simulador de investimentos - Sicredi")
root.geometry("400x420")
root.configure(bg="#004363")
root.resizable(False, False)

tk.Label(root, text="Simulador de Investimentos", font=("Arial", 14), bg="#004363", fg="White").pack(pady=20)

tkLabel = tk.Label(root, text="sicredi", font=("Arial", 14, "italic"), bg="#004363", fg="White").pack(pady=10)

tk.label = tk.Label(root,text="Valor inicial($):", font=("Arial",12), bg="#004363", fg="White").pack(anchor= "center")

entrada_principal = tk.Entry(root, font=("Arial", 12), width=20,relief="groove").pack(pady=(5,0),ipadx=5, ipady=5,fill = tk.x)

##aaaaaaaaa

root.mainloop()
