import tkinter as tk
from tkinter import messagebox


# Janela principal
root = tk.Tk()
root.title("Simulador de Investimentos - Sicredi")
root.geometry("450x520")
root.configure(bg="#0B3D2E")
root.resizable(True, True)

# Função de cálculo
def calcular():
    try:
        valor = float(entrada_principal.get())
        taxa = float(entrada_taxa.get()) / 100
        tempo = int(entrada_tempo.get())

        montante = valor * (1 + taxa) ** tempo

        lbl_resultado.config(
            text=f"Montante Final: R$ {montante:,.2f}",
            fg="#D8FFDB"
        )

    except:
        messagebox.showerror(
            "Erro",
            "Preencha os campos corretamente!"
        )

# Cores e estilos
COR_FUNDO = "#0B3D2E"
COR_CARD = "#145A41"
COR_BOTAO = "#00A86B"
COR_BOTAO_HOVER = "#00C97F"
COR_TEXTO = "white"

fonte_titulo = ("Segoe UI", 18, "bold")
fonte_texto = ("Segoe UI", 11)
fonte_entry = ("Segoe UI", 12)

# Título
tk.Label(root,text="Simulador de Investimentos",font=fonte_titulo,bg=COR_FUNDO,fg="white").pack(pady=(25, 5))
tk.Label(root,text="Sicredi",font=("Segoe UI", 12, "italic"),bg=COR_FUNDO,fg="#A8E6B0").pack(pady=(0, 20))

# Card central
frame = tk.Frame(root,bg=COR_CARD,bd=0)
frame.pack(padx=25, pady=10, fill="both", expand=True)

# Campo Valor Inicial
tk.Label(frame,text="Valor inicial (R$)",font=fonte_texto,bg=COR_CARD,fg=COR_TEXTO).pack(pady=(25, 5))
entrada_principal = tk.Entry(frame,font=fonte_entry,width=28,justify="center",relief="flat")
entrada_principal.pack(ipady=8)

# Campo Taxa
tk.Label(frame,text="Taxa de juros mensal (%)",font=fonte_texto,bg=COR_CARD,fg=COR_TEXTO).pack(pady=(20, 5))

entrada_taxa = tk.Entry(frame,font=fonte_entry,width=28,justify="center",relief="flat")
entrada_taxa.pack(ipady=8)

# Campo Tempo
tk.Label(frame,text="Tempo (meses)",font=fonte_texto,bg=COR_CARD,fg=COR_TEXTO).pack(pady=(20, 5))

entrada_tempo = tk.Entry(frame,font=fonte_entry,width=28,justify="center",relief="flat")
entrada_tempo.pack(ipady=8)

# Botão
btn_calcular = tk.Button(frame,text="Calcular Investimento",font=("Segoe UI", 11, "bold"),bg=COR_BOTAO,fg="white",activebackground=COR_BOTAO_HOVER,activeforeground="white",relief="flat",cursor="hand2",padx=15,pady=10,command=calcular)
btn_calcular.pack(pady=30)

# Resultado
lbl_resultado = tk.Label(frame,text="Montante Final: R$ 0,00",font=("Segoe UI", 13, "bold"),bg=COR_CARD,fg="white")
lbl_resultado.pack(pady=(0, 25))

# Rodapé
tk.Label(root,text="© Simulador Financeiro",font=("Segoe UI", 9),bg=COR_FUNDO,fg="#A0CFA5").pack(pady=10)



root.mainloop()